
import random
import turtle as t
t.hideturtle()

parole = [
    "mela", "banana", "arancia", "fragola", "ananas",
    "limone", "uva", "ciliegia", "pera", "kiwi",
    "pesca", "melone", "mango", "pompelmo", "mirtillo",
    "ribes", "lamponi", "lampone", "mandarino", "nocciola",
    "cocco", "papaya", "clementina", "albicocca", "frutto",
    "limetta", "pomodoro", "zucca", "carota", "patata",
    "sedano", "cipolla", "peperone", "insalata", "spinaci",
    "cavolo", "broccolo", "zucchine", "cetriolo", "ravanelli",
    "barbabietola", "porro", "prezzemolo", "basilico", "rosmarino",
    "salvia", "menta", "dragoncello", "origano", "timo",
    "alloro", "chiodi di garofano", "cannella", "peperoncino", "zenzero",
    "aglio", "cipollotto", "melanzana", "funghi", "porcini",
    "champignon", "tartufo", "asparago", "fagiolo", "pisello",
    "lenticchia", "ceci", "cereale", "riso", "avena",
    "orzo", "mais", "grano", "farro", "segale",
    "quinoa", "grano saraceno", "amaranto", "miglio", "sorgo",
    "frumento", "pane", "pasta", "pizza", "biscotto",
    "torta", "cioccolato", "gelato", "dolce", "salato",
    "piccante", "amaro", "acido", "salato", "saporito"
]

stri=""

cont=0
pos=t.pos()
indovina=parole[random.randint(0,29)]

for x in range(len(indovina)):
    
    if indovina[x]==" ":
        stri=stri+" "
    else:
        stri=stri+"_"



parola=""
while cont<7:
    
    flag=False
    t.setup(1000,1080)
    t.color("white")
    t.goto(-200,200)
    t.color("black")
    t.write("NUMERO PAROLE: "+str(len(indovina)),move=False, font=('monaco',30,'bold'),align='left')
    t.color("white")
    t.setpos(300,100)
    
    t.color("black")
    t.write(stri,move=False, font=('monaco',30,'bold'),align='left')
    
    
    
    parola=t.textinput("Indovina","Inserisci una lettera ")
    
    for x in range(len(parola)):
        
            
        if  parola[x] in indovina:
            for y in range(len(indovina)):
                    if parola==indovina[y]:
                        stri=stri[:y]+indovina[y]+stri[y+1:]
                        flag=True
    t.color("white")
    t.setpos(pos)
    t.color("black")
    if flag==False:
        cont+=1
         
        if cont==1:

         t.left(90)
         t.forward(100)
         t.right(-90)
         t.forward(300)
         t.left(90)
         t.forward(500)
         t.left(-270)
         
            
         
        elif cont==2:
            t.right(90)
            t.color("white")
            t.forward(100)
            t.color("black")
            t.left(90)
            t.circle(50)
            pos=t.pos()
        elif cont==3:
            t.left(-90)
            t.forward(200)
            pos1=t.pos()
        elif cont==4:
            t.setpos(pos)
            t.left(-45)
            t.forward(100)
        elif cont==5:
            t.setpos(pos)
            t.left(90)
            t.forward(100)
        elif cont==6:
            t.setpos(pos1)
            t.left(-90)
            t.forward(100)
        elif cont==7:
            t.setpos(pos1)
            t.left(90)
            t.forward(100)
            
            

    
             
       
    
     
            
    

    
    t.color("white")
    t.setpos(300,100)
    
    t.color("black")
    t.write(stri,move=False, font=('monaco',30,'bold'),align='left')
    
    if stri==indovina:
        t.color("white")
        t.setpos(-200,300)
        t.color("black")
        t.write("MANNAGGIA HAI VINTO",move=False, font=('monaco',30,'bold'),align='left')
        t.done()
        break

t.color("white")
t.setpos(-400,300)
t.color("black")
t.write("COMPLIMENTI HAI PERSO, PAROLA DA INDOVINARE: " + str(indovina),move=False, font=('monaco',30,'bold'),align='left')
t.done()  