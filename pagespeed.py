import requests
import urllib.parse

# https://www.googleapis.com/pagespeedonline/v4/runPagespeed?url=http://www.performance-law.com&strategy=mobile&key=AIzaSyDJNu6pW7kifKiVssTdMlyad-hUc3stgOg
api_key = "AIzaSyDJNu6pW7kifKiVssTdMlyad-hUc3stgOg"
url = "performance-law.com"
api_url = 'https://www.googleapis.com/pagespeedonline/v4/runPagespeed?url=http://www.' + url + '&strategy=mobile&key=' + api_key

json_data = requests.get(api_url).json()

json_status = json_data['formattedResults']['ruleResults']['OptimizeImages']['urlBlocks'][0]['urls'][0]['result']['args'][0]['value']
print(json_status)