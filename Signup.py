from tkinter import *

root=Tk()
root.geometry("1920x1080")
root.wm_attributes('-fullscreen', 'True')

def login():
    show_frame(login_frame)
    ul.place(x=245,y=373,width=60,height=3)
    rg_btn.config(bg="white",fg="black",activebackground="white",activeforeground="black")
    rg_btn.place(x=1282,y=87,width=130,height=40)
    lg_btn.config(fg="white",bg="#fbc79b",activebackground="#fbc79b",activeforeground="white")
    lg_btn.place(x=1148,y=90,width=115,height=35)
    g1.config(text="Login to El Amour")

def signup():
    show_frame(signup_frame)
    ul.place(x=155,y=373,width=85,height=3)
    rg_btn.config(bg="#fbc79b",fg="white",activebackground="#fbc79b",activeforeground="white")
    rg_btn.place(x=1290,y=90,width=115,height=35)
    lg_btn.config(fg="black",bg="white",activebackground="white",activeforeground="black")
    lg_btn.place(x=1143,y=87,width=123,height=41)
    g1.config(text="Register to El Amour")

def show_frame(frame):
    frame.tkraise()

signup_frame=Frame(root,bd=0,relief=FLAT,bg="#f7f7f7")

s_img=PhotoImage(file="./Assets/Signup.png")
Label(signup_frame,image=s_img).place(x=0,y=0)

login_frame=Frame(root,relief=FLAT,bg="#f7f7f7")

l_img=PhotoImage(file="./Assets/login.png")
Label(login_frame,image=l_img).place(x=0,y=0)

for frame in (signup_frame, login_frame,):
    frame.place(x=155,y=390,width=340,height=310)

img=PhotoImage(file="./Assets/Signup_bg.png")
Label(root,image=img).place(x=0,y=0)

Label(root,text="Best Price Rooms Available",font=("Arial",10,"bold"),bg="white").place(x=785,y=685)

Label(root,text="Book Accommodation in El Amour online. No Reservation Costs. Great Rates. No Booking Fees. Motels."
      ,font=("Abadi",8),bg="white").place(x=785,y=710)

Label(root,text="24/7 Customer Service. Hostels. Apartments. Hotels. Read Real Guest Reviews. Villas. We speak your language."
      ,font=("Abadi",8),bg="white").place(x=785,y=725)

Label(root,text="Bed and Breakfasts...."
      ,font=("Abadi",8),bg="white").place(x=785,y=740)

lg_btn=Button(root,text="Login",bd=0,font=("Arial",14),bg="white",activebackground="white",cursor="hand2",command=login)
lg_btn.place(x=1143,y=87,width=123,height=41)

rg_btn=Button(root,text="Register",bd=0,font=("Arial",14),bg="#fbc79b",fg="white",cursor="hand2"
       ,activebackground="#fbc79b",activeforeground="white",command=signup)
rg_btn.place(x=1290,y=90,width=115,height=35)

g1=Label(root,text="Register to El Amour",font=("carlytte demo",46,"bold"),bg="#f8f8f8")
g1.place(x=150,y=190)

Label(root,text="Join to El Amour you will get the latest recommendations on the",font=("abadi",9),bg="#f8f8f8",fg="grey").place(x=155,y=280)
Label(root,text="services given by the hotel.",font=("abadi",9),bg="#f8f8f8",fg="grey").place(x=155,y=300)

Button(root,text="Register",font=("abadi",12),bg="#f8f8f8",bd=0,activebackground="#f8f8f8",cursor="hand2",command=signup).place(x=162,y=340)
Button(root,text="Login",font=("abadi",12),bg="#f8f8f8",bd=0,activebackground="#f8f8f8",cursor="hand2",command=login).place(x=250,y=340)

ul=Label(root,text="",bg="#fbc79b")
ul.place(x=155,y=373,width=85,height=3)

Label(signup_frame,text="Name",font=("abadi",8),bg="#f8f8f8",fg="grey").place(x=30,y=23)
Entry(signup_frame,font=("arial",10),bg="#f8f8f8",width=45,bd=0).place(x=32,y=40,height=30,width=290)

Label(signup_frame,text="Password",font=("abadi",8),bg="#f8f8f8",fg="grey").place(x=30,y=93)
Entry(signup_frame,font=("arial",10),show="●",bg="#f8f8f8",width=45,bd=0).place(x=32,y=110,height=30,width=290)

Label(signup_frame,text="Email",font=("abadi",8),bg="#f8f8f8",fg="grey").place(x=30,y=163)
Entry(signup_frame,font=("arial",10),bg="#f8f8f8",width=45,bd=0).place(x=32,y=180,height=30,width=290)

Button(signup_frame,text="Register",bd=0,font=("Arial",14),bg="#fbc79b",fg="white",cursor="hand2"
       ,activebackground="#fbc79b",activeforeground="white").place(x=25,y=245,height=45,width=300)

Label(login_frame,text="Name",font=("abadi",8),bg="#f8f8f8",fg="grey").place(x=30,y=23)
Entry(login_frame,font=("arial",10),bg="#f8f8f8",width=45,bd=0).place(x=32,y=40,height=30,width=290)

Label(login_frame,text="Password",font=("abadi",8),bg="#f8f8f8",fg="grey").place(x=30,y=93)
Entry(login_frame,font=("arial",10),show="●",bg="#f8f8f8",width=45,bd=0).place(x=32,y=110,height=30,width=290)

Button(login_frame,text="Login",bd=0,font=("Arial",14),bg="#fbc79b",fg="white",cursor="hand2"
       ,activebackground="#fbc79b",activeforeground="white").place(x=27,y=178,height=45,width=300)

show_frame(signup_frame)

root.mainloop()
