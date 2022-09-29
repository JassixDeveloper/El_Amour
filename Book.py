from tkinter import *
from tkinter import ttk
from tkcalendar import *

root=Tk()
root.geometry("1920x1080")
root.wm_attributes('-fullscreen', 'True')

img=PhotoImage(file="./Assets/book_bg.png")
Label(root,image=img).place(x=0,y=0)

n=StringVar()
r=StringVar()
c=StringVar()

check=Button(root,text="CHECK AVAILABILITY →",font=("Arial",16),bg="#fb4545",fg="white",bd=0,activebackground="#fb4545"
       ,activeforeground="white",cursor="hand2")
check.place(x=965,y=470,height=56,width=310)

help=Button(root,text="Need Help?",font=("Arial",11,"underline"),bg="white",fg="grey",bd=0,activebackground="white"
       ,activeforeground="blue",cursor="hand2")
help.place(x=1150,y=565)

home=Button(root,text="Home",font=("Arial",15),bg="white",fg="black",bd=0,activebackground="#fb4545"
       ,activeforeground="white",cursor="hand2")
home.place(x=836,y=20,height=57,width=141)

browse=Button(root,text="Browse",font=("Arial",15),bg="white",fg="black",bd=0,activebackground="#fb4545"
       ,activeforeground="white",cursor="hand2")
browse.place(x=1006,y=20,height=57,width=141)

reviews=Button(root,text="Reviews",font=("Arial",15),bg="white",fg="black",bd=0,activebackground="#fb4545"
       ,activeforeground="white",cursor="hand2")
reviews.place(x=1176,y=20,height=57,width=141)

contact=Button(root,text="Contact",font=("Arial",15),bg="white",fg="black",bd=0,activebackground="#fb4545"
       ,activeforeground="white",cursor="hand2")
contact.place(x=1346,y=20,height=57,width=141)

style= ttk.Style()
style.configure("TCombobox", background= "white",relief=FLAT,foreground="grey")

adult=ttk.Combobox(root,textvariable=n,font=("Arial 16"),justify=CENTER)

adult['values']=(1,2,3,4)

adult.set("Adult")
adult['state']='readonly'

adult.place(x=275,y=471,width=253,height=55)

checkin_cal=DateEntry(root,justify=CENTER,font=("Arial 16"))
checkin_cal.place(x=273,y=368,width=255,height=55)

checkin_cal['state']='readonly'

checkout_cal=DateEntry(root,justify=CENTER,font=("Arial 16"))
checkout_cal.place(x=648,y=368,width=255,height=55)

checkout_cal['state']='readonly'

room_type=ttk.Combobox(root,textvariable=r,font=("Arial 16"),justify=CENTER)

room_type['values']=('Ac','Non Ac')

room_type.set("Room")
room_type['state']='readonly'

room_type.place(x=1030,y=368,width=245,height=55)

child=ttk.Combobox(root,textvariable=c,font=("Arial 16"),justify=CENTER)

child['values']=(1,2,3,4)

child.set("Child")
child['state']='readonly'

child.place(x=648,y=471,width=255,height=55)

def home_hover(e):
    home["bg"]='#fb4545'
    home["fg"]='white'    

def home_hover_leave(e):
    home["bg"]="white"
    home["fg"]='black'

def browse_hover(e):
    browse["bg"]='#fb4545'
    browse["fg"]='white'    

def browse_hover_leave(e):
    browse["bg"]="white"
    browse["fg"]='black'

def reviews_hover(e):
    reviews["bg"]='#fb4545'
    reviews["fg"]='white'    

def reviews_hover_leave(e):
    reviews["bg"]="white"
    reviews["fg"]='black'

def contact_hover(e):
    contact["bg"]='#fb4545'
    contact["fg"]='white'    

def contact_hover_leave(e):
    contact["bg"]="white"
    contact["fg"]='black'

def help_hover(e):
    help["fg"]='blue'    

def help_hover_leave(e):
    help["fg"]='grey'

home.bind("<Enter>",home_hover)
home.bind("<Leave>",home_hover_leave)

browse.bind("<Enter>",browse_hover)
browse.bind("<Leave>",browse_hover_leave)

reviews.bind("<Enter>",reviews_hover)
reviews.bind("<Leave>",reviews_hover_leave)

contact.bind("<Enter>",contact_hover)
contact.bind("<Leave>",contact_hover_leave)

help.bind("<Enter>",help_hover)
help.bind("<Leave>",help_hover_leave)

root.mainloop()
