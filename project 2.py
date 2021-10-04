
from tkinter import *
from tkinter import ttk,messagebox
from tkinter.font import Font
from PIL import ImageTk
import random
import sys
import os


#ฟังก์ชันก์เปลีี่ยนเฟรม
def raise_frame(frame):
    frame.tkraise()

#ฟังก์ชั่นรีสตาร์ท
def restart_program():
    GUI.destroy()
    os.startfile("Lab Project.py")
#################################################   codeที่เก็บข้อมูล  SQL 1
import sqlite3  

conn = sqlite3.connect('Life.db') ####ใส่ไฟล์ database.db
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

################################################# codeที่เก็บข้อมูล  SQL 2

sonn = sqlite3.connect('Academic.db')  ####ใส่ไฟล์ database.db
son = sonn.cursor()

son.execute("""CREATE TABLE IF NOT EXISTS vocab(
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
        vocab text,
        meaning text,
        score int)""")

def insert_vocabAca(vocabAca,meaningAca):
    ID = None
    score = 0
    with sonn: #with คำสั่งเปิดปิด
        son.execute("""INSERT INTO vocab VALUES (?,?,?,?)""",
                  (ID,vocabAca,meaningAca,score))
    sonn.commit() #คำสั่งsave vocab
    print('Data was inserted Vocab Academic')

def view_vocabAca():
    with sonn:
        son.execute("SELECT * FROM vocab")
        allvocabAca = son.fetchall()
        print(allvocabAca)

    return allvocabAca


#####################WINDOW######################

GUI = Tk()
GUI.geometry("500x500")
GUI.configure(bg = "#ffffff")
GUI.title("VOCAB")
GUI.iconbitmap('C:/Users/09723/Desktop/Project/เว็ป/resume/static/image/icon1.ico')  #icon app
fonttext = Font(family = 'times',size = 20,weight = "bold",slant="roman",underline=0,overstrike = 0)


#frame มี 5 เฟรม
f1 = Frame(GUI,width = 500,height = 500)  
f2 = Frame(GUI,width = 500,height = 500)
f3 = Frame(GUI,width = 500,height = 500)
f4 = Frame(GUI,width = 500,height = 500)
f5 = Frame(GUI,width = 500,height = 500)

for frame in (f1, f2, f3, f4, f5):  # ลูปเอาไว้เปลี่ยนเฟรม
    frame.grid(row=1, column=1, sticky='news')


