import requests
import json
import os
import tinify
import random

api_key = 'AIzaSyDJNu6pW7kifKiVssTdMlyad-hUc3stgOg'
tinify.key = 'DJxqxb2DBprtLcm5QlsbpsJt8MNrvLkc'

print('Enter domain: ')
url = input().replace('https', '').replace('http', '').replace('/', '').replace(':', '').strip()
print("Querying " + url + '...')
api_url = 'https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=https://' + url + '&strategy=mobile&key=' + api_key

# creates a folder for the compressed images
try:
    save_path = 'C:/users/marcus.legault/scripts/pagespeed/' + url
    os.makedirs(save_path)

except FileExistsError:
    save_path = 'C:/users/marcus.legault/scripts/pagespeed/' + url + str(random.randint(1,101))
    os.makedirs(save_path)

# return JSON
data = json.loads(requests.get(api_url).text)

try:
    # loop through the image URLs from the JSON
    for item in data['lighthouseResult']['audits']['uses-optimized-images']['details']['items']:
        pic_url = item['url']
        pic_name = pic_url.split("/")[-1]
        completeName = os.path.join(save_path, pic_name)

        # tinypng pulls from image URLs, compresses, then saves
        print('Compressing ' + pic_name + '...')
        tinify.from_url(pic_url).to_file(completeName)
        print('Saved to ' + completeName)

    # create text file list for image URLs
    image_list = open(save_path + '/' + 'image_list.txt', 'a')
    print('Image URLs saved to ' + save_path + '/' + 'image_list.txt')

    # loop through the image URL to print references
    for item in data['lighthouseResult']['audits']['uses-optimized-images']['details']['items']:
        image_list.write(item['url'] + "\n")

except KeyError:
    print(url + ' is not a valid domain name')

except:
    print('Something went wrong')