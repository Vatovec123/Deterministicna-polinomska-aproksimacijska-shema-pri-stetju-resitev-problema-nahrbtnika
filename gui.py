from program1 import resitve
from tkinter import *

root = Tk()

root.title('Računanje števila rešitev problema nahrbtnika')

root.iconbitmap('d:/Faks/3. letnik/fp/program/program.ico')


Label1 = Label(root, text = 'Vnesi teže predmetov:')
Label1.pack()
e = Entry(root, width = 50)
e.pack()

Label2 = Label(root, text = 'Vnesi kapaciteto nahbrtnika:')
Label2.pack()
maxteza = Entry(root, width = 50)
maxteza.pack()

Label3 = Label(root, text = 'Vnesi dopustno napako epsilon:')
Label3.pack()
napaka = Entry(root, width = 50)
napaka.pack()


#def izbrisi():
#    myLabel.destroy()
#    zaokrozi_gumb.destroy()

def zaokrozi():
    naravna_vr = int(round(rezultat))
    n_priblizek= Label(root, text = 'Točno število rešitev pri težah {}, kapaciteti {}, bi moralo biti {}'.format(teze,c,naravna_vr))
    n_priblizek.pack()



def racunaj():
    global rezultat
    skupno = 0

    koraki = 0
    for i in range(1,10):
        skupno += resitve(teze,c,i / 10)  
        koraki +=1
    rezultat = skupno / koraki
    priblizek= Label(root, text = 'Približno število rešitev pri težah {}, kapaciteti {}, je {}'.format(teze,c,rezultat))
    priblizek.pack()

    zaokrozi_gumb = Button(root, text =  'Zaokroži', command= zaokrozi)
    zaokrozi_gumb.pack()



def myClick():
    global teze,c ,eps, rezultat, myLabel
    #try:
    #    myLabel
    #except NameError:
    #    pass
    #else:    
    #    myLabel.pack_destroy()
  
    teze = list(e.get().split(','))
    print(teze)
    teze2 = []
    for i in teze:
        teze2.append(int(i))
    print(teze2)
    teze = teze2
    c = int(maxteza.get())
    print(c)
    eps = float(napaka.get().replace(',','.'))
    print(eps)
    rezultat = resitve(teze,c,eps)
    e.delete(0, 'end')
    maxteza.delete(0,'end')
    napaka.delete(0,'end')
    vsota = sum(teze)
    if vsota > c:
        myLabel= Label(root, text = 'Približno število rešitev pri težah {}, kapaciteti {} je {}'.format(teze,c,rezultat))
        myLabel.pack()

        zaokrozi_gumb = Button(root, text =  'Zaokroži', command= zaokrozi)
        zaokrozi_gumb.pack()

        nov_gumb = Button(root, text =  'Želim povprečje vrednosti pri različnih epsilonih', command= racunaj)
        nov_gumb.pack()
    else: 
        myLabel= Label(root, text = 'Točno število rešitev pri težah {}, kapaciteti {} in epsilonu {} je {}'.format(teze,c,eps,rezultat))
        myLabel.pack()
myButton = Button(root, text='Izračunaj', command= myClick) 
myButton.pack()


#izbrisi_button = Button(root, text='Izbriši', command=izbrisi)
#izbrisi_button.pack()




root.mainloop()


#pyinstaller.exe --onefile --icon=program/program.ico program/gui.py