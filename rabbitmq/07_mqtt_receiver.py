import paho.mqtt.client as mqtt
import time
#import input

def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)


#Create new client instance
client = mqtt.Client("P1")
#Connect to broker
client.connect(host="localhost")
#Subscribe to topic
client.subscribe("house/light")
client.on_message = on_message

client.loop_start()

#Publish message

#client.publish("house/light","OFF")
#time.sleep(4) # wait
#client.loop_stop() #stop the loop

input("Press Enter to continue...")
