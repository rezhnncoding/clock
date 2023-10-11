
from tkinter import *
import time

window= Tk()
window.title('clock')
window.geometry('600x400')

def mytime():
    hour=time.strftime('%I')
    minute=time.strftime("%M")
    second=time.strftime('%S')
    amp_pm=time.strftime("%p")
    day =  time.strftime("%A")
    zone = time.strftime("%Z")
    mytext=hour+":"+minute+":"+second+" " +amp_pm
    mytext2=day+","+zone
    mylabel2.config(text=mytext2)
    mylabel.config(text=mytext)
    mylabel.after(1000,mytime)

mylabel= Label(window,text="",font=('arial',72),fg='White',background='Black')
mylabel.pack()

mylabel2=Label(window,text="h",font=("Arial",24))

mylabel2.pack()

mytime()

window.mainloop()
