from tkinter import *
from tkinter import ttk
from tkcalendar import *
from tkinter import messagebox
import os

root=Tk()
root.geometry("1920x1080")
root.wm_attributes('-fullscreen', 'True')

img=PhotoImage(file="./Assets/dashboard_bg.png")
Label(root,image=img).place(x=0,y=0)

def show_frame(frame):
    frame.tkraise()

frame1=Frame(root,relief=GROOVE,bg="white")
frame2=Frame(root,relief=GROOVE,bg="white")
frame3=Frame(root,relief=GROOVE,bg="white")
frame4=Frame(root,relief=GROOVE,bg="white")

for frame in (frame1, frame2, frame3, frame4,):
    frame.place(x=163,y=155,width=1210,height=653)

def home_frame():
    frame1.place(x=163,y=155,height=653,width=1210)
    frame2.place_forget()
    frame3.place_forget()
    frame4.place_forget()

def room_frame():
    frame2.place(x=163,y=155,height=653,width=1210)
    frame1.place_forget()
    frame3.place_forget()
    frame4.place_forget()

def order_frame():
    frame3.place(x=163,y=155,height=653,width=1210)
    frame1.place_forget()
    frame2.place_forget()
    frame4.place_forget()

def view_frame():
    frame4.place(x=163,y=155,height=653,width=1210)
    frame1.place_forget()
    frame2.place_forget()
    frame3.place_forget()

def open_bk():
    filename="book.py"
    os.system(filename)

pizza_frame=Frame(frame3,relief=GROOVE,bg="white")
burger_frame=Frame(frame3,relief=GROOVE,bg="white")
snacks_frame=Frame(frame3,relief=GROOVE,bg="white")
salad_frame=Frame(frame3,relief=GROOVE,bg="white")
drinks_frame=Frame(frame3,relief=GROOVE,bg="white")

def show_order_frame(get_frame):
    get_frame.tkraise()

for get_frame in (pizza_frame, burger_frame, snacks_frame, salad_frame, drinks_frame,):
    get_frame.place(x=100,y=240,width=1020,height=370)

def p_frame():
    pizza_frame.place(x=100,y=240,width=1020,height=370)
    burger_frame.place_forget()
    snacks_frame.place_forget()
    salad_frame.place_forget()
    drinks_frame.place_forget()

    pizza_btn.config(font="Arial 14 underline",fg="orange")
    burger_btn.config(font="Arial 14",fg="black")
    snacks_btn.config(font="Arial 14",fg="black")
    salads_btn.config(font="Arial 14",fg="black")
    drinks_btn.config(font="Arial 14",fg="black")
    head.config(text="Pizza")
    size.config(text="32cm/48cm")
    size.place(x=560,y=210)

def b_frame():
    burger_frame.place(x=100,y=240,width=1020,height=370)
    show_order_frame(burger_frame)
    pizza_frame.place_forget()
    snacks_frame.place_forget()
    salad_frame.place_forget()
    drinks_frame.place_forget()

    pizza_btn.config(font="Arial 14",fg="black")
    burger_btn.config(font="Arial 14 underline",fg="orange")
    snacks_btn.config(font="Arial 14",fg="black")
    salads_btn.config(font="Arial 14",fg="black")
    drinks_btn.config(font="Arial 14",fg="black")
    head.config(text="Burger")
    size.config(text="Small/Medium/Large")
    size.place(x=530,y=210)

def s_frame():
    snacks_frame.place(x=100,y=240,width=1020,height=370)
    show_order_frame(snacks_frame)
    pizza_frame.place_forget()
    burger_frame.place_forget()
    salad_frame.place_forget()
    drinks_frame.place_forget()

    pizza_btn.config(font="Arial 14",fg="black")
    burger_btn.config(font="Arial 14",fg="black")
    snacks_btn.config(font="Arial 14 underline",fg="orange")
    salads_btn.config(font="Arial 14",fg="black")
    drinks_btn.config(font="Arial 14",fg="black")
    head.config(text="Snacks")
    size.config(text="Fries/Sandwiches")
    size.place(x=540,y=210)

