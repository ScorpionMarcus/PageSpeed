import requests
import json
import urllib.request
import os.path

# https://www.googleapis.com/pagespeedonline/v4/runPagespeed?url=http://www.performance-law.com&strategy=mobile&key=AIzaSyDJNu6pW7kifKiVssTdMlyad-hUc3stgOg

api_key = "AIzaSyDJNu6pW7kifKiVssTdMlyad-hUc3stgOg"
url = input('Enter domain: ')
print("Querying " + url + '...')
api_url = 'https://www.googleapis.com/pagespeedonline/v4/runPagespeed?url=http://' + url + '&strategy=mobile&key=' + api_key

json_data = requests.get(api_url)

data = json.loads(json_data.text)

def download_image(pic_name, pic_url):

	# Request the image URL
	r = requests.get(pic_url, allow_redirects=True)

	# Declare a save path
	save_path = 'C:/Users/marcus.legault/scripts/PageSpeed/pics'

	# Join save path with file name
	completeName = os.path.join(save_path, pic_name)

	print('Saving ' + pic_name + ' -----> ' + completeName)

	# Write the file to the completeName path
	open(completeName, 'wb').write(r.content)

# Loop through the image URLs from the JSON
for item in data['formattedResults']['ruleResults']['OptimizeImages']['urlBlocks'][0]['urls']:

	pic_url = item['result']['args'][0]['value']

	# Split the image name from the URL
	pic_name = item['result']['args'][0]['value'].split("/")[-1]

	# Input into function
	download_image(pic_name, pic_url)

# Loop through the image URL to print references
for i in data['formattedResults']['ruleResults']['OptimizeImages']['urlBlocks'][0]['urls']:
	print(i['result']['args'][0]['value'])