import tkinter #vložím tkinter
canvas = tkinter.Canvas(width = 600, height = 400, bg = 'white') #spravím plátno
canvas.pack() #vykreslím plátno
entry1 = tkinter.Entry() #stvorím okienko na písanie
entry1.pack() #vložím okienko na písanie do plátna

def ziaci (suradnice): #funkcia s názvom ziaci
    x = suradnice.x #do písmenka x sa vložia súradnice x z klikania myšou
    y = suradnice.y #do písmenka y sa vložia súradnice y z klikania myšou 
    a = entry1.get() #do písmenka a sa vloží hodnota / text z entry1
    canvas.create_oval(x, y, x - 20, y - 20) #nakreslí sa kruh
    canvas.create_rectangle(x, y, x - 20, y + 20) #nakreslí sa štvorec pod kruh
    canvas.create_text(x - 10, y + 30, text = a) #vypíse sa text pod štvorec

canvas.bind('<Button-1>', ziaci) #nastavím si spúštanie funkcie ziaci po kliknutí mišou na ĺavé tlačidlo myši