def sa_frame():
    salad_frame.place(x=100,y=240,width=1020,height=370)
    show_order_frame(salad_frame)
    pizza_frame.place_forget()
    burger_frame.place_forget()
    snacks_frame.place_forget()
    drinks_frame.place_forget()

    pizza_btn.config(font="Arial 14",fg="black")
    burger_btn.config(font="Arial 14",fg="black")
    snacks_btn.config(font="Arial 14",fg="black")
    salads_btn.config(font="Arial 14 underline",fg="orange")
    drinks_btn.config(font="Arial 14",fg="black")
    head.config(text="Salads")
    size.config(text="Medium/Large")
    size.place(x=550,y=210)

def d_frame():
    drinks_frame.place(x=100,y=240,width=1020,height=370)
    show_order_frame(drinks_frame)
    pizza_frame.place_forget()
    burger_frame.place_forget()
    snacks_frame.place_forget()
    salad_frame.place_forget()

    pizza_btn.config(font="Arial 14",fg="black")
    burger_btn.config(font="Arial 14",fg="black")
    snacks_btn.config(font="Arial 14",fg="black")
    salads_btn.config(font="Arial 14",fg="black")
    drinks_btn.config(font="Arial 14 underline",fg="orange")
    head.config(text="Drinks")
    size.config(text="300ml/500ml")
    size.place(x=552,y=210)

def exit():
    messagebox.askokcancel("Exit","Are you sure want to exit")
    root.destroy()

def first_click(*args):
    l1.delete(0, 'end')

def second_click(*args):
    l2.delete(0, 'end')

def third_click(*args):
    l3.delete(0, 'end')

def fourth_click(*args):
    l4.delete(0, 'end')

def fifth_click(*args):
    l5.delete(0, 'end')

def sixth_click(*args):
    l6.delete(0, 'end')

def first_leave(*args):
    if l1.get() == "":
        l1.insert(0, 'Country, ZIP, City.....')
    else:
        pass
    frame2.focus()

def second_leave(*args):
    if l2.get() == "":
        l2.insert(0, 'No of rooms')
    else:
        pass
    frame2.focus()

def third_leave(*args):
    if l3.get() == "":
        l3.insert(0, 'No of adults')
    else:
        pass
    frame2.focus()

def fourth_leave(*args):
    if l4.get() == "":
        l4.insert(0, 'No of children')
    else:
        pass
    frame2.focus()

def fifth_leave(*args):
    if l5.get() == "":
        l5.insert(0, 'Enter your Email')
    else:
        pass
    frame2.focus()

def sixth_leave(*args):
    if l6.get() == "":
        l6.insert(0, 'Enter your Phone')
    else:
        pass
    frame2.focus()

def in_click(*args):
    c1.delete(0, 'end')

def in_leave(*args):
    if c1.get() == "":
        c1.insert(0, 'mm/dd/yyyy')
    else:
        pass
    frame2.focus()

def out_click(*args):
    c2.delete(0, 'end')

def out_leave(*args):
    if c2.get() == "":
        c2.insert(0, 'mm/dd/yyyy')
    else:
        pass
    frame2.focus()
    
Button(root,text="Home",fg="white",bg="#c2c2c2",font=("Crescendo",22,"bold"),bd=0
       ,activebackground="#c2c2c2",activeforeground="White",command=home_frame).place(x=725,y=25,width=120,height=45)

Button(root,text="Rooms",fg="white",bg="#c2c2c2",font=("Crescendo",22,"bold"),bd=0
       ,activebackground="#c2c2c2",activeforeground="White",command=room_frame).place(x=887,y=25,width=120,height=45)

