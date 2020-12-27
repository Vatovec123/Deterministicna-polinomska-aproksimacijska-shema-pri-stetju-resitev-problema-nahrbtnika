from program1 import resitve
from tkinter import *

root = Tk()

Label1 = Label(root, text = 'Vnesi teže predmetov:')
Label1.pack()
e = Entry(root, width = 50)
e.pack()

Label2 = Label(root, text = 'Vnesi kapaciteto nahbrntika:')
Label2.pack()
maxteza = Entry(root, width = 50)
maxteza.pack()

Label3 = Label(root, text = 'Vnesi dopustno napako epsilon:')
Label3.pack()
napaka = Entry(root, width = 50)
napaka.pack()

def myClick():
    teze = list(e.get().split(','))
    print(teze)
    teze2 = []
    for i in teze:
        teze2.append(int(i))
    print(teze2)
    teze = teze2
    c = int(maxteza.get())
    print(c)
    eps = float(napaka.get())
    print(eps)
    rezultat = resitve(teze,c,eps)
    myLabel= Label(root, text = rezultat)
    myLabel.pack()

myButton = Button(root, text='vnesi', command= myClick) 
myButton.pack()



root.mainloop()
