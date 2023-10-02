import paho.mqtt.client as mqtt
import json
import query

SLAVE_NODE_ID = 2

def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT Broker with result code " + str(rc))
    client.subscribe("slave_node_2")

def on_message(client, userdata, msg):
    message = json.loads(msg.payload)
    print("Received Message : {0} to Slave Node  {1} ".format(message["data"], message["node"]))
    query.Process_Message_Node(message)
    

def main():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect("localhost", 1883, 60)

    client.loop_forever()

if __name__ == "__main__":
    main()

