import time
import threading
import pynput.mouse  # pynput和tkinter都有Button这个包，注意区分
from pynput.keyboard import Key, Listener
from tkinter import *
import ctypes
from random import*
import requests
import math
from tkinter import ttk
from tqdm import tqdm
import zipfile
import tempfile
import tkinter.messagebox
import tkinter.simpledialog
import webbrowser
import os


LEFT = 0
RIGHT = 1
MIDDLE = 2

ON = 3
OFF = 4
lan = 2
# 鼠标连点控制类
class MouseClick:
    def __init__(self, button, time):
        self.mouse = pynput.mouse.Controller()
        self.running = False  # 确认是否在运行
        self.time = time
        self.button = button
        # 开启主监听线程
        self.listener = Listener(on_press=self.key_press)
        self.listener.start()

    def key_press(self, key):
        if key == Key.f8:
            if self.running:
                self.running = False
                state.delete('0.0', END)
                if lan == 2:
                    
                    state.insert(INSERT, "Current State: Listening\n")
                    state.insert(INSERT, "Press ESC to stop listening.\n")
                    state.insert(INSERT, "Press F8 to start clicking.")
                else:
                    state.insert(INSERT, "当前状态：正在监听按键\n")
                    state.insert(INSERT, "按下ESC键结束监听\n")
                    state.insert(INSERT, "按下F8键开始运行程序")
                # 停止连点也需要调用这个函数
                self.mouse_click()
            else:
                self.running = True
                state.delete('0.0', END)
                if lan == 2:
                    state.insert(INSERT, "Current State: Clicking\n")
                    state.insert(INSERT, "Press F8 to stop clicking.\n")
                else:
                    state.insert(INSERT, "当前状态：正在运行\n")
                    state.insert(INSERT, "按下F8键结束运行\n")
                self.mouse_click()
        elif key == Key.esc:
            btn_start['state'] = NORMAL
            state.delete('0.0', END)
            if lan == 2:
                state.insert(INSERT, "Current State: IDLE\n")
                state.insert(
                    INSERT, "Choose which mouse button you want to click and enter CPS in CPS setting, then click START button to start clicking.")
            else:
                state.insert(INSERT, "当前状态：空闲\n")
                state.insert(
                    INSERT, "选择一个鼠标点击对象并在CPS Setting一栏中输入CPS， 然后，你就可以点击'START'按钮以运行程序")
            # 退出主监听线程
            self.listener.stop()

    def mouse_click(self):
        # 这里还需要额外线程进行监听，为了能够更新self.running，防止陷入死循环
        key_listener = Listener(on_press=self.key_press)
        key_listener.start()
        while self.running:
            self.mouse.click(self.button)
            time.sleep(self.time)
    
        key_listener.stop()


# 新线程处理函数
def new_thread_start(button, time):
    MouseClick(button, time)


# START按键处理函数
def start():
    try:
        # 将文本框读到的字符串转化为浮点数
        ach = float(input.get())
        time = 1 / ach
        if mouse.get() == LEFT:
            button = pynput.mouse.Button.left
        elif mouse.get() == RIGHT:
            button = pynput.mouse.Button.right
        else:
            button = pynput.mouse.Button.middle
        btn_start['state'] = DISABLED
        state.delete('0.0', END)
        try:
            if lan == 2:
                try:
                    state.insert(INSERT, "Current State: Listening\n")
                    state.insert(INSERT, "Press ESC to stop listening.\n")
                    state.insert(INSERT, "Press F8 to start clicking.")
                except:
                    tkinter.messagebox.showerror('Error','Unknown error')
            else:
                try:
                    state.insert(INSERT, "当前状态：正在监听按键\n")
                    state.insert(INSERT, "按下ESC键结束监听\n")
                    state.insert(INSERT, "按下F8键开始运行程序")
                except:
                    tkinter.messagebox.showerror('Error','Unknown error')
        except:
            tkinter.messagebox.showerror('Error','Unknown error')
        # 开启新线程，避免GUI卡死
        t = threading.Thread(target=new_thread_start, args=(button, time))
        # 开启守护线程，这样在GUI意外关闭时线程能正常退出
        #t.setDaemon(True)
        t.start()
        # 不能使用 t.join()，否则也会卡死
    except:
        state.delete('0.0', END)
        if lan == 2:
            try:
                state.insert(INSERT, "CPS input ERROR!\n")
                state.insert(INSERT, "You should enter an integer or a float number.")
                tkinter.messagebox.showerror('Error','You should enter an integer or a float number.')
            except:
                tkinter.messagebox.showerror('Error','Unknown error')
        else:
            try:
                state.insert(INSERT, "CPS输入错误\n")
                state.insert(INSERT, "您应该在CPS Setting栏中输入一个实数")
                tkinter.messagebox.showerror('Error','You should enter an integer or a float number.')
            except:
                tkinter.messagebox.showerror('Error','Unknown error')

