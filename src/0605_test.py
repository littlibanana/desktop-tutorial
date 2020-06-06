import tkinter as tk
from PIL import ImageTk
import tkinter.font as tkFont
import webbrowser
import csv
import random
import pygame
file = 'cat.wav'
pygame.mixer.init()
track = pygame.mixer.music.load(file)
pygame.mixer.music.play()

class Helper():
	def __init__(self, root):
		self.root = root
		self.root.config()  # ?
		self.root.title('Cat Adopting Helper')
		self.root.icon_img = ImageTk.PhotoImage(file='小圖示.png')
		self.root.iconphoto(True, self.root.icon_img)  # 設定視窗標題前的小圖示(jpg檔不適用)(布林值為True代表每個視窗都用一樣圖示)
		self.root.geometry('1000x563+145+30')  # 設定視窗啟動時的大小與位置(寬x長+左位移+右位移)(此長寬為ppt等比例縮放尺寸)
		#self.root.resizable(False, False)
		self.root.ft = tkFont.Font(family='内海フォント-Bold', size=15, weight=tkFont.BOLD)  #　設定文字字體、大小、粗細
		#initface(self.root)
		#part1_endingface(self.root,1,2,10)
		part1_questionface(self.root)

class initface():
	def __init__(self, root):
		self.root = root
		self.initface = tk.Canvas(self.root, bd=0, width=1000, height=563, highlightthickness=0) # 設定畫布大小
		self.background_img = ImageTk.PhotoImage(file = 'background_initface.png')  # 若要讓此圖片尺寸符合canvas且保持ppt原畫面比例，此背景圖檔需先調整。(做法:用ppt做好後另存新檔成圖片、再用"小畫家3D"點選裁剪、右上角設定、鎖定外觀比例&與畫布一起調整圖片大小、寬度設定與width一樣，再儲存即完成)
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


file1 = "question_part1.csv"
filesopen = open(file1, 'r', newline='')
rows = csv.reader(filesopen)
question_list = []
for row in rows:
	question_list.append(row)

# 讀取貓咪資料存進dict
file2 = "貓咪.csv"
filesopen = open(file2, 'r', newline='')
rows = csv.reader(filesopen)
cat_dict = dict()
for row in rows:
	cat_dict[int(row[0])] = row[1:]


