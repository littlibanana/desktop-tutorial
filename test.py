import tkinter as tk
from PIL import ImageTk
import tkinter.font as tkFont
import time
import os
import random

correct = ['correct(1).gif', 'correct(2).gif', 'correct(3).gif']
root = tk.Tk()
ft = tkFont.Font(family='内海フォント-Bold', size=20, weight=tkFont.BOLD)  #　設定文字字體、大小、粗細

canvas = tk.Canvas(width=1000,height=563,bd=0, highlightthickness=0) # 設定畫布大小
backphoto = ImageTk.PhotoImage(file = 'right photo.png')
canvas.create_image(400, 285, image=backphoto)  

numIdx = 15 
picture = correct[random.randint(0,2)]
frames = [tk.PhotoImage(file = picture, format='gif -index %i' %(i)) for i in range(numIdx)]

def update(idx):
    frame = frames[idx]
    idx += 1
    label.configure(image=frame) 
    root.after(100, update, idx%numIdx)
btn2 = tk.Button(text='你答對了\n繼續下一題',font = ft,bg="white",fg = 'black',anchor = tk.CENTER)
btn2.grid()

label = tk.Label(root)
label.grid()
canvas.create_window(400, 280,window=label)
canvas.create_window(780, 500, width=200, height=90,window=btn2)
canvas.grid()
root.after(0, update, 0)
root.mainloop()