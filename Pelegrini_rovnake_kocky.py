import tkinter #vložím plátno
from random import * #vložím možnosť robíť náhody
canvas = tkinter.Canvas(width = 400, height = 400, bg = 'white') #vytvoril som plátno so šírkou,výškou a farbou
canvas.pack() #vykrelil som si plátno

def kocky(): #vytvoril som funkciu kocky
    global x, y #nastavil som hodnoty x a y, aby boli platné v celom programe
    canvas.delete('k') #vymažem text zo štvorčekov
    x = randint(1, 6) #do písmenka x sa vloží náhodné čislo od 1 do 6
    y = randint(1, 6) #do písmenka x sa vloží náhodné čislo od 1 do 6
    canvas.create_text(200, 50, tex = 'pocet bodov:') #hore na stred plátna si vypíšem tento text
    canvas.create_text(150, 200, text = x, font = 'Arial 25', tags = 'k') #v lavom štvorci sa vykreslí čislo od 1 do 6 podla toho aká hodnota je v písmenku x
    canvas.create_text(250, 200, text = y, font = 'Arial 25', tags = 'k') #v pravom štvorci sa vykreslí čislo od 1 do 6 podla toho aká hodnota je v písmenku y
    canvas.create_rectangle(130, 180, 170, 220) #vykreslím ľaví štvorec
    canvas.create_rectangle(230, 180, 270, 220) #vykreslím praví štvorec
    canvas.after(500, kocky) #celá funkci kocky sa zopakuje po pol sekunde
kocky() #uzatváram funkciu kocky

def body(): #vytvoril som funkciu body
    canvas.delete('a') #vymyže sa text s počtom tvojích bodov
    global b #hodnota b je nastavená pre celí program a nie len pre funkciu
    b = 0
    if x == y: #spraví sa podmienka ak sa x rovná y tak:
        b = b + 2 #do b sa pripočítajú 2 body
    if x < y: #spraví sa podmienka ak je x menšie ako y tak:
        b = b - 2 #od b sa odpočítaju 2 body
    canvas.create_text(250, 50, text = b, tags = 'a') #po kliknutí sa body prepíšu


canvas.bind('<Button-1>', text='rovnake', comand = body) #po kliknutí lavim tlacidlom mysi sa spustí funkcia body