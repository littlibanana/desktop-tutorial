import tkinter as tk
import random
import csv
import webbrowser
import tkinter.font as tkFont
from PIL import ImageTk, Image
import pygame
import winsound
from skimage import io
#import getpass
import winreg

def get_desktop():
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')
    return winreg.QueryValueEx(key, "Desktop")[0]
'''
user = getpass.getuser()
user_desktop = 'C:\\Users\\'+user+'\\Desktop\\'
'''
user_desktop = get_desktop()+'\\\\'
#print(user_desktop)
file = 'music.wav'
pygame.mixer.init()
track = pygame.mixer.music.load(file)
pygame.mixer.music.play(-1)


def read_PART2_question():

    with open(file='part2.csv', mode='r', encoding='utf-8-sig') as part2:
        question_list = []  # list of dict
        csvfile = csv.DictReader(part2)
        for row in csvfile:
            question_dict = {}
            question_dict['question'] = row['question']
            question_dict['option1'] = row['option1']
            question_dict['option2'] = row['option2']
            question_dict['answer'] = row['answer']
            question_dict['info'] = row['info']
            question_dict['score1'] = row['score1']
            question_dict['score2'] = row['score2']

            question_list.append(question_dict)

    random_num = []
    while len(random_num) <= 10:
        tmp_num = random.choice(range(0, 29))
        if tmp_num not in random_num:
            random_num.append(tmp_num)
    # print(random_num)
    final_question = []

    for num in random_num:
        final_question.append(question_list[num])

    questions = []
    option1s = []
    option2s = []
    true_answers = []
    info = []
    btn_1_score = []
    btn_2_score = []

    for q in final_question:
        questions.append(q['question'])
        option1s.append(q['option1'])
        option2s.append(q['option2'])
        true_answers.append(q['answer'])
        info.append(q['info'])
        btn_1_score.append(q['score1'])
        btn_2_score.append(q['score2'])

    return questions, option1s, option2s, true_answers, info, btn_1_score, btn_2_score


questions, option1s, option2s, true_answers, info, btn_1_score, btn_2_score = read_PART2_question()

# print(true_answers)
answer = {}
number = 0
part2_grade = 0


class Helper():
    def __init__(self, root):
        self.root = root
        self.root.config()  # ?
        self.root.title('Cat Adopting Helper')
        self.root.icon_img = ImageTk.PhotoImage(file='小圖示.png')
        # 設定視窗標題前的小圖示(jpg檔不適用)(布林值為True代表每個視窗都用一樣圖示)
        self.root.iconphoto(True, self.root.icon_img)
        # 設定視窗啟動時的大小與位置(寬x長+左位移+右位移)(此長寬為ppt等比例縮放尺寸)
        self.root.geometry('1000x563+145+30')
        # self.root.resizable(False, False)
        self.root.ft = tkFont.Font(
            family='内海フォント-Bold', size=15, weight=tkFont.BOLD)  # 　設定文字字體、大小、粗細
        self.root.ft1 = tkFont.Font(
            family='内海フォント-Bold', size=20, weight=tkFont.BOLD)
        self.root.ft2 = tkFont.Font(
            family='内海フォント-Bold', size=40, weight=tkFont.BOLD)
        # part1_endingface(self.root,1,2,10)
        #initface(self.root)
        part2_endingface(self.root,95)


class initface():
    def __init__(self, root):
        self.root = root
        self.initface = tk.Canvas(
            self.root, bd=0, width=1000, height=563, highlightthickness=0)  # 設定畫布大小
        # 若要讓此圖片尺寸符合canvas且保持ppt原畫面比例，此背景圖檔需先調整。(做法:用ppt做好後另存新檔成圖片、再用"小畫家3D"點選裁剪、右上角設定、鎖定外觀比例&與畫布一起調整圖片大小、寬度設定與width一樣，再儲存即完成)
        self.background_img = ImageTk.PhotoImage(
            file='background_initface.png')
        # 設定圖片在畫布上的位置(原點(錨定點)預設為畫布左上角，前兩參數為圖片正中間那個點的座標)
        self.initface.create_image(400, 280, image=self.background_img)
        self.initface.grid()  # sticky = tk.NE
        self.btn1 = tk.Button(self.initface, text='Part1 貓咪速配小遊戲', font=self.root.ft, bg="white", fg='pink',
                              anchor=tk.CENTER, command=self.change_part1_questionface)  # 設定按鈕上的文字、字體、按鈕被景色、按鈕文字色、按鈕文字位置
        self.btn1.grid()
        self.btn2 = tk.Button(self.initface, text='Part2 貓咪知識小學堂', font=self.root.ft, bg="white",
                              fg='pink', anchor=tk.CENTER, command=self.change_part2_questionface)
        self.btn2.grid()
        self.btn3 = tk.Button(self.initface, text='我想給回饋!!!', font=self.root.ft, bg="white",
                              fg='pink', anchor=tk.CENTER, command=lambda: webbrowser.open('https://forms.gle/1bRsQAEoicZD1v9G6'))
        self.btn3.grid()
        self.initface.create_window(
            800, 370, width=220, height=40, window=self.btn1)  # 設定按鈕的位置、長寬
        self.initface.create_window(
            800, 420, width=220, height=40, window=self.btn2)
        self.initface.create_window(
            800, 470, width=220, height=40, window=self.btn3)

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

