import json


with open('log.json') as f:     
    jason=json.load(f)

try:
    i=0
    listx=[]
    listy=[]
    while True:
        top=(jason[i]["faceRectangle"]["top"])   
        left=(jason[i]["faceRectangle"]["left"])
        listx+=[top]
        listy+=[left]
        print(listx)
        print(listy)
        i+=1
        
except:
    pass
    
    
    