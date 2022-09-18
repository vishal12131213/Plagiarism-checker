import csv
from tkinter import *
r=Tk()
data=StringVar()
r.title("PytheNticheck")
r.geometry("700x580+400+70")
r.configure(bg="dim gray")
r.resizable(False,False)
frame2=Frame(r,bg="light coral",highlightbackground="dim gray", highlightthickness=3,width=710, height=590, bd= 0)
frame2.pack()
l1=Label(r,bg="light coral",fg="Snow",text="Enter Data:",font=("Garamond",20,"bold"))
l1.place(x=20,y=150)
l2=Label(r,bg="light coral",fg="snow",text="PytheNticheck",font=("Microsoft New Tai Lue",24,"bold"))
#l2.configure(underline=True)
l2.place(x=250,y=10)
e1=Entry(r,textvariable=data,width=50,borderwidth=2,font=("Garamond",16))
e1.place(x=180,y=150,height=100)
#print(ct)
#e1.insert(0,"Enter Data")
def fmt_csv():
    ct=[e1.get()]
    with open('C:/Users/VAIBHAV/Desktop/test1.csv','w') as csv_file:
        csv_writer=csv.writer(csv_file)
        csv_writer.writerow(ct)
    with open('C:/Users/VAIBHAV/Desktop/test1.csv','r') as f:
        f_read=csv.reader(f)
        for i in f_read:
            print(i)
#def com1():
#from project_2 import *
#fpc=check()
b1=Button(r,text="Submit",font=("Garamond",15,"bold"),width=10,command=fmt_csv,bg='pale violet red',fg="snow",activeforeground='red')
#l3=Label(r,text=fpc,bg='light coral',font=("Garamond",10),fg='snow')
b1.place(x=270,y=400)
b2=Button(r,text="Check",font=("Garamond",15,"bold"),width=7,command=r.destroy,bg='pale violet red',fg="snow",activeforeground='red')
b2.place(x=603,y=540)
r.mainloop()