pic_list = [['虎斑.png', '三花.png'], ['白底橘.png', '乳牛.png'], ['黑貓.png', '金吉拉.png']]


class part1_questionface():
    # 讀取問題存進dict
    def __init__(self, root):
        self.root = root
        self.part1_questionface = tk.Canvas(
            self.root, bd=0, width=1000, height=563, highlightthickness=0)
        self.background_img = ImageTk.PhotoImage(
            file='part1_question_background.png')
        self.part1_questionface.create_image(
            500, 280, image=self.background_img)  # ?
        self.part1_questionface.grid()
        self.color_list = []
        self.cat_score = {}
        for cat_id in cat_dict.keys():
            self.cat_score[int(cat_id)] = 60  # 分數60起跳
        # self.click1()
        # self.click2()
        # self.get_3_cat()
        self.q_id = 0
        self.questionlbl = tk.Label(
            self.part1_questionface, text=question_list[0][0], bg='gray', fg='white', font=self.root.ft)
        self.questionlbl.grid()  # place(anchor = 'center', relx = 0.5, rely = 0.45)
        self.ans_btn1 = tk.Button(self.part1_questionface, text=question_list[0][1], height=1, font=self.root.ft, bg="white", fg='pink', anchor=tk.CENTER, command=lambda: self.click1(
            question_list, cat_dict, self.cat_score, self.color_list, self.q_id))  # ?
        self.ans_btn1.grid()  # .place(anchor = 'center', relx = 0.3, rely = 0.8)
        self.ans_btn2 = tk.Button(self.part1_questionface, text=question_list[0][2], height=1, font=self.root.ft, bg="white", fg='pink', anchor=tk.CENTER, command=lambda: self.click2(
            question_list, cat_dict, self.cat_score, self.color_list, self.q_id))
        self.ans_btn2.grid()  # .place(anchor = 'center', relx = 0.7, rely = 0.8)
        self.part1_questionface.create_window(
            500, 200, height=40, window=self.questionlbl)  # width=200,
        self.part1_questionface.create_window(
            310, 300, height=40, window=self.ans_btn1)  # ,
        self.part1_questionface.create_window(
            650, 300, height=40, window=self.ans_btn2)  # width=200,

    def click1(self, question_list, cat_dict, cat_score, color_list, i):
        global q_id
        for cat_id in cat_dict.keys():  # 計算分數
            if question_list[self.q_id][1] == cat_dict[cat_id][self.q_id]:
                self.cat_score[cat_id] += int(question_list[self.q_id][3])
            else:
                self.cat_score[cat_id] += int(question_list[self.q_id][4])
        if self.q_id <= 10:  # 進下一題
            self.q_id += 1
        if self.q_id <= 10:
            self.questionlbl.config(text=question_list[self.q_id][0])
            self.ans_btn1.config(text=question_list[self.q_id][1])
            self.ans_btn2.config(text=question_list[self.q_id][2])
            if self.q_id >= 8:
                if self.q_id == 8:
                    self.img_left = ImageTk.PhotoImage(file=pic_list[0][0])
                    self.img_right = ImageTk.PhotoImage(file=pic_list[0][1])
                elif self.q_id == 9:
                    self.img_left = ImageTk.PhotoImage(file=pic_list[1][0])
                    self.img_right = ImageTk.PhotoImage(file=pic_list[1][1])
                else:
                    self.img_left = ImageTk.PhotoImage(file=pic_list[2][0])
                    self.img_right = ImageTk.PhotoImage(file=pic_list[2][1])
                self.left = tk.Label(image=self.img_left)
                self.right = tk.Label(image=self.img_right)
                self.left.place(anchor='center', relx=0.31, rely=0.7)
                self.right.place(anchor='center', relx=0.65, rely=0.7)
        else:
            # print(self.cat_score)
            self.max_id_all = self.get_3_cat(self.cat_score)
            # print(self.max_id_all)
            self.change_part1_endingface(self.max_id_all)

    def click2(self, question_list, cat_dict, cat_score, color_list, i):
        global q_id
        for cat_id in cat_dict.keys():  # 計算分數
            if question_list[self.q_id][2] == cat_dict[cat_id][self.q_id]:
                self.cat_score[cat_id] += int(question_list[self.q_id][5])
            else:
                self.cat_score[cat_id] += int(question_list[self.q_id][6])
        if self.q_id <= 10:  # 進下一題
            self.q_id += 1
        if self.q_id <= 10:
            self.questionlbl.config(text=question_list[self.q_id][0])
            self.ans_btn1.config(text=question_list[self.q_id][1])
            self.ans_btn2.config(text=question_list[self.q_id][2])
            if self.q_id >= 8:
                if self.q_id == 8:
                    self.img_left = ImageTk.PhotoImage(file=pic_list[0][0])
                    self.img_right = ImageTk.PhotoImage(file=pic_list[0][1])
                elif self.q_id == 9:
                    self.img_left = ImageTk.PhotoImage(file=pic_list[1][0])
                    self.img_right = ImageTk.PhotoImage(file=pic_list[1][1])
                else:
                    self.img_left = ImageTk.PhotoImage(file=pic_list[2][0])
                    self.img_right = ImageTk.PhotoImage(file=pic_list[2][1])
                self.left = tk.Label(image=self.img_left)
                self.right = tk.Label(image=self.img_right)
                self.left.place(anchor='center', relx=0.31, rely=0.7)
                self.right.place(anchor='center', relx=0.65, rely=0.7)
        else:
            # print(self.cat_score)
            self.max_id_all = self.get_3_cat(self.cat_score)
            # print(self.max_id_all)
            self.change_part1_endingface(self.max_id_all)

    def get_3_cat(self, cat_score):
        # 找分數前三高貓咪
        max_id_all = []
        for _ in range(3):
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

    def change_part1_endingface(self, max_id_all):
        self.max_id_all = max_id_all
        # print(max_id_all)  # error
        self.part1_questionface.destroy()
        part1_endingface(
            self.root, self.max_id_all[0], self.max_id_all[1], self.max_id_all[2])


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
        self.part1_endingface = tk.Canvas(
            self.root, bd=0, width=1000, height=563, highlightthickness=0)
        self.background_img = ImageTk.PhotoImage(
            file='part1_result_background.png')
        self.part1_endingface.create_image(
            500, 280, image=self.background_img)  # ?
        self.part1_endingface.grid()
        self.cat1_img = ImageTk.PhotoImage(file=cats_dict[cat1][1])
        self.cat2_img = ImageTk.PhotoImage(file=cats_dict[cat2][1])
        self.cat3_img = ImageTk.PhotoImage(file=cats_dict[cat3][1])
        self.lb1 = tk.Label(self.part1_endingface, image=self.cat1_img)
        self.lb1.grid()
        self.lb2 = tk.Label(self.part1_endingface, image=self.cat2_img)
        self.lb2.grid()
        self.lb3 = tk.Label(self.part1_endingface, image=self.cat3_img)
        self.lb3.grid()
        self.btn_cat1 = tk.Button(self.part1_endingface, text='點此看{name}的資訊'.format(
            name=cats_dict[cat1][2]), font=self.root.ft, bg="white", fg='orange', anchor=tk.CENTER, command=lambda: webbrowser.open(cats_dict[cat1][0]))  # 設定按鈕上的文字、字體、按鈕被景色、按鈕文字色、按鈕文字位置
        self.btn_cat1.grid()
        self.btn_cat2 = tk.Button(self.part1_endingface, text='點此看{name}的資訊'.format(
            name=cats_dict[cat2][2]), font=self.root.ft, bg="white", fg='orange', anchor=tk.CENTER, command=lambda: webbrowser.open(cats_dict[cat2][0]))  # 設定按鈕上的文字、字體、按鈕被景色、按鈕文字色、按鈕文字位置
        self.btn_cat2.grid()
        self.btn_cat3 = tk.Button(self.part1_endingface, text='點此看{name}的資訊'.format(
            name=cats_dict[cat3][2]), font=self.root.ft, bg="white", fg='orange', anchor=tk.CENTER, command=lambda: webbrowser.open(cats_dict[cat3][0]))  # 設定按鈕上的文字、字體、按鈕被景色、按鈕文字色、按鈕文字位置
        self.btn_cat3.grid()
        self.btn_initface = tk.Button(self.part1_endingface, text='回到主頁', font=self.root.ft, bg="white",
                                      fg='pink', anchor=tk.CENTER, command=self.change_initface)  # 設定按鈕上的文字、字體、按鈕被景色、按鈕文字色、按鈕文字位置
        self.btn_initface.grid()
        self.part1_endingface.create_window(
            220, 265, width=160, height=335, window=self.lb1)
        self.part1_endingface.create_window(
            500, 265, width=160, height=335, window=self.lb2)
        self.part1_endingface.create_window(
            780, 265, width=160, height=335, window=self.lb3)
        self.part1_endingface.create_window(
            500, 510, anchor=tk.CENTER, width=200, height=40, window=self.btn_initface)
        self.part1_endingface.create_window(
            220, 460, anchor=tk.CENTER, width=190, height=40, window=self.btn_cat1)
        self.part1_endingface.create_window(
            500, 460, anchor=tk.CENTER, width=190, height=40, window=self.btn_cat2)
        self.part1_endingface.create_window(
            780, 460, anchor=tk.CENTER, width=190, height=40, window=self.btn_cat3)

    def change_initface(self):
        self.part1_endingface.destroy()
        initface(self.root)


