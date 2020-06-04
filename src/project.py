import tkinter as tk
from PIL import ImageTk
import tkinter.font as tkFont
import webbrowser

class Helper():
	def __init__(self, root):
		self.root = root
		self.root.config()  # ?
		self.root.title('Cat Adopting Helper')
		self.root.iconphoto(True, tk.PhotoImage(file='C:\\Users\\JamieLin\\Desktop\\圖片11.png'))  # 設定視窗標題前的小圖示(jpg檔不適用)(布林值為True代表每個視窗都用一樣圖示)
		self.root.geometry('1000x563+145+30')  # 設定視窗啟動時的大小與位置(寬x長+左位移+右位移)(此長寬為ppt等比例縮放尺寸)
		#self.root.resizable(False, False)
		self.root.ft = tkFont.Font(family='内海フォント-Bold', size=15, weight=tkFont.BOLD)  #　設定文字字體、大小、粗細
		#initface(self.root)
		part1_endingface(self.root,1,2,3)


class initface():
	def __init__(self, root):
		self.root = root
		self.initface = tk.Canvas(self.root,bd=0, width=1000,height=563, highlightthickness=0) # 設定畫布大小
		self.background_img = ImageTk.PhotoImage(file = '圖片3.png')  # 若要讓此圖片尺寸符合canvas且保持ppt原畫面比例，此背景圖檔需先調整。(做法:用ppt做好後另存新檔成圖片、再用"小畫家3D"點選裁剪、右上角設定、鎖定外觀比例&與畫布一起調整圖片大小、寬度設定與width一樣，再儲存即完成)
		self.initface.create_image(400, 280, image=self.background_img)  # 設定圖片在畫布上的位置(原點(錨定點)預設為畫布左上角，前兩參數為圖片左上角那個點的座標)
		self.initface.grid()#sticky = tk.NE
		self.btn1 = tk.Button(self.initface,text='小幫手Part 1',font = self.root.ft,bg="white",fg = 'pink',anchor = tk.CENTER,command=self.change_part1_questionface)  # 設定按鈕上的文字、字體、按鈕被景色、按鈕文字色、按鈕文字位置
		self.btn1.grid()
		self.btn2 = tk.Button(self.initface,text='小幫手Part 2',font = self.root.ft,bg="white",fg = 'pink',anchor = tk.CENTER,command=self.change_part2_questionface)
		self.btn2.grid()
		self.initface.create_window(800, 420, width=200, height=40,window = self.btn1)  # 設定按鈕的位置、長寬
		self.initface.create_window(800, 470, width=200, height=40,window = self.btn2)
		
	def change_part1_questionface(self):
		self.initface.destroy()
		part1_questionface(self.root)

	def change_part2_questionface(self):
		self.initface.destroy()
		part2_questionface(self.root)


'''
class part1_questionface():


class part2_questionface():
	def __init__(self, root):
		self.root = root
		self.part2_questionface = 

	def change_part2_endingface(self):
		self.grade = grade
		self..destroy()
		part2_endingface(self.root, self.grade)
'''
class part1_endingface():
	def __init__(self, root, cat1, cat2, cat3):  # cat1...為貓編號(從1開始)
		self.root = root
		self.cat1 = cat1 - 1
		self.cat2 = cat2 - 1
		self.cat3 = cat3 - 1
		self.part1_endingface = tk.Canvas(self.root, bd=0, width=1000, height=563, highlightthickness=0)
		self.background_img = ImageTk.PhotoImage(file = 'background_nothing.png')
		self.part1_endingface.create_image(400, 280, image=self.background_img) #?
		self.part1_endingface.grid()
		self.imglist = ['奶酥.png','奶酥.png','奶酥.png']
		self.cat1_img = ImageTk.PhotoImage(file = self.imglist[self.cat1])
		self.cat2_img = ImageTk.PhotoImage(file = self.imglist[self.cat2])
		self.cat3_img = ImageTk.PhotoImage(file = self.imglist[self.cat3])
		self.lb1 = tk.Label(self.part1_endingface, image = self.cat1_img)
		self.lb1.grid()
		self.lb2 = tk.Label(self.part1_endingface, image = self.cat2_img)
		self.lb2.grid()
		self.lb3 = tk.Label(self.part1_endingface, image = self.cat3_img)
		self.lb3.grid()
		self.btn = tk.Button(self.part1_endingface,text='回到主頁', font = self.root.ft, bg="white", fg = 'pink', anchor = tk.CENTER, command=self.change_initface)  # 設定按鈕上的文字、字體、按鈕被景色、按鈕文字色、按鈕文字位置
		self.btn.grid()
		self.part1_endingface.create_window(250, 200, width=234, height=514,window = self.lb1)
		self.part1_endingface.create_window(400, 470, width=234, height=514,window = self.lb2)
		self.part1_endingface.create_window(800, 470, width=234, height=514,window = self.lb3)
		self.part1_endingface.create_window(400, 500, anchor=tk.CENTER, width=200, height=40,window = self.btn)

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
