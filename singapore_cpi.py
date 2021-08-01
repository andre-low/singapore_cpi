import json
import urllib3
import calendar
from datetime import datetime

def fixSingstatCpiDates() :
    http = urllib3.PoolManager()
    response = http.request('GET', 'http://tablebuilder.singstat.gov.sg/api/table/tabledata/M212881?resourceId=M212881&seriesno=3&sortBy=seriesno%20desc')
    data = json.loads(response.data)

    for i in data['Data']['row'][0]['columns'] :
        date = datetime.strptime(i['key'], '%Y %b')
        dateMonthEnd = datetime.strptime(str(date.year) + '/' + str(date.month) + '/' + str(calendar.monthrange(date.year, date.month)[1]), '%Y/%m/%d')
        i['key'] = str(dateMonthEnd)

    return json.dumps(data)

print(fixSingstatCpiDates())