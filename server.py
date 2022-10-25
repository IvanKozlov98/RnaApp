import pika
import sys
import logging
import socket
import time

class HumanGenetic:
    def __init__(self, id, dna):
        self.id = id
        self.dna = dna

class Hospital:
    def __init__(self):
        """Simple delegating constructor"""
        logging.debug("start initialize Servive")
        self.dict_dna = dict()
        self.connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        self.channel = self.connection.channel()
        self.channel.exchange_declare(exchange='logs', exchange_type='fanout')

        self.channel_clients = self.connection.channel()
        logging.debug("finish initialize Servive")

    def _add_dna_impl(self, id: str, dna: str):
        """Add dna to base of all dna"""
        self.dict_dna[id] = dna

    @staticmethod
    def _get_common_part(dna_a: str, dna_b: str):
        common_part = 0
        for i in range(min(len(dna_a), len(dna_b))):
            common_part += (dna_a[i] == dna_b[i])
        res = common_part / max(len(dna_a), len(dna_b))
        logging.debug(f"calculate common part: {res}")
        return res


    @staticmethod
    def is_relative(dna_a: str, dna_b: str) -> bool:
        """Check is relative dna_a and dna_b"""
        return Hospital._get_common_part(dna_a, dna_b) > 0.8

    @staticmethod
    def is_same_ethnic_group(dna_a: str, dna_b: str) -> bool:
        """Check is same ethnic group dna_a and dna_b"""
        return Hospital._get_common_part(dna_a, dna_b) > 0.6

    @staticmethod
    def _get_message_relative(ids: [str]):
        return f"Relative: {' '.join(ids)}"

    @staticmethod
    def _get_message_ethnic(ids: [str]):
        return f"Ethnic: {' '.join(ids)}"

    def add_dna(self, request: HumanGenetic):
        """add DNA to service database and notify rest clients news about affinity"""
        time.sleep(3)
        logging.debug("start searching relative")
        ids_relative = [request.id]
        ids_ethnic = [request.id]
        for (id, dna) in self.dict_dna.items():
            if Hospital.is_relative(dna, request.dna):
                ids_relative.append(id)
            if Hospital.is_same_ethnic_group(dna, request.dna):
                ids_ethnic.append(id)

        if len(ids_relative) > 1:
            message = Hospital._get_message_relative(ids_relative)
            self.channel.basic_publish(exchange='logs', routing_key='',
                                       body=bytes(message, encoding='utf8'))
            logging.debug("published messages about relatives our clients")
        if len(ids_ethnic) > 1:
            message = Hospital._get_message_ethnic(ids_ethnic)
            self.channel.basic_publish(exchange='logs', routing_key='',
                                       body=bytes(message, encoding='utf8'))
            logging.debug("published messages about ethnic our clients")
        logging.debug("finish searching relative/ethnic groups")
        self._add_dna_impl(id=request.id, dna=request.dna)
        logging.debug("added to list all DNA")

    @staticmethod
    def _get_human_genetic(msg: str)-> HumanGenetic:
        """Convert string message to HumanGenetic"""
        dna, idPerson = str(msg).split(' ')
        return HumanGenetic(dna=dna, id=idPerson)

    def run(self):
        """Main executing server"""
        print("Run server!")
        server_socket = socket.socket()
        server_socket.bind(('localhost', 5000))
        server_socket.listen(2)

        while True:
            conn, address = server_socket.accept()
            logging.debug("Connection from: " + str(address))
            data = conn.recv(1024).decode()
            if not data:
                break
            msg = str(data)
            logging.debug("from connected user: " + msg)
            hum_gen = Hospital._get_human_genetic(msg)
            self.add_dna(hum_gen)
        logging.debug("close connection")
        conn.close()


if __name__ == '__main__':
    logging.basicConfig(stream=sys.stdout, level=logging.INFO)
    logging.getLogger("pika").propagate = False
    hospital = Hospital()
    hospital.run()