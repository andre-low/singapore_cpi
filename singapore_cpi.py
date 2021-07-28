import json
import requests

response = requests.get("http://tablebuilder.singstat.gov.sg/api/table/tabledata/M212881?resourceId=M212881&seriesno=3&sortBy=seriesno%20desc")
data = json.loads(response.text)

print(data)