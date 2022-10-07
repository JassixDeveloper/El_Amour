from tkinter import *
import os

root=Tk()
root.geometry("1920x1080")
root.wm_attributes('-fullscreen', 'True')

def sup_hover(e):
    sup_btn["bg"]='white'
    sup_btn["fg"]='blue'

def sup_hover_leave(e):
    sup_btn["bg"]="white"
    sup_btn["fg"]='grey'

def open_signup():
    root.withdraw()
    os.system("signup.py")
    root.destroy()

img=PhotoImage(file="./Assets/login_bg.png")
Label(root,image=img).place(x=0,y=0)

img1=PhotoImage(file="./Assets/back.png")
back_btn=Button(root,image=img1,bg="white",bd=0,activebackground="white")
back_btn.place(x=190,y=130)

Label(root,text="Sign In",font=("Flourissha",60),bg="white").place(x=700,y=110)

Label(root,text="Name",font=("Arial",10,"bold"),fg="grey",bg="white").place(x=870,y=310)
Entry(root,font=("Abadi",12),bd=0,width=35).place(x=872,y=340,height=30)
Label(root,bg="black",width=45).place(x=872,y=370,height=2)

Label(root,text="Password",font=("Arial",10,"bold"),fg="grey",bg="white").place(x=870,y=420)
Entry(root,font=("Abadi",12),bd=0,width=35).place(x=872,y=450,height=30)
Label(root,bg="black",width=45).place(x=872,y=480,height=2)

Button(root,text="Forgot Password?",bd=0,bg="white",cursor="hand2",fg="red"
       ,activeforeground="red",activebackground="white",font=("Abadi",10)).place(x=872,y=495)

s_btn=Button(root,text="Submit",bd=0,bg="#4361ee",cursor="hand2",fg="white",width=26
       ,activeforeground="white",activebackground="#4361ee",font=("Arial",16))
s_btn.place(x=875,y=558)

Label(root,text="Don't have an account?",font=("Arial",10),fg="grey",bg="white").place(x=935,y=613)

sup_btn=Button(root,text="Sign up",bd=0,bg="white",cursor="hand2",fg="grey"
       ,activeforeground="blue",activebackground="white",font=("Abadi",10,"bold"),command=open_signup)
sup_btn.place(x=1072,y=611)

sup_btn.bind("<Enter>",sup_hover)
sup_btn.bind("<Leave>",sup_hover_leave)

Label(root,text="ⓒ 2022 El Amour.in | All Rights Reserved",font=("Arial",10),fg="grey",bg="white").place(x=665,y=700)

root.mainloop()
