import tkinter as tk
import webbrowser
import random

#判斷程式
def start_btn_action():
    global frequency   #全域變數
    if question.get() == "" :
        message_label.config(text="不可空白")
        question.delete(0, tk.END)
    elif not question.get().isdigit():
        message_label.config(text="請輸入數字")
        question.delete(0, tk.END)
    elif len(question.get()) != 4 :
        message_label.config(text="請輸入4位數")
        question.delete(0, tk.END)
    elif len(question.get()) != len(set(question.get())):
        message_label.config(text="數字重覆")
        question.delete(0, tk.END)
    else:
        a_value=0; b_value =0
        a_value = [a_value+1 for i , item in enumerate(question.get()) if int(item) == answer[i]]
        b_value = [b_value+1 for i , item in enumerate(question.get()) if int(item) in answer]
        c_value= len(b_value)-len(a_value)
        no[frequency]= f"{question.get()} - {len(a_value)}A{c_value}B"
        record_label.config(text=f'遊戲記錄:\n① {no[0]}\n② {no[1]}\n③ {no[2]}\n④ {no[3]}\n⑤ {no[4]}\n⑥ {no[5]}\n⑦ {no[6]}\n⑧ {no[7]}\n⑨ {no[8]}\n⑩ {no[9]}')
        question.delete(0, tk.END)
        if frequency != 9:
            if len(a_value) == 4:
                message_label.config(text='恭喜過關')
                start_btn.config(state='disabled')
            else:
                message_label.config(text='')
        else:
            if len(a_value) == 4:
                message_label.config(text='恭喜過關')
                start_btn.config(state='disabled')
            else:
                answer_show = ''.join(map(str, answer))
                message_label.config(text=f'遊戲結束\n答案為: {answer_show}')
                start_btn.config(state='disabled')
        frequency += 1

def finish_btn_action():
    exit()

def restart_btn_action():
    global frequency
    global no
    global answer
    frequency = 0
    no = [' '] * 10
    answer = random.sample(number, 4)
    question.delete(0, tk.END)
    record_label.config(text='遊戲記錄:\n①\n②\n③\n④\n⑤\n⑥\n⑦\n⑧\n⑨\n⑩')
    message_label.config(text='')
    print(answer)
    start_btn.config(state='normal')

# 定義點擊超連結的函數
def open_link(event):
    webbrowser.open('https://github.com/fpdkeoo/1A2B')

#======================================================================
#產生數字
frequency = 0
no=[''] * 10
number=range(0,10)
answer=random.sample(number,4)

#======================================================================
# 視窗
root = tk.Tk()
root.title('1A2B猜數字')

#視窗大小位置
window_width = root.winfo_screenwidth()    # 取得螢幕寬度
window_height = root.winfo_screenheight()  # 取得螢幕高度
width = 400
height = 260
left = int((window_width - width)/2)       # 計算左上 x 座標
top = int((window_height - height)/2)      # 計算左上 y 座標
root.geometry(f'{width}x{height}+{left}+{top}')

#文字label
user_label=tk.Label(root,text='請輸入答案:',font=('Arial',18))
user_label.place(x=10, y=5)

record_label=tk.Label(root,text='遊戲記錄:\n①\n②\n③\n④\n⑤\n⑥\n⑦\n⑧\n⑨\n⑩',font=('Arial',14, 'bold'),justify='left')
record_label.place(x=230, y=5)

message_label=tk.Label(root,text='',font=('Arial',25),fg='#f00')
message_label.place(x=10, y=90)

#輸入
question = tk.Entry(root, font=('Arial', 15), width=5)  # 放入單行輸入框
question.place(x=145, y=5)

#按鈕
start_btn = tk.Button(root,text='確定',font=('Arial',15,'bold'), width=7 ,command=start_btn_action)
start_btn.place(x=10, y=38)

finish_btn = tk.Button(root,text='離開',font=('Arial',15,'bold'), width=7 ,command=finish_btn_action)
finish_btn.place(x=10, y=190)

restart_btn = tk.Button(root,text='重新開始',font=('Arial',15,'bold'), width=7 ,command=restart_btn_action)
restart_btn.place(x=115, y=190)

#===========================================================================
#出處
by_label=tk.Label(root,text='by: 點擊這裡訪問 fpdkeoo github',font=('Arial',10), fg='blue', cursor="hand2" )
by_label.place(x=10, y=235)
by_label.bind("<Button-1>", open_link)

root.mainloop()