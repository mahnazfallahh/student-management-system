import pika
import json
# from core.database.database import Database
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class RabbitMqConsumer:
    def __init__(
            self,
            host:str='localhost',
            port:int=5672,
            queue:str='student_records'
        ):
        self.host = host
        self.port = port
        self.queue = queue
        self.connection = None
        self.channel = None

    def connect(self):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(
            host=self.host,
            port=self.port
            )
        )
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=self.queue)

    def disconnect(self):
        if self.connection is not None and not self.connection.is_closed:
            self.connection.close()

    def read_messages(self, callback):
        queue_declare_ok = self.channel.queue_declare(queue=self.queue, passive=True)
        if queue_declare_ok.method.message_count > 0:
            self.channel.basic_consume(
                queue=self.queue,
                on_message_callback=callback,
                auto_ack=True
            )
            print("Waiting for messaging. To Exit press CTRL+C")
            self.channel.start_consuming()
        else:
            print(f"The '{self.queue}' queue does not exist or is empty.")
