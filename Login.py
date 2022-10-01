from tkinter import *

root=Tk()
root.geometry("1920x1080")
root.wm_attributes('-fullscreen', 'True')

img=PhotoImage(file="./Assets/login_bg.png")
Label(root,image=img).place(x=0,y=0)

Label(root,text="Sign In",font=("Flourissha",60),bg="white").place(x=700,y=110)

Label(root,text="Name",font=("Arial",10,"bold"),fg="grey",bg="white").place(x=870,y=310)
Entry(root,font=("Abadi",12),bd=0,width=35).place(x=872,y=340,height=30)
Label(root,bg="black",width=45).place(x=872,y=370,height=2)

Label(root,text="Password",font=("Arial",10,"bold"),fg="grey",bg="white").place(x=870,y=420)
Entry(root,font=("Abadi",12),bd=0,width=35).place(x=872,y=450,height=30)
Label(root,bg="black",width=45).place(x=872,y=480,height=2)

Button(root,text="Forget Password",bd=0,bg="white",cursor="hand2",fg="red"
       ,activeforeground="red",activebackground="white",font=("Abadi",10)).place(x=872,y=495)

Button(root,text="Submit",bd=0,bg="#4361ee",cursor="hand2",fg="white",width=26
       ,activeforeground="white",activebackground="#4361ee",font=("Arial",16)).place(x=875,y=558)

Label(root,text="Don't have an account?",font=("Arial",10),fg="grey",bg="white").place(x=935,y=613)

Button(root,text="Sign up",bd=0,bg="white",cursor="hand2",fg="grey"
       ,activeforeground="grey",activebackground="white",font=("Abadi",10,"bold")).place(x=1072,y=611)

Label(root,text="ⓒ 2022 El Amour.in | All Rights Reserved",font=("Arial",10),fg="grey",bg="white").place(x=665,y=700)

root.mainloop()
