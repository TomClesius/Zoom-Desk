import os
import pickle
from tkinter import *
from tkinter.filedialog import askopenfilename
os.system('CLS')
import pathlib
import subprocess
import time
import pyautogui


root = Tk(className="zoomDesk")
root.eval('tk::PlaceWindow . center')

btn = [] #creates list to store the buttons in
x = [] #creates list to store the x buttons in


SessionFrame = LabelFrame(root,padx=10,pady=10)

abspath = pathlib.Path("data.dat").absolute()

#--------------------------------------------------------------------
def safe(array):
    pickle.dump(array,open(str(abspath),"wb"))

def load():
    data = pickle.load(open(str(abspath),"rb"))
    return data


def addZoomPath():
    data = load()
    if not data[3] or data[3][0] == '':
        filename = askopenfilename(initialdir= "/", title="Select Zoom.exe", filetypes = ((".exe","*.exe"),("all","*.*"))) 
        data[3].append(filename) 
        safe(data)

def waitfor(img):
    while(not pyautogui.locateCenterOnScreen(img ,confidence=0.8)):
        time.sleep(0.1)
        print("here")


#--------------------------------------------------------------------
def zoomClass(meet_id, password):
    data = load()
    
    #need to kill task to stay everytime in focus
    os.system("taskkill /f /im zoom.exe")
    time.sleep(1)
    subprocess.Popen(data[3][0],stdout=subprocess.PIPE)
    
    waitfor('buttons\\wait_1.png')

    xy = pyautogui.locateCenterOnScreen('buttons\\join_button.png' ,confidence=0.8)
    pyautogui.moveTo(xy)
    pyautogui.click()

    time.sleep(1)
    
    pyautogui.press('enter',interval=0.4)
    pyautogui.write(meet_id)
    pyautogui.press('enter',interval=0.4)
    time.sleep(0.8)
    pyautogui.write(password)
    pyautogui.press('enter',interval=0.4)


#--------------------------------------------------------------------
def delete(index):
    btn[index].destroy()
    x[index].destroy()
    data = load()
    del data[0][index]
    del data[1][index]
    del data[2][index]
    print(data)
    
    safe(data)
    iniBtns()

#--------------------------------------------------------------------
def iniBtns():
    # data = [[name],[id],[pw],[path]]
    data = load()
    print(data)
    for i in range(len(data[0])): 
        btn.append(Button(SessionFrame, text= data[0][i],padx=25, command=lambda c=i: zoomClass(data[1][c],data[2][c]),width = 30))
        x.append(Button(SessionFrame, text="x",padx=5, command=lambda c=i: delete(c)))
        
        btn[i].grid(row=i,column=0,pady = 2)
        x[i].grid(row=i,column=1)
        safe(data)
        
#--------------------------------------------------------------------
def addBtns():
    print(len(btn))
    data = load()
    data[2].append(str(password_value.get())) 
    data[0].append(str(name_value.get())) 
    data[1].append(str(id_value.get()))  

    btn.append(Button(SessionFrame, text=data[0][-1],padx=25, command=lambda c= len(data[0])-1: zoomClass(data[1][c],data[2][c]),width = 30))
    x.append(Button(SessionFrame, text="x",padx=5, command=lambda c= len(x): delete(c)))
   
    btn[-1].grid(row=len(btn)+1,column=0,pady = 2) #this packs the buttons
    x[-1].grid(row=len(x)+1,column=1)
   
    safe(data)


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

nameFeld.grid(row=1,column=0,padx=5)
idFeld.grid(row=1,column=1,padx=5)
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
addZoomPath()

root.mainloop()