Button(root,text="Order",fg="white",bg="#c2c2c2",font=("Crescendo",22,"bold"),bd=0
       ,activebackground="#c2c2c2",activeforeground="White",command=order_frame).place(x=1047,y=25,width=120,height=45)

Button(root,text="View",fg="white",bg="#c2c2c2",font=("Crescendo",22,"bold"),bd=0
       ,activebackground="#c2c2c2",activeforeground="White",command=view_frame).place(x=1207,y=25,width=120,height=45)

Button(root,text="Exit",fg="white",bg="#c2c2c2",font=("Crescendo",22,"bold"),bd=0
       ,activebackground="#c2c2c2",activeforeground="White",command=exit).place(x=1368,y=25,width=120,height=45)

img2=PhotoImage(file="./Assets/frame1.png")
Label(frame1,image=img2,relief=FLAT,bg="white").place(x=0,y=0)

Label(frame1,text="Monitor health of",font="helvetica 24",bg="white").place(x=40,y=40)
Label(frame1,text="your business",font="helvetica 24",bg="white").place(x=40,y=75)
Label(frame1,text="Control and analyse your data in the easiest way",font=("Segoe ui", 9),bg="white").place(x=40,y=125)

bk_img=PhotoImage(file="./Assets/right-arrow.png")
bk_btn=Button(frame1,image=bk_img,bg="white",bd=0,activebackground="White",relief=FLAT,cursor="hand2",command=open_bk)
bk_btn.place(x=1090,y=505,width=36,height=36)

img3=PhotoImage(file="./Assets/frame2.png")
Label(frame2,image=img3,relief=FLAT,bg="white").place(x=0,y=0)

l1=Entry(frame2,font=("Muli",12))
l1.insert(0, 'Country, ZIP, City.....')
l1.place(x=370,y=170,width=540,height=40)
l1.configure(relief="flat")
l1.configure(foreground="#e8e8e8")
l1.configure(background="#b7b7b7")
l1.configure(borderwidth="0")

l1.bind("<Button-1>", first_click)
l1.bind("<Leave>", first_leave)

Label(frame2,text="Check in",font=("muli",8,"bold"),bg="#b7b7b7",fg="#f46d25").place(x=365,y=254)

c1=Entry(frame2,font=("Muli",12))
c1.insert(0, 'mm/dd/yyyy')
c1.place(x=365,y=275,width=220,height=35)
c1.configure(relief="flat")
c1.configure(foreground="#e8e8e8")
c1.configure(background="#b7b7b7")
c1.configure(borderwidth="0")

c1.bind("<Button-1>", in_click)
c1.bind("<Leave>", in_leave)

Label(frame2,text="Check out",font=("muli",8,"bold"),bg="#b7b7b7",fg="#f46d25").place(x=680,y=254)

c2=Entry(frame2,font=("Muli",12))
c2.insert(0, 'mm/dd/yyyy')
c2.place(x=680,y=274,width=200,height=35)
c2.configure(relief="flat")
c2.configure(foreground="#e8e8e8")
c2.configure(background="#b7b7b7")
c2.configure(borderwidth="0")

c2.bind("<Button-1>", out_click)
c2.bind("<Leave>", out_leave)

l2=Entry(frame2,font=("Muli",12))
l2.insert(0, 'No of rooms')
l2.place(x=370,y=357,width=125,height=40)
l2.configure(relief="flat")
l2.configure(foreground="#e8e8e8")
l2.configure(background="#b7b7b7")
l2.configure(borderwidth="0")

l2.bind("<Button-1>", second_click)
l2.bind("<Leave>", second_leave)

l3=Entry(frame2,font=("Muli",12))
l3.insert(0, 'No of adults')
l3.place(x=565,y=357,width=125,height=40)
l3.configure(relief="flat")
l3.configure(foreground="#e8e8e8")
l3.configure(background="#b7b7b7")
l3.configure(borderwidth="0")

