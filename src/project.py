import tkinter as tk
from PIL import ImageTk
import tkinter.font as tkFont
import webbrowser
import csv

class Helper():
	def __init__(self, root):
		self.root = root
		self.root.config()  # ?
		self.root.title('Cat Adopting Helper')
		self.root.icon_img = ImageTk.PhotoImage(file='src\\小圖示.png')
		self.root.iconphoto(True, self.root.icon_img)  # 設定視窗標題前的小圖示(jpg檔不適用)(布林值為True代表每個視窗都用一樣圖示)
		self.root.geometry('1000x563+145+30')  # 設定視窗啟動時的大小與位置(寬x長+左位移+右位移)(此長寬為ppt等比例縮放尺寸)
		#self.root.resizable(False, False)
		self.root.ft = tkFont.Font(family='内海フォント-Bold', size=15, weight=tkFont.BOLD)  #　設定文字字體、大小、粗細
		#initface(self.root)
		part1_endingface(self.root,1,2,10)


class initface():
	def __init__(self, root):
		self.root = root
		self.initface = tk.Canvas(self.root, bd=0, width=1000, height=563, highlightthickness=0) # 設定畫布大小
		self.background_img = ImageTk.PhotoImage(file = 'src\\background_initface.png')  # 若要讓此圖片尺寸符合canvas且保持ppt原畫面比例，此背景圖檔需先調整。(做法:用ppt做好後另存新檔成圖片、再用"小畫家3D"點選裁剪、右上角設定、鎖定外觀比例&與畫布一起調整圖片大小、寬度設定與width一樣，再儲存即完成)
		self.initface.create_image(400, 280, image=self.background_img)  # 設定圖片在畫布上的位置(原點(錨定點)預設為畫布左上角，前兩參數為圖片正中間那個點的座標)
		self.initface.grid()#sticky = tk.NE
		self.btn1 = tk.Button(self.initface, text='小幫手Part 1', font = self.root.ft, bg="white", fg = 'pink', anchor = tk.CENTER,command=self.change_part1_questionface)  # 設定按鈕上的文字、字體、按鈕被景色、按鈕文字色、按鈕文字位置
		self.btn1.grid()
		self.btn2 = tk.Button(self.initface, text='小幫手Part 2', font = self.root.ft, bg="white", fg = 'pink', anchor = tk.CENTER,command=self.change_part2_questionface)
		self.btn2.grid()
		self.initface.create_window(800, 420, width=200, height=40, window = self.btn1)  # 設定按鈕的位置、長寬
		self.initface.create_window(800, 470, width=200, height=40, window = self.btn2)
		
	def change_part1_questionface(self):
		self.initface.destroy()
		part1_questionface(self.root)

	def change_part2_questionface(self):
		self.initface.destroy()
		part2_questionface(self.root)


'''
class part1_questionface():
		self.background_img = ImageTk.PhotoImage(file = 'src\\part1_question_background.png')


class part2_questionface():
	def __init__(self, root):
		self.root = root
		self.part2_questionface = 

	def change_part2_endingface(self):
		self.grade = grade
		self..destroy()
		part2_endingface(self.root, self.grade)
'''
# 貓的dict 含有超連結跟圖片位址跟貓的名字
cats_dict = dict()
with open(file='src\\cat_info.csv', mode='r') as f:
    rows = csv.reader(f)
    for row in rows:
        cnum = int(row[0])
        # url, image, name
        datas = [row[5], row[6], row[1]]
        cats_dict[cnum] = datas

