import paho.mqtt.client as mqtt
import json



def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT Broker with result code " + str(rc))
    client.subscribe("SPEECH_TO_TEXT")

def on_message(client, userdata, msg):
    message = json.loads(msg.payload)
    print("Received Message : ", message)
    

def main():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect("10.0.0.5", 1883, 60)

    client.loop_forever()

if __name__ == "__main__":
    main()

