from tkinter import *

root=Tk()
root.geometry("1920x1080")
root.wm_attributes('-fullscreen', 'True')

img=PhotoImage(file=r"C:\Users\Anmol\Documents\My Vasiyat\python\Meet Project\Assets\Signup_bg.png")
Label(root,image=img).place(x=0,y=0)

Label(root,text="Best Price Rooms Available",font=("Arial",10,"bold"),bg="white").place(x=785,y=685)

Label(root,text="Book Accommodation in El Amour online. No Reservation Costs. Great Rates. No Booking Fees. Motels."
      ,font=("Abadi",8),bg="white").place(x=785,y=710)

Label(root,text="24/7 Customer Service. Hostels. Apartments. Hotels. Read Real Guest Reviews. Villas. We speak your language."
      ,font=("Abadi",8),bg="white").place(x=785,y=725)

Label(root,text="Bed and Breakfasts...."
      ,font=("Abadi",8),bg="white").place(x=785,y=740)

Button(root,text="Login",bd=0,font=("Arial",14),bg="white",activebackground="white",cursor="hand2").place(x=1200,y=90)

Button(root,text="Register",bd=0,font=("Arial",14),bg="#fbc79b",fg="white",cursor="hand2"
       ,activebackground="#fbc79b",activeforeground="white").place(x=1305,y=90)

Label(root,text="Register to El Amour",font=("carlytte demo",46,"bold"),bg="#f8f8f8").place(x=150,y=190)

Label(root,text="Join to El Amour you will get the latest recommendations on the",font=("abadi",9),bg="#f8f8f8",fg="grey").place(x=155,y=280)
Label(root,text="services given by the hotel.",font=("abadi",9),bg="#f8f8f8",fg="grey").place(x=155,y=300)

Button(root,text="Register",font=("abadi",12),bg="#f8f8f8",bd=0,activebackground="#f8f8f8").place(x=162,y=340)
Button(root,text="Login",font=("abadi",12),bg="#f8f8f8",bd=0,activebackground="#f8f8f8").place(x=250,y=340)

Label(root,text="Name",font=("abadi",8),bg="#f8f8f8",fg="grey").place(x=170,y=400)
Entry(root,font=("arial",10),bg="#f8f8f8",width=45,bd=0).place(x=172,y=420,height=35)

Label(root,text="Password",font=("abadi",8),bg="#f8f8f8",fg="grey").place(x=170,y=480)
Entry(root,font=("arial",10),show="●",bg="#f8f8f8",width=45,bd=0).place(x=172,y=500,height=35)

Label(root,text="Email",font=("abadi",8),bg="#f8f8f8",fg="grey").place(x=170,y=560)
Entry(root,font=("arial",10),bg="#f8f8f8",width=45,bd=0).place(x=172,y=580,height=35)

Button(root,text="Register",bd=0,width=29,font=("Arial",14),bg="#fbc79b",fg="white",cursor="hand2"
       ,activebackground="#fbc79b",activeforeground="white").place(x=160,y=640,height=50)

root.mainloop()
