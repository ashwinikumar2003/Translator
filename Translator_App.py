from tkinter import *
from tkinter import ttk,messagebox
import googletrans
from googletrans import Translator
import pyttsx3

win=Tk()
win.title("Translator")
win.resizable(False,False)
win.iconbitmap("2.ico")
canvas = Canvas(win, width=888, height=500)
canvas.pack()

def label_change():
    c1=combo1.get()
    c2=combo2.get()
    lbl1.configure(text=c1)
    lbl2.configure(text=c2)
    win.after(500,label_change)

def translate():
    text_=txt1.get(1.0,END).strip()
    if not text_:
        messagebox.showwarning("Warning", "Please enter text to translate.")
    else:
        t1 = Translator()
        trans_text = t1.translate(text_, src=combo1.get(), dest=combo2.get())
        translation = trans_text.text
        pr = trans_text.pronunciation
        if ((type(pr) is list) and (not pr)):
            translation = translation
        elif (type(pr) is str):
            translation = translation + ", " + pr

        txt2.delete(1.0, END)
        txt2.insert(END, translation)

def speak_it():
    pass

bg_image = PhotoImage(file="Background.png")
button_image=PhotoImage(file="button.png")

canvas.create_image(0, 0, image=bg_image, anchor="nw")

language = googletrans.LANGUAGES
languageV = list(language.values())
lang1=language.keys()

combo1=ttk.Combobox(win, values=languageV, font="Roboto 11", state="r", width=11)
combo1.place(x=90,y=127)
combo1.set("English")

lbl1 = Label(win, text="English", font="segoe 15 bold", bg="white", width=16, bd=5, relief=GROOVE)
lbl1.place(x=45,y=150)

combo2=ttk.Combobox(win, values=languageV, font="Roboto 11", state="r", width=11)
combo2.place(x=690,y=127)
combo2.set("hindi")

lbl2 = Label(win, text="English", font="segoe 15 bold", bg="white", width=16, bd=5, relief=GROOVE)
lbl2.place(x=645,y=150)

f1=Frame(win,bg="Black", bd=5)
f1.place(x=10,y=218,width=410,height=180)

txt1=Text(f1,font="Roboto 16", bg="white", relief=GROOVE, wrap=WORD)
txt1.place(x=0,y=0,width=380,height=170)

sb1=Scrollbar(f1)
sb1.pack(side="right",fill='y')
sb1.configure(command=txt1.yview)
txt1.configure(yscrollcommand=sb1.set)

f2=Frame(win,bg="Black", bd=5)
f2.place(x=470,y=218,width=410,height=180)

txt2=Text(f2,font="Roboto 16", bg="white", relief=GROOVE, wrap=WORD)
txt2.place(x=0,y=0,width=380,height=170)

sb2=Scrollbar(f2)
sb2.pack(side="right",fill='y')
sb2.configure(command=txt2.yview)
txt2.configure(yscrollcommand=sb2.set)

translate_button=Button(win, image=button_image, borderwidth=0, activebackground="#010738", cursor="hand2", command=translate)
translate_button.place(x=390, y=420)

listen = Button(win, borderwidth=0, text="Listen",command=speak_it)
listen.place(x=670,y=420)

label_change()
win.mainloop()