#######################Frame 1##########################
canvas = Canvas(f1,
    bg = "#ffffff",
    height = 500,
    width = 500,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")

canvas.place(x = 0, y = 0)
background_img = PhotoImage(file = f"background.png")   #file = f"..." เป็นไฟล์รูปใน github
background = canvas.create_image(
    250.0, 250.0,
    image=background_img)


E1_img = PhotoImage(file = f"img_textBox0.png")
E1_bg = canvas.create_image(
    249.0, 309.5,
    image = E1_img)

v_vocab = StringVar()
v_mean = StringVar()

E1 = Entry(f1,textvariable = v_mean,font = fonttext,
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


E2 = Entry(f1,textvariable = v_vocab,font = fonttext,
    bd = 0,
    bg = "#c4c4c4",
    highlightthickness = 0)

E2.place(
    x = 146.0, y = 133,
    width = 206.0,
    height = 51)


###############################BUTTON###################################### ปุ่ม save 1
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
        vocabtable1.delete(*vocabtable1.get_children())
        for v in addvocabLife:
            vocabtable1.insert('','end',value=v)
            
        print('----------------')

    else:
        messagebox.showinfo('ไม่มีข้อมูล')

img1 = PhotoImage(file = f"img1.png")
savelife = Button(f1,
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = SaveVocabLife,
    relief = "flat")

savelife.place(
    x = 180, y = 393,
    width = 45,
    height = 30)


E2.bind('<Return>',SaveVocabLife)

###################################################################### ปุ่ม save 2
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
        vocabtable2.delete(*vocabtable2.get_children())
        for v in addvocabAca:
            vocabtable2.insert('','end',value=v)
            
        print('----------------')

    else:
        messagebox.showinfo('ไม่มีข้อมูล')

img0 = PhotoImage(file = f"img0.png")
saveaca = Button(f1,
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = SaveVocabAca,
    relief = "flat")

saveaca.place(
    x = 270, y = 393,
    width = 45,
    height = 30)


E2.bind('<Return>',SaveVocabAca)



#######################ปุ่มรีโปรแกรม อัพเดทศัพท์#############################


imgup = PhotoImage(file = f"up.png")
buttonup = Button(f1,
    image = imgup,
    borderwidth = 0,
    highlightthickness = 0,
    command=restart_program,
    relief = "flat")

buttonup.place(
    x = 200, y = 27,
    width = 63,
    height = 33)


#####################ปุ่มเปลี่ยนไปหน้าอื่น frame1##############################

img4 = PhotoImage(file = f"img4.png")
b4 = Button(f1,
    image = img4,
    borderwidth = 0,
    highlightthickness = 0,
    command=lambda:raise_frame(f2),
    relief = "flat")

b4.place(
    x = 48, y = 26,
    width = 63,)


img3 = PhotoImage(file = f"img3.png")
b3 = Button(f1,
    image = img3,
    borderwidth = 0,
    highlightthickness = 0,
    command=lambda:raise_frame(f3),
    relief = "flat")

b3.place(
    x = 123, y = 26,
    width = 63,
    height = 35)

##############Frame 2###############################

canvas2 = Canvas(
    f2,
    bg = "#ffffff",
    height = 500,
    width = 500,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas2.place(x = 0, y = 0)

background_img2 = PhotoImage(file = f"background2.png")
background2 = canvas2.create_image(
    250.0, 250.0,
    image=background_img2)

img00 = PhotoImage(file = f"imgg0.png")
b00 = Button(f2,
    image = img00,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:raise_frame(f4),
    relief = "flat")

b00.place(
    x = 256, y = 394,
    width = 63,
    height = 35)

img11 = PhotoImage(file = f"imgg1.png")
b11 = Button(f2,
    image = img11,
    borderwidth = 0,
    highlightthickness = 0,
    command =lambda:raise_frame(f1),
    relief = "flat")

b11.place(
    x = 177, y = 394,
    width = 63,
    height = 35)





##############Frame 3###############################

canvas3 = Canvas(
    f3,
    bg = "#ffffff",
    height = 500,
    width = 500,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas3.place(x = 0, y = 0)

background_img3 = PhotoImage(file = f"background2.png")
background3 = canvas3.create_image(
    250.0, 250.0,
    image=background_img3)

img000 = PhotoImage(file = f"imgg0.png")
b000 = Button(f3,
    image = img00,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:raise_frame(f5),
    relief = "flat")

b000.place(
    x = 256, y = 394,
    width = 63,
    height = 35)

img111 = PhotoImage(file = f"imgg1.png")
b111 = Button(f3,
    image = img111,
    borderwidth = 0,
    highlightthickness = 0,
    command =lambda:raise_frame(f1),
    relief = "flat")

b111.place(
    x = 177, y = 394,
    width = 63,
    height = 35)




#################################Frame2###################################  

header = ['ID','Vocab','Meaning'] #ตาราง sql 
hdzise = [50,300,100]

vocabtable1 = ttk.Treeview(f2,columns = header,show='headings',height=15)
vocabtable1.place(x=20,y=50)

for h,s in zip(header,hdzise):
    vocabtable1.heading(h,text = h)
    vocabtable1.column(h,width = s)


addvocabLife = view_vocabLife()
if len(addvocabLife )  > 0:
    for v in addvocabLife :
        vocabtable1.insert('','end',value=v)


#################################Frame3#######################################

header2 = ['ID','Vocab','Meaning'] #ตาราง sql
hdzise2 = [50,300,100]

vocabtable2 = ttk.Treeview(f3,columns = header,show='headings',height=15)
vocabtable2.place(x=20,y=50)
for h,s in zip(header2,hdzise2):
    vocabtable2.heading(h,text = h)
    vocabtable2.column(h,width = s)

addvocabAca = view_vocabAca()
if len(addvocabAca)  > 0:
    for j in addvocabAca:
        vocabtable2.insert('','end',value=j)

#######################RECITE Frame 4############################  

#####Frame 4 เหมือนกับ 5 เอาไว้ท่องศัพท์ถ้าข้อความตรงกับศัพท์ที่สุ่มถ้าตรง socre +-#####

canvas4 = Canvas(
    f4,
    bg = "#ffffff",
    height = 500,
    width = 500,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas4.place(x = 0, y = 0)

background_img4 = PhotoImage(file = f"background2.png")
background4 = canvas4.create_image(
    250.0, 250.0,
    image=background_img4)

rv_vocab = StringVar()
rv_vocab.set('Vocabulary')


rv_meaning = StringVar()
rv_meaning.set('Meaning')

R1 = Label(f4,textvariable = rv_vocab,font = fonttext,bg = '#EEEB8F',fg = 'black')
R1.pack(pady = 30)


R2 = Label(f4,textvariable = rv_meaning,font = fonttext,bg = '#EEEB8F',fg = 'black')
R2.pack(pady = 30)




Frame4 = Frame(f4)
Frame4.pack()


vcurent = []
def Nextbutton():  #สุ่มคำศัพท์ใหม่
    global vcurent
    global score
    current = random.choice(addvocabLife)
    vcurent = current
    rv_vocab.set(current[1])
    rv_meaning.set('>>Meaning<<')
    
    
def Showbutton():  #โชว์คำศัพท์
    rv_meaning.set(vcurent[2])

#########################################################################################
imgshow = PhotoImage(file = f"imgshow.png")
buttonshow = Button(f4,
    image = imgshow,
    borderwidth = 0,
    highlightthickness = 0,
    command = Showbutton,
    relief = "flat")

buttonshow.place(
    x = 265, y = 205,
    width = 50,
    height = 29)

imgnext = PhotoImage(file = f"imgnext.png")
buttonnext = Button(f4,
    image = imgnext,
    borderwidth = 0,
    highlightthickness = 0,
    command = Nextbutton,
    relief = "flat")

buttonnext.place(
    x = 185, y = 205,
    width = 50,
    height = 29)

############################################

def UpdateScore():  #ฟังก์ชันให้เพิ่ม score
    global score
    guess = Entrymeaning.get()
    if guess == vcurent[2]:
        score +=1
        Frame4.update()  
    else :
        score -=1
    status_str.set('Score: ' + str(score))
    Entrymeaning.delete(0, 'end')

score = 0
status_str = StringVar()
status_str.set('Score: ' + str(score))
show_status = Label(f4, textvariable = status_str,font = ('times',10),bg = 'black',fg = 'white')
show_status.pack(pady=160,padx = 10)



entry_img = PhotoImage(file = f"img_textBox3.png")
entry_bg = canvas4.create_image(
    242.0, 303.5,
    image = entry_img)
Entrymeaning = Entry(f4,font = fonttext,
    bd = 0,
    bg = "#c4c4c4",
    highlightthickness = 0)

Entrymeaning.place(
    x = 142.0, y = 280,
    width = 200.0,
    height = 45)


imgtrue = PhotoImage(file = f"imgTrue.png")
buttonyes = Button(f4,
    image = imgtrue,
    borderwidth = 0,
    highlightthickness = 0,
    command = UpdateScore,
    relief = "flat")

buttonyes.place(
    x = 373, y = 290,
    width = 38,
    height = 23)


img1111 = PhotoImage(file = f"imgg1.png")
b1111 = Button(f4,
    image = img1111,
    borderwidth = 0,
    highlightthickness = 0,
    command =lambda:raise_frame(f1),
    relief = "flat")

b1111.place(
    x = 218, y = 410,
    width = 63,
    height = 35)

 
#######################RECITE Frame 5############################

canvas5 = Canvas(
    f5,
    bg = "#ffffff",
    height = 500,
    width = 500,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas5.place(x = 0, y = 0)

background_img5 = PhotoImage(file = f"background2.png")
background5 = canvas5.create_image(
    250.0, 250.0,
    image=background_img5)



background_img4 = PhotoImage(file = f"background2.png")
background4 = canvas4.create_image(
    250.0, 250.0,
    image=background_img4)

rv_vocab1 = StringVar()
rv_vocab1.set('Vocabulary')


rv_meaning1 = StringVar()
rv_meaning1.set('Meaning')

R11 = Label(f5,textvariable = rv_vocab1,font = fonttext,bg = '#ABC456',fg = 'white')
R11.pack(pady = 30)


R22 = Label(f5,textvariable = rv_meaning1,font = fonttext,bg = '#ABC456',fg = 'white')
R22.pack(pady = 30)




Frame5 = Frame(f5)
Frame5.pack()


vcurent1 = []
def Nextbutton1():
    global vcurent1
    global score1
    current1 = random.choice(addvocabAca)
    vcurent1 = current1
    rv_vocab1.set(current1[1])
    rv_meaning1.set('>>Meaning<<')
    
    
def Showbutton1():
    rv_meaning1.set(vcurent1[2])


imgshow1 = PhotoImage(file = f"imgshow.png")
buttonshow1 = Button(f5,
    image = imgshow1,
    borderwidth = 0,
    highlightthickness = 0,
    command = Showbutton1,
    relief = "flat")

buttonshow1.place(
    x = 265, y = 205,
    width = 50,
    height = 29)

imgnext1 = PhotoImage(file = f"imgnext.png")
buttonnext1 = Button(f5,
    image = imgnext1,
    borderwidth = 0,
    highlightthickness = 0,
    command = Nextbutton1,
    relief = "flat")

buttonnext1.place(
    x = 185, y = 205,
    width = 50,
    height = 29)

############################################

def UpdateScore1():
    global score1
    guess = Entrymeaning1.get()
    if guess == vcurent1[2]:
        score1 +=1
        Frame5.update()  
    else :
        score1 -=1
    status_str1.set('Score: ' + str(score1))
    Entrymeaning1.delete(0, 'end')

score1 = 0
status_str1 = StringVar()
status_str1.set('Score: ' + str(score1))
show_status1 = Label(f5, textvariable = status_str1,font = ('times',10),bg = 'black',fg = 'white')
show_status1.pack(pady=160,padx = 10)



entry_img1 = PhotoImage(file = f"img_textBox3.png")
entry_bg1 = canvas5.create_image(
    242.0, 303.5,
    image = entry_img1)
Entrymeaning1 = Entry(f5,font = fonttext,
    bd = 0,
    bg = "#c4c4c4",
    highlightthickness = 0)

Entrymeaning1.place(
    x = 142.0, y = 280,
    width = 200.0,
    height = 45)


imgtruee = PhotoImage(file = f"imgTrue.png")
buttonyess = Button(f5,
    image = imgtruee,
    borderwidth = 0,
    highlightthickness = 0,
    command = UpdateScore1,
    relief = "flat")

buttonyess.place(
    x = 373, y = 290,
    width = 38,
    height = 23)


img11111 = PhotoImage(file = f"imgg1.png")
b11111 = Button(f5,
    image = img1111,
    borderwidth = 0,
    highlightthickness = 0,
    command =lambda:raise_frame(f1),
    relief = "flat")

b11111.place(
    x = 218, y = 410,
    width = 63,
    height = 35)

###########################################################

raise_frame(f1)
GUI.mainloop()
