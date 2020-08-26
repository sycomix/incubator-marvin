# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

#do this relative import to get it right
from . import daemon_pb2 as daemon__pb2


class CommandCallStub(object):
    """Missing associated documentation comment in .proto file"""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.callCommand = channel.unary_unary(
                '/CommandCall/callCommand',
                request_serializer=daemon__pb2.Command.SerializeToString,
                response_deserializer=daemon__pb2.Status.FromString,
                )
        self.stopCommand = channel.unary_unary(
                '/CommandCall/stopCommand',
                request_serializer=daemon__pb2.Interruption.SerializeToString,
                response_deserializer=daemon__pb2.Status.FromString,
                )
        self.getState = channel.unary_unary(
                '/CommandCall/getState',
                request_serializer=daemon__pb2.Request.SerializeToString,
                response_deserializer=daemon__pb2.State.FromString,
                )


class CommandCallServicer(object):
    """Missing associated documentation comment in .proto file"""

    def callCommand(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def stopCommand(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getState(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CommandCallServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'callCommand': grpc.unary_unary_rpc_method_handler(
                    servicer.callCommand,
                    request_deserializer=daemon__pb2.Command.FromString,
                    response_serializer=daemon__pb2.Status.SerializeToString,
            ),
            'stopCommand': grpc.unary_unary_rpc_method_handler(
                    servicer.stopCommand,
                    request_deserializer=daemon__pb2.Interruption.FromString,
                    response_serializer=daemon__pb2.Status.SerializeToString,
            ),
            'getState': grpc.unary_unary_rpc_method_handler(
                    servicer.getState,
                    request_deserializer=daemon__pb2.Request.FromString,
                    response_serializer=daemon__pb2.State.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'CommandCall', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class CommandCall(object):
    """Missing associated documentation comment in .proto file"""

    @staticmethod
    def callCommand(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/CommandCall/callCommand',
            daemon__pb2.Command.SerializeToString,
            daemon__pb2.Status.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def stopCommand(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/CommandCall/stopCommand',
            daemon__pb2.Interruption.SerializeToString,
            daemon__pb2.Status.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getState(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/CommandCall/getState',
            daemon__pb2.Request.SerializeToString,
            daemon__pb2.State.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
