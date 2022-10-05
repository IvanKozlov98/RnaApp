import grpc
import sys

from definitions.builds.service_pb2 import HumanGenetic
from server import Service


def execute_client():
    """Main executing client"""
    with grpc.insecure_channel("localhost:3000") as channel:
        client = Service(channel)
        answ = "yes"
        while answ == "yes":
            print("Enter label: ", flush=True, end='')
            label = sys.stdin.readline()[:-1]
            print("Enter DNA: ", flush=True, end='')
            DNA = sys.stdin.readline()[:-1]
            health = client.check_health(HumanGenetic(DNA=DNA, label=label))
            print(health.health)
            print("Complete? yes/no: ", flush=True, end='')
            answ = sys.stdin.readline()[:-1]


if __name__ == "__main__":
    execute_client()
