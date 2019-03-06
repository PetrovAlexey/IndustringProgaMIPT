import pika
import random
import time
import sys

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

for i in range(100):
    number = random.randint(1, 1000)
    print("Sending number {}".format(number))

    channel.basic_publish(
        exchange='', routing_key='numbers', body=str(number))

    delay = random.randint(1, 10)
    time.sleep(delay)


connection.close()
