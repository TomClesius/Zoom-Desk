import os
import pickle
from tkinter import *
from tkinter.filedialog import askopenfilename
os.system('CLS')
import pathlib
import subprocess
import time
import pyautogui

root = Tk()

btn = [] #creates list to store the buttons in
x = [] #creates list to store the x buttons in


SessionFrame = LabelFrame(root,padx=10,pady=10)



# TODO safe in file
ZoomPath = []

def addZoomPath():
    filename = askopenfilename(initialdir="/", title="Select File", filetypes = ((".exe","*.exe"),("all","*.*"))) 
    ZoomPath.append(filename)

##############ZoomCode####################
def zoomClass(meet_id, password):
    pyautogui.press('ESC',interval=0.2)

    subprocess.Popen(ZoomPath[0],stdout=subprocess.PIPE)
    
    time.sleep(1)
    
    xy = pyautogui.locateCenterOnScreen('buttons\\join_button.png' ,confidence=0.8)
    pyautogui.moveTo(xy)
    pyautogui.click()
    time.sleep(0.2)
    
    pyautogui.press('enter',interval=0.2)
    pyautogui.write(meet_id)
    pyautogui.press('enter',interval=0.2)
    pyautogui.write(password)
    pyautogui.press('enter',interval=0.2)


abspath = pathlib.Path("data.dat").absolute()

def safe(array):
    pickle.dump(array,open(str(abspath),"wb"))

def load():
    data = pickle.load(open(str(abspath),"rb"))
    return data

#TODO index out of range BUG
def delete(index):
    if(len(btn) == 1):
        SessionFrame.pack_forget()


    btn[index].destroy()
    x[index].destroy()
    data = load()
    del data[0][index]
    del data[1][index]
    del data[2][index]
    print(data)
    
    safe(data)
    iniBtns()

##############Displayes all already safed Buttons####################
def iniBtns():
    # data = [[name],[id],[pw]]
    data = load()
    print(data)
    for i in range(len(data[0])): #this says for *counter* in *however many elements there are in the list files*
        #the below line creates a button and stores it in an array we can call later, it will print the value of it's own text by referencing itself from the list that the buttons are stored in

        btn.append(Button(SessionFrame, text= data[0][i],padx=25, command=lambda c=i: zoomClass(data[1][c],data[2][c])))
        x.append(Button(SessionFrame, text="x",padx=5, command=lambda c=i: delete(c)))
        
        btn[i].grid(row=i,column=0)
        x[i].grid(row=i,column=1)
        

        safe(data)
        
##############Add Button function####################
def addBtns():
    print(len(btn))
    if(len(btn) == 0):
        SessionFrame.pack(padx=10,pady=10,)
    data = load()
    data[2].append(str(password_value.get())) 
    data[1].append(str(name_value.get())) 
    data[0].append(str(id_value.get()))  

    btn.append(Button(SessionFrame, text=data[0][-1],padx=25, command=lambda c= len(data[0])-1: zoomClass(data[1][c],data[2][c])))
    x.append(Button(SessionFrame, text="x",padx=5, command=lambda c= len(x)-1: delete(c)))
   
    btn[-1].grid(row=len(btn)+1,column=0) #this packs the buttons
    x[-1].grid(row=len(x)+1,column=1)
   
    safe(data)


DepFrame = LabelFrame(root,padx=10,pady=10)
DepFrame.pack(padx=10,pady=10)
FileBtn = Button(DepFrame, text = "Zoom Path" ,command= 0,width=10) ##TODO COMMAND # idea no button- automatic command when nothig saved
FileBtn.pack()
#--------------------------------------------------------------------
AddFrame = LabelFrame(root,padx=10,pady=10)
AddFrame.pack(padx=10,pady=10)


#Entrys
name_value = StringVar()
id_value = StringVar()
password_value = StringVar()

nameFeld = Entry(AddFrame, textvariable=name_value)
idFeld = Entry(AddFrame, textvariable=id_value)
passwortFeld = Entry(AddFrame, textvariable=password_value)

idFeld.grid(row=1,column=0,padx=5)
nameFeld.grid(row=1,column=1,padx=5)
passwortFeld.grid(row=1,column=2,padx=5)

#Entry labels
NameLabel = Label(AddFrame, text="Name")
IdLabel = Label(AddFrame, text="Session-ID")
PwLabel = Label(AddFrame, text="Password")

NameLabel.grid(row=0,column=0)
IdLabel.grid(row=0,column=1)
PwLabel.grid(row=0,column=2)

#Add button
AddBtn = Button(AddFrame, text = "Save",command = addBtns,width=10,)
AddBtn.grid(row=1,column=3,padx=10,sticky="ew")
SessionFrame.pack(padx=10,pady=10,)

iniBtns()

root.mainloop()