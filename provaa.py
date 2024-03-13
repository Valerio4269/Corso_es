

def disegna_campo(campo):
    
    str=""
   
    
    
    for x in range(4):
        if x==2 or x==1 or x==3:
            app=5
        else:
            app=4
        for y in range(app):
            if campo[x][y]==2:
                str=str+"°w°"
            if campo[x][y]==7:
                str=str+"   "
            if campo[x][y]==1:   
                str=str+" \u001b[31m°\033[0;36m "
             
                
            elif campo[x][y]==4:
                str=str+"O_O"
            elif campo[x][y]==3:
                str=str+" \u001b[31m*\033[0;36m "
                
                
            elif campo[x][y]==0:
                str=str+" - "
            
            
        print(str)
        str=""
        
   
    
        
        
        
        
        
    return 

def controllo_pos(turno,scelta,campo):
    pos=[]
    if turno%2==1:
        if scelta==1:
            for x in range(4):
                for y in range(3):
                    
                    if campo[x][y]==1:
                        pos.append(x)
                        
                        pos.append(y)
                        
                       
                        return pos
        if scelta==2:
            for x in range(4):
                for y in range(3):
                    if campo[x][y]==2:
                        pos.append(x)
                        pos.append(y)
                        
                        return pos
    if turno%2==0:
         if scelta==1:
            for x in range(4):
                for y in range(3):
                    if campo[x][y]==3:
                        pos.append(x)
                        pos.append(y)
                        
                        return pos
         if scelta==2:
            for x in range(4):
                for y in range(3):
                    if campo[x][y]==4:
                        pos.append(x)
                        pos.append(y)
                        
                        return pos
    return False               
   
            
            
            




campo=[[6,6,6,6],[7,2,0,0,6],[2,0,0,0,4],[7,2,0,0,6],[7,7,7,7]]

turno=1

