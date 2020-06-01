import tkinter as tk
import tkinter.font as tkFont
from tkinter import PhotoImage

class Window(tk.Frame):
  def __init__(self):
    tk.Frame.__init__(self)
    self.grid()
    self.create_widgets()

  # def create_widgets(self):
    # font1 = tkFont.Font(size = 32)
    # font2 = tkFont.Font(size = 20)
    # self.lb = tk.Label(self, height=1, width = 20, text="恭喜你答對啦!!!", bg = 'green', font = font1)
    # self.fireimg = tk.PhotoImage(file = '煙火.gif')
    # self.firelb_right = tk.Label(self, image = self.fireimg, bg = 'green')
    # self.firelb_left = tk.Label(self, image = self.fireimg, bg = 'green')
    # self.continue_button = tk.Button(self, height = 3, width = 10, text = '繼續  Continue', bg = 'orange', font = font2)  #command = continue

    # full = tk.NE+ tk.SW
    # self.lb.grid(row = 0, column = 1,columnspan = 2, sticky = full)
    # self.firelb_left.grid(row = 1, column = 0, sticky = full)
    # self.firelb_right.grid(row = 1, column = 3, sticky = full)
    # self.continue_button.grid(row = 2, column = 1, columnspan = 2, sticky = full)
  
  # def picture(self): 
    # import time
    # import os
    
    # numIdx = 6 
    # frames = [PhotoImage(file='correct(1).gif', format='gif -index %i' %(i)) for i in range(numIdx)]

    # def update(idx): 
      # frame = frames[idx]
      # idx += 1 
      # label.configure(image=frame) 
      # self.after(100, update, idx%numIdx) 

    # label = tk.Label(self, bg = 'green')
    # self.after(0, update, 0)
    # return label




  def create_widgets(self):
    font1 = tkFont.Font(size = 32)
    font2 = tkFont.Font(size = 20)
    self.lb = tk.Label(self, height=1, width = 20, text="答錯了!!!再加油喔~", bg = 'red', font = font1)
    self.fireimg = tk.PhotoImage(file = '加油.gif')
    self.firelb_right = tk.Label(self, image = self.fireimg, bg = 'red')
    self.firelb_left = tk.Label(self, image = self.fireimg, bg = 'red')
    self.continue_button = tk.Button(self, height = 3, width = 10, text = '繼續  Continue', bg = 'orange', font = font2)  #command = continue

    full = tk.NE+ tk.SW
    self.lb.grid(row = 0, column = 1,columnspan = 2, sticky = full)
    self.firelb_left.grid(row = 1, column = 0, sticky = full)
    self.firelb_right.grid(row = 1, column = 3, sticky = full)
    self.continue_button.grid(row = 2, column = 1, columnspan = 2, sticky = full)
  
  def picture(self): 
    import time
    import os
    
    numIdx = 6 
    frames = [PhotoImage(file='Wrong(2).gif', format='gif -index %i' %(i)) for i in range(numIdx)]

    def update(idx): 
      frame = frames[idx]
      idx += 1 
      label.configure(image=frame) 
      self.after(100, update, idx%numIdx) 

    label = tk.Label(self, bg = 'red')
    self.after(0, update, 0)
    return label
window = Window()
img = window.picture()
img.grid(row = 1, column = 1,columnspan = 2, sticky = tk.NE+ tk.SW)
window.master.geometry('1000x500')
window.master.configure(background = 'red')      #小心對或錯
window.master.title("Right or Wrong")
window.mainloop()
