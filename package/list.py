import json


def llistyaya(jason):
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
    
    return llist,world