def about():
    state.delete('0.0', END)
    state.insert(INSERT, "MouseClicker PRO PLUS\n")
    state.insert(INSERT, "Version: 5.0.0 Build 6107 (Preview & Beta) \n")
    state.insert(INSERT, "2022/5/20 22:00 Update 27 (Made by 12sdj) \n")




def func(*args):
    global lan
    if (mode.get() == "简体中文（中国大陆）"):
        lan = 1
        state.delete('0.0', END)
        state.insert(INSERT, "语言已切换至'简体中文（中国大陆）' \n")
    else:
        lan = 2
        state.delete('0.0', END)
        state.insert(INSERT, "Language switched to 'English(United States)' \n")
        state.insert(INSERT, "CHANGE: \n")



def helpa():
        helpa = Toplevel()
        helpa.geometry("895x685")
        helpa.title("HELP")
        
        state = Text(helpa, relief="flat", font=("微软雅黑", 10))
        state.place(relx=0.03, y=10, relwidth=0.95, height=660)
        if lan == 2:
            state.insert(INSERT, "What is CPS?\n")
            state.insert(INSERT, "  CPS, is short for Click Per Second, means the number of clicks per second\n")
            state.insert(INSERT, "\n")
            state.insert(INSERT, "How to convert time interval to CPS?\n")
            state.insert(INSERT, "  TIME INTERVAL = 1/CPS \n")
        else:
            state.insert(INSERT, "什么是CPS？\n")
            state.insert(INSERT, "  CPS，是Click Per Second的简写，意思是每秒点击次数\n")
            state.insert(INSERT, "时间间隔和CPS怎么换算?\n")
            state.insert(INSERT, "  时间间隔 = 1/CPS \n")
        
    
        helpa.mainloop()






    
def logs():
    state.delete('0.0', END)
    state.insert(INSERT, "Update 27\n")
    state.insert(INSERT, "CHANGE: \n")
    
    state.insert(INSERT, "[Security]  \n")
    state.insert(INSERT, "Added the latest May 2022 dependency component patch to enhance software security  \n")
    state.insert(INSERT, "[Stability]  \n")
    state.insert(INSERT, "Using multi-threading technology, the program can be greatly improved to run stably. However, it will increase CPU power consumption  \n")
    state.insert(INSERT, "[Popularity]  \n")
    state.insert(INSERT, "Remove some unnecessary components. At the same time, add “? “to introduce component uses and to be more oriented towards game users  \n")
    state.insert(INSERT, "[Language universality]  \n")
    state.insert(INSERT, "Increase the Chinese Simplified  \n")
    state.insert(INSERT, "[Practicality]  \n")
    state.insert(INSERT, "Improved user interface. At the same time, the “Anti-Machine Cheat Detection” function was added (version 4.25)  \n")
    state.insert(INSERT, "[Quality Update]  \n")
    state.insert(INSERT, "Fixed bugs and introduced a bug-proofing mechanism to reduce the incidence of bugs  \n")

    state.insert(INSERT, "Update 26(Unpublished)\n")
    state.insert(INSERT, "CHANGE: \n")
    state.insert(INSERT, " 1. Improve user page \n")
    
    state.insert(INSERT, "Update 25(Unpublished)\n")
    state.insert(INSERT, "CHANGE: \n")
    state.insert(INSERT, " 1. Improve user page \n")
    
    state.insert(INSERT, "Update 24(Unpublished)\n")
    state.insert(INSERT, "CHANGE: \n")
    state.insert(INSERT, " 1. Improve user page \n")

    state.insert(INSERT, "Update 23(Unpublished)\n")
    state.insert(INSERT, "CHANGE: \n")
    state.insert(INSERT, " 1. Improve user page \n")

    state.insert(INSERT, "Update 22(Unpublished)\n")
    state.insert(INSERT, "CHANGE: \n")
    state.insert(INSERT, " 1. Improve user page \n")

    state.insert(INSERT, "Update 21(Unpublished)\n")
    state.insert(INSERT, "CHANGE: \n")
    state.insert(INSERT, " 1. Improve user page \n")

    state.insert(INSERT, "Update 20(Unpublished)\n")
    state.insert(INSERT, "CHANGE: \n")
    state.insert(INSERT, " 1. Improve user page \n")

    state.insert(INSERT, "Update 19(Unpublished)\n")
    state.insert(INSERT, "CHANGE: \n")
    state.insert(INSERT, " 1. Improve user page \n")

    state.insert(INSERT, "Update 18(Unpublished)\n")
    state.insert(INSERT, "CHANGE: \n")
    state.insert(INSERT, " 1. Improve user page \n")
    
    state.insert(INSERT, "Update 17(Unpublished)\n")
    state.insert(INSERT, "CHANGE: \n")
    state.insert(INSERT, " 1. Improve user page \n")
    
    state.insert(INSERT, "Update 16\n")
    state.insert(INSERT, "CHANGE: \n")
    state.insert(INSERT, " 1. Add a button \n")
    state.insert(INSERT, " 2. Optimization Experience to Reduce the bug occurs \n")
    
    state.insert(INSERT, "Update 15(Unpublished)\n")
    state.insert(INSERT, "CHANGE: \n")
    state.insert(INSERT, " 1. Add some buttons \n")
    
    state.insert(INSERT, "Update 14\n")
    state.insert(INSERT, "CHANGE: \n")
    state.insert(INSERT, " 1. Add Middle-click button \n")
    state.insert(INSERT, " 2. Optimize the user interface \n")
    
    state.insert(INSERT, "Update 13(Unpublished)\n")
    state.insert(INSERT, "CHANGE: \n")
    state.insert(INSERT, " 1. Fix bugs \n")
    state.insert(INSERT, " 2. Optimize the user interface \n")

    
