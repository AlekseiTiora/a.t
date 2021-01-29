from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
from tkinter.filedialog import *
import sys,fileinput
from tkinter.messagebox import *
root=Tk()
root.geometry("400x300")
root.title("Elemendid Tkinteris")

tabs=ttk.Notebook(root)

texts=["Esimene","Teine","Kolmas","Neljas"]
def funktion(a):
    tab.select(a)

def open_():
    file=askopenfilename()
    for text in fileinput.input(file):
        txt_box.insert(0.0,text)

def save_():
    file=asksaveasfile(mode='w',defaultextension=((".txt"),(".docx")),filetypes=(("Notepad",".txt"),("Word",".docx")))
    t=txt_box.get(0.0,END)
    file.write(t)
    file.close()
def exit_():
    if askyeno("Exit","Yes/No"):
        showinfo("Exit","Message: Yes")
        root.destroy()
    else:
        showinfo("No")

def image_car():
    global img
    tabs.select(1)
    img=PhotoImage(file="car.png").subsample(4)
    can.create_image(10,10,image=img,anchor=NW)
    
def image_cat():
    global img
    tabs.select(1)
    img=PhotoImage(file="cat.png").subsample(4)
    can.create_image(10,10,image=img,anchor=NW)

def image_dog():
    global img
    tabs.select(1)
    img=PhotoImage(file="dog.png").subsample(4)
    can.create_image(10,10,image=img,anchor=NW)

 
#for i in range(4): #len(text)
#    tab1=Frame(tabs)
#    tabs.add(tab1,text=texts[i])
tab1=Frame(tabs)
tab2=Frame(tabs)
tab3=Frame(tabs)
tab4=Frame(tabs)
tabs.add(tab1,text="Esimene")
tabs.add(tab2,text="Teine")
tabs.add(tab3,text="Kolmas")
tabs.add(tab4,text="Neljas")
tabs.pack()

M=Menu(root)
root.config(menu=M)
m1=Menu(M,tearoff=1)
M.add_cascade(label="Menu1",menu=m1)
m1.add_command(label="Tab1",accelerator='Command+V',command=lambda:funktion(0))
m1.add_command(label="Tab2",command=lambda:funktion(1))
m1.add_command(label="Tab3",command=lambda:funktion(1))
m1.add_command(label="Tab4",command=lambda:funktion(1))
m1.add_separator()


m2=Menu(M,tearoff=2)
M.add_cascade(label="BG Colors",menu=m2)
m2.add_command(label="Green",command=lambda:root.config(bg="green"))
m2.add_command(label="Red",command=lambda:root.config(bg="red"))
m2.add_command(label="Blue",command=lambda:root.config(bg="blue"))
m2.add_command(label="Dark",command=lambda:root.config(bg="black"))


can=Canvas(tab2,width=300,height=200)
can.pack()

m3=Menu(M,tearoff=3)
M.add_cascade(label="Pictures",menu=m3)
m3.add_command(label="Cat",command=lambda:image_cat())
m3.add_command(label="Dog",command=lambda:image_dog())
m3.add_command(label="Car",command=lambda:image_car())

btn_open=Button(tab1,text="Open")
btn_save=Button(tab1,text="Save")
btn_exit=Button(tab1,text="Exit")
txt_box= scrolledtext.ScrolledText(tab1,width=40,height=5)
#Text(tab,width=40,height)
txt_box.grid(row=0,column=0,columnspan=3)
btn_open.grid(row=1,column=0)
btn_save.grid(row=1,column=1)
btn_exit.grid(row=1,column=2)

#can=Canvas(tab2,width=300,height=200)
#img=PhotoImage(file="car.png").subsample(4)
#can.create_image(10,10,image=img,anchor=NW)
#can.pack()
tabs.pack(fill="both")

root.mainloop()