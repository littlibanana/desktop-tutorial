import tkinter as tk
import random
import csv

def PART2():

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

    random_num = random.choices(range(0, 29), k = 10)
    print(random_num)
    final_question = []
    for num in random_num:
        final_question.append(question_list[num])
    
    return final_question

win = tk.Tk()
win.geometry('1000x500')
win.config(bg = '#323232')


number = 0


def test1(i):
    global number
    if number < 9:    
        number += 1
    temp = questions[i]
    answer[temp] = 1
    i += 1
    if i <= 9:
        questionlbl.config(text = questions[i])
        ans_btn1.config(text = option1s[i])
        ans_btn2.config(text = option2s[i])
    print(answer)
    

def test2(i):
    global number
    if number < 9:    
        number += 1
    answer[questions[i]] = 2
    i += 1
    if i <= 9:    
        questionlbl.config(text = questions[i])
        ans_btn1.config(text = option1s[i])
        ans_btn2.config(text = option2s[i])
    print(answer)
    

def test3():
    global number
    if number > 0:
        number -= 1
        answer[questions[number]] = ''
        questionlbl.config(text = questions[number])
        ans_btn1.config(text = option1s[number])
        ans_btn2.config(text = option2s[number])
    print(answer)
questions = []
option1s = []
option2s = []
questions_list = PART2()

for q in questions_list:
    questions.append(q['question'])
    option1s.append(q['option1'])
    option2s.append(q['option2'])
    

questionlbl = tk.Label(text = questions[number], bg = 'gray', fg = 'white', font = '微軟正黑體 25')
questionlbl.place(anchor = 'center', relx = 0.5, rely = 0.45)



answer = {}
ans_btn1 = tk.Button(text = option1s[number], height = 1, width = 20, font = '微軟正黑體 20', command = lambda: test1(number))
ans_btn2 = tk.Button(text = option2s[number], height = 1, width = 20, font = '微軟正黑體 20', command = lambda: test2(number))
ans_btn1.place(anchor = 'center', relx = 0.3, rely = 0.8)
ans_btn2.place(anchor = 'center', relx = 0.7, rely = 0.8)

back_btn = tk.Button(text = '上一題', font = '微軟正黑體 15', command = test3)
back_btn.place(anchor = 'center', relx = 0.9, rely = 0.9)

win.mainloop()