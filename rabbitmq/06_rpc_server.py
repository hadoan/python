
import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()
channel.queue_declare("rpc_queue",durable=True)


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def callback(ch, method, properties, body):
    n = int(body)
    print(" [.] fib(%s)" % n)
    response = 2

    ch.basic_publish(exchange='',
                     routing_key = properties.reply_to,
                     properties = pika.BasicProperties(correlation_id=properties.correlation_id),
                     body=str(response))
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_consume(queue="rpc_queue",on_message_callback = callback)
    

print(" [x] Awaiting RPC requests")
channel.start_consuming()
