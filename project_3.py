from tkinter import *
s=Tk()
data=StringVar()
s.title("PytheNticheck")
s.geometry("600x200+400+190")
s.resizable(False,False)

f2=Frame(s,bg="light coral",highlightbackground="dim gray", highlightthickness=3,width=710, height=590, bd= 0)
f2.pack()
from project_2 import *
for data in check():
    a=data*100            
fpc=round(a,2)
l2=Label(s,bg="light coral",fg="snow",text="PytheNticheck",font=("Microsoft New Tai Lue",24,"bold"))
l2.place(x=190,y=10)
l=Label(s,bg="light coral",text="Plagiarism Detected:",fg="Snow",font=("Garamond",20,"bold"))
l.place(x=140,y=110)
l1=Label(s,bg="light coral",text=fpc,fg="Snow",font=("Garamond",20,"bold"))
l1.place(x=390,y=110)
l3=Label(s,bg="light coral",fg="snow",text="%",font=("Microsoft New Tai Lue",18,"bold"))
l3.place(x=445,y=110)
b1=Button(s,text="Close",font=("Garamond",15,"bold"),width=7,command=s.destroy,bg='pale violet red',fg="snow",activeforeground='red')
b1.place(x=503,y=160)
s.mainloop()
import pyttsx3
def voice_line_2():
    engine=pyttsx3.init()
    voice = engine.getProperty('voices')
    engine.setProperty('voice',voice[1].id)
    engine.setProperty('rate',125)

    engine.say('Thank You For Using PytheNticheck')
    engine.runAndWait()
voice_line_2()


