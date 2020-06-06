import tkinter as tk
import random
import csv
import pygame


file = 'cat.wav'
pygame.mixer.init()
track = pygame.mixer.music.load(file)
pygame.mixer.music.play()


def read_PART2_question():

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

    random_num = []
    while len(random_num) <= 10:
        tmp_num = random.choice(range(0, 29))
        if tmp_num not in random_num:
            random_num.append(tmp_num)
    print(random_num)
    final_question = []

    for num in random_num:
        final_question.append(question_list[num])

    return final_question


questions = []
option1s = []
option2s = []
true_answers = []

info = []
btn_1_score = []
btn_2_score = []

questions_list = read_PART2_question()


for q in questions_list:
    questions.append(q['question'])
    option1s.append(q['option1'])
    option2s.append(q['option2'])
    true_answers.append(q['answer'])
    info.append(q['info'])
    btn_1_score.append(q['score1'])
    btn_2_score.append(q['score2'])

print(true_answers)
answer = {}
number = 0


class Part2(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.place()
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

    def back(self):
        global number
        if number > 0:
            number -= 1
        answer[number] = ''
        self.questionlbl.config(text=str(number+1)+','+questions[number])
        self.ans_btn1.config(text=option1s[number])
        self.ans_btn2.config(text=option2s[number])
        print(answer, number)

    def part2_count_grade(self):
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

    def btn1(self, i):
        global number
        if number <= 9:
            number += 1

        answer[number-1] = 1

        if answer[number-1] == int(true_answers[number-1]):
            self.questionlbl.config(text='恭喜答對')
            if number <= 9:
                self.back_btn.config(
                    text='下一題', command=lambda: self.next(number))
            if number == 10:
                self.back_btn.config(
                    text='點我看分數', command=lambda: self.next(number))
            self.ans_btn1.place_forget()
            self.ans_btn2.place_forget()

        if answer[number-1] != int(true_answers[number-1]):
            self.questionlbl.config(text='答錯囉，因為'+info[number-1])
            if number <= 9:
                self.back_btn.config(
                    text='下一題', command=lambda: self.next(number))
            if number == 10:
                self.back_btn.config(
                    text='點我看分數', command=lambda: self.next(number))
            self.ans_btn1.place_forget()
            self.ans_btn2.place_forget()

    def btn2(self, i):
        global number
        if number <= 9:
            number += 1

        answer[number-1] = 2

        if answer[number-1] == int(true_answers[number-1]):
            self.questionlbl.config(text='恭喜答對ฅ’ω’ฅ')
            if number <= 9:
                self.back_btn.config(
                    text='下一題', command=lambda: self.next(number))
            if number == 10:
                self.back_btn.config(
                    text='點我看分數', command=lambda: self.next(number))
            self.ans_btn1.place_forget()
            self.ans_btn2.place_forget()

        if answer[number-1] != int(true_answers[number-1]):
            self.questionlbl.config(text='答錯囉!'+info[number-1])
            if number <= 9:
                self.back_btn.config(
                    text='下一題', command=lambda: self.next(number))
            if number == 10:
                self.back_btn.config(
                    text='點我看分數', command=lambda: self.next(number))
            self.ans_btn1.place_forget()
            self.ans_btn2.place_forget()

        print(answer, number)

    def next(self, i):
        if number <= 9:
            self.questionlbl.config(text=str(number+1)+'.'+questions[number])
            self.ans_btn1.config(text=option1s[number])
            self.ans_btn2.config(text=option2s[number])
            self.ans_btn1.place(anchor='center', relx=0.3, rely=0.8)
            self.ans_btn2.place(anchor='center', relx=0.7, rely=0.8)
            self.back_btn.config(text='上一題', command=self.back)
        if number == 10:
            part2_grade = self.part2_count_grade()
            self.questionlbl.config(text='你的分數是:'+str(part2_grade)+'分')
            self.ans_btn1.place_forget()
            self.ans_btn2.place_forget()
            self.back_btn.config(text='回到首頁')  # 這裡加上回到主葉面的函數


part2 = Part2()
part2.master.title('Part2')
part2.mainloop()