class part1_endingface():
	def __init__(self, root, cat1, cat2, cat3):  # cat1為貓編號(從1開始)
		self.root = root
		self.part1_endingface = tk.Canvas(self.root, bd=0, width=1000, height=563, highlightthickness=0)
		self.background_img = ImageTk.PhotoImage(file = 'src\\part1_result_background.png')
		self.part1_endingface.create_image(500, 280, image=self.background_img) #?
		self.part1_endingface.grid()
		self.cat1_img = ImageTk.PhotoImage(file = cats_dict[cat1][1])
		self.cat2_img = ImageTk.PhotoImage(file = cats_dict[cat2][1])
		self.cat3_img = ImageTk.PhotoImage(file = cats_dict[cat3][1])
		self.lb1 = tk.Label(self.part1_endingface, image = self.cat1_img)
		self.lb1.grid()
		self.lb2 = tk.Label(self.part1_endingface, image = self.cat2_img)
		self.lb2.grid()
		self.lb3 = tk.Label(self.part1_endingface, image = self.cat3_img)
		self.lb3.grid()
		self.btn_cat1 = tk.Button(self.part1_endingface,text='點此看{name}的資訊'.format(name=cats_dict[cat1][2]), font = self.root.ft, bg="white", fg = 'orange', anchor = tk.CENTER, command = lambda: webbrowser.open(cats_dict[cat1][0]))  # 設定按鈕上的文字、字體、按鈕被景色、按鈕文字色、按鈕文字位置
		self.btn_cat1.grid()
		self.btn_cat2 = tk.Button(self.part1_endingface,text='點此看{name}的資訊'.format(name=cats_dict[cat2][2]), font = self.root.ft, bg="white", fg = 'orange', anchor = tk.CENTER, command = lambda: webbrowser.open(cats_dict[cat2][0]))  # 設定按鈕上的文字、字體、按鈕被景色、按鈕文字色、按鈕文字位置
		self.btn_cat2.grid()
		self.btn_cat3 = tk.Button(self.part1_endingface,text='點此看{name}的資訊'.format(name=cats_dict[cat3][2]), font = self.root.ft, bg="white", fg = 'orange', anchor = tk.CENTER, command = lambda: webbrowser.open(cats_dict[cat3][0]))  # 設定按鈕上的文字、字體、按鈕被景色、按鈕文字色、按鈕文字位置
		self.btn_cat3.grid()
		self.btn_initface = tk.Button(self.part1_endingface,text='回到主頁', font = self.root.ft, bg="white", fg = 'pink', anchor = tk.CENTER, command=self.change_initface)  # 設定按鈕上的文字、字體、按鈕被景色、按鈕文字色、按鈕文字位置
		self.btn_initface.grid()
		self.part1_endingface.create_window(220, 265, width=160, height=335,window = self.lb1)
		self.part1_endingface.create_window(500, 265, width=160, height=335,window = self.lb2)
		self.part1_endingface.create_window(780, 265, width=160, height=335,window = self.lb3)
		self.part1_endingface.create_window(500, 510, anchor=tk.CENTER, width=200, height=40, window = self.btn_initface)
		self.part1_endingface.create_window(220, 460, anchor=tk.CENTER, width=180, height=40, window = self.btn_cat1)
		self.part1_endingface.create_window(500, 460, anchor=tk.CENTER, width=180, height=40, window = self.btn_cat2)
		self.part1_endingface.create_window(780, 460, anchor=tk.CENTER, width=180, height=40, window = self.btn_cat3)

	def change_initface(self):
		self.part2_endingface.destroy()
		initface(self.root)
		#self.part1_endingface.create_image(0, 0, anchor = tk.E, image = self.cat3_img)

		'''
		self.btn1 = tk.Button(self.part1_endingface,text='小幫手Part 1',font = self.root.ft,bg="white",fg = 'pink',anchor = tk.CENTER,command=self.change_part1_questionface)  # 設定按鈕上的文字、字體、按鈕被景色、按鈕文字色、按鈕文字位置
		self.btn1.grid()
		self.btn2 = tk.Button(self.part1_endingface,text='小幫手Part 2',font = self.root.ft,bg="white",fg = 'pink',anchor = tk.CENTER,command=self.change_part2_questionface)
		self.btn2.grid()
		self.part1_endingface.create_window(800, 420, width=200, height=40,window = self.btn1)  # 設定按鈕的位置、長寬
		self.part1_endingface.create_window(800, 470, width=200, height=40,window = self.btn2)
	def change_part1_questionface(self):
		self.initface.destroy()
		part1_questionface(self.root)

	def change_part2_questionface(self):
		self.initface.destroy()
		part2_questionface(self.root)
		'''

'''

class part2_endingface():
	def __init__(self, root, grade):
		self.root = root
		self.grade = grade
		self.part2_endingface = tk.Canvas(self.root, bd=0, width=1000, height=600, highlightthickness=0)
		self.part2_endingface.grid()
		self.imglist = ["小龍女橘字.png"]
		if self.grade <= 10:
			self.img = ImageTk.PhotoImage(file = self.imglist[0])
		elif 10 < self.grade <= 20:
			self.img = ImageTk.PhotoImage(file = self.imglist[1])
		elif 10 < self.grade <= 20:
			self.img = ImageTk.PhotoImage(file = self.imglist[2])
		elif 10 < self.grade <= 20:
			self.img = ImageTk.PhotoImage(file = self.imglist[3])
		elif 10 < self.grade <= 20:
			self.img = ImageTk.PhotoImage(file = self.imglist[4])
		elif 10 < self.grade <= 20:s
			self.img = ImageTk.PhotoImage(file = self.imglist[5])
		elif 10 < self.grade <= 20:
			self.img = ImageTk.PhotoImage(file = self.imglist[6])
		self.part2_endingface.create_image(0, 0, anchor = tk.NW, image = self.img)
		self.lb = tk.Label(text = '98',bg ='lemon chiffon') #'#323232'
		self.lb.grid()
		self.part2_endingface.create_window(800, 330, width=200, height=40,window = self.lb)
		self.btn = tk.Button(text = '回到主頁', font = self.root.ft, bg="white", fg = 'pink', anchor = tk.CENTER, command=self.change_initface)
		self.btn.grid()
		self.part2_endingface.create_window(880, 330, width=200, height=40,window = self.btn)
		

	def change_initface(self):
		self.part2_endingface.destroy()
		initface(self.root)

		
'''

if __name__ == '__main__':  # ?
	root = tk.Tk()
	Helper(root)
	root.mainloop()
