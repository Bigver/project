from tkinter import *

from tkinter import *
from tkinter import ttk,messagebox
from tkinter.font import Font
from PIL import ImageTk
import random

#################################################
import sqlite3

conn = sqlite3.connect('Life.db')
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS vocab(
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
        vocab text,
        meaning text,
        score int)""")

def insert_vocabLife(vocabLife,meaningLife):
    ID = None
    score = 0
    with conn: #with คำสั่งเปิดปิด
        c.execute("""INSERT INTO vocab VALUES (?,?,?,?)""",
                  (ID,vocabLife,meaningLife,score))
    conn.commit() #คำสั่งsave vocab
    print('Data was inserted Vocab Life')

def view_vocabLife():
    with conn:
        c.execute("SELECT * FROM vocab")
        allvocabLife = c.fetchall()
        print(allvocabLife)

    return allvocabLife

#################################################

sonn = sqlite3.connect('Academic.db')
s = sonn.cursor()

s.execute("""CREATE TABLE IF NOT EXISTS vocab(
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
        vocab text,
        meaning text,
        score int)""")

def insert_vocabAca(vocabAca,meaningAca):
    ID = None
    score = 0
    with sonn: #with คำสั่งเปิดปิด
        s.execute("""INSERT INTO vocab VALUES (?,?,?,?)""",
                  (ID,vocabAca,meaningAca,score))
    sonn.commit() #คำสั่งsave vocab
    print('Data was inserted Vocab Academic')

def view_vocabAca():
    with sonn:
        s.execute("SELECT * FROM vocab")
        allvocabAca = s.fetchall()
        print(allvocabAca)

    return allvocabAca


#####################WINDOW######################


GUI = Tk()
GUI.geometry("500x500")
GUI.configure(bg = "#ffffff")
GUI.title("VOCAB")
GUI.iconbitmap('C:/Users/09723/Desktop/Project/เว็ป/resume/static/image/icon1.ico')
fonttext = Font(family = 'times',size = 20,weight = "bold",slant="roman",underline=0,overstrike = 0)


#################################################

T1 = Frame(GUI)
T2 = Frame(GUI)
T3 = Frame(GUI)


######################ENTRY###########################
canvas = Canvas(
    GUI,
    bg = "#ffffff",
    height = 500,
    width = 500,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)
background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    250.0, 250.0,
    image=background_img)

E1_img = PhotoImage(file = f"img_textBox0.png")
E1_bg = canvas.create_image(
    249.0, 309.5,
    image = E1_img)

v_vocab = StringVar()
E1 = Entry(textvariable = v_vocab,font = fonttext,
    bd = 0,
    bg = "#c4c4c4",
    highlightthickness = 0)

E1.place(
    x = 146.0, y = 283,
    width = 206.0,
    height = 51)

E2_img = PhotoImage(file = f"img_textBox1.png")
E2_bg = canvas.create_image(
    249.0, 159.5,
    image = E2_img)

v_mean = StringVar()
E2 = Entry(textvariable = v_mean,font = fonttext,
    bd = 0,
    bg = "#c4c4c4",
    highlightthickness = 0)

E2.place(
    x = 146.0, y = 133,
    width = 206.0,
    height = 51)


###############################BUTTON######################################
def SaveVocabLife(event = None):   ####funsion save
    global addvocabLife
    vocabLife = v_vocab.get()
    meaningLife = v_mean.get()
    if len(vocabLife) > 0 and len(meaningLife) > 0:
        insert_vocabLife(vocabLife,meaningLife)
        print('Vocab :{}\nMeaning:{}'.format(vocabLife,meaningLife))
        v_vocab.set('')
        v_mean.set('')
        E1.focus()
        

    else:
        messagebox.showinfo('ไม่มีข้อมูล')

img1 = PhotoImage(file = f"img1.png")
b0 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = SaveVocabLife,
    relief = "flat")

b0.place(
    x = 180, y = 393,
    width = 45,
    height = 30)


E2.bind('<Return>',SaveVocabLife)

######################################################################
def SaveVocabAca(event = None):   ####funsion save
    global addvocabAca
    vocabAca = v_vocab.get()
    meaningAca = v_mean.get()
    if len(vocabAca) > 0 and len(meaningAca) > 0:
        insert_vocabAca(vocabAca,meaningAca)
        print('Vocab :{}\nMeaning:{}'.format(vocabAca,meaningAca))
        v_vocab.set('')
        v_mean.set('')
        E1.focus()
        
    else:
        messagebox.showinfo('ไม่มีข้อมูล')

img0 = PhotoImage(file = f"img0.png")
b1 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = SaveVocabAca,
    relief = "flat")

b1.place(
    x = 270, y = 393,
    width = 45,
    height = 30)


E2.bind('<Return>',SaveVocabAca)

#########################PACK Life#################################


def click1() :
    header = ['ID','Vocab','Meaning']
    hdzise = [50,300,100]

    vocabtable1 = ttk.Treeview(GUI,columns = header,show='headings',height=18)
    vocabtable1.place(x=20,y=90)

    for h,s in zip(header,hdzise):
        vocabtable1.heading(h,text = h)
        vocabtable1.column(h,width = s)
    global addvocab
    addvocab = view_vocabLife()
    if len(addvocab)  > 0:
        for v in addvocab:
            vocabtable1.insert('','end',value=v)
    #GUI.destroy()


img4 = PhotoImage(file = f"img4.png")
b4 = Button(
    image = img4,
    borderwidth = 0,
    highlightthickness = 0,
    command = click1,
    relief = "flat")

b4.place(
    x = 48, y = 26,
    width = 63,
    height = 35)


######################PACK academic#############################

def click2() :
    header = ['ID','Vocab','Meaning']
    hdzise = [50,300,100]

    vocabtable2 = ttk.Treeview(GUI,columns = header,show='headings',height=18)
    vocabtable2.place(x=20,y=90)

    for h,s in zip(header,hdzise):
        vocabtable2.heading(h,text = h)
        vocabtable2.column(h,width = s)
    global addvocab
    addvocab = view_vocabAca()
    if len(addvocab)  > 0:
        for v in addvocab:
            vocabtable2.insert('','end',value=v)
    


img3 = PhotoImage(file = f"img3.png")
b3 = Button(
    image = img3,
    borderwidth = 0,
    highlightthickness = 0,
    command = click2,
    relief = "flat")

b3.place(
    x = 123, y = 26,
    width = 63,
    height = 35)



##########################RECITE##################################
  

img2 = PhotoImage(file = f"img2.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    relief = "flat")
b2.place(
    x = 199, y = 26,
    width = 63,
    height = 35)



##################################################################
GUI.resizable(False, False)
GUI.mainloop()