def more():
    def handler():
        window = Toplevel()
        window.geometry("895x685")
        window.title("LICENSE")
        
        state = Text(window, relief="flat", font=("微软雅黑", 10))
        state.place(relx=0.03, y=10, relwidth=0.95, height=660)
        state.insert(INSERT, "MIT License\n")
        state.insert(INSERT, "\n")
        state.insert(INSERT, "Copyright (c) 2022 12sdj\n")
        state.insert(INSERT, "\n")
        state.insert(INSERT, "Permission is hereby granted, free of charge, to any person obtaining a copy\n")
        state.insert(INSERT, "of this software and associated documentation files (the 'Software'), to deal\n")
        state.insert(INSERT, "in the Software without restriction, including without limitation the rights\n")
        state.insert(INSERT, "to use, copy, modify, merge, publish, distribute, sublicense, and/or sell\n")
        state.insert(INSERT, "copies of the Software, and to permit persons to whom the Software is\n")
        state.insert(INSERT, "furnished to do so, subject to the following conditions:\n")
        state.insert(INSERT, "\n")
        state.insert(INSERT, "The above copyright notice and this permission notice shall be included in all\n")
        state.insert(INSERT, "copies or substantial portions of the Software.\n")
        state.insert(INSERT, "\n")
        state.insert(INSERT, "THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\n")
        state.insert(INSERT, "IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\n")
        state.insert(INSERT, "FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE\n")
        state.insert(INSERT, "AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\n")
        state.insert(INSERT, "LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,\n")
        state.insert(INSERT, "OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE\n")
        state.insert(INSERT, "SOFTWARE.\n")
        window.mainloop()
        
    
    def view():
        if tkinter.messagebox.askyesno('Ask', 'The following will open https://github.com/12sdj/MouseClicker-by-12sdj.git. Are you sure to execute?') == 1:
            try:
                webbrowser.open('https://github.com/12sdj/MouseClicker-by-12sdj.git')
            except:
                tkinter.messagebox.showerror('Error','Unknown error')
        
        
    otherFrame = Toplevel()
    otherFrame.geometry("540x300")
    otherFrame.title("MouseClicker PRO PLUS - More")
    

    btn = Button(otherFrame, text="LICENSE",font=('Arial', 14), command=handler)
    btn.pack()
    btn2 = Button(otherFrame, text="View the source code", font=('Arial', 14), command=view)
    btn2.pack()

    otherFrame.mainloop()

    