def part2_count_grade():
    results = []
    for i in range(0, 10):
        results.append(answer[i])
    # print(results)
    score = 100
    for i in range(0, 10):
        if str(results[i]) == '1':
            score += int(btn_1_score[i])
        if str(results[i]) == '2':
            score += int(btn_2_score[i])
    return score


class part2_questionface():
    def __init__(self, root):
        self.root = root
        self.part2_questionface = tk.Canvas(self.root, bd=0, width=1000,
                                            height=563, highlightthickness=0)
        self.background_img = ImageTk.PhotoImage(
            file='part2_question_background.png')
        self.part2_questionface.create_image(
            500, 280, image=self.background_img)
        self.part2_questionface.grid()
        self.questionlbl = tk.Label(
            text=str(number+1)+'.'+questions[number], bg='gray', fg='white', font=self.root.ft)

        self.questionlbl.place(anchor='center', relx=0.5, rely=0.4)

        self.ans_btn1 = tk.Button(
            text=option1s[number], height=1, font=self.root.ft, command=lambda: self.btn1(number), bg='pink', fg='white')
        self.ans_btn2 = tk.Button(
            text=option2s[number], height=1, font=self.root.ft, command=lambda: self.btn2(number), bg='pink', fg='white')
        self.ans_btn1.place(anchor='center', relx=0.3, rely=0.55)
        self.ans_btn2.place(anchor='center', relx=0.7, rely=0.55)

        self.back_btn = tk.Button(
            text='喵', font=self.root.ft, command=self.back, bg='white')
        self.back_btn.place(anchor='center', relx=0.85, rely=0.8)

    def back(self):
        global number
        if number == 0:
            winsound.PlaySound(
                r'meow.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)
        if number > 0:
            number -= 1
        answer[number] = ''
        self.questionlbl.config(text=str(number+1)+'.'+questions[number])
        self.ans_btn1.config(text=option1s[number])
        self.ans_btn2.config(text=option2s[number])
        # print(answer, number)

    def btn1(self, i):
        global number
        global part2_grade
        if number <= 9:
            number += 1

        answer[number-1] = 1

        if answer[number-1] == int(true_answers[number-1]):
            self.back_btn.place(anchor='center', relx=0.85, rely=0.8)
            self.questionlbl.place(anchor='center', relx=0.5, rely=0.45)
            self.correct_img = ImageTk.PhotoImage(
                file='correct_cat.png')
            self.questionlbl.config(image=self.correct_img, borderwidth=0)
            self.wronglbl = tk.Label(text='恭喜答對囉', bg='pink',
                                     fg='white', font=self.root.ft1)
            self.wronglbl.place(anchor='center', relx=0.5, rely=0.75)
            if number <= 9:
                self.back_btn.config(
                    text='下一題', command=lambda: self.next(number))
            if number == 10:
                self.back_btn.config(
                    text='點我看分數', command=self.to_part2_end)
                part2_grade = part2_count_grade()

            self.ans_btn1.place_forget()
            self.ans_btn2.place_forget()

        if answer[number-1] != int(true_answers[number-1]):
            self.back_btn.place(anchor='center', relx=0.85, rely=0.8)
            self.questionlbl.place(anchor='center', relx=0.5, rely=0.45)

            self.wronglbl = tk.Label(text='答錯囉', bg='orange red',
                                     fg='white', font=self.root.ft1)
            self.wronglbl.place(anchor='center', relx=0.55, rely=0.8)

            self.info_img = ImageTk.PhotoImage(
                file='part2_answers//'+str(info[number-1]))
            self.questionlbl.config(
                image=self.info_img, borderwidth=0)

            if number <= 9:
                if number == '0':
                    self.back_btn.config(
                        text='喵', command=lambda: self.next(number))
                if number != '0':
                    self.back_btn.config(
                        text='下一題', command=lambda: self.next(number))
            if number == 10:
                self.back_btn.config(
                    text='點我看分數', command=self.to_part2_end)
                part2_grade = part2_count_grade()
            self.ans_btn1.place_forget()
            self.ans_btn2.place_forget()

        # print(answer, number)

    def btn2(self, i):
        global number
        global part2_grade
        if number <= 9:
            number += 1

        answer[number-1] = 2

        if answer[number-1] == int(true_answers[number-1]):
            self.back_btn.place(anchor='center', relx=0.85, rely=0.8)
            self.questionlbl.place(anchor='center', relx=0.5, rely=0.45)

            self.correct_img = ImageTk.PhotoImage(
                file='correct_cat.png')
            self.questionlbl.config(image=self.correct_img, borderwidth=0)
            self.wronglbl = tk.Label(text='恭喜答對囉', bg='pink',
                                     fg='white', font=self.root.ft1)
            self.wronglbl.place(anchor='center', relx=0.5, rely=0.72)
            if number <= 9:
                self.back_btn.config(
                    text='下一題', command=lambda: self.next(number))
            if number == 10:
                self.back_btn.config(
                    text='點我看分數', command=self.to_part2_end)
                part2_grade = part2_count_grade()
            self.ans_btn1.place_forget()
            self.ans_btn2.place_forget()

        if answer[number-1] != int(true_answers[number-1]):
            self.back_btn.place(anchor='center', relx=0.85, rely=0.8)
            self.questionlbl.place(anchor='center', relx=0.5, rely=0.45)
            self.wronglbl = tk.Label(text='答錯囉', bg='orange red',
                                     fg='white', font=self.root.ft1)
            self.wronglbl.place(anchor='center', relx=0.55, rely=0.8)

            self.info_img = ImageTk.PhotoImage(
                file='part2_answers//'+str(info[number-1]))
            self.questionlbl.config(
                image=self.info_img, borderwidth=0)

            if number <= 9:
                if number == '0':
                    self.back_btn.config(
                        text='喵', command=lambda: self.next(number))
                if number != '0':
                    self.back_btn.config(
                        text='下一題', command=lambda: self.next(number))
            if number == 10:
                self.back_btn.config(
                    text='點我看分數', command=self.to_part2_end)
                part2_grade = part2_count_grade()
            self.ans_btn1.place_forget()
            self.ans_btn2.place_forget()
        # print(answer, number)

    def to_part2_end(self):
        global number
        global answer

        self.part2_questionface.destroy()
        part2_endingface(self.root, part2_grade)
        number = 0
        answer = {}

    def next(self, i):
        global number
        if number <= 9:
            self.questionlbl.config(
                text=str(number+1)+'.'+questions[number], image='')
            self.ans_btn1.config(text=option1s[number])
            self.ans_btn2.config(text=option2s[number])
            self.ans_btn1.place(anchor='center', relx=0.3, rely=0.55)
            self.ans_btn2.place(anchor='center', relx=0.7, rely=0.55)
            self.questionlbl.place(anchor='center', relx=0.5, rely=0.4)
            # self.back_btn.config(text='上一題', command=self.back)
            self.back_btn.place_forget()
            self.wronglbl.place_forget()


class part2_endingface():
    def __init__(self, root, grade):
        #global part2_grade
        self.root = root
        self.grade = grade
        #self.grade = part2_grade
        #print(self.grade)
        self.part2_endingface = tk.Canvas(
            self.root, bd=0, width=1000, height=600, highlightthickness=0)
        self.part2_endingface.grid()
        self.imglist = ['paints\\招財喵.png', 'paints\\仙杜瑞喵.png', 'paints\\傻眼貓咪.png', 'paints\\白爛貓.png', 'paints\\柯南.png',
                        'paints\\躲貓貓.png', '60.png', 'paints\\令傑喵.png', 'paints\\多拉A喵.png', 'paints\\豆漿.png','paints\\小龍女.png']# paints\\小龍女.png
        if self.grade == 0:
            self.img = ImageTk.PhotoImage(file=self.imglist[0])
            self.introduce_btn = tk.Button(text='點我看招財貓由來', font=self.root.ft, bg="white",fg='pink', anchor=tk.CENTER, command=lambda: webbrowser.open('https://www.peekme.cc/post/763438'))
            self.introduce_btn.grid()
            self.part2_endingface.create_window(650, 520, width=180, height=40, window=self.introduce_btn)
            self.save_img=io.imread('download_imgs\\招財喵.png')
            self.save_img_btn = tk.Button(text='下載我的貓咪至桌面', font=self.root.ft, bg="white",fg='pink', anchor=tk.CENTER, command=lambda: io.imsave(user_desktop+'招財喵.png',self.save_img))
            self.save_img_btn.grid()
            self.part2_endingface.create_window(900, 20, width=200, height=40, window=self.save_img_btn)
        elif 0 < self.grade <= 10:
            self.img = ImageTk.PhotoImage(file=self.imglist[1])
            self.introduce_btn = tk.Button(text='點我看襤褸貓的介紹', font=self.root.ft, bg="white",fg='pink', anchor=tk.CENTER, command=lambda: webbrowser.open('https://kknews.cc/zh-tw/pet/yexak6n.html'))
            self.introduce_btn.grid()
            self.part2_endingface.create_window(650, 520, width=200, height=40, window=self.introduce_btn)
            self.save_img=io.imread('download_imgs\\先杜瑞喵.png')
            self.save_img_btn = tk.Button(text='下載我的貓咪至桌面', font=self.root.ft, bg="white",fg='pink', anchor=tk.CENTER, command=lambda: io.imsave(user_desktop+'先杜瑞喵.png',self.save_img))
            self.save_img_btn.grid()
            self.part2_endingface.create_window(900, 20, width=200, height=40, window=self.save_img_btn)
        elif 10 < self.grade <= 20:
            self.img = ImageTk.PhotoImage(file=self.imglist[2])
            self.introduce_btn = tk.Button(text='點我看奶牛貓洗澡視頻', font=self.root.ft, bg="white",fg='pink', anchor=tk.CENTER, command=lambda: webbrowser.open('https://youtu.be/eWXaPZMXahE'))
            self.introduce_btn.grid()
            self.part2_endingface.create_window(650, 520, width=250, height=40, window=self.introduce_btn)
            self.save_img=io.imread('download_imgs\\傻眼貓咪.png')
            self.save_img_btn = tk.Button(text='下載我的貓咪至桌面', font=self.root.ft, bg="white",fg='pink', anchor=tk.CENTER, command=lambda: io.imsave(user_desktop+'傻眼貓咪.png',self.save_img))
            self.save_img_btn.grid()
            self.part2_endingface.create_window(900, 20, width=200, height=40, window=self.save_img_btn)
        elif 20 < self.grade <= 30:
            self.img = ImageTk.PhotoImage(file=self.imglist[3])
            self.introduce_btn = tk.Button(text='點我看虎斑貓個性8大分析！', font=self.root.ft, bg="white",fg='pink', anchor=tk.CENTER, command=lambda: webbrowser.open('https://www.google.com/search?rlz=1C1CHBF_zh-TWTW903TW903&sxsrf=ALeKk01tMLLknrCUyAU756oeVyY2kof99g%3A1591718339825&ei=w7HfXvz9MeSWr7wP75iy0AY&q=%E6%9B%BC%E5%88%87%E5%A0%AA%E7%8C%AB&oq=%E6%9B%BC%E5%88%87&gs_lcp=CgZwc3ktYWIQARgAMgQIIxAnMgQIABBDMgIIADICCAAyAggAMgIIADICCAAyAggAMgIIADICCAA6BwgAEEcQsAM6BwgjEOoCECc6CQgjECcQRhD_AToFCAAQsQNQ8oUBWNmrAWDtxQFoAnAAeACAAbMBiAHqCJIBAzQuNpgBAKABAaoBB2d3cy13aXqwAQo&sclient=psy-ab'))
            self.introduce_btn.grid()
            self.part2_endingface.create_window(620, 520, width=300, height=40, window=self.introduce_btn)
            self.save_img=io.imread('download_imgs\\白爛喵.png')
            self.save_img_btn = tk.Button(text='下載我的貓咪至桌面', font=self.root.ft, bg="white",fg='pink', anchor=tk.CENTER, command=lambda: io.imsave(user_desktop+'白爛喵.png',self.save_img))
            self.save_img_btn.grid()
            self.part2_endingface.create_window(900, 20, width=200, height=40, window=self.save_img_btn)
        elif 30 < self.grade <= 40:
            self.img = ImageTk.PhotoImage(file=self.imglist[4])
            self.introduce_btn = tk.Button(text='點我看曼切堪猫介紹', font=self.root.ft, bg="white",fg='pink', anchor=tk.CENTER, command=lambda: webbrowser.open('https://www.google.com/search?rlz=1C1CHBF_zh-TWTW903TW903&sxsrf=ALeKk01tMLLknrCUyAU756oeVyY2kof99g%3A1591718339825&ei=w7HfXvz9MeSWr7wP75iy0AY&q=%E6%9B%BC%E5%88%87%E5%A0%AA%E7%8C%AB&oq=%E6%9B%BC%E5%88%87&gs_lcp=CgZwc3ktYWIQARgAMgQIIxAnMgQIABBDMgIIADICCAAyAggAMgIIADICCAAyAggAMgIIADICCAA6BwgAEEcQsAM6BwgjEOoCECc6CQgjECcQRhD_AToFCAAQsQNQ8oUBWNmrAWDtxQFoAnAAeACAAbMBiAHqCJIBAzQuNpgBAKABAaoBB2d3cy13aXqwAQo&sclient=psy-ab'))
            self.introduce_btn.grid()
            self.save_img=io.imread('download_imgs\\柯南喵.png')
            self.save_img_btn = tk.Button(text='下載我的貓咪至桌面', font=self.root.ft, bg="white",fg='pink', anchor=tk.CENTER, command=lambda: io.imsave(user_desktop+'柯南喵.png',self.save_img))
            self.save_img_btn.grid()
            self.part2_endingface.create_window(900, 20, width=200, height=40, window=self.save_img_btn)
        elif 40 < self.grade <= 50:
            self.img = ImageTk.PhotoImage(file=self.imglist[5])
            self.introduce_btn = tk.Button(text='點我看斯芬克斯貓介紹', font=self.root.ft, bg="white",fg='pink', anchor=tk.CENTER, command=lambda: webbrowser.open('https://www.google.com/search?rlz=1C1CHBF_zh-TWTW903TW903&sxsrf=ALeKk038ITmC4IeAtj7zAMkUEgjM1HKlsQ%3A1591718932390&ei=FLTfXpasF5KWr7wPru2daA&q=%E6%96%AF%E8%8A%AC%E5%85%8B%E6%96%AF%E8%B2%93&oq=%E6%96%AF%E8%8A%AC%E5%85%8B%E6%96%AF%E8%B2%93&gs_lcp=CgZwc3ktYWIQAzIECCMQJzICCAAyAggAMgIIADICCAAyAggAMgIIADICCAAyAggAMgIIADoHCCMQsAMQJzoFCAAQsAM6BwgAELADEB46CQgAELADEAcQHjoFCAAQsQNQ3tkSWM2FFGCpihRoAXAAeACAAYQBiAG-BZIBAzAuNpgBAKABAaABAqoBB2d3cy13aXo&sclient=psy-ab&ved=0ahUKEwiWhrCMj_XpAhUSy4sBHa52Bw0Q4dUDCAw&uact=5'))
            self.introduce_btn.grid()
            self.part2_endingface.create_window(650, 520, width=240, height=40, window=self.introduce_btn)
            self.save_img=io.imread('download_imgs\\斯芬克喵.png')
            self.save_img_btn = tk.Button(text='下載我的貓咪至桌面', font=self.root.ft, bg="white",fg='pink', anchor=tk.CENTER, command=lambda: io.imsave(user_desktop+'斯芬克喵.png',self.save_img))
            self.save_img_btn.grid()
            self.part2_endingface.create_window(900, 20, width=200, height=40, window=self.save_img_btn)
        elif 50 < self.grade <= 60:
            self.img = ImageTk.PhotoImage(file=self.imglist[6])
        elif 60 < self.grade <= 70:
            self.img = ImageTk.PhotoImage(file=self.imglist[7])
            self.introduce_btn = tk.Button(text='點我看麝香貓與咖啡的故事', font=self.root.ft, bg="white",fg='pink', anchor=tk.CENTER, command=lambda: webbrowser.open('https://www.natgeomedia.com/environment/article/content-6091.html'))
            self.introduce_btn.grid()
            self.part2_endingface.create_window(590, 520, width=340, height=40, window=self.introduce_btn)
            self.save_img=io.imread('download_imgs\\令傑喵.png')
            self.save_img_btn = tk.Button(text='下載我的貓咪至桌面', font=self.root.ft, bg="white",fg='pink', anchor=tk.CENTER, command=lambda: io.imsave(user_desktop+'令傑喵.png',self.save_img))
            self.save_img_btn.grid()
            self.part2_endingface.create_window(900, 20, width=200, height=40, window=self.save_img_btn)
        elif 70 < self.grade <= 80:
            self.img = ImageTk.PhotoImage(file=self.imglist[8])
            self.introduce_btn = tk.Button(text='點我看狸花貓介紹', font=self.root.ft, bg="white",fg='pink', anchor=tk.CENTER, command=lambda: webbrowser.open('https://kknews.cc/zh-tw/pet/zg5eryq.html'))
            self.introduce_btn.grid()
            self.part2_endingface.create_window(650, 520, width=200, height=40, window=self.introduce_btn)
            self.save_img=io.imread('download_imgs\\多拉A喵.png')
            self.save_img_btn = tk.Button(text='下載我的貓咪至桌面', font=self.root.ft, bg="white",fg='pink', anchor=tk.CENTER, command=lambda: io.imsave(user_desktop+'多拉A喵.png',self.save_img))
            self.save_img_btn.grid()
            self.part2_endingface.create_window(900, 20, width=200, height=40, window=self.save_img_btn)
        elif 80 < self.grade <= 90:
            self.img = ImageTk.PhotoImage(file=self.imglist[9])
            self.introduce_btn = tk.Button(text='點我看豆漿ig', font=self.root.ft, bg="white",fg='pink', anchor=tk.CENTER, command=lambda: webbrowser.open('https://www.instagram.com/soybeanmilk_cat/?hl=zh-tw'))
            self.introduce_btn.grid()
            self.part2_endingface.create_window(650, 520, width=200, height=40, window=self.introduce_btn)
            self.save_img=io.imread('download_imgs\\豆漿.png')
            self.save_img_btn = tk.Button(text='下載我的貓咪至桌面', font=self.root.ft, bg="white",fg='pink', anchor=tk.CENTER, command=lambda: io.imsave(user_desktop+'豆漿.png',self.save_img))
            self.save_img_btn.grid()
            self.part2_endingface.create_window(900, 20, width=200, height=40, window=self.save_img_btn)
        elif 90 < self.grade <= 100:
            self.img = ImageTk.PhotoImage(file=self.imglist[10])
            self.introduce_btn = tk.Button(text='點我看世界最美異瞳白貓姊妹花', font=self.root.ft, bg="white",fg='pink', anchor=tk.CENTER, command=lambda: webbrowser.open('https://pets.ettoday.net/news/750605'))
            self.introduce_btn.grid()
            self.part2_endingface.create_window(600, 520, width=300, height=40, window=self.introduce_btn)
            self.save_img=io.imread('download_imgs\\小龍女喵.png')
            self.save_img_btn = tk.Button(text='下載我的貓咪至桌面', font=self.root.ft, bg="white",fg='pink', anchor=tk.CENTER, command=lambda: io.imsave(user_desktop+'小龍女喵.png',self.save_img))
            self.save_img_btn.grid()
            self.part2_endingface.create_window(900, 20, width=200, height=40, window=self.save_img_btn)
        self.part2_endingface.create_image(500, 280, image=self.img)  # anchor=tk.NW,
        self.part2_endingface.grid()
        self.lb = tk.Label(text='你的分數是 : '+str(self.grade), font=self.root.ft2, bg="white",fg='orange', anchor=tk.CENTER)  # '#323232' bg='lemon chiffon'
        self.lb.grid()
        self.part2_endingface.create_window(500, 40, width=450, height=70, window=self.lb)
        self.btn_initface = tk.Button(text='回到主頁', font=self.root.ft, bg="white",fg='pink', anchor=tk.CENTER, command=self.change_initface)
        self.btn_initface.grid()
        self.part2_endingface.create_window(870, 520, width=150, height=40, window=self.btn_initface)
        

    def change_initface(self):
        global questions, option1s, option2s, true_answers, info, btn_1_score, btn_2_score
        self.part2_endingface.destroy()
        initface(self.root)
        questions, option1s, option2s, true_answers, info, btn_1_score, btn_2_score = read_PART2_question()


if __name__ == '__main__':  # ?
    root = tk.Tk()
    root.resizable(0, 0)
    Helper(root)
    root.mainloop()
