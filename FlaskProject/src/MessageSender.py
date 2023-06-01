import pika
import time
from JsonReader import read_json

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.exchange_declare(exchange='data_exchange', exchange_type='fanout')

def request_data(num):
    if (num == 1):
        return read_json("1")
    if (num == 2):
        return read_json("2")
    if (num == 3):
        return read_json("3")
    else:
        return "no data"


def send(num):
    body = request_data(num)
    while True:
        channel.basic_publish(exchange='data_exchange', routing_key='', body=str.encode(body))
        #       print("sent: " + body)
        time.sleep(2)