while True:
        print("\033[0;31mTURNO", turno,"\033[0;36m ")
        
        if turno%2==1:
            print("\033[0;31mTURNO GIOCATORE 1\033[0;36m")
        else:
            print("\033[0;31mTURNO GIOCATORE 2\033[0;36m")
        
        
        
        
        pos=[]
        
        
        disegna_campo(campo)
    
        
        if controllo_pos(turno,1,campo)!=False and controllo_pos(turno,2,campo)!=False:
            pos=controllo_pos(turno,1,campo)
            
            if campo[pos[0]-1][pos[1]]!=0 and campo[pos[0]][pos[1]-1]!=0 and campo[pos[0]][pos[1]+1]!=0 and campo[pos[0]-1][pos[1]]!=6   :
                pos=controllo_pos(turno,2,campo)
                if campo[pos[0]-1][pos[1]]!=0 and campo[pos[0]][pos[1]-1]!=0 and campo[pos[0]][pos[1]+1]!=0 and campo[pos[0]-1][pos[1]]!=6 :
                        print("IL GIOCATORE 2 HA VINTO")
                        break
        elif controllo_pos(turno,1,campo)!=False and controllo_pos(turno,2,campo)!=False:
                pos=controllo_pos(turno,1,campo)
                if campo[pos[0]-1][pos[1]]!=0 and campo[pos[0]][pos[1]-1]!=0 and campo[pos[0]][pos[1]+1]!=0 and campo[pos[0]-1][pos[1]]!=6   :
                    print("IL GIOCATORE 2 HA VINTO")
                    break
        elif controllo_pos(turno,1,campo)==False and controllo_pos(turno,2,campo)!=False:
                pos=controllo_pos(turno,2,campo)
                if campo[pos[0]-1][pos[1]]!=0 and campo[pos[0]][pos[1]-1]!=0 and campo[pos[0]][pos[1]+1]!=0 and campo[pos[0]-1][pos[1]]!=6   :
                    print("IL GIOCATORE 2 HA VINTO")
                    break
            
    
        if controllo_pos(turno,1,campo)!=False and controllo_pos(turno,2,campo)!=False:
            pos=controllo_pos(turno,1,campo)
            if campo[pos[0]-1][pos[1]]!=0 and campo[pos[0]+1][pos[1]]!=0 and campo[pos[0]][pos[1]+1]!=0 and  campo[pos[0]][pos[1]+1]!=6:
                pos=controllo_pos(turno,2,campo)
                if campo[pos[0]-1][pos[1]]!=0 and campo[pos[0]+1][pos[1]]!=0 and campo[pos[0]][pos[1]+1]!=0 and campo[pos[0]][pos[1]+1]!=6:
                    print("IL GIOCATORE 1 HA VINTO")
                    break
        elif controllo_pos(turno,1,campo)!=False and controllo_pos(turno,2,campo)!=False:
                pos=controllo_pos(turno,1,campo)
                if campo[pos[0]-1][pos[1]]!=0 and campo[pos[0]+1][pos[1]]!=0 and campo[pos[0]][pos[1]+1]!=0 and campo[pos[0]][pos[1]+1]!=6  :
                    print("IL GIOCATORE 1 HA VINTO")
                    break
        elif controllo_pos(turno,1,campo)==False and controllo_pos(turno,2,campo)!=False:
                pos=controllo_pos(turno,2,campo)
                if campo[pos[0]-1][pos[1]]!=0 and campo[pos[0]+1][pos[1]]!=0 and campo[pos[0]][pos[1]+1]!=0  and campo[pos[0]][pos[1]+1]!=6  :
                    print("IL GIOCATORE 1 HA VINTO")
                    break
            
        
        
            
            
            
        if controllo_pos(turno,1,campo)!=False and controllo_pos(turno,2,campo)!=False:
            
            scelta=int(input("Inserisci quale delle due macchine spostare "))
            
        if controllo_pos(turno,1,campo)==False:
            scelta=2
        elif controllo_pos(turno,2,campo)==False:
            scelta=1
         
        
        pos=controllo_pos(turno,scelta,campo)
        if turno%2==0:
            if campo[pos[0]-1][pos[1]]!=0 and campo[pos[0]+1][pos[1]]!=0 and campo[pos[0]][pos[1]+1]!=0 and campo[pos[0]-1][pos[1]]!=6 and campo[pos[0]+1][pos[1]]!=6 and campo[pos[0]][pos[1]+1]!=6:
                if scelta==1:
                    scelta=2
                    pos=controllo_pos(turno,scelta,campo)
                    print("Questa nave non si può spostare, sposta l'altra ")
                else:
                    scelta=1
                    pos=controllo_pos(turno,scelta,campo)
                    print("Questa nave non si può spostare, sposta l'altra ")
        else:
          if  campo[pos[0]-1][pos[1]]!=0 and campo[pos[0]][pos[1]-1]!=0 and campo[pos[0]][pos[1]+1]!=0 and campo[pos[0]-1][pos[1]]!=6 and campo[pos[0]][pos[1]-1]!=6 and campo[pos[0]][pos[1]+1]!=6:
              if scelta==1:
                    scelta=2
                    pos=controllo_pos(turno,scelta,campo)
                    print("Questa nave non si può spostare, sposta l'altra ")
              else:
                    scelta=1
                    pos=controllo_pos(turno,scelta,campo)
                    print("Questa nave non si può spostare, sposta l'altra ")
        
        
        
        
        mossa=input("Inserisci una mossa :  w,a,d ")
        
            
            
            
        if turno%2==1:
            
            
            
            
            
            while mossa=="w" and campo[pos[0] -1][pos[1]]!=0 and campo[pos[0]-1][pos[1]]!=6 or mossa=="a" and campo[pos[0]][pos[1]-1]!=0 or mossa=="d" and campo[pos[0]][pos[1]+1]!=0 :
                mossa=input("Inserisci una mossa valida :  w,a,d ")
        
            
            
            if mossa=="w":
                  
                if campo[pos[0]-1][pos[1]]==6:
                      campo[pos[0]][pos[1]]=0
                else:
                       
                    app=campo[pos[0]][pos[1]]
                    campo[pos[0]][pos[1]]=campo[pos[0]-1][pos[1]]
                    campo[pos[0]-1][pos[1]]=app
            if mossa=="a":
                app=campo[pos[0]][pos[1]]
                campo[pos[0]][pos[1]]=campo[pos[0]][pos[1]-1]
                campo[pos[0]][pos[1]-1]=app
            if mossa=="d":
                app=campo[pos[0]][pos[1]]
                campo[pos[0]][pos[1]]=campo[pos[0]][pos[1]+1]
                campo[pos[0]][pos[1]+1]=app
        else:
            while mossa=="a" and campo[pos[0]-1][pos[1]]!=0 or mossa=="w" and campo[pos[0]][pos[1]+1]!=0 and campo[pos[0]][pos[1]+1]!=6 or mossa=="d" and campo[pos[0]+1][pos[1]]!=0:
                mossa=input("Inserisci una mossa valida :  w,a,d ")
                
           
            
            
            
            
            if mossa=="a":
                        
                app=campo[pos[0]][pos[1]]
                campo[pos[0]][pos[1]]=campo[pos[0]-1][pos[1]]
                campo[pos[0]-1][pos[1]]=app
            if mossa=="w":
                
                if campo[pos[0]][pos[1]+1]==6:
                      campo[pos[0]][pos[1]]=0
                else:
                
                    app=campo[pos[0]][pos[1]]
                    campo[pos[0]][pos[1]]=campo[pos[0]][pos[1]+1]
                    campo[pos[0]][pos[1]+1]=app
            if mossa=="d":
                app=campo[pos[0]][pos[1]]
                campo[pos[0]][pos[1]]=campo[pos[0]+1][pos[1]]
                campo[pos[0]+1][pos[1]]=app
        
        if turno%2==1:
            if controllo_pos(turno,1,campo)==False and controllo_pos(turno,2,campo)==False:
                print("IL GIOCATORE 1 HA VINTO")
                break
        else:
            if controllo_pos(turno,1,campo)==False and controllo_pos(turno,2,campo)==False:
                print("IL GIOCATORE 2 HA VINTO")
                break
          
        
        disegna_campo(campo)
            
            
        turno+=1

                
        
    
#     turno+=1