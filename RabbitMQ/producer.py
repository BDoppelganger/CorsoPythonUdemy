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

i = 0
while True:
    message = str(i)
    i += 1
    
    #pubblica su exchange standard passando direttamente alla coda il messaggio message
    channel.basic_publish(exchange = '', routing_key='worker_queue', body=message)
    
    print("inviato messaggio %s", message)
    
    if i > 100000:
        break

connection.close()
    

