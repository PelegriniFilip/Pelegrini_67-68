import tkinter #vytvorím si tkinter
import random #vložím možnosť robiť náhody
canvas = tkinter.Canvas(width = 400, height = 800, bg = 'white') #vytvorím si plátno a nastavím mu veľkosť, šírku a farbu
canvas.pack() #vykreslím plátno

y = 10 #do y sa vloží hodnota 10
y2 = 10 #do y2 sa vloží hodnota 10
stop = 0 #do stop sa vloží hodnota 0

def bos(): #vytvorím si funkciu s názvom bos
    global stop, y, y2 #hodnoty stop, y a y2 sa nastavia ako globálne hodnoty(všetko čo bude hodnota obsahovať, bude plaťiť pre celí program a nie len pre funkciu)
    minus = random.randint(0, 10) #do minus sa vloží náhodnéčislo od 0 po 10
    minus2 = random. randint(0, 10) #do minus2 sa vloží náhodné čislo od 0 po 10
    canvas.delete('all') #vymaže sa všetko na plátne
    y = y + minus #do y sa vloží hodnota y plus hodnota minus
    y2 = y2 + minus2 #do y2 sa vloží hodnota y2 plus hodnota minus2
    
    canvas.create_rectangle(100, y, 140, y + 50) #vytvorím štvorec(telo bosorky)
    canvas.create_oval(100, y - 40, 140, y) #vytvorím kruh(hlava bosorky)
    canvas.create_line(40, y + 40, 160, y + 40) #vytvorím čiaru(porisko z metli bosorky)
    canvas.create_line(40, y - 10, 60, y+ 40, 40, y + 10, 60, y + 40, 40, y + 60, 40, y + 40) #vytvorím viacero čiar(štetiny na metle bosorky)
    
    canvas.create_rectangle(300, y2, 340, y2 + 50) #vytvorím štvorec(telo bosorky)
    canvas.create_oval(300, y2 - 40, 340, y2) #vytvorím kruh(hlava bosorky)
    canvas.create_line(240, y2 + 40, 360, y2 + 40) #vytvorím čiaru(porisko z metli bosorky)
    canvas.create_line(240, y2 - 10, 260, y2 + 40, 260, y2 + 10, 260, y2 + 20, 260, y2 + 40, 260, y2 + 60) #vytvorím viacero čiar(štetiny na metle bosorky)
    
    if y <= 0 and y2 > 0: #vytvorím podmienku ak je y menšie alebo rovné nule a ak je y2 väčšie 0 tak:
        stop = 1 #do stop sa vloží 1
        print('pretekárka 1 vyhrala') #do shellu sa vypíše text
    elif y2 <=0 and y > 0: #pokračujem v podmienke ak nieje horná podmienka splnená, tak sa spúšta táto druhá podmienka: ak je y2 menšie alebo rovné 0 a ak je y väčšie 0 tak:
        stop = 1 #do stop sa vloží 1
        print('pretekáraka 2 výhrala') #do shellu sa vypíše text
    if stop == 0: #vytvorím podmienku ak je stop rovné 0 tak:
        canvas.update() #canvas sa zresetuje
        canvas.after(10, bos) #po resetesa každích 10 stotín privolá funkcia bos
bos() #uzatváram funkciu bos