import sys
import time
import logging
import subprocess
import threading

from socket import timeout

from paramiko import SSHClient, AutoAddPolicy

from .rpc import Client, TimeoutError
from .rpc_interface import IFlightControl


class AlreadyRunningError(Exception):
    pass


class IServerLauncher:
    @property
    def logger(self):
        return logging.getLogger(self.__class__.__qualname__)

    def is_server_running(self):
        try:
            c = Client(IFlightControl(), f'tcp://{self._addr}:{self._port}', timeout=200)
            return c.ping() == b'pong'
        except TimeoutError:
            return False

    def start(self, addr):
        raise NotImplementedError

    def stop(self):
        c = Client(IFlightControl(), f'tcp://{self._addr}:{self._port}', timeout=200)
        c.shutdown()


def wait(done, interval=0.1, max_wait=10):
    total = 0

    while True:
        if done():
            break

        total += interval
        time.sleep(interval)

        if total > max_wait:
            raise TimeoutError()


class LocalServerLauncher(IServerLauncher):
    def __init__(self):
        self._process = None

    def start(self, addr, port):
        if addr != '127.0.0.1':
            raise ValueError('LocalServerHandler only possible to run on localhost')

        self._addr, self._port = addr, port

        if self._process:
            raise AlreadyRunningError(f'Local server is already running (pid:{self._process.pid})')

        self.logger.info('Starting local TikTorchServer on %s:%s', addr, port)
        self._process = subprocess.Popen(
            [sys.executable, '-m', 'tiktorch.server', '--port',  str(port), '--addr', addr],
            stdout=sys.stdout, stderr=sys.stderr
        )

        try:
            wait(self.is_server_running)
        except TimeoutError:
            raise Exception('Failed to start local TikTorchServer')


class RemoteSSHServerLauncher(IServerLauncher):
    def __init__(self, *, user: str, password: str, ssh_port: int = 22) -> None:
        self._user = user
        self._password = password
        self._ssh_port = ssh_port
        self._channel = None

        self._setup_ssh_client()

    def _setup_ssh_client(self):
        self._ssh_client = SSHClient()
        self._ssh_client.set_missing_host_key_policy(AutoAddPolicy())
        self._ssh_client.load_system_host_keys()

    def start(self, addr, port):
        if self._channel:
            raise RuntimeError('SSH server is already running')

        self._addr, self._port = addr, port

        ssh_params = {
            'hostname': addr,
            'port': self._ssh_port,
            'username': self._user,
            'password': self._password,
            'timeout': 10
        }

        try:
            self._ssh_client.connect(**ssh_params)
        except timeout as e:
            raise RuntimeError('Failed to establish SSH connection')

        transport = self._ssh_client.get_transport()

        channel = transport.open_session()
        channel.set_combine_stderr(True)
        buf_rdy = threading.Event()
        channel.in_buffer.set_event(buf_rdy)

        def _monitor_and_report():
            should_continue = True
            while should_continue:
                if channel.status_event.wait(timeout=1):
                    should_continue = False

                if buf_rdy.wait(timeout=1):
                    buf = b''
                    while channel.recv_ready():
                        buf += channel.recv(2048)

                    if buf:
                        print(buf.decode('utf-8'))

                if not should_continue:
                    print('Server exited with status: %s' % channel.recv_exit_status())

        t = threading.Thread(target=_monitor_and_report)
        t.start()
        self._channel = channel

        try:
            channel.exec_command(f'/home/novikov/bin/tiktorch --addr {addr} --port {port}')
        except timeout as e:
            raise RuntimeError('Failed to start TiktorchServer')
