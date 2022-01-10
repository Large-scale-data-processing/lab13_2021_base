
import grpc

from  protobuf import sample_pb2
from  protobuf import sample_pb2_grpc


channel = grpc.insecure_channel('localhost:50051')

stub = sample_pb2_grpc.SampleStub(channel)

request = sample_pb2.Request(value="John")

response = stub.Test(request)

print(response.value)