import cv2
import json
import time
import threading
import tkinter as tk
import datetime as dt
import logging as log
from package.list import llistyaya
from package.update import updata_image

#opencv 基礎設定
cv2.useOptimized()
cascPath = (r"haarcascade_frontalface_default.xml")
faceCascade = cv2.CascadeClassifier(cascPath)
log.basicConfig(filename='webcam.log',level=log.INFO)

#video_capture = cv2.VideoCapture('rtsp:192.168.46.5/')
video_capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)
anterior = 0

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

#AZURE重置
Tstart=time.time()

#色影機拉
class ipcamCapture:
    def __init__(self, URL):
        self.Frame = []
        self.status = False
        self.isstop = False
		
	#攝影機連接。
        self.video_capture = cv2.VideoCapture(URL)

    def start(self):
	#把程式放進子執行緒
        print('ipcam started!')
        threading.Thread(target=self.queryframe, daemon=True, args=()).start()

    def stop(self):
	#停止無限迴圈的開關。
        self.isstop = True
        print('ipcam stopped!')
   
    def getframe(self):
	#再回傳最新的影像。
        return self.Frame
        
    def queryframe(self):
        while (not self.isstop):
            self.status, self.Frame = self.video_capture.read()
        
        self.video_capture.release()

#設定攝影機
URL = "rtsp:192.168.46.5/"
ipcam = ipcamCapture(1)

#啟動搂!
ipcam.start()

#填充影像
time.sleep(1)

#建立執行續拉
upd=threading.Thread(target = updata_image)
llya=threading.Thread(target = llistyaya)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~主迴圈~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
while True:
    
    
    #獲取攝影機畫面
    frame = ipcam.getframe()
    output = ipcam.getframe()
    #ret, frame = video_capture.read()
    #ret, output = video_capture.read()
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
            jason=updata_image()                      
            llist,world=llistyaya(jason)
            

    if anterior != len(faces):
        anterior = len(faces)
        log.info("faces: "+str(len(faces))+" at "+str(dt.datetime.now()))  
      
    if cv2.waitKey(1) & 0xFF == ord('q'):
        video_capture.release()
        ipcam.stop()
        cv2.destroyAllWindows()
        break
    cv2.imshow('Video', frame)


window.mainloop()