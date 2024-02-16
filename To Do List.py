from tkinter import *
from tkinter import messagebox
from tkinter import ttk


def add():
    task = input.get()
    if task != "":
        lb.insert(END, task)
        input.delete(0, "end")
    else:
        messagebox.showwarning("warning", "Nothing to add")


def deleteTask():
    lb.delete(ANCHOR)


window = Tk()
window.geometry('500x450')
window.title('To Do list')
window.config(bg='#1B3828')
window.resizable(width=False, height=False)
msg = Message(window, text="This is what you should do today:", width=200, background='#1B3828', fg='white',
              font=("Arial", 10))
msg.pack(side=TOP, pady=(15, 5))
frame = Frame(window)
frame.pack(pady=10)
lb = Listbox(
    frame,
    width=40,
    height=10,
    font=('Times', 15),
    bd=0,
    fg='white',
    highlightthickness=0,
    selectbackground='#5DC28A',
    background='#3B7A57',
    activestyle="none",

)
lb.pack(side=LEFT, fill=BOTH)
task_list = [
    'Do Homework',
    'Learn programming',
    'Read about databases',
    'Don\'t forget to pass an exam',
    'Print docs',
    'Find Keys'
]

for item in task_list:
    lb.insert(END, item)

sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

msg = Message(window, text="Insert a task:", width=200, background='#1B3828', fg='white', font=("Arial", 10))
msg.pack(side=TOP, pady=(0, 0))
input = Entry(
    window,
    background='#1B5A17',
    borderwidth=0,
    fg='white',
    font=('times', 24),

)
input.pack(pady=5)

button_frame = Frame(window)
button_frame.pack(pady=3)

addTask_btn = Button(
    button_frame,
    text='+',
    font=('times 14'),
    bg='black',
    fg='white',
    padx=20,
    pady=10,
    command=add,
    borderwidth=0,

)
addTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

delTask_btn = Button(
    button_frame,
    text='-',
    font=('times 14'),
    bg='black',
    fg='white',
    padx=20,
    pady=10,
    command=deleteTask,
    borderwidth=0
)
delTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

window.mainloop()
