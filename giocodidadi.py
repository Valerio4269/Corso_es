import random 

  

    
    
fine=False
player=input("Inserisci il nome del giocatore ")
banchiere=input("Inserisci il nome del banchiere ")
turno=1
dado=0
dado1=0
dado2=0
soldip=10
soldib=10
casella=[]
posizione=[]
while soldip>0 and soldib>0:
    print("TURNO ",turno )
    print("player: ",player ,"scommetti su una casella o più caselle ")
    print("Su quante caselle vuoi scommettere? ")
    for x in range(int(input("Inserisci il numero delle caselle a cui puntare "))):
       
       
        print("Inserisci una posizione da 1 a 6 ")
        
        pos=int(input("Inserisci la posizione della scommessa "))
        while pos<1 or pos>6:
            print("Inserisci una posizione valida ")
            pos=int(input("Inserisci la posizione della scommessa "))
        
        posizione.append(pos)
        
        
        
        
        valore=int(input("Inserisci la scommessa da inserire: "))
        while valore>soldip:
            print("Inserisci una scommessa valida ")
            valore=int(input("Inserisci la scommessa da inserire: "))    
        
        casella.append(valore)
        soldip-=valore
        print("Ecco il tuo saldo: ", soldip)
    print("LANCIO DEI DADI: ")
    dado=random.randint(1,6)
    dado1=random.randint(1,6)
    dado2=random.randint(1,6)
    cont=0
    print("PRIMO DADO: ",dado, "SECONDO DADO: ",dado1, "TERZO DADO: ",dado2 )
    for x in range(len(casella)):
        
        if dado==dado1==dado2 and posizione[x]==dado and posizione[x]==dado1 and posizione[x]==dado2:
            soldip+=casella[0]*3
            soldib=soldib-(casella[0]*3-casella[0])
            
        elif dado==dado1  and posizione[x]==dado  and posizione[x]==dado1 :
            soldip+=casella[0]*2
            soldib-=casella[0]
            
            casella.remove(casella[0])
        elif dado1==dado2 and posizione[x]==dado1 and posizione[x]==dado2:
            soldip+=casella[0]*2
            soldib-=casella[0]
        
            
            casella.remove(casella[0])
        elif dado==dado2 and posizione[x]==dado and posizione[x]==dado2:
            soldip+=casella[0]*2
            soldib-=casella[0]
            casella.remove(casella[0])
            
            
            casella.remove(casella[0])
        elif dado==posizione[x] or dado1==posizione[x] or dado2==posizione[x]:
            soldip+=casella[0]
            casella.remove(casella[0])


    if len(casella)>0:
        for x in range(len(casella)):
            soldib+=casella[x]
    
    
    turno+=1
    print("Soldi del banchiere: ",soldib)
    print("Soldi del giocatore: ",soldip)
    posizione.clear()
    casella.clear()

print("GIOCO CONCLUSO ")
if soldip>soldib:
    print("IL GIOCATORE ",player, " HA VINTO ")
else:
    print("IL BANCHIERE ",banchiere, "HA VINTO ")
    