l3.bind("<Button-1>", third_click)
l3.bind("<Leave>", third_leave)

l4=Entry(frame2,font=("Muli",12))
l4.insert(0, 'No of children')
l4.place(x=760,y=357,width=125,height=40)
l4.configure(relief="flat")
l4.configure(foreground="#e8e8e8")
l4.configure(background="#b7b7b7")
l4.configure(borderwidth="0")

l4.bind("<Button-1>", fourth_click)
l4.bind("<Leave>", fourth_leave)

l5=Entry(frame2,font=("Muli",12))
l5.insert(0, 'Enter your Email')
l5.place(x=365,y=445,width=250,height=40)
l5.configure(relief="flat")
l5.configure(foreground="#e8e8e8")
l5.configure(background="#b7b7b7")
l5.configure(borderwidth="0")

l5.bind("<Button-1>", fifth_click)
l5.bind("<Leave>", fifth_leave)

l6=Entry(frame2,font=("Muli",12))
l6.insert(0, 'Enter your Phone')
l6.place(x=675,y=445,width=240,height=40)
l6.configure(relief="flat")
l6.configure(foreground="#e8e8e8")
l6.configure(background="#b7b7b7")
l6.configure(borderwidth="0")

l6.bind("<Button-1>", sixth_click)
l6.bind("<Leave>", sixth_leave)

button1 = Button(frame2,text="Book Now",font=("Muli",16,"bold"))
button1.place(x=360,y=533, width=550, height=42)
button1.configure(relief="flat")
button1.configure(overrelief="flat")
button1.configure(activebackground="#f68e56")
button1.configure(activeforeground="#ffffff")
button1.configure(cursor="hand2")
button1.configure(foreground="#ffffff")
button1.configure(background="#f68e56")
button1.configure(borderwidth="0")

img4=PhotoImage(file="./Assets/frame3.png")
Label(frame3,image=img4,relief=FLAT,bg="white").place(x=0,y=0)

pizza_btn=Button(frame3,text="Pizza",fg="orange",bg="white",font="Arial 14 underline",bd=0,activebackground="white",cursor="hand2",activeforeground="orange",command=p_frame)
pizza_btn.place(x=310,y=140)
burger_btn=Button(frame3,text="Burger",fg="black",bg="white",font="Arial 14",bd=0,activebackground="white",cursor="hand2",activeforeground="orange",command=b_frame)
burger_btn.place(x=445,y=140)
snacks_btn=Button(frame3,text="Snacks",fg="black",bg="white",font="Arial 14",bd=0,activebackground="white",cursor="hand2",activeforeground="orange",command=s_frame)
snacks_btn.place(x=575,y=140)
salads_btn=Button(frame3,text="Salads",fg="black",bg="white",font="Arial 14",bd=0,activebackground="white",cursor="hand2",activeforeground="orange",command=sa_frame)
salads_btn.place(x=710,y=140)
drinks_btn=Button(frame3,text="Drinks",fg="black",bg="white",font="Arial 14",bd=0,activebackground="white",cursor="hand2",activeforeground="orange",command=d_frame)
drinks_btn.place(x=840,y=140)

head=Label(frame3,text="Pizza",fg="#f8845d",bg="white",font="Helvetica 24 bold")
head.place(x=530,y=170,width=150)
size=Label(frame3,text="32cm/48cm",fg="grey",bg="white",font=("Bahnschrift Light", 12))
size.place(x=560,y=210)

img5=PhotoImage(file="./Assets/pizza_frame.png")
Label(pizza_frame,image=img5,relief=FLAT,bg="white").place(x=0,y=0)

img6=PhotoImage(file="./Assets/arrow.png")
arr_btn=Button(pizza_frame,image=img6,bg="#6edefa",bd=0,activebackground="#6edefa")
arr_btn.place(x=444,y=50,height=32,width=32)

