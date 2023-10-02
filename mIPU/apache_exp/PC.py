import pyarrow as pa
import pyarrow.parquet as pq
import pandas as pd
from common import *

def menu():
    while True:
        print("######################################")
        print("1. Send Message to Slave Node 1")
        print("2. Send Message to Slave Node 2")
        print("3. Search for String in DB")
        print("######################################")
        return input("Enter Choice :")

def process(choice, client):
    if choice == "1":
        data = input("Enter Message String : ")
        message = Message_Node(SLAVE_NODE_1, REQ_MESSAGE_SLAVE, data)
        message = json.dumps(message)
        client.publish(TOPIC_SLAVE_NODE_1, message)
    elif choice == "2":
        data = input("Enter Message String : ")
        message = Message_Node(SLAVE_NODE_2, REQ_MESSAGE_SLAVE, data)
        message = json.dumps(message)
        client.publish(TOPIC_SLAVE_NODE_2, message)
    elif choice == "3":
        data = input("Enter Search String : ")
        for topic, node in zip([TOPIC_SLAVE_NODE_1, TOPIC_SLAVE_NODE_2],[SLAVE_NODE_2, SLAVE_NODE_2]):
            message = Message_Node(node, REQ_SEARCH_DB, data)
            message = json.dumps(message)
            client.publish(topic, message)
        

def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT Broker with result code " + str(rc))
    client.subscribe("slave_node_2")

def on_message(client, userdata, msg):
    message = json.loads(msg.payload)
    print("Message : {0} to Slave  {1} ".format(message["data"], message["node"]))


def main():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect("localhost", 1883, 60)

    while True :
        choice = menu()
        process(choice, client)

    client.loop_forever()

if __name__ == "__main__":
    main()

