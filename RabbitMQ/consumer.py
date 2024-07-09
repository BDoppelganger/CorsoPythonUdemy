#programma del producer che manda i messaggi in sequenza all'exchange

import pika

print("Collegamento a RabbitMQ...")

#connessione a rabbitmq a macchina locale: local host
params = pika.ConnectionParameters(host="localhost")
connection = pika.BlockingConnection(params)

#ottenere canale
channel = connection.channel()

#creare coda
channel.queue_declare(queue = 'worker_queue')

print("...eseguito")

#dichiarare funzione chiamata automaticamente ogni volta che viene passato un messaggio alla coda - funzione callback

def callback(ch, method, properties, body):
    print("Ricveuto %s" % body)

channel.basic_consume(callback, queue='worker_queue', no_ack=True) #consumare i messaggi dalla coda
channel.start_consuming()