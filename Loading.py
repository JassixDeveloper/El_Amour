from tkinter import ttk
from tkinter.ttk import Progressbar
from tkinter import *
import os

w=Tk()

width_of_window = 427
height_of_window = 250
screen_width = w.winfo_screenwidth()
screen_height = w.winfo_screenheight()
x_coordinate = (screen_width/2)-(width_of_window/2)
y_coordinate = (screen_height/2)-(height_of_window/2)
w.geometry("%dx%d+%d+%d" %(width_of_window,height_of_window,x_coordinate,y_coordinate))

w.overrideredirect(1)

s = ttk.Style()
s.theme_use('clam')
s.configure("red.Horizontal.TProgressbar", foreground='red', background='#4f4f4f')
progress=Progressbar(w,style="red.Horizontal.TProgressbar",orient=HORIZONTAL,length=500,mode='determinate',)

def new_win():
    os.system("main.py")

def bar():
    l4=Label(w,text='Loading...',fg='white',bg=a)
    lst4=("Helvetica 12")
    l4.config(font=lst4)
    l4.place(x=18,y=210)
    
    import time
    r=0
    for i in range(100):
        progress['value']=r
        w.update_idletasks()
        time.sleep(0.03)
        r=r+1
        
    w.destroy()
    new_win()
    
progress.place(x=-5,y=235)

a='#765ac8'
logo_frame=Frame(w,width=430,height=241,bg=a)
logo_frame.place(x=-2,y=-2)
logo_img=PhotoImage(file="./Assets/logo.png")
Label(logo_frame,image=logo_img,relief=FLAT,bg="white").place(x=0,y=0)
b1=Button(w,width=10,height=1,text='Get Started >',command=bar,bd=0,bg=a
          ,font="Helvetica 12",fg="white",activeforeground="white",activebackground=a)
b1.place(x=310,y=210)

w.mainloop()
