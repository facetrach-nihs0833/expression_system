import pyimgur
import json
import requests


#image updata setting
CLIENT_ID = "a9dba5d23914502"
PATH = r"image\0.jpg" #A Filepath to an image on your computer"
title = "az"
im = pyimgur.Imgur(CLIENT_ID)
uploaded_image = im.upload_image(PATH, title=title) 

#azure setting
subscription_key = 'dfbde64e106b449e9fb3a45bd626e9f1'
assert subscription_key

#azure api
face_api_url = 'https://the-face.cognitiveservices.azure.com/face/v1.0/detect'
image_url = uploaded_image.link
headers = {'Ocp-Apim-Subscription-Key': subscription_key}
params = {
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'emotion',
}

def updata_image():
    print("update")
    uploaded_image = im.upload_image(PATH, title=title)
    image_url = uploaded_image.link  
    print(image_url)
    response = requests.post(face_api_url, params=params,headers=headers, json={"url": image_url}) #dict
    #jason=json.dumps(response.json())#轉回字串    
    jason = response.json()
    print(jason)
    with open('face-data.json', 'w') as f:     
        json.dump(jason, f)
    return jason