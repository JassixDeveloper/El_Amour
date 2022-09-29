from tkinter import *

root=Tk()
root.geometry("1920x1080")
root.wm_attributes('-fullscreen', 'True')

img=PhotoImage(file=r"C:\Users\Anmol\Documents\My Vasiyat\python\Meet Project\Assets\Main_bg.png")
Label(root,image=img).place(x=0,y=0)

Label(root,text="BEST HOTEL",bg="#171841",fg="white",font=("bebas neue",78, "bold")).place(x=1040,y=150)
Label(root,text="IN TOWN",bg="#171841",fg="white",font=("bebas neue",78, "bold")).place(x=1045,y=260)

Label(root,text='''An extra lavish environment in a cheap price by El Amour Hotel.'''      
      ,bg="#171841",fg="white",font=("Segoe UI",12)).place(x=1065,y=400)

Label(root,text='''A best hotel in town by the great ratings of people who'''      
      ,bg="#171841",fg="white",font=("Segoe UI",12)).place(x=1077,y=425)

Label(root,text='''consumes the El Amour Hotel services.'''      
      ,bg="#171841",fg="white",font=("Segoe UI",12)).place(x=1095,y=450)

Label(root,text="Enjoy Your Vacations With Us",bg="#171841"
      ,fg="white",font=("bebas neue",22,"bold")).place(x=1150,y=520)

book=Button(root,text="Book Now",bg="#cf9a55",bd=0,activebackground="#cf9a55"
            ,activeforeground="white",fg="white",font=("Caramel Sweets",20)).place(x=1260,y=600)

signin=Button(root,text="SIGN IN",bg="#cf9a55",bd=0,activebackground="#cf9a55"
            ,activeforeground="white",fg="white",font=("Roboto",15)).place(x=1404,y=21)

login=Button(root,text="LOGIN",bg="#171841",bd=0,activebackground="#171841"
            ,activeforeground="white",fg="white",font=("Roboto",15)).place(x=1260,y=21)

review=Button(root,text="REVIEWS",bg="#171841",bd=0,activebackground="#171841"
            ,activeforeground="white",fg="white",font=("Roboto",15)).place(x=1130,y=21)

contact=Button(root,text="CONTACTS",bg="#171841",bd=0,activebackground="#171841"
            ,activeforeground="white",fg="white",font=("Roboto",15)).place(x=980,y=21)

home=Button(root,text="HOME",bg="#171841",bd=0,activebackground="#171841"
            ,activeforeground="white",fg="white",font=("Roboto",15)).place(x=875,y=21)

root.mainloop()
