import grpc
from concurrent import futures
import time

from  protobuf import sample_pb2
from  protobuf import sample_pb2_grpc


class SampleServicer(sample_pb2_grpc.SampleServicer):

    def Test(self, request, context):
        print("Got a call "+request.value)
        response = sample_pb2.Response()
        response.value = "Hello "+request.value
        return response


server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

sample_pb2_grpc.add_SampleServicer_to_server(
        SampleServicer(), server)

print('Starting server. Listening on port 50051.')
server.add_insecure_port('[::]:50051')
server.start()

try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)