from concurrent.futures import ThreadPoolExecutor

import grpc

from definitions.builds.service_pb2 import Health
from definitions.builds.service_pb2_grpc import TestServiceStub, add_TestServiceServicer_to_server


class Service(TestServiceStub):
    def __init__(self, channel):
        """Simple delegating constructor"""
        super().__init__(channel)

    @staticmethod
    def _check_health_impl(DNA):
        """Check health of human based on his DNA

        :DNA is DNA of human
        :return: is human health or not
        """
        return "AAG" in DNA

    def check_health(self, request):
        """Check health of human based on his DNA
        :request is request(health) for server
        :return: health of human based on his DNA
        """
        if Service._check_health_impl(request.DNA):
            result = Health(health=f"{request.label} is healthy")
        else:
            result = Health(health=f"{request.label} isn't healthy")
        return result


def execute_server():
    """Main executing server"""
    with grpc.insecure_channel("localhost:3000") as channel:
        server = grpc.server(ThreadPoolExecutor(max_workers=10))
        add_TestServiceServicer_to_server(Service(channel), server)
        server.start()

    print("The server is up and running...")
    server.wait_for_termination()


if __name__ == "__main__":
    execute_server()
