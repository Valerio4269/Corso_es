


    
def disegnastring(col,rig):
    nim=[]
    for x in range(col):
        
        
        for y in range(rig[x]):
            if y==0:
                stringa=""
            stringa=stringa+"*"
        nim.insert(col,stringa)
    for x in nim:
        print(x)
                
def verifica(num):
    if len(num)==0:
        print("HAI VINTO")
        return True
    
        
    
   
 
    
numeri=[]
player1=input("Inserisci il nome ")
player2=input("Inserisci il nome ")

num=int(input("Inserisci il numero di colonne "))
stringa='x'
nim=[]
for x in range(num):
    stel=int(input("Inserisci il numero di nim "))
    for y in range(stel):
        if y==0:
            stringa=""
        stringa=stringa+"*"
    nim.insert(num,stringa)
    numeri.insert(num,stel)

    

print("------------------------------------")
for x in nim:
    print(x)

fine=0

decidi=""
decidi1=0
turno=1
giocatore=0
while fine!=1:
    try:
        if turno%2==1:
            giocatore=1
        else: giocatore=2
        print("NUMERO TURNO: ", turno)
        print("TURNO GIOCATORE ",giocatore)

            
        if len(numeri)>1:
            decidi=int(input("Decidi a quale colonna cancellare il nim "))-1
        else:
            decidi=0
        decidi1=int(input("Inserisci il numero di nim da cancellare "))
        numeri[decidi]=numeri[decidi]-decidi1
        if(numeri[decidi]<=0):
            numeri.remove(numeri[decidi])

        if verifica(numeri)==True:
            fine=1
            break
        disegnastring(len(numeri),numeri)
    
        turno+=1

            

        
       
    except:
        print("Inserisci un numero valido!")
        if len(numeri)>1:
            decidi=int(input("Decidi a quale colonna cancellare il nim "))-1
        else:
            decidi=0
        decidi1=int(input("Inserisci il numero di nim da cancellare "))
        numeri[decidi]=numeri[decidi]-decidi1
        if(numeri[decidi]<=0):
            numeri.remove(numeri[decidi])
        verifica(numeri)
        disegnastring(len(numeri),numeri)

    
    
    
         
        
    
    
        
        
        


    