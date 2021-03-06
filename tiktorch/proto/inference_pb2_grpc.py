# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from . import inference_pb2 as inference__pb2


class InferenceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.CreateModelSession = channel.unary_unary(
        '/Inference/CreateModelSession',
        request_serializer=inference__pb2.CreateModelSessionRequest.SerializeToString,
        response_deserializer=inference__pb2.ModelSession.FromString,
        )
    self.CloseModelSession = channel.unary_unary(
        '/Inference/CloseModelSession',
        request_serializer=inference__pb2.ModelSession.SerializeToString,
        response_deserializer=inference__pb2.Empty.FromString,
        )
    self.CreateDatasetDescription = channel.unary_unary(
        '/Inference/CreateDatasetDescription',
        request_serializer=inference__pb2.CreateDatasetDescriptionRequest.SerializeToString,
        response_deserializer=inference__pb2.DatasetDescription.FromString,
        )
    self.GetLogs = channel.unary_stream(
        '/Inference/GetLogs',
        request_serializer=inference__pb2.Empty.SerializeToString,
        response_deserializer=inference__pb2.LogEntry.FromString,
        )
    self.ListDevices = channel.unary_unary(
        '/Inference/ListDevices',
        request_serializer=inference__pb2.Empty.SerializeToString,
        response_deserializer=inference__pb2.Devices.FromString,
        )
    self.Predict = channel.unary_unary(
        '/Inference/Predict',
        request_serializer=inference__pb2.PredictRequest.SerializeToString,
        response_deserializer=inference__pb2.PredictResponse.FromString,
        )


class InferenceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def CreateModelSession(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CloseModelSession(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateDatasetDescription(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetLogs(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListDevices(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Predict(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_InferenceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'CreateModelSession': grpc.unary_unary_rpc_method_handler(
          servicer.CreateModelSession,
          request_deserializer=inference__pb2.CreateModelSessionRequest.FromString,
          response_serializer=inference__pb2.ModelSession.SerializeToString,
      ),
      'CloseModelSession': grpc.unary_unary_rpc_method_handler(
          servicer.CloseModelSession,
          request_deserializer=inference__pb2.ModelSession.FromString,
          response_serializer=inference__pb2.Empty.SerializeToString,
      ),
      'CreateDatasetDescription': grpc.unary_unary_rpc_method_handler(
          servicer.CreateDatasetDescription,
          request_deserializer=inference__pb2.CreateDatasetDescriptionRequest.FromString,
          response_serializer=inference__pb2.DatasetDescription.SerializeToString,
      ),
      'GetLogs': grpc.unary_stream_rpc_method_handler(
          servicer.GetLogs,
          request_deserializer=inference__pb2.Empty.FromString,
          response_serializer=inference__pb2.LogEntry.SerializeToString,
      ),
      'ListDevices': grpc.unary_unary_rpc_method_handler(
          servicer.ListDevices,
          request_deserializer=inference__pb2.Empty.FromString,
          response_serializer=inference__pb2.Devices.SerializeToString,
      ),
      'Predict': grpc.unary_unary_rpc_method_handler(
          servicer.Predict,
          request_deserializer=inference__pb2.PredictRequest.FromString,
          response_serializer=inference__pb2.PredictResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'Inference', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class FlightControlStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Ping = channel.unary_unary(
        '/FlightControl/Ping',
        request_serializer=inference__pb2.Empty.SerializeToString,
        response_deserializer=inference__pb2.Empty.FromString,
        )
    self.Shutdown = channel.unary_unary(
        '/FlightControl/Shutdown',
        request_serializer=inference__pb2.Empty.SerializeToString,
        response_deserializer=inference__pb2.Empty.FromString,
        )


class FlightControlServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Ping(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Shutdown(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_FlightControlServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Ping': grpc.unary_unary_rpc_method_handler(
          servicer.Ping,
          request_deserializer=inference__pb2.Empty.FromString,
          response_serializer=inference__pb2.Empty.SerializeToString,
      ),
      'Shutdown': grpc.unary_unary_rpc_method_handler(
          servicer.Shutdown,
          request_deserializer=inference__pb2.Empty.FromString,
          response_serializer=inference__pb2.Empty.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'FlightControl', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
