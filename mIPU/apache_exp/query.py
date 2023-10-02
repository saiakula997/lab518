from common import * 


def Process_Message_Node(message):
    if message["request"] == REQ_MESSAGE_SLAVE:
        print("Slave {0} : Message : {1}".format(message["node"], message["data"]))
    elif message["request"] == REQ_SEARCH_DB:
        print("Slave {0} : Search for  : {1}".format(message["node"], message["data"]))