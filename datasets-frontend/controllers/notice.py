import requests
import json

graphql_url = "http://localhost:4000/graphql"

def notice(epoch):
    query = "query getNotice { GetNotice( query: { epoch_index:" + '"' + epoch + '"' + " } ) { session_id epoch_index input_index notice_index payload } }"
    print(query)
    response = requests.post(graphql_url, json={"query":query})
    content = json.loads(response.content.decode("utf-8"))
    print(content)
    if content["data"]["GetNotice"]:
        return content["data"]["GetNotice"][0]["payload"]
    else:
        return "0x4552524f52202d20454d505459204e4f54494345"
