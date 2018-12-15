import requests
import json
import os.path
import tinify

api_key = "AIzaSyDJNu6pW7kifKiVssTdMlyad-hUc3stgOg"
tinify.key = 'DJxqxb2DBprtLcm5QlsbpsJt8MNrvLkc'
save_path = 'C:/Users/marcus.legault/scripts/PageSpeed/pics'

print('Enter domain: ')
url = input().replace('https', '').replace('http', '').replace('/', '').replace(':', '')
print("Querying " + url + '...')
api_url = 'https://www.googleapis.com/pagespeedonline/v4/runPagespeed?url=http://' + url + '&strategy=mobile&key=' + api_key

# return JSON
data = json.loads(requests.get(api_url).text)

try:
    # loop through the image URLs from the JSON
    for item in data['formattedResults']['ruleResults']['OptimizeImages']['urlBlocks'][0]['urls']:
        pic_url = item['result']['args'][0]['value']
        pic_name = item['result']['args'][0]['value'].split("/")[-1]
        completeName = os.path.join(save_path, pic_name)

        # tinypng pulls from image URLs, compresses, then saves
        print('Compressing ' + pic_name + '...')
        tinify.from_url(pic_url).to_file(completeName)
        print('Saved to ' + completeName)

    # loop through the image URL to print references
    for i in data['formattedResults']['ruleResults']['OptimizeImages']['urlBlocks'][0]['urls']:
        print(i['result']['args'][0]['value'])

except KeyError:
    print(url + ' is not a valid domain name')

except:
    print('Something went wrong')

'''
def download_image(pic_name, pic_url):
	r = requests.get(pic_url, allow_redirects=True)
	open(completeName, 'wb').write(r.content)
'''
