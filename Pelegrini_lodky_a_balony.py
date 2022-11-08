import tkinter #vygenerujem si tkinter
canvas = tkinter.Canvas(width = 600, height = 400, bg = 'white') #zadefinujem si plátno aj s veĺkosťami a farbou
canvas.pack() #vytvorím si plátno

canvas.create_line(0, 320, 600, 320, fill = 'blue', width = 180) #vykreslím si more pomocou čiary

def kresli(suradnice): #vytvorím si funkciu kreslenie
    x = suradnice.x #do písmenka x sa vloží súradnica x z kliknutia myšou na  plátno
    y = suradnice.y #do písmenka y sa vloží súradnica y z kliknutia myšou na  plátno
    if 0 < y < 208: #zadefinujem si podmienku a je y väčšie ako nula a menšie ako 208 tak kresli:
        canvas.create_rectangle(x - 6,y - 6, x + 6, y + 6) #vykreslím štvorec(kôš od balónu)
        canvas.create_line(x, y - 6, x - 6, y - 16) #vykreslím lavé lano
        canvas.create_line(x, y - 6, x + 6, y - 16) #vykreslím pravé lano
        canvas.create_oval(x - 8, y - 28, x + 8, y - 13) #vykreslím balón(kruh)
    elif 226 < y < 600: #pokračujem v podmienke ale s novým zadaním, ak je y väčšie ako 226 a menšie ako 600 tak kresli:
        canvas.create_rectangle(x - 5, y - 5, x +15, y + 2) #vykreslím obdĺžnik
        canvas.create_line(x + 5, y - 15, x + 5, y - 5) #vykreslím sťažeň
        canvas.create_line(x + 5, y - 8, x + 14, y - 12) #vykrslím hornú časť vlajky
        canvas.create_line(x + 14, y - 12, x + 5, y - 15) #vykreslím spodnú časť vlajky
        
canvas.bind('<Button-1>', kresli) #nastavím si spúštanie funkcie kresli po kliknutí ľavím tlačidlom myši