class part1_questionface():
	# 讀取問題存進dict
	def __init__(self, root):
		self.root = root
		self.part1_questionface = tk.Canvas(self.root,bd=0, width=1000,height=563, highlightthickness=0)
		self.background_img = ImageTk.PhotoImage(file = 'part1_question_background.png')
		self.part1_questionface.create_image(500, 280, image=self.background_img)#?
		self.part1_questionface.grid()
		self.color_list = []
		self.cat_score = {}
		for cat_id in cat_dict.keys():
			self.cat_score[int(cat_id)] = 60 # 分數60起跳    
		#self.click1()
		#self.click2()
		#self.get_3_cat()
		self.q_id = 0
		self.questionlbl = tk.Label(self.part1_questionface, text = question_list[0][0], bg = 'gray', fg = 'white', font = self.root.ft)
		self.questionlbl.grid()#place(anchor = 'center', relx = 0.5, rely = 0.45)
		self.ans_btn1 = tk.Button(self.part1_questionface, text = question_list[0][1], height = 1, width = 5, font = self.root.ft, bg="white", fg = 'pink', anchor = tk.CENTER, command = lambda: self.click1(question_list, cat_dict, self.cat_score, self.color_list, self.q_id))#?
		self.ans_btn1.grid()#.place(anchor = 'center', relx = 0.3, rely = 0.8)
		self.ans_btn2 = tk.Button(self.part1_questionface, text = question_list[0][2], height = 1, width = 5, font = self.root.ft, bg="white", fg = 'pink', anchor = tk.CENTER, command = lambda: self.click2(question_list, cat_dict, self.cat_score, self.color_list, self.q_id))
		self.ans_btn2.grid()#.place(anchor = 'center', relx = 0.7, rely = 0.8)
		self.part1_questionface.create_window(500, 200, height=40, window = self.questionlbl)#width=200, 
		self.part1_questionface.create_window(310, 300, width=200, height=40, window = self.ans_btn1)#, 
		self.part1_questionface.create_window(650, 300, width=200, height=40, window = self.ans_btn2)#width=200, 


	def click1(self, question_list, cat_dict, cat_score, color_list, i):
		global q_id
		for cat_id in cat_dict.keys():  # 計算分數
			if self.q_id <= 12:
				if question_list[self.q_id][1] == cat_dict[cat_id][self.q_id]:
					self.cat_score[cat_id] += int(question_list[self.q_id][3])
				else:
					self.cat_score[cat_id] += int(question_list[self.q_id][4])
			else:
				if self.q_id == 13:
					if color_list[0] == cat_dict[cat_id][self.q_id]:
						self.cat_score[cat_id] += int(question_list[self.q_id][3])
				elif self.q_id == 14:
					if color_list[1] == cat_dict[cat_id][self.q_id]:
						self.cat_score[cat_id] += int(question_list[self.q_id][3])
				else:
					if color_list[0] == cat_dict[cat_id][self.q_id]:
						self.cat_score[cat_id] += int(question_list[self.q_id][3])
		if self.q_id >= 10:  # 製造最後三題
			if self.q_id <= 12:
				color_list.append(question_list[self.q_id][1])
		if self.q_id <= 15:  # 進下一題
			self.q_id += 1
		if self.q_id <= 15:
			if self.q_id == 13:
				self.questionlbl.config(text = question_list[self.q_id][0]+color_list[0]+"還是"+color_list[1]+"？")
				self.ans_btn1.config(text = color_list[0])
				self.ans_btn2.config(text = color_list[1])
			elif self.q_id == 14:
				self.questionlbl.config(text = question_list[self.q_id][0]+color_list[1]+"還是"+color_list[2]+"？")
				self.ans_btn1.config(text = color_list[1])
				self.ans_btn2.config(text = color_list[2])
			elif self.q_id == 15:
				self.questionlbl.config(text = question_list[self.q_id][0]+color_list[0]+"還是"+color_list[2]+"？")
				self.ans_btn1.config(text = color_list[0])
				self.ans_btn2.config(text = color_list[2])
			else:
				self.questionlbl.config(text = question_list[self.q_id][0])
				self.ans_btn1.config(text = question_list[self.q_id][1])
				self.ans_btn2.config(text = question_list[self.q_id][2])
		else:
			print(self.cat_score)
			self.max_id_all = self.get_3_cat(self.cat_score) 
			print(self.max_id_all)
			self.change_part1_endingface(self.max_id_all)

	def click2(self, question_list, cat_dict, cat_score, color_list, i):
		global q_id
		for cat_id in cat_dict.keys():  # 計算分數
			if self.q_id <= 12:
				if question_list[self.q_id][2] == cat_dict[cat_id][self.q_id]:
					self.cat_score[cat_id] += int(question_list[self.q_id][5])
				else:
					self.cat_score[cat_id] += int(question_list[self.q_id][6])
			else:
				if self.q_id == 13:
					if color_list[1] == cat_dict[cat_id][self.q_id]:
						self.cat_score[cat_id] += int(question_list[self.q_id][3])
				elif self.q_id == 14:
					if color_list[2] == cat_dict[cat_id][self.q_id]:
						self.cat_score[cat_id] += int(question_list[self.q_id][3])
				else:
					if color_list[2] == cat_dict[cat_id][self.q_id]:
						self.cat_score[cat_id] += int(question_list[self.q_id][3])
		if self.q_id >= 10:  # 製造最後三題
			if self.q_id <= 12:
				color_list.append(question_list[self.q_id][2])
		if self.q_id <= 15:  # 進下一題
			self.q_id += 1
		if self.q_id <= 15:
			if self.q_id == 13:
				self.questionlbl.config(text = question_list[self.q_id][0]+color_list[0]+"還是"+color_list[1]+"？")
				self.ans_btn1.config(text = color_list[0])
				self.ans_btn2.config(text = color_list[1])
			elif self.q_id == 14:
				self.questionlbl.config(text = question_list[self.q_id][0]+color_list[1]+"還是"+color_list[2]+"？")
				self.ans_btn1.config(text = color_list[1])
				self.ans_btn2.config(text = color_list[2])
			elif self.q_id == 15:
				self.questionlbl.config(text = question_list[self.q_id][0]+color_list[0]+"還是"+color_list[2]+"？")
				self.ans_btn1.config(text = color_list[0])
				self.ans_btn2.config(text = color_list[2])
			else:
				self.questionlbl.config(text = question_list[self.q_id][0])
				self.ans_btn1.config(text = question_list[self.q_id][1])
				self.ans_btn2.config(text = question_list[self.q_id][2])
		else:
			print(self.cat_score)
			self.max_id_all = self.get_3_cat(self.cat_score) 
			print(self.max_id_all)
			self.change_part1_endingface(self.max_id_all)

	def get_3_cat(self, cat_score):
		# 找分數前三高貓咪
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
	
	def change_part1_endingface(self,max_id_all):
		self.max_id_all = max_id_all
		print(max_id_all)#error
		self.part1_questionface.destroy()
		part1_endingface(self.root, self.max_id_all[0], self.max_id_all[1], self.max_id_all[2])



# 貓的dict 含有超連結跟圖片位址跟貓的名字
cats_dict = dict()
with open(file='cat_info.csv', mode='r') as f:
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
		self.background_img = ImageTk.PhotoImage(file = 'part1_result_background.png')
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
		self.part1_endingface.destroy()
		initface(self.root)
		#self.part1_endingface.create_image(0, 0, anchor = tk.E, image = self.cat3_img)

'''
class part2_questionface():
	def __init__(self, root):
		self.root = root
		self.part2_questionface = 

	def change_part2_endingface(self):
		self.grade = grade
		self.destroy()
		part2_endingface(self.root, self.grade)


class part2_endingface():
	def __init__(self, root, grade):
		self.root = root
		self.grade = grade
		self.part2_endingface = tk.Canvas(self.root, bd=0, width=1000, height=600, highlightthickness=0)
		self.part2_endingface.grid()
		self.imglist = ['小龍女橘字.png','小龍女橘字.png','小龍女橘字.png','小龍女橘字.png','小龍女橘字.png','小龍女橘字.png']
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
		elif 10 < self.grade <= 20:
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