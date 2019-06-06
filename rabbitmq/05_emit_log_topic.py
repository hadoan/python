import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()

channel.exchange_declare(exchange="topic_logs", exchange_type="topic")
channel.queue_declare("rabbitmqnhucac",durable=True)
routing_key = sys.argv[1] if len(sys.argv) > 2 else 'anonymous.info'
message = ' '.join(sys.argv[2:]) or 'Hello World!'

channel.basic_publish("topic_logs", routing_key=routing_key, body=message,properties=pika.BasicProperties(
                         delivery_mode = 2, # make message persistent
                      ))
print(" [x] Sent %r:%r" % (routing_key, message))
connection.close()