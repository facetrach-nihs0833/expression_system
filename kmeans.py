import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline
from sklearn.cluster import KMeans
import json
import time
import os
while True:
    with open('face-data.json') as f:     
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
        print("error")
        pass
    try:    
        df = pd.DataFrame({
            'x': listx,
            'y': listy
        })

        kmeans = KMeans(n_clusters=3)
        kmeans.fit(df)
        labels = kmeans.predict(df)
        centroids = kmeans.cluster_centers_
        fig = plt.figure(figsize=(5, 5))
        colmap = {1:'r',2:'g',3:'b'}
        colors = map(lambda x: colmap[x+1], labels)

        plt.scatter(df['x'], df['y'], color=list(colors), alpha=0.5, edgecolor='k')
        for idx, centroid in enumerate(centroids):
            plt.scatter(*centroid, color=colmap[idx+1])
            print(centroid)
        plt.xlim(0, 400)
        plt.ylim(0, 400)
        plt.show()
    except:
        print("人數過少")
        time.sleep(1)
        print("重新啟動中")
        time.sleep(1)
        print("重新啟動中..")
        time.sleep(1)
        print("重新啟動中....")
        time.sleep(1)
        os.system("cls")
        pass