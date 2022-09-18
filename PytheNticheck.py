import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
 
 
w=tk.Tk()
w.title("PytheNticheck")
w.configure(bg="")
w.geometry("700x580+400+70")
w.resizable(False,False)
lg=ImageTk.PhotoImage(file='D:\Vaibhav Singh\Logo (2).PNG')
#my_canvas=Canvas(w,width=800,height=900)
#my_canvas.pack(fill='both',expand=True)
#my_canvas.create_image(0,0,image=lg,anchor='nw')

#def resizer(e):
global bg1,resized_bg,new_bg
bg1=Image.open('D:\Vaibhav Singh\Logo (2).PNG')
#resized_bg=bg1.resize((e.width,e.height))
rs=bg1.resize((690,571))
ni=ImageTk.PhotoImage(rs)
frame1 = Frame(w, highlightbackground="dim gray", highlightthickness=3,width=710, height=590, bd= 0)
frame1.pack()
img=tk.Label(w,image=ni).place(x=3,y=3)
    #new_bg=ImageTk.PhotoImage(resized_bg)
    #my_canvas.create_image(0,0,image=new_bg,anchor='nw')
#w.bind('<Configure>',resizer)
"""from tkinter import ttk
ttk.Style().configure("TButton", padding=6, relief="flat",
   background="#ccc")

btn = ttk.Button(text="Sample")
btn.pack(padx=400,pady=200)"""
wm=Button(w,text="Click To Proceed",font=("Garamond",24,"bold"),command=w.destroy,fg="white",bg="dim gray",activebackground='pink',activeforeground='red').place(x=230,y=500)
#quit_button_window = my_canvas.create_window(240,470, anchor='nw', window=wm)  
import pyttsx3
def voice_line_1():
    engine=pyttsx3.init()
    voice = engine.getProperty('voices')
    engine.setProperty('voice',voice[1].id)
    engine.setProperty('rate',125)

    engine.say('Hello Welcome To PytheNticheck')
    engine.runAndWait()
voice_line_1()

w.mainloop()
from read_csv import *
from project_3 import *
def abc(): 
    # Specify Grid
    Grid.rowconfigure(w,0,weight=1)
    Grid.columnconfigure(w,0,weight=1)
 
    #Grid.rowconfigure(w,1,weight=1)
 
    # Create Buttons
    button_1 = Button(w,text="Button 1")
    button_2 = Button(w,text="Button 2")
 
    # Set grid
    button_1.grid(row=0,column=0,sticky="NSEW")
    button_2.grid(row=1,column=0,sticky="NSEW") 
    #Grid.columnconfigure(w,0,weight=1)
    #Grid.rowconfigure(w,1,weight=1)
 
