import csv

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
        for id in max_id:
            max_id_all.append(id)
            del cat_score[id]
        if len(max_id_all)>3:
            break
    return(max_id_all)

import tkinter as tk
import random


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
max_id_all = random.sample(max_id_all,3)
print(max_id_all)



