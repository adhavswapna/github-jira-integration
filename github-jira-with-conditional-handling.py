import requests
from requests.auth import HTTPBasicAuth
import json
from flask import Flask, request

#creating flask instance
app = Flask(__name__)

@app.route("/createjira", methods=['POST'])
def createjira():

    url = "https://swapnaadhav.atlassian.net/rest/api/3/issue"

    API_TOKEN = "ATATT3xFfGF0uZYqpdPCICJKnd0MY3BX-dqIK9S4r1PCqgjjvGy_ZFfgfk5KjixBkScQ2oKwWC_6Ca04a3TS3ZgDaf9SrfBKBIfgPTkIZLzP3dofDRLqTZBPLAjeI-BL6A6jvuGubltQKUVp2HTu-sF3YjKn71LQnXaypdlYZHmIW0qwNdCd3ck=124E3F40"

    auth = HTTPBasicAuth("swapnaadhav123@gmail.com", API_TOKEN)

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    payload = json.dumps( {
        "fields": {
        
        "description": {
            "content": [
            {
                "content": [
                {
                    "text": "create First jira Ticket.",
                    "type": "text"
                }
                ],
                "type": "paragraph"
            }
            ],
            "type": "doc",
            "version": 1
        },
        
        "issuetype": {
            "id": "10030"
        },
        
        "project": {
            "key": "GJI"
        },
        
        "summary": "My jira ticket",
        
        },
        "update": {}
    } )


    body = request.json.get("comment", {}).get("body", "")
    if body =="/jira":

            response = requests.request(
                "POST",
                url,
                data=payload,
                headers=headers,
                auth=auth
            )

            return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))

    else:
        return "comment should be /jira only"


app.run('0.0.0.0', port=5000)