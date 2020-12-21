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
        btn.append(Button(root, text= data[0][i], command=lambda c=i: zoomClass(data[1][c],data[2][c])))
        btn[i].pack()
        
        x.append(Button(root, text="x", command=lambda c=i: delete(c)))
        x[i].pack()
        
        safe(data)
        


##############Add Button function####################
def refreshBtns():
    data = load()
    data[2].append(str(passwort_wert.get())) 
    data[0].append(str(name_wert.get())) 
    data[1].append(str(id_wert.get()))  

    btn.append(Button(root, text=data[0][-1], command=lambda c= len(data[0])-1: zoomClass(data[1][c],data[2][c])))
    btn[-1].pack() #this packs the buttons

    x.append(Button(root, text="x", command=lambda c= len(x)-1: delete(c)))
    x[-1].pack()

    safe(data)

#add button
Button(root, text = "Add",command= refreshBtns).pack()
Button(root, text = "Zoom Path",command= addZoomPath).pack()

#input name
name_wert = StringVar()
nameFeld = Entry(root, textvariable=name_wert)
Label(root, text="Name").pack()
nameFeld.pack()
#input id
id_wert = StringVar()
idFeld = Entry(root, textvariable=id_wert)
Label(root, text="Session-ID").pack()
idFeld.pack()
#input passwort
passwort_wert = StringVar()
passwortFeld = Entry(root, textvariable=passwort_wert)
Label(root, text="Passwort").pack()
passwortFeld.pack()



iniBtns()

root.mainloop()











