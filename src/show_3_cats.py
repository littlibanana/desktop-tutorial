import tkinter as tk
from PIL import Image, ImageTk
import csv
import webbrowser
import random

# 讀取問題存進dict
file = "src\\question_part1.csv"
filesopen = open(file, 'r', newline='')
rows = csv.reader(filesopen)
question_list = []
for row in rows:
    question_list.append(row)

# 讀取貓咪資料存進dict
file1 = "src\\貓咪.csv"
filesopen = open(file1, 'r', newline='')
rows = csv.reader(filesopen)
cat_dict = dict()
for row in rows:
    cat_dict[int(row[0])] = row[1:]

q_id = 0

def click1(question_list, cat_dict, cat_score, color_list, i):
    global q_id
    global stop
    for cat_id in cat_dict.keys():  # 計算分數
        if q_id <= 12:
            if question_list[q_id][1] == cat_dict[cat_id][q_id]:
                cat_score[cat_id] += int(question_list[q_id][3])
            else:
                cat_score[cat_id] += int(question_list[q_id][4])
        else:
            if q_id == 13:
                if color_list[0] == cat_dict[cat_id][q_id]:
                    cat_score[cat_id] += int(question_list[q_id][3])
            elif q_id == 14:
                if color_list[1] == cat_dict[cat_id][q_id]:
                    cat_score[cat_id] += int(question_list[q_id][3])
            else:
                if color_list[0] == cat_dict[cat_id][q_id]:
                    cat_score[cat_id] += int(question_list[q_id][3])
    if q_id >= 10:  # 製造最後三題
        if q_id <= 12:
            color_list.append(question_list[q_id][1])
    if q_id < 15:  # 進下一題
        q_id += 1
    if q_id <= 15:
        if q_id == 13:
            questionlbl.config(text = question_list[q_id][0]+color_list[0]+"還是"+color_list[1]+"？")
            ans_btn1.config(text = color_list[0])
            ans_btn2.config(text = color_list[1])
        elif q_id == 14:
            questionlbl.config(text = question_list[q_id][0]+color_list[1]+"還是"+color_list[2]+"？")
            ans_btn1.config(text = color_list[1])
            ans_btn2.config(text = color_list[2])
        elif q_id == 15:
            questionlbl.config(text = question_list[q_id][0]+color_list[0]+"還是"+color_list[2]+"？")
            ans_btn1.config(text = color_list[0])
            ans_btn2.config(text = color_list[2])
        else:
            questionlbl.config(text = question_list[q_id][0])
            ans_btn1.config(text = question_list[q_id][1])
            ans_btn2.config(text = question_list[q_id][2])
    else:
        pass

def click2(question_list, cat_dict, cat_score, color_list, i):
    global q_id
    global stop
    for cat_id in cat_dict.keys():  # 計算分數
        if q_id <= 12:
            if question_list[q_id][2] == cat_dict[cat_id][q_id]:
                cat_score[cat_id] += int(question_list[q_id][5])
            else:
                cat_score[cat_id] += int(question_list[q_id][6])
        else:
            if q_id == 13:
                if color_list[1] == cat_dict[cat_id][q_id]:
                    cat_score[cat_id] += int(question_list[q_id][3])
            elif q_id == 14:
                if color_list[2] == cat_dict[cat_id][q_id]:
                    cat_score[cat_id] += int(question_list[q_id][3])
            else:
                if color_list[2] == cat_dict[cat_id][q_id]:
                    cat_score[cat_id] += int(question_list[q_id][3])
    if q_id >= 10:  # 製造最後三題
        if q_id <= 12:
            color_list.append(question_list[q_id][2])
    if q_id < 15:  # 進下一題
        q_id += 1
    if q_id <= 15:
        if q_id == 13:
            questionlbl.config(text = question_list[q_id][0]+color_list[0]+"還是"+color_list[1]+"？")
            ans_btn1.config(text = color_list[0])
            ans_btn2.config(text = color_list[1])
        elif q_id == 14:
            questionlbl.config(text = question_list[q_id][0]+color_list[1]+"還是"+color_list[2]+"？")
            ans_btn1.config(text = color_list[1])
            ans_btn2.config(text = color_list[2])
        elif q_id == 15:
            questionlbl.config(text = question_list[q_id][0]+color_list[0]+"還是"+color_list[2]+"？")
            ans_btn1.config(text = color_list[0])
            ans_btn2.config(text = color_list[2])
        else:
            questionlbl.config(text = question_list[q_id][0])
            ans_btn1.config(text = question_list[q_id][1])
            ans_btn2.config(text = question_list[q_id][2])
    else:
        pass

def get_3_cat(cat_score):
    '''找分數前三高貓咪'''
    max_id_all = []
    for i in range(3):
        max = -1
        max_id = []
        for cat_id in cat_score.keys():
            if cat_score[cat_id] > max:
                max_id = []
                max = cat_score[cat_id]
                max_id.append(cat_id)
            elif cat_score[cat_id] == max:
                max_id.append(cat_id)
            else:
                pass
        if len(max_id_all) + len(max_id) <= 3:
            for id in max_id:
                max_id_all.append(id)
                del cat_score[id]
        else:
            need_num = 3 - len(max_id_all)
            max_id = random.sample(max_id, need_num)
            for id in max_id:
                max_id_all.append(id)
                del cat_score[id]
        if len(max_id_all) >= 3:
            break
    return max_id_all


win = tk.Tk()
win.geometry('500x300')
win.config(bg = '#323232')


color_list = []
cat_score = {}
for cat_id in cat_dict.keys():
    cat_score[int(cat_id)] = 60 # 分數60起跳    

questionlbl = tk.Label(text = question_list[0][0], bg = 'gray', fg = 'white', font = '微軟正黑體 25')
questionlbl.place(anchor = 'center', relx = 0.5, rely = 0.45)
ans_btn1 = tk.Button(text = question_list[0][1], height = 1, width = 5, font = '微軟正黑體 20', command = lambda: click1(question_list, cat_dict, cat_score, color_list, q_id))
ans_btn2 = tk.Button(text = question_list[0][2], height = 1, width = 5, font = '微軟正黑體 20', command = lambda: click2(question_list, cat_dict, cat_score, color_list, q_id))
ans_btn1.place(anchor = 'center', relx = 0.3, rely = 0.8)
ans_btn2.place(anchor = 'center', relx = 0.7, rely = 0.8) 
win.mainloop()

print(cat_score)
max_id_all = get_3_cat(cat_score)
print(max_id_all)


# 存進貓資料dict
cats_dict = dict()
with open(file='src\\cat_info.csv', mode='r') as f:
    rows = csv.reader(f)
    for row in rows:
        cnum = int(row[0])
        # name, gen, color, yrs, url, photo site
        datalst = [row[1], row[2], row[3], row[4], row[5], row[6]]
        cats_dict[cnum] = datalst

# 選到的三隻貓
first = max_id_all[0]
second = max_id_all[1]
third = max_id_all[2]

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
