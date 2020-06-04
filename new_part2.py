import tkinter as tk
import random
import csv
import pygame
file = 'cat.wav'
pygame.mixer.init()
track = pygame.mixer.music.load(file)
pygame.mixer.music.play()

def read_PART2():

    with open(file=r'C:/Users\User\Desktop\part2.csv', mode='r', encoding='utf-8-sig') as part2:
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

    random_num = random.choices(range(0, 29), k=10)
    print(random_num)
    final_question = []
    for num in random_num:
        final_question.append(question_list[num])

    return final_question


def count_grade():
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


questions = []
option1s = []
option2s = []
true_answers = []
info = []
btn_1_score = []
btn_2_score = []

questions_list = read_PART2()

for q in questions_list:
    questions.append(q['question'])
    option1s.append(q['option1'])
    option2s.append(q['option2'])
    true_answers.append(q['answer'])
    info.append(q['info'])
    btn_1_score.append(q['score1'])
    btn_2_score.append(q['score2'])


answer = {}
number = 0


class Part2(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()
        self.createWidgits()

    def createWidgits(self):

        self.questionlbl = tk.Label(
            text=questions[number], bg='gray', fg='white', font='微軟正黑體 25')
        self.questionlbl.place(anchor='center', relx=0.5, rely=0.45)

        self.ans_btn1 = tk.Button(
            text=option1s[number], height=1, width=20, font='微軟正黑體 20', command=lambda: self.btn1(number))
        self.ans_btn2 = tk.Button(
            text=option2s[number], height=1, width=20, font='微軟正黑體 20', command=lambda: self.btn2(number))
        self.ans_btn1.place(anchor='center', relx=0.3, rely=0.8)
        self.ans_btn2.place(anchor='center', relx=0.7, rely=0.8)

        self.back_btn = tk.Button(
            text='上一題', font='微軟正黑體 15', command=self.back)
        self.back_btn.place(anchor='center', relx=0.9, rely=0.9)

    def btn1(self, i):
        global number
        if number <= 9:
            number += 1

        answer[number-1] = 1

        if number <= 9:
            self.questionlbl.config(text=str(number+1)+'.'+questions[number])
            self.ans_btn1.config(text=option1s[number])
            self.ans_btn2.config(text=option2s[number])

        if number == 10:
            part2_grade = count_grade()
            self.questionlbl.config(text=part2_grade)
            self.ans_btn1.destroy()
            self.ans_btn2.destroy()
            self.back_btn.config(text='回到首頁')
        print(answer, number)

    def btn2(self, i):
        global number
        if number <= 9:
            number += 1

        answer[number-1] = 2

        if number <= 9:
            self.questionlbl.config(text=str(number+1)+'.'+questions[number])
            self.ans_btn1.config(text=option1s[number])
            self.ans_btn2.config(text=option2s[number])

        if number == 10:
            part2_grade = count_grade()
            self.questionlbl.config(text=part2_grade)
            self.ans_btn1.destroy()
            self.ans_btn2.destroy()
            self.back_btn.config(text='回到首頁')
        print(answer, number)

    def back(self):
        global number
        if number > 0:
            number -= 1
        answer[number] = ''
        self.questionlbl.config(text=str(number+1)+','+questions[number])
        self.ans_btn1.config(text=option1s[number])
        self.ans_btn2.config(text=option2s[number])
        print(answer, number)


part2 = Part2()
part2.master.title('Part2')
part2.mainloop()
