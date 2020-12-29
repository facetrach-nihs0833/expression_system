import cv2
import sys
import requests
import logging as log
import datetime as dt
from time import sleep

import time
import json
import pyimgur
import webbrowser
import tkinter as tk
#不是給我看的註解

#opencv setting
cv2.useOptimized()
cascPath = (r"haarcascade_frontalface_default.xml")
faceCascade = cv2.CascadeClassifier(cascPath)
log.basicConfig(filename='webcam.log',level=log.INFO)

#video_capture = cv2.VideoCapture('rtsp:192.168.46.5/')
video_capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)
anterior = 0

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

#opencv setting
text="no data"
jason=[]
world="is me again"
llist="setting"

#gui介面
window = tk.Tk()
window.title("面部表情辨識系統")
window.iconbitmap("idk.ico")
window.geometry('200x200')
window.configure(background="#2d3436")

label2 = tk.Label(window)
label2.place(x=0,y=0)
label2.configure(text = "nodata")
label = tk.Label(window)
label.place(x=0,y=25)
label.configure(text = "nodata")

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
    
def llistyaya():
    i=0;anger2=0;contempt2=0;disgust2=0;fear2=0;happiness2=0;neutral2=0;sadness2=0;surprise2=0
    try:
        while True:
            print(i)
            debuggg=(jason[i]["faceAttributes"]["emotion"])   
            anger=(jason[i]["faceAttributes"]["emotion"]["anger"])
            contempt=(jason[i]["faceAttributes"]["emotion"]["contempt"])
            disgust=(jason[i]["faceAttributes"]["emotion"]["disgust"])
            fear=(jason[i]["faceAttributes"]["emotion"]["fear"])
            happiness=(jason[i]["faceAttributes"]["emotion"]["happiness"])
            neutral=(jason[i]["faceAttributes"]["emotion"]["neutral"])
            sadness=(jason[i]["faceAttributes"]["emotion"]["sadness"])
            surprise=(jason[i]["faceAttributes"]["emotion"]["surprise"])
            print(debuggg)
            anger2=anger2+anger;contempt2=contempt+contempt2;disgust2=disgust+disgust2;fear2=fear+fear2;happiness2=happiness+happiness2;neutral2=neutral+neutral2;sadness2=sadness+sadness2;surprise2=surprise+surprise2
            i=i+1            
    except:
        print("error")
        pass
    #取最大值
    if i >= 1:
        anger2=anger2/i;contempt2=contempt2/i;disgust2=disgust2/i;fear2=fear2/i;happiness2=happiness2/i;neutral2=neutral2/i;sadness2=sadness2/i;surprise2=surprise2/i
    
    llist=(max(anger2,contempt2,disgust2,fear2,happiness2,neutral2,sadness2,surprise2))
    label2.configure(text = f"目前最大值{llist}")
    print(f"ohhhh{llist}")
    
    if anger2==llist:
        world="anger"
    if contempt2==llist:
        world="contempt"
    if disgust2==llist:
        world="disgust"    
    if fear2==llist:
        world="fear"
    if happiness2==llist:
        world="happiness"
    if neutral2==llist:
        world="neutral"    
    if sadness2==llist:
        world="sadness"    
    if surprise2==llist:
        world="surprise"
    label.configure(text = f"目前面部表情{world}")
    window.update()
    return llist,world

Tstart=time.time()

while True:
    #主迴圈
    if not video_capture.isOpened():
        print('找不到相機')
        sleep(5)
        pass
    #獲取攝影機畫面
    ret, frame = video_capture.read()
    ret, output = video_capture.read()
    #轉灰階
    try:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30)
        )
    except:
        print("轉換錯誤，切換模式")
        faces = faceCascade.detectMultiScale(
            frame,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30)
        )
    #如果畫面上出現了臉部
    for (x, y, w, h) in faces:
        #顯示綠色線條
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        #寫入照片
        cv2.imwrite(r"image\0.jpg",output)
        
        #顯示文字
        cv2.putText(frame, world+" "+str(llist), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2, 4)  
        cv2.imwrite(r"image\face.jpg",frame)      
        #計算時間
        Tend=time.time()
        thetime=round(Tend-Tstart)
        time.sleep(0.01)
        if thetime % 6 == 0:
            time.sleep(0.1)         
            updata_image()
            llistyaya()
            jason=updata_image()
            llist,world=llistyaya()
            

    if anterior != len(faces):
        anterior = len(faces)
        log.info("faces: "+str(len(faces))+" at "+str(dt.datetime.now()))    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    cv2.imshow('Video', frame)
window.mainloop()
#釋放所有攝影機
video_capture.release()
#關閉所有窗口
cv2.destroyAllWindows()