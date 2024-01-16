# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://swapnaadhav.atlassian.net/rest/api/3/project"

API_TOKEN = "ATATT3xFfGF0uZYqpdPCICJKnd0MY3BX-dqIK9S4r1PCqgjjvGy_ZFfgfk5KjixBkScQ2oKwWC_6Ca04a3TS3ZgDaf9SrfBKBIfgPTkIZLzP3dofDRLqTZBPLAjeI-BL6A6jvuGubltQKUVp2HTu-sF3YjKn71LQnXaypdlYZHmIW0qwNdCd3ck=124E3F40"

auth = HTTPBasicAuth("swapnaadhav123@gmail.com", API_TOKEN)

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

output = json.loads(response.text)

name = output[0]["name"]

print(name)