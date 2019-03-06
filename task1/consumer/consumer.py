import pika
import sys
import time

time.sleep(20)

for i in range(15):
    time.sleep(i + 1)
    try:
        conn_params = pika.ConnectionParameters('rabbitmq', 5672)
        connection = pika.BlockingConnection(conn_params)
        channel = connection.channel()

        channel.queue_declare(queue='numbers')
    except:
        pass

def callback(ch, method, properties, body):
    print("Recieved number {}".format(body.decode("utf-8")))


channel.basic_consume(callback, queue='numbers', no_ack=True)

while True:
    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        channel.stop_consuming()
    except Exception:
        channel.stop_consuming()
        print("Exception occured")
