import tkinter as tk
from PIL import Image, ImageTk
import csv
import webbrowser

cats_dict = dict()
with open(file='src\\cats.csv', mode='r') as f:
    rows = csv.reader(f)
    for row in rows:
        cnum = int(row[0])
        # name, gen, color, yrs, url, photo site
        datalst = [row[1], row[2], row[3], row[4], row[12], row[13]]
        cats_dict[cnum] = datalst

# 選到的三隻貓
first = 1 # list[0]
second = 2 # list[1]
third = 3 # list[2]

class Showing3Cats(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()
        self.title_words()
        self.images()
        self.infos()
        self.main_page_btn()
        self.url()

    # 標題文字
    def title_words(self):
        self.title = tk.Label(self, height = 3, text='最適合你的貓咪', font=('Times', 20, 'bold'), bg='green')
        self.title.grid(row = 0, column = 0, columnspan=3, sticky = tk.NE + tk.SW)

    # Resize圖片大小(在label框框中)
    def resize(self, w_box, h_box, pil_image):  
        w, h = pil_image.size
        f1 = 1.0*w_box/w  
        f2 = 1.0*h_box/h  
        factor = min([f1, f2])
        width = int(w*factor)  
        height = int(h*factor)  
        return pil_image.resize((width, height), Image.ANTIALIAS) 

    # 三張照片
    def images(self):
        w = 100
        h = 300
        wt = 200
        ht = 200
        img1 = Image.open(cats_dict[first][5])
        img1_resized = self.resize(wt, ht, img1)
        img2 = Image.open(cats_dict[second][5])
        img2_resized = self.resize(wt, ht, img2)
        img3 = Image.open(cats_dict[third][5])
        img3_resized = self.resize(wt, ht, img3)

        self.photo1 = ImageTk.PhotoImage(img1_resized)
        self.photo2 = ImageTk.PhotoImage(img2_resized)
        self.photo3 = ImageTk.PhotoImage(img3_resized)

        self.image1 = tk.Label(self, image = self.photo1, height = h, width = w, bg='red')
        self.image2 = tk.Label(self, image = self.photo2, height = h, width = w, bg='blue')
        self.image3 = tk.Label(self, image = self.photo3, height = h, width = w, bg='purple')

        self.image1.grid(row = 1, column = 0, sticky = tk.NE + tk.SW)
        self.image2.grid(row = 1, column = 1, sticky = tk.NE + tk.SW)
        self.image3.grid(row = 1, column = 2, sticky = tk.NE + tk.SW)

    # 資訊欄(名 性別 花色 年齡)
    def infos(self):
        w = 37
        name1, gender1, color1, yrs1 = cats_dict[first][0], cats_dict[first][1], cats_dict[first][2], cats_dict[first][3]
        name2, gender2, color2, yrs2 = cats_dict[second][0], cats_dict[second][1], cats_dict[second][2], cats_dict[second][3]
        name3, gender3, color3, yrs3 = cats_dict[third][0], cats_dict[third][1], cats_dict[third][2], cats_dict[third][3]

        self.info1 = tk.Label(self, height = 5, width = w, text = '姓名:{name}\n性別:{gender}\n年紀:{yrs}\n花色:{color}'.format(name=name1, gender=gender1, yrs=yrs1, color=color1), anchor="w", justify = 'left')
        self.info2 = tk.Label(self, height = 5, width = w, text = '姓名:{name}\n性別:{gender}\n年紀:{yrs}\n花色:{color}'.format(name=name2, gender=gender2, yrs=yrs2, color=color2), anchor="w", justify = 'left')
        self.info3 = tk.Label(self, height = 5, width = w, text = '姓名:{name}\n性別:{gender}\n年紀:{yrs}\n花色:{color}'.format(name=name3, gender=gender3, yrs=yrs3, color=color3), anchor="w", justify = 'left')

        self.info1.grid(row = 2, column = 0, sticky = tk.W)
        self.info2.grid(row = 2, column = 1, sticky = tk.W)
        self.info3.grid(row = 2, column = 2, sticky = tk.W)
    
    # 網頁連結
    def url(self):
        w=37
        url1 = cats_dict[first][4]
        url2 = cats_dict[second][4]
        url3 = cats_dict[third][4]

        self.web1 = tk.Button(self, height = 1, width = w, text = '點我查看詳細資料', command = lambda: webbrowser.open(url1))
        self.web2 = tk.Button(self, height = 1, width = w, text = '點我查看詳細資料', command = lambda: webbrowser.open(url2))
        self.web3 = tk.Button(self, height = 1, width = w, text = '點我查看詳細資料', command = lambda: webbrowser.open(url3))
        self.web1.grid(row = 3, column = 0, sticky = tk.NE + tk.SW)
        self.web2.grid(row = 3, column = 1, sticky 
        = tk.NE + tk.SW)
        self.web3.grid(row = 3, column = 2, sticky = tk.NE + tk.SW)

    # 回到主頁
    def main_page_btn(self):
        self.main_page = tk.Button(self, height = 2, text='Main Page')
        self.main_page.grid(row=4, column=0, columnspan=3, sticky = tk.NE + tk.SW)

# 顯示
window = Showing3Cats()
window.master.title('cats')
window.master.geometry('800x600')
window.configure(background='white')
window.mainloop()
