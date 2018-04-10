# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from communicator import academy_parameters_pb2 as communicator_dot_academy__parameters__pb2
from communicator import python_parameters_pb2 as communicator_dot_python__parameters__pb2
from communicator import unity_input_pb2 as communicator_dot_unity__input__pb2
from communicator import unity_output_pb2 as communicator_dot_unity__output__pb2


class PythonToUnityStub(object):
  """This would require two separate channels ?
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Initialize = channel.unary_unary(
        '/communicator.PythonToUnity/Initialize',
        request_serializer=communicator_dot_python__parameters__pb2.PythonParameters.SerializeToString,
        response_deserializer=communicator_dot_academy__parameters__pb2.AcademyParameters.FromString,
        )
    self.Send = channel.unary_unary(
        '/communicator.PythonToUnity/Send',
        request_serializer=communicator_dot_unity__input__pb2.UnityInput.SerializeToString,
        response_deserializer=communicator_dot_unity__output__pb2.UnityOutput.FromString,
        )


class PythonToUnityServicer(object):
  """This would require two separate channels ?
  """

  def Initialize(self, request, context):
    """Sends the academy parameters
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Send(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_PythonToUnityServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Initialize': grpc.unary_unary_rpc_method_handler(
          servicer.Initialize,
          request_deserializer=communicator_dot_python__parameters__pb2.PythonParameters.FromString,
          response_serializer=communicator_dot_academy__parameters__pb2.AcademyParameters.SerializeToString,
      ),
      'Send': grpc.unary_unary_rpc_method_handler(
          servicer.Send,
          request_deserializer=communicator_dot_unity__input__pb2.UnityInput.FromString,
          response_serializer=communicator_dot_unity__output__pb2.UnityOutput.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'communicator.PythonToUnity', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