img7=PhotoImage(file="./Assets/arrow.png")
arr_btn1=Button(pizza_frame,image=img7,bg="#6edefa",bd=0,activebackground="#6edefa")
arr_btn1.place(x=444,y=181,height=32,width=32)

img8=PhotoImage(file="./Assets/arrow.png")
arr_btn2=Button(pizza_frame,image=img8,bg="#6edefa",bd=0,activebackground="#6edefa")
arr_btn2.place(x=444,y=309,height=32,width=32)

img9=PhotoImage(file="./Assets/arrow.png")
arr_btn=Button(pizza_frame,image=img9,bg="#6edefa",bd=0,activebackground="#6edefa")
arr_btn.place(x=899,y=46,height=32,width=32)

img10=PhotoImage(file="./Assets/arrow.png")
arr_btn=Button(pizza_frame,image=img10,bg="#6edefa",bd=0,activebackground="#6edefa")
arr_btn.place(x=899,y=181,height=32,width=32)

img11=PhotoImage(file="./Assets/arrow.png")
arr_btn=Button(pizza_frame,image=img11,bg="#6edefa",bd=0,activebackground="#6edefa")
arr_btn.place(x=899,y=309,height=32,width=32)

img12=PhotoImage(file="./Assets/burger_frame.png")
Label(burger_frame,image=img12,relief=FLAT,bg="white").place(x=0,y=0)

img13=PhotoImage(file="./Assets/arrow.png")
arr_btn=Button(burger_frame,image=img13,bg="#6edefa",bd=0,activebackground="#6edefa")
arr_btn.place(x=444,y=50,height=32,width=32)

img14=PhotoImage(file="./Assets/arrow.png")
arr_btn1=Button(burger_frame,image=img14,bg="#6edefa",bd=0,activebackground="#6edefa")
arr_btn1.place(x=444,y=181,height=32,width=32)

img15=PhotoImage(file="./Assets/arrow.png")
arr_btn2=Button(burger_frame,image=img15,bg="#6edefa",bd=0,activebackground="#6edefa")
arr_btn2.place(x=444,y=309,height=32,width=32)

img16=PhotoImage(file="./Assets/arrow.png")
arr_btn=Button(burger_frame,image=img16,bg="#6edefa",bd=0,activebackground="#6edefa")
arr_btn.place(x=899,y=46,height=32,width=32)

img17=PhotoImage(file="./Assets/arrow.png")
arr_btn=Button(burger_frame,image=img17,bg="#6edefa",bd=0,activebackground="#6edefa")
arr_btn.place(x=899,y=181,height=32,width=32)

img18=PhotoImage(file="./Assets/arrow.png")
arr_btn=Button(burger_frame,image=img18,bg="#6edefa",bd=0,activebackground="#6edefa")
arr_btn.place(x=899,y=309,height=32,width=32)

img19=PhotoImage(file="./Assets/drinks_frame.png")
Label(drinks_frame,image=img19,relief=FLAT,bg="white").place(x=0,y=0)

img20=PhotoImage(file="./Assets/arrow.png")
arr_btn=Button(drinks_frame,image=img20,bg="#6edefa",bd=0,activebackground="#6edefa")
arr_btn.place(x=444,y=50,height=32,width=32)

img21=PhotoImage(file="./Assets/arrow.png")
arr_btn1=Button(drinks_frame,image=img21,bg="#6edefa",bd=0,activebackground="#6edefa")
arr_btn1.place(x=444,y=181,height=32,width=32)

img22=PhotoImage(file="./Assets/arrow.png")
arr_btn2=Button(drinks_frame,image=img22,bg="#6edefa",bd=0,activebackground="#6edefa")
arr_btn2.place(x=444,y=309,height=32,width=32)

img23=PhotoImage(file="./Assets/arrow.png")
arr_btn=Button(drinks_frame,image=img23,bg="#6edefa",bd=0,activebackground="#6edefa")
arr_btn.place(x=899,y=46,height=32,width=32)

