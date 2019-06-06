
import pika
import uuid

class FibonacciRpcClient(object):

    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
        self.channel = self.connection.channel()
        result =  self.channel.queue_declare('', exclusive=True)
        self.queue_name = result.method.queue

        self.channel.basic_consume(queue = self.queue_name, on_message_callback = self.on_response,auto_ack = True)

    def on_response(self,ch, method, props, body):
        if self.correlation_id== props.correlation_id:
            self.response = body


    def call(self,n):
        self.response = None
        self.correlation_id = str(uuid.uuid4())

        self.channel.basic_publish(exchange = '',
                                   routing_key='rpc_queue',
                                   body=str(n),
                                   properties = pika.BasicProperties(
                                       correlation_id=self.correlation_id, reply_to=self.queue_name
                                   ))

        while self.response is None:
            self.connection.process_data_events()

        return int(self.response)



client = FibonacciRpcClient()
print(" [x] Requesting fib(30)")
response = client.call(3)
print(" [.] Got %r" % response)