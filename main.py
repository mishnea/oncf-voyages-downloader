import sys

import requests
import base64


if len(sys.argv) < 2:
    raise Exception("Missing argument order number")

order_number = sys.argv[1]

req_data = {
    "numeroCommande": order_number,
}

print("fetch data")
res = requests.post("https://www.oncf-voyages.ma/api/getTicket", data=req_data)

res_json_data = res.json()

for ticket in res_json_data["body"]["tickets"]:
    displayname = ticket["displayName"]
    filename = ticket["fileName"]
    contents = ticket["contents"]
    print("writing", displayname)
    with open(filename, "wb") as f:
        f.write(base64.b64decode(contents))