img24=PhotoImage(file="./Assets/arrow.png")
arr_btn=Button(drinks_frame,image=img24,bg="#6edefa",bd=0,activebackground="#6edefa")
arr_btn.place(x=899,y=181,height=32,width=32)

img25=PhotoImage(file="./Assets/arrow.png")
arr_btn=Button(drinks_frame,image=img25,bg="#6edefa",bd=0,activebackground="#6edefa")
arr_btn.place(x=899,y=309,height=32,width=32)

img26=PhotoImage(file="./Assets/snacks_frame.png")
Label(snacks_frame,image=img26,relief=FLAT,bg="white").place(x=0,y=0)

img27=PhotoImage(file="./Assets/arrow.png")
arr_btn=Button(snacks_frame,image=img27,bg="#6edefa",bd=0,activebackground="#6edefa")
arr_btn.place(x=444,y=50,height=32,width=32)

img28=PhotoImage(file="./Assets/arrow.png")
arr_btn1=Button(snacks_frame,image=img28,bg="#6edefa",bd=0,activebackground="#6edefa")
arr_btn1.place(x=444,y=181,height=32,width=32)

img29=PhotoImage(file="./Assets/arrow.png")
arr_btn2=Button(snacks_frame,image=img29,bg="#6edefa",bd=0,activebackground="#6edefa")
arr_btn2.place(x=444,y=309,height=32,width=32)

img30=PhotoImage(file="./Assets/arrow.png")
arr_btn=Button(snacks_frame,image=img30,bg="#6edefa",bd=0,activebackground="#6edefa")
arr_btn.place(x=899,y=46,height=32,width=32)

img31=PhotoImage(file="./Assets/arrow.png")
arr_btn=Button(snacks_frame,image=img31,bg="#6edefa",bd=0,activebackground="#6edefa")
arr_btn.place(x=899,y=181,height=32,width=32)

img32=PhotoImage(file="./Assets/arrow.png")
arr_btn=Button(snacks_frame,image=img32,bg="#6edefa",bd=0,activebackground="#6edefa")
arr_btn.place(x=899,y=309,height=32,width=32)

img33=PhotoImage(file="./Assets/salad_frame.png")
Label(salad_frame,image=img33,relief=FLAT,bg="white").place(x=0,y=0)

img34=PhotoImage(file="./Assets/arrow.png")
arr_btn=Button(salad_frame,image=img34,bg="#6edefa",bd=0,activebackground="#6edefa")
arr_btn.place(x=444,y=50,height=32,width=32)

img35=PhotoImage(file="./Assets/arrow.png")
arr_btn1=Button(salad_frame,image=img35,bg="#6edefa",bd=0,activebackground="#6edefa")
arr_btn1.place(x=444,y=181,height=32,width=32)

img36=PhotoImage(file="./Assets/arrow.png")
arr_btn2=Button(salad_frame,image=img36,bg="#6edefa",bd=0,activebackground="#6edefa")
arr_btn2.place(x=444,y=309,height=32,width=32)

img37=PhotoImage(file="./Assets/arrow.png")
arr_btn=Button(salad_frame,image=img37,bg="#6edefa",bd=0,activebackground="#6edefa")
arr_btn.place(x=899,y=46,height=32,width=32)

img38=PhotoImage(file="./Assets/arrow.png")
arr_btn=Button(salad_frame,image=img38,bg="#6edefa",bd=0,activebackground="#6edefa")
arr_btn.place(x=899,y=181,height=32,width=32)

img39=PhotoImage(file="./Assets/arrow.png")
arr_btn=Button(salad_frame,image=img39,bg="#6edefa",bd=0,activebackground="#6edefa")
arr_btn.place(x=899,y=309,height=32,width=32)

show_frame(frame1)
show_order_frame(pizza_frame)

root.mainloop()
