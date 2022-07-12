import requests
import json
import array

def hex2str(hex):
    return bytes.fromhex(hex[2:]).decode("utf-8")

graphql_url = "http://localhost:4000/graphql"

def notice(epoch):
    query = "query getNotice { GetNotice( query: { epoch_index:" + '"' + epoch + '"' + " } ) { session_id epoch_index input_index notice_index payload } }"
    response = requests.post(graphql_url, json={"query":query})
    content = json.loads(response.content.decode("utf-8"))
    payload = hex2str(content["data"]["GetNotice"][-1]["payload"])[:-1].replace("[","").replace("]","").replace('"', "").replace(" ", "").split(",")
    print(payload)
    p_list = []
    payload_list = []
    c = 0
    for p in payload:
        c = c + 1
        p_list.append(p)
        if c == 7:
            payload_list.append(p_list)
            p_list = []
            c = 0
    return payload_list
    

