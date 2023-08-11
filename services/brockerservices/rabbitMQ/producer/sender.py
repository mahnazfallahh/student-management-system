import pika
import json


class RabbitMqProducer:
    def __init__(self, host:str='localhost', port:int=5672, queue:str='student_records') -> None:
        self.host = host
        self.port = port
        self.queue = queue
        self.connection = None
        self.channel = None

    def connect(self):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=self.host)
        )
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=self.queue)

    def send_message(self, message:dict):
        self.channel.basic_publish(
            exchange = '',
            routing_key = self.queue,
            body=json.dumps(message)
        )

    def disconnect(self):
        if self.connection is not None and not self.connection.is_closed:
            self.connection.close()