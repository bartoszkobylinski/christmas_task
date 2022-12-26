import os
import openai

OPENAI_APIKEY = os.environ.get('OPENAI_APIKEY','there were some problem with APIKEY')
'''
openai.api_key = OPENAI_APIKEY
openai.Model.list()
images = openai.Image.create(prompt='photogenic turkish women with bikini suit holding in hand',n=2, size="512x512")
#print(images)
for image in images['data']:
    print(image['url'])
'''

def create_images(api_key, prompt):
    openai.api_key = api_key
    openai.Model.list()
    images = openai.Image.create(
        prompt=prompt,
        n=2,
        size="1024x1024"
    )
    for image in images['data']:
        yield image['url']

for link in create_images(OPENAI_APIKEY,'small dragon battle with godzilla on the beach'):
    print(link)