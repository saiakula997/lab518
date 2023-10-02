import paho.mqtt.client as mqtt
import pandas as pd
from common import *
import json

import pyarrow as pa
import pandas as pd

def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT Broker with result code " + str(rc))
    client.subscribe("master_node")

def on_message(client, userdata, msg):
    message = json.loads(msg.payload)
    print("Received message Req: " + message["request"])
    process(message,client)

def process(messsage, client):
    request = message["request"]
    if request == "REQ_MESSAGE_SLAVE":
        message = Message_Node(SLAVE_NODE_1, data=data)
        client.publish(TOPIC_SLAVE_NODE_1, json.dumps(message))
    elif choice == 2:
        message = Message_Node(SLAVE_NODE_2, data=data)
        client.publish(TOPIC_SLAVE_NODE_2, json.dumps(message))
      

def main():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect("localhost", 1883, 60) 
    while True:
        choice = menu()
        process(choice, client)


    client.loop_forever()
if __name__ == "__main__":
    main()
