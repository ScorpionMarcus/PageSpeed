import requests
import json
import urllib.request
import os.path

# https://www.googleapis.com/pagespeedonline/v4/runPagespeed?url=http://www.performance-law.com&strategy=mobile&key=AIzaSyDJNu6pW7kifKiVssTdMlyad-hUc3stgOg

api_key = "AIzaSyDJNu6pW7kifKiVssTdMlyad-hUc3stgOg"
url = "performance-law.com"
api_url = 'https://www.googleapis.com/pagespeedonline/v4/runPagespeed?url=http://www.' + url + '&strategy=mobile&key=' + api_key

json_data = requests.get(api_url)

data = json.loads(json_data.text)

def download_image(pic_name, pic_url):
	r = requests.get(pic_url, allow_redirects=True)
	save_path = 'C:/Users/marcus.legault/Downloads/Pics'
	completeName = os.path.join(save_path, pic_name)
	print('Saving ' + pic_name + ' -----> ' + completeName)
	open(completeName, 'wb').write(r.content)

for item in data['formattedResults']['ruleResults']['OptimizeImages']['urlBlocks'][0]['urls']:
	pic_url = item['result']['args'][0]['value']
	pic_name = item['result']['args'][0]['value'].split("/")[-1]
	
	download_image(pic_name, pic_url)