# -------------------------------- GUI界面 --------------------------------
root = Tk()
# 高dpi
winWidth = 850
winHeight = 330

ctypes.windll.shcore.SetProcessDpiAwareness(1)
ScaleFactor = ctypes.windll.shcore.GetScaleFactorForDevice(0)
root.tk.call('tk', 'scaling', ScaleFactor/75)
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()

x = int((screenWidth - winWidth) / 2)
y = int((screenHeight - winHeight) / 2)

root.title('MouseClicker PRO PLUS')
#root.geometry('850x330')
root.resizable(0,0)
root.geometry("%sx%s+%s+%s" % (winWidth, winHeight, x, y))
mouse = IntVar()
cheat = IntVar()

lab1 = Label(root, text='Mouse Button', font=("微软雅黑", 11), fg="gray")
lab1.place(relx=0.05, y=10, relwidth=0.4, height=30)
r1 = Radiobutton(root,
                 text='LEFT',
                 font=("微软雅黑", 10),
                 value=0,
                 variable=mouse)
r1.place(relx=0.05, y=40, relwidth=0.1, height=30)
r2 = Radiobutton(root,
                 text='RIGHT',
                 font=("微软雅黑", 10),
                 value=1,
                 variable=mouse)
r2.place(relx=0.18, y=40, relwidth=0.1, height=30)
r3 = Radiobutton(root,
                 text='MIDDLE',
                 font=("微软雅黑", 10),
                 value=2,
                 variable=mouse)
r3.place(relx=0.31, y=40, relwidth=0.12, height=30)

lab2 = Label(root, text='CPS Setting', font=("微软雅黑", 11), fg="gray")
lab2.place(relx=0.5, y=10, relwidth=0.45, height=30)

h1 = Button(root, text='?', font=('Arial', 10),command=helpa)
h1.place(relx=0.8, y=10, relwidth=0.04, height=30)

input = Entry(root, relief="flat", font=("微软雅黑", 10))
input.place(relx=0.575, y=40, relwidth=0.3, height=30)

label3 = Label(root,
               text='---------- Current State and Instruction ----------',
               font=("微软雅黑", 8),
               fg="gray")
label3.place(relx=0.5, y=90, relwidth=0.45, height=20)
state = Text(root, relief="flat", font=("微软雅黑", 10))
state.place(relx=0.5, y=110, relwidth=0.45, height=150)
state.insert(INSERT, "Current State: IDLE\n")
state.insert(INSERT, "Choose which mouse button you want to click and enter CPS in CPS Setting, then click START button to start listening.")

btn_start = Button(root,
                   text='START',
                   font=("微软雅黑", 12),
                   fg="white",
                   bg="#207fdf",
                   relief="flat",
                   command=start)
btn_start.place(relx=0.5, y=280, relwidth=0.45, height=30)
b2 = Button(root, text='ABOUT', font=('Arial', 10),command=about)
b2.place(relx=0.07, y=250, relwidth=0.16, height=30)

b3 = Button(root, text='CHANGELOG', font=('Arial', 10),command=logs)
b3.place(relx=0.23, y=250, relwidth=0.20, height=30)
b4 = Button(root, text='MORE', font=('Arial', 10),command=more)
b4.place(relx=0.07, y=280, relwidth=0.36, height=30)


lag = Label(root, text='Anti-Machine Cheat Detection', font=("微软雅黑", 11), fg="gray")
lag.place(relx=0.05, y=100, relwidth=0.4, height=30)

xon = Radiobutton(root,
                 text='ON',
                 font=("微软雅黑", 10),
                 value=3,
                 variable=cheat)
xon.place(relx=0.07, y=140, relwidth=0.15, height=30)
xr = Radiobutton(root,
                 text='OFF',
                 font=("微软雅黑", 10),
                 value=4,
                 variable=cheat)
xr.place(relx=0.25, y=140, relwidth=0.15, height=30)
xr.select()


mode = StringVar()
cmb = ttk.Combobox(root,textvariable=mode, state='readonly',width = 20)
cmb.pack()
# 设置下拉菜单中的值
cmb['value'] = ('简体中文（中国大陆）','English(United States)')

# 设置默认值，即默认下拉框中的内容
cmb.current(1)
# 默认值中的内容为索引，从0开始


cmb.bind("<<ComboboxSelected>>",func)






root.mainloop()
