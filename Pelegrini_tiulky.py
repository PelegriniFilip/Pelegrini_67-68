import tkinter #vložím plátno
from random import * #vložím možnosť robíť náhody
canvas = tkinter.Canvas(width = 400, height = 400, bg = 'white') #vytvoril som plátno so šírkou,výškou a farbou
canvas.pack() #vykrelil som si plátno

x = 400 #do x sa vloží hodnota 400

def titulky(): #vytvorím si funkciu titulky
    canvas.delete('all') #vymaže sa všetko sa plátna
    x = x - 5 #do x sa vložínová hodnota x pod odčítaní 5 od x
    canvas.create_text(x, 370, text = entry1.get()) #vykreslísa tex čo si napísal do entry1
    if x < 0: #spravil som podminku ak je x menšie ako 0 tak:
        x = 400 #x sa nastaví na hodnotu 400
    canvas.after(100, titulky) #po jednej stotine sa funkcia titulky spustí znovu

entry1 = tkinter.Entry() #vytvorim si políčko do ktorého sa dá písať
entry1.pack() #vykreslí ssa toto políčko na plátno
titulky() #uzavrie sa funkcia titulky