import tkinter #vložím plátno
from random import * #vložím možnosť robíť náhody
canvas = tkinter.Canvas(width = 400, height = 400, bg = 'white') #vytvoril som plátno so šírkou,výškou a farbou
canvas.pack() #vykrelil som si plátno

entry1 = tkinter.Entry() #vytvorím si okienko do ktorého sa dápísať
entry1.pack() #okienko vložím do plátna

def zmas(): #vytvorím si funkciu zmas
    canvas.delete('all') #vymaže sa všetko na plátne
    
def setric(): #vytvorím si funkciu setric
    a = 10 #do a sa vloží hodnota 10
    canvas.delete('all') #všetko na plátne sa vymaže
    x = randint(0, 400) #do x sa vloží náhodné číslo od 0 po 400
    y = randint(0, 400) #do y sa vloží náhodné číslo od 0 po 400
    if a > 90: #spravím si podmienku ak je a väčšie ako 90 tak:
        a = 10 #do a sa vloží hodnota 10
    canvas.create_text(x, y, text = str(entry1.get()), angle = a) #vypíše sa plátne text napísaný z entry1 
    a = a + 10 #do a sa vloží a plus 10
    canvas.after(2500,setric) #po dva a pol sekunde sa funkcia setric zopakuje
setric() #uzavriem funkciu setric

canvas.bind('<Button>', zmas) #po kliknutí ľavím tlačidlom myši sa zavolá funkcia zmas
