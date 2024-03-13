
import random
import turtle as t
import time as ti

nomep1=""
nomep2=""
t.hideturtle()
t.bgcolor("orange")
t.color("white")
t.setup(1920,1080)
def disegna(t,soldip1,soldip2,turno):
    global nomep1
    global nomep2
    t.teleport(300,100)
    
    if len(stri)>35:
        t.write(stri,move=False, font=('monaco',15,'bold'),align='left')
    else:
        t.write(stri,move=False, font=('monaco',20,'bold'),align='left')
    
    t.teleport(-800,400)
    
    
    
    t.write("TURNO: "+ str(turno),move=False, font=('monaco',30,'bold'),align='left')
    if turno%2==1:
        t.teleport(-800,300)
        t.write("Saldo attuale di "+ nomep1+": "+ str(soldip1)+ " Euro",move=False, font=('monaco',30,'bold'),align='left')
    else:
        t.teleport(-800,300)
        t.write("Saldo attuale di "+nomep2+": "+ str(soldip2)+ " Euro",move=False, font=('monaco',30,'bold'),align='left')
    
    
    t.teleport(0,0)
    
    
    t.speed(200)
    
def disegnaruota(t,ruota,soldip1,soldip2,turno):
    t.reset()
    
    t.color("white")
    t.hideturtle()
    disegna(t,soldip1,soldip2,turno)
    
    t.teleport(0,-100)
    t.circle(200)
    
    t.teleport(0,100)
   
    for x in range(0,8):
        t.pendown()
        t.left(45)
        
        t.forward(200)
        
        
        t.penup()
        t.backward(200)

    for x in range(0,8):
   
        t.pendown()
        
        t.left(45)
        t.up()
        t.forward(120)
        t.left(90)
        t.forward(50)
        
        
        t.down()
        
        t.write(str(ruota[x]), font=('monaco',20,'bold'),align='center')
        t.up()
        t.backward(50)
        t.left(-90)
        
        t.penup()
        t.backward(120)

def gira(t,gira,ruota,soldip1,soldip2,turno):
    ruotagira(t,soldip1,soldip2,turno)
    t.reset()
    
    t.color("white")
    t.hideturtle()
    disegna(t,soldip1,soldip2,turno)
    disegnaruota(t,ruota,soldip1,soldip2,turno)
    
    for x in range(0,8):
   
        t.pendown()
        
        t.left(45)
        t.up()
        t.forward(225)
        t.left(90)
        t.forward(50)
        
        
        t.down()
        
        if x==gira:
            t.right(45)
            t.circle(20,None,3)
            t.right(-45)
        
        t.up()
        t.backward(50)
        t.left(-90)
        
        t.penup()
        t.backward(225)
    
    
        
def ruotagira(t,soldip1,soldip2,turno):
    t.reset()
    
    t.color("white")
    t.hideturtle()
    disegna(t,soldip1,soldip2,turno)
    
    t.teleport(0,-100)
    t.circle(200)
    
    t.teleport(0,100)
   
    for x in range(0,15):
        t.pendown()
        t.left(25)
        
        t.forward(200)
        
        
        t.penup()
        t.backward(200)

    for x in range(0,12):
   
        t.pendown()
        
        t.left(25)
        t.up()
        t.forward(120)
        t.left(90)
        t.forward(50)
        
        
        t.down()
        
        t.up()
        t.backward(50)
        t.left(-90)
        
        t.penup()
        t.backward(120)


    
    
    
        
frasi = [
    "Il gatto mangia il pesce",
    "Il sole splende nel cielo blu",
    "La pizza è il mio cibo preferito",
    "La musica rende tutto migliore",
    "Sto imparando a suonare la chitarra",
    "Andrò al parco per fare una passeggiata",
    "Mi piace guardare film d'azione",
    "La pioggia batte contro la finestra",
    "Ho una lista infinita di cose da fare",
    "Ho trovato un libro interessante da leggere",
    "L'amicizia è un tesoro prezioso",
    "Il caffè è la mia bevanda preferita al mattino",
    "Il sorriso è contagioso",
    "Sto ascoltando la mia canzone preferita",
    "Oggi è una giornata tranquilla",
    "Ho un sacco di energia oggi",
    "Mi piace cucinare per i miei amici",
    "Il tramonto dipinge il cielo di rosso",
    "Ho perso le chiavi di casa",
    "La neve cade silenziosamente",
    "Sto guardando le stelle nel cielo notturno",
    "Mi sento ispirato a creare qualcosa di nuovo",
    "Sto aspettando l'arrivo di un pacco",
    "Ho fatto una passeggiata nel bosco",
    "Il mio computer si è bloccato improvvisamente",
    "Ho sognato di volare stanotte",
    "Sto pianificando una vacanza al mare",
    "La torta al cioccolato è la mia debolezza",
    "Ho perso la partita di calcio ieri sera",
    "Mi piace dipingere quadri astratti",
    "Oggi ho incontrato un vecchio amico per un caffe",
    "Sto leggendo un romanzo fantasy",
    "La risata è la migliore medicina",
    "Ho comprato dei fiori per decorare la casa",
    "Oggi è una giornata noiosa",
    "Ho comprato un biglietto per il concerto",
    "Mi sento fortunato oggi",
    "Sto scrivendo una poesia",
    "Ho bisogno di fare un riposino",
    "Il profumo dei fiori riempie l'aria",
    "Sto aspettando con ansia il mio compleanno",
    "Ho pianto guardando un film commovente",
    "Ho appena finito di leggere un libro fantastico",
    "Il mio telefono è scarico",
    "Sto navigando su Internet alla ricerca di idee",
    "Ho ricevuto una lettera da un amico lontano.",
    "Sto aspettando una telefonata importante",
    "Ho un desiderio segreto che voglio realizzare",
    "Sto godendo di una giornata di sole al parco",
]


