import turtle as t
import random
import threading
import time
mela=t.Turtle()
posxapple=0
posyapple=0
snake=30

flag=False
comando="z"
serpente=[]
cont=1

def scorri(s,cont):
    print(cont)
    return s[cont]
        


def disegna_mela():
    global posxapple
    global posyapple
    global mela
    
    mela.teleport(posxapple,posyapple)
    mela.begin_fill()
    mela.circle(10)
    mela.end_fill()

def w():
    global cont
    cont=1
    testa.sety(t.ycor()+5) 
    avanti(serpente[1])
  

def avanti(s):
    global snake
    global comando
    global cont
    global serpente
    global flag
    
    
    
    s.clear()
        
    
    
        
    
    
    s.sety(t.ycor()+snake)

    
        
    if not posyapple>s.ycor() and posyapple-s.ycor()<50 and posyapple-s.ycor()>0  or posyapple<s.ycor() and s.ycor()-posyapple<50 and s.ycor()-posyapple>0:
                if not posxapple>s.xcor() and posxapple-s.xcor()<50 and posxapple-s.xcor()>0  or posxapple<s.xcor() and s.xcor()-posxapple<50 and s.xcor()-posxapple>0:
                    disegna_mela()
    
    
    cont+=1
    if len(serpente)>2:
        if len(serpente)>cont:
            
            return avanti(scorri(serpente,cont))



def a():
  global cont
  cont=1
  testa.setx(t.xcor()-5) 
  sinistra(serpente[1])
  

def sinistra(s):
    global snake
    global comando
    global cont
    global serpente

    s.clear()
        
    s.setx(t.xcor()-snake) 
        
    if not posyapple>s.ycor() and posyapple-s.ycor()<50 and posyapple-s.ycor()>0  or posyapple<s.ycor() and s.ycor()-posyapple<50 and s.ycor()-posyapple>0:
                if not posxapple>s.xcor() and posxapple-s.xcor()<50 and posxapple-s.xcor()>0  or posxapple<s.xcor() and s.xcor()-posxapple<50 and s.xcor()-posxapple>0:
                    disegna_mela()
    comando="w"
   
    cont+=1
    if len(serpente)>2:
        if len(serpente)>cont:
            return sinistra(scorri(serpente,cont))




def s():
  global cont
  cont=1
  testa.sety(t.ycor()-5) 
  indietro(serpente[1])
  


def indietro(s):
    global snake
    global comando
    global cont
    global serpente
    s.clear()
    
    
    s.sety(t.ycor()-snake)
   
        
    comando="s"
    if not posyapple>s.ycor() and posyapple-s.ycor()<50 and posyapple-s.ycor()>0  or posyapple<s.ycor() and s.ycor()-posyapple<50 and s.ycor()-posyapple>0:
            if not posxapple>s.xcor() and posxapple-s.xcor()<50 and posxapple-s.xcor()>0  or posxapple<s.xcor() and s.xcor()-posxapple<50 and s.xcor()-posxapple>0:
                disegna_mela()
    
    cont+=1
    if len(serpente)>2:
        if len(serpente)>cont:
            return indietro(scorri(serpente,cont))

           
                
def d():
    global cont
    cont=1
    testa.setx(t.xcor()+5)    
    destra(serpente[1])           
    
def destra(s):
    global snake
    global comando
    global cont
    global serpente
    
     
    s.clear()
        
   
    s.setx(t.xcor()+snake)
        
    comando="d"
    if not posyapple>s.ycor() and posyapple-s.ycor()<50 and posyapple-s.ycor()>0  or posyapple<s.ycor() and s.ycor()-posyapple<50 and s.ycor()-posyapple>0:
            if not posxapple>s.xcor() and posxapple-s.xcor()<50 and posxapple-s.xcor()>0  or posxapple<s.xcor() and s.xcor()-posxapple<50 and s.xcor()-posxapple>0:
                disegna_mela()
    
    cont+=1
    if len(serpente)>2:
        if len(serpente)>cont:
            return destra(scorri(serpente,cont))


    

def ascolta():
    
    t.onkeypress(w,"w")
    t.onkeypress(a,"a")
    t.onkeypress(s,"s")
    t.onkeypress(d,"d")
    
    t.listen()

def controlla():
    global snake
    global posyapple
    global posxapple
    global serpente
 
    global flag
    while True:

        
        
        
        
        
        
        if posyapple>t.ycor() and posyapple-t.ycor()<50 and posyapple-t.ycor()>0  or posyapple<t.ycor() and t.ycor()-posyapple<50 and t.ycor()-posyapple>0:
            if posxapple>t.xcor() and posxapple-t.xcor()<50 and posxapple-t.xcor()>0  or posxapple<t.xcor() and t.xcor()-posxapple<50 and t.xcor()-posxapple>0:
                
                mela.clear()
                posxapple=random.randint(-500,500)
                posyapple=random.randint(-500,500)
                
                mela.teleport(posxapple,posyapple)
                mela.begin_fill()
                mela.circle(10)
                mela.end_fill()
                flag=True
                segmento=t.Turtle()
                segmento.color("green")
                segmento.width(10)
                segmento.hideturtle()
                segmento.speed(0)
                
                serpente.append(segmento)
                serpente[len(serpente)-1].teleport(t.xcor(),t.ycor())
                
                
                
                time.sleep(3)
                
                
                


t.setup(1920,1080)
t.bgcolor("black")
t.color("green")
mela.color("red")
mela.speed(100000)
testa=t

serpente.append(testa)
serpente.append(t)


t.width(10)
t.hideturtle()
mela.hideturtle()

t.setx(t.xcor()-snake)


posy=t.ycor()
posx=t.xcor()
posxapple=random.randint(-500,500)
posyapple=random.randint(-500,500)
mela.teleport(posxapple,posyapple)
t.speed(10000000000)
mela.begin_fill()
mela.circle(10)
mela.end_fill()




thread1=threading.Thread(target=ascolta)

thread1.start()
thread=threading.Thread(target=controlla)
thread.start()
t.mainloop()


    
    
