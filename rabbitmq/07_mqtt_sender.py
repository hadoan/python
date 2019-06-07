
import paho.mqtt.client as mqtt
client = mqtt.Client("test_mqtt_client")
client.connect(host = "localhost",port=1883)

client.publish("house/light","ON")