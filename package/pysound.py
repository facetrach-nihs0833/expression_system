from playsound import playsound
import threading

class playy:
    def __init__(self, URL):
        print("lol")
        self.playsong=URL
    def start(self):
	#把程式放進子執行緒
        print("isme")
        threading.Thread(target=self.playsound,name="playla",  args=()).start()

    def playsound(self):    
        print("thatme")
        print(self.playsong)
        
        print("dick")
        playsound(self.playsong,'mp3')    