stri=""

soldip1=0
soldip2=0
indovina=(frasi[random.randint(0,47)].lower())

for x in range(len(indovina)):
    
    if indovina[x]==" ":
        stri=stri+" "
    elif indovina[x]=="'":
        stri=stri+"'"
        
    else:
        stri=stri+"-"
cont=0

turno=1
parola=""
ruota=[200,100,50,"P","PT","P",500,"P"]
random.shuffle(ruota)


nomep1=t.textinput("Primo giocatore","Inserisci il nome del primo giocatore ")
nomep2=t.textinput("Secondo giocatore","Inserisci il nome del secondo giocatore ")

while True:
    print(indovina)
    disegna(t,soldip1,soldip2,turno)
    
    disegnaruota(t,ruota,soldip1,soldip2,turno)
    scelta=t.textinput("Cosa vuoi fare? ","Scegli se: 1-girare la ruota, 2-provare ad indovinare la frase ,3-comprare una vocale (500 euro) ")
        
    if scelta=="1":
        
        g=random.randint(0,7)
        gira(t,g,ruota,soldip1,soldip2,turno)
        
        
        
        
        
        
        
        if ruota[g]==50 or ruota[g]==100 or ruota[g]==200 or ruota[g]==500:
            
            
           
            
            t.teleport(300,300)
    
            

            t.write("Soldi da vincere: "+ str(ruota[g]),move=False, font=('monaco',30,'bold'),align='left')
            parola=t.textinput("Indovina","Inserisci una consonante ").lower()
            if parola!="a" and parola!="e" and parola!="i" and parola!="o" and parola!="u":
                
                for x in range(len(parola)):
                    
                        
                    if  parola[x] in indovina:
                        for y in range(len(indovina)):
                                if parola==indovina[y]:
                                    stri=stri[:y]+indovina[y]+stri[y+1:]
                                    cont+=1
                                    
                                    
                if turno%2==1 and cont!=0:
                    
                    soldip1=soldip1+ruota[g]*cont
                    t.teleport(300,400)
                    
                    t.write("Soldi vinti "+ str(ruota[g]*cont),move=False, font=('monaco',30,'bold'),align='left')
                    ti.sleep(2)
                    
                    
                    cont=0
    
                elif turno%2==0 and cont!=0:
                    soldip2=soldip2+ruota[g]*cont
                    
                    t.teleport(300,400)
                    t.write("Soldi vinti "+ str(ruota[g]*cont),move=False, font=('monaco',30,'bold'),align='left')
                    ti.sleep(2)

                    
                    
                
                    cont=0
        if ruota[g]=="PT":
            if turno%2==1:
                soldip1=0
            if turno%2==0:
                soldip2=0
    if scelta=="2":
        if t.textinput("Indovina","Prova ad indovinare la frase ")==indovina:
            t.clear()
            t.teleport(-300,100)
            if turno%2==1:
                t.write("MANNAGGIA HAI VINTO "+ str(soldip1+1000)+" Euro",move=False, font=('monaco',30,'bold'),align='left')
                t.done()
                break
            else:
                t.write("MANNAGGIA HAI VINTO "+ str(soldip2+1000)+ " Euro",move=False, font=('monaco',30,'bold'),align='left')
                t.done()
                break
    if scelta=="3":
        if turno%2==1:
            if soldip1>=500:  
            
                scelta=t.textinput("Scegli","Scegli quale vocale comprare: 1 - A , 2 - E , 3 - I , 4 - O , 5 - U")
                if scelta=="1":
                    app="a"
                elif scelta=="2":
                    app="e"
                elif scelta=="3":
                    app="i"
                elif scelta=="4":
                    app="o"
                else:
                    app="u"
                    
                if app in indovina:
                        for y in range(len(indovina)):
                            if app==indovina[y]:
                                stri=stri[:y]+indovina[y]+stri[y+1:]
                
                soldip1-=500
                
        else:
             if soldip2>=500:
                scelta=t.textinput("Scegli","Scegli quale vocale comprare: 1 - A , 2 - E , 3 - I , 4 - O , 5 - U")
                if scelta=="1":
                    app="a"
                elif scelta=="2":
                    app="e"
                elif scelta=="3":
                    app="i"
                elif scelta=="4":
                    app="o"
                else:
                    app="u"
                    
                if app in indovina:
                        for y in range(len(indovina)):
                            if app==indovina[y]:
                                stri=stri[:y]+indovina[y]+stri[y+1:]
                
                soldip2-=500
             
         
    if stri==indovina:
        t.clear()
        t.teleport(-300,100)
        if turno%2==1:
            t.write("MANNAGGIA HAI VINTO "+ str(soldip1+20000)+" Euro",move=False, font=('monaco',30,'bold'),align='left')
            t.done()
            break
        else:
            t.write("MANNAGGIA HAI VINTO "+ str(soldip2+20000)+ " Euro",move=False, font=('monaco',30,'bold'),align='left')
            t.done()
            break
        
            
            
            
                    
    turno+=1            

                
        
 
    
            

    
             
       
    
     