import tkinter as tk
import json
#setting
window = tk.Tk()
window.title("面部表情辨識系統")
window.iconbitmap("idk.ico")
window.geometry('200x200')
window.configure(background="#2d3436")

label = tk.Label(window)
label.place(x=0,y=0)
jason=0
with open('face-data.json', 'w') as f:     
    json.dump(jason, f)
print(jason)


window.mainloop()