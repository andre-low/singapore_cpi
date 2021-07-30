import json
import requests
import calendar
from datetime import datetime

def fixSingstatDates() :
    response = requests.get("http://tablebuilder.singstat.gov.sg/api/table/tabledata/M212881?resourceId=M212881&seriesno=3&sortBy=seriesno%20desc")
    data = json.loads(response.text)

    for i in data["Data"]["row"][0]["columns"] :
        date = datetime.strptime(i["key"], "%Y %b")
        dateMonthEnd = datetime.strptime(str(date.year) + '/' + str(date.month) + '/' + str(calendar.monthrange(date.year, date.month)[1]), "%Y/%m/%d")
        i["key"] = str(dateMonthEnd)

    return json.dumps(data)

print(fixSingstatDates())