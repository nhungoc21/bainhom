import tkinter as tk
from tkinter import *
from PIL import Image,ImageTk
import speech_recognition as sr
#tao giao dien bang tkinter
main=Tk()
main.title('Speech into Text')
canvas=tk.Canvas(main,width=700, height=700)
canvas.config(bg='pink')
canvas.grid(columnspan=3,rowspan=4)
#logo
logo=Image.open('264079285_n.png')
logo=ImageTk.PhotoImage(logo)
logo_label=tk.Label(image=logo)
logo_label.image=logo
logo_label.grid(columnspan=3,column=0, row=0)
#huong dan
hd=tk.Label(main,text='Welcome my Master!',fg='black',bg='pink')
hd.config(font=('Tahoma', 33,'bold'))
cnn=tk.Label(main,text='Please select your language:',fg='BLACK',font='Tahoma')
hd.grid(columnspan=3, column=0,row=1)
cnn.grid(column=0,row=2)
#thu tieng bang mic
def tienganh():
    c=sr.Recognizer()
    with sr.Microphone() as source:
        c.pause_threshold=2
        audio=c.listen(source)
    try:
        said=c.recognize_google(audio,language='en')
    except sr.UnknownValueError:
        Label(main, text="I didn't get your point, please repeat")
        textbox.insert(tk.END, Label)
        c = sr.Recognizer()
        with sr.Microphone() as source:
            c.pause_threshold = 2
            audio = c.listen(source)
        said = c.recognize_google(audio,language='en')
    textbox.insert(tk.END, said)
def tiengviet():
    c=sr.Recognizer()
    with sr.Microphone() as source:
        c.pause_threshold=2
        audio=c.listen(source)
    try:
        said=c.recognize_google(audio,language='vi')
    except sr.UnknownValueError:
        Label(main,text="I didn't get your point, please repeat")
        textbox.insert(tk.END,Label)
        c = sr.Recognizer()
        with sr.Microphone() as source:
            c.pause_threshold = 2
            audio = c.listen(source)
        said = c.recognize_google(audio,language='vi')
    textbox.insert(tk.END, said) #in ra textbox
#nut bam
nutbama=tk.Button(main, text='English',command=tienganh,height=1,width=9,bg='#CD5E77',fg='white')
nutbama.config(font=('Ink Free',20,'bold'))
nutbama.grid(column=1,row=2)
nutbamv=tk.Button(main, text='Vietnamese',command=tiengviet,height=1, width=9,bg='#CD5E77',fg='white')
nutbamv.config(font=('Ink Free',20,'bold'))
nutbamv.grid(column=2,row=2)
#def xoa text
def clear():
    textbox.delete(1.0,END)
#textbox
textbox=Text(main, height=20,width=50,bg='#FADADD')
textbox.grid(columnspan=3,column=1, row=3)
nut_xoa=Button(main,text='Clear text',command=clear,height=2,width=8)
nut_xoa.grid(columnspan=3,column=1,row=4)
label=Label(main,text='You have said:')
label.config(font=('Tahoma',25))
label.grid(column=0, row=3)
main.mainloop()