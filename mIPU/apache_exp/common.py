import copy
import json
import paho.mqtt.client as mqtt

MASTER_NODE=0
SLAVE_NODE_1 = 1
SLAVE_NODE_2 = 2

TOPIC_SLAVE_NODE_1 = "slave_node_1"
TOPIC_SLAVE_NODE_2 = "slave_node_2"

MAX_PAYLOAD_SIZE = 128 * 1024  #128 KB

REQ_LOAD_DATABASE = "LOAD_DATABASE"
REQ_MESSAGE_SLAVE = "REQ_MESSAGE_SLAVE"
REQ_SEARCH_DB = "REQ_SEARCH_DB"

def Message_Node(node_id, request="None_Request", data="Empty String"):
    message_node = {
        "node" : node_id,
        "request" : request,
        "data" : data, 
        }
    return copy.deepcopy(message_node)






# # Create sample data
# data = {'name': ['Alice', 'Bob', 'Charlie'],
#         'age': [25, 30, 28]}

# # Create a Pandas DataFrame from the data
# df = pd.DataFrame(data)
# # Convert the Pandas DataFrame to an Arrow table
# table = pa.Table.from_pandas(df)

# # Serialize the Arrow table to a JSON string
# serialized_json = table.to_pandas().to_json()