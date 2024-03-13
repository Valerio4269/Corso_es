

def disegna_campo(campo):
    
    str=""
   
    
    
    for x in range(4):
        if  x==1 or x==3:
            app=5
        if  x==2:
            app=6
        else:
            app=4
        for y in range(app):
            if campo[x][y]==2 :
                str=str+"\033[0;46m°w°\033[0;36m"
            
            if campo[x][y]==3 :
                str=str+"\033[0;45m°w°\033[0;36m"
            if campo[x][y]==5:
                str=str+"\033[0;43m°w°\033[0;36m"
            
            
            if campo[x][y]==7:
                str=str+"   "
            if campo[x][y]==1:   
                str=str+" \u001b[31m°\033[0;36m "
             
                
            elif campo[x][y]==4:
                str=str+"\033[0;47mO_O\033[0;36m"
            
                
                
            elif campo[x][y]==0:
                if x==1 and y==1 or x==3 and y==1 or x==2 and y==2 or x==3 and y==1 or x==3 and y==3 or x==1 and y==3 or x==2 and y==4 or x==2 and y==0 :
                  str=str+"\u001b[31m - \033[0;36m"
                
                else:
                    str=str+" - "
            
            
            
        print(str)
        str=""
        
   
    
        
        
        
        
        
    return 

def controllo_pos(turno,scelta,campo):
    pos=[]
    if turno%2==1:
        if scelta==1:
            for x in range(4):
                if x==2 or x==1 or x==3:
                 app=5
                else:
                  app=4
                for y in range(app):
                    
                    if campo[x][y]==2:
                        pos.append(x)
                        
                        pos.append(y)
                        
                       
                        return pos
        if scelta==2:
            for x in range(4):
                if x==2 or x==1 or x==3:
                 app=5
                else:
                  app=4
                for y in range(app):
                    if campo[x][y]==3:
                        pos.append(x)
                        pos.append(y)
                        
                        return pos
        if scelta==3:
            for x in range(4):
                if x==2 or x==1 or x==3:
                 app=5
                else:
                  app=4
                for y in range(app):
                    if campo[x][y]==5:
                        pos.append(x)
                        pos.append(y)
                        
                        return pos
    if turno%2==0:
         
        for x in range(4):
                if  x==1 or x==3:
                 app=5
                if  x==2:
                 app=6
                else:
                  app=4
                for y in range(app):
                    if campo[x][y]==4:
                        pos.append(x)
                        pos.append(y)
                        
                        return pos
                       
   
            
            
            




campo=[[7,7,7,7,7,7,7],[7,2,0,0,7,7,7],[3,0,0,0,4,7,7,7],[7,5,0,0,7,7,7],[7,7,7,7,7,7,7]]

turno=1

while True:
        print("\033[0;31mTURNO", turno,"\033[0;36m ")
        
        if turno%2==1:
            print("\033[0;31mTURNO GIOCATORE 1\033[0;36m")
        else:
            print("\033[0;31mTURNO GIOCATORE 2\033[0;36m")
        
        
        
        
        pos=[]
        
        
        disegna_campo(campo)
    
        
        if turno%2==1:
            scelta=int(input("Inserisci quale dei lupi spostare: (1-Celeste, 2-Viola, 3-Giallo) "))
           
                
         
            
            pos=controllo_pos(turno,scelta,campo)
        
                
                
                
        
                
                
            mossa=input("Inserisci una mossa :  w,a,d,x,e ")
            
             
            while mossa=="x" or mossa=="e":
                
                if  pos[0]==2 and pos[1]==1 or pos[0]==1 and pos[1]==1 or pos[0]==2 and pos[1]==3 or pos[0]==2 and pos[1]==3 :
                    mossa=input("Inserisci una mossa valida :  w,a,d  ")
                else:
                    break
                        
            
            while mossa!="w" and mossa!="a"  and mossa!="d" and mossa!="e" and mossa!="x":
                mossa=input("Inserisci una mossa valida :  w,a,d,e,x  ")
               
            
            
            while mossa=="w" and campo[pos[0]][pos[1]+1]!=0 or mossa=="a" and campo[pos[0]-1][pos[1]]!=0 or mossa=="d" and campo[pos[0]+1][pos[1]]!=0   or mossa=="e" and campo[pos[0]-1][pos[1]+1]!=0  or mossa=="d" and campo[pos[0]+1][pos[1]]!=0 or mossa=="x" and campo[pos[0]+1][pos[1]+1]!=0:
                mossa=input("Inserisci una mossa valida :  w,a,d,e,x ")
                
                
            
            
                
                
            if mossa=="w":
                
                    
                    app=campo[pos[0]][pos[1]]
                    campo[pos[0]][pos[1]]=campo[pos[0]][pos[1]+1]
                    campo[pos[0]][pos[1]+1]=app
            if mossa=="a":
                if campo[pos[0]-1][pos[1]]==7:
                    app=campo[pos[0]][pos[1]]
                    campo[pos[0]][pos[1]]=campo[pos[0]-1][pos[1]+1]
                    campo[pos[0]-1][pos[1]+1]=app
                else:
                    app=campo[pos[0]][pos[1]]
                    campo[pos[0]][pos[1]]=campo[pos[0]-1][pos[1]]
                    campo[pos[0]-1][pos[1]]=app
                    
            
            if mossa=="d":
                if campo[pos[0]-1][pos[1]]==7:
                    app=campo[pos[0]][pos[1]]
                    campo[pos[0]][pos[1]]=campo[pos[0]+1][pos[1]+1]
                    campo[pos[0]+1][pos[1]+1]=app
                else:
                    app=campo[pos[0]][pos[1]]
                    campo[pos[0]][pos[1]]=campo[pos[0]+1][pos[1]]
                    campo[pos[0]+1][pos[1]]=app
            
            if mossa=="e":
                    app=campo[pos[0]][pos[1]]
                    campo[pos[0]][pos[1]]=campo[pos[0]-1][pos[1]+1]
                    campo[pos[0]-1][pos[1]+1]=app
            if mossa=="x":
                    app=campo[pos[0]][pos[1]]
                    campo[pos[0]][pos[1]]=campo[pos[0]+1][pos[1]+1]
                    campo[pos[0]+1][pos[1]+1]=app
           
                
            
        else: 
            pos=controllo_pos(turno,scelta,campo)
            if  campo[pos[0]][pos[1]-1]!=0  and campo[pos[0]-1][pos[1]]!=0 and campo[pos[0]-1][pos[1]]!=0 and campo[pos[0]+1][pos[-1]]!=0  and campo[pos[0]+1][pos[1]]!=0 and campo[pos[0]+1][pos[1]]!=0  and campo[pos[0]+1][pos[1]+1]!=0 and campo[pos[0]-1][pos[1]+1]!=0  and campo[pos[0]+1][pos[1]]!=0 and campo[pos[0]+1][pos[1]]!=0  and campo[pos[0]-1][pos[1]-1]!=0  and campo[pos[0]+1][pos[1]+1]!=0  and campo[pos[0]][pos[1]+1]!=0:
                print("\033[0;31mIL GIOCATORE 1 HA VINTO ")
                break
            
            mossa=input("Inserisci una mossa :  w,a,s,d,e,x,r,v ")
            
            while mossa!="w" and mossa!="a" and mossa!="s" and mossa!="d" and mossa!="e" and mossa!="x" and mossa!="r" and mossa!="v":
                mossa=input("Inserisci una mossa valida :  w,a,s,d,e,x,r,v  ")
                
            while mossa=="x" or mossa=="e" or mossa=="r" or mossa=="v":
                
                if  pos[0]==2 and pos[1]==1 or pos[0]==1 and pos[1]==1 or pos[0]==2 and pos[1]==3  :
                    mossa=input("Inserisci una mossa valida :  w,a,s,d  ")
                else:
                    break
                        
                
                
            while mossa=="w" and campo[pos[0]][pos[1]-1]!=0 or mossa=="v" and campo[pos[0]+1][pos[1]+1]!=0  or mossa=="r" and campo[pos[0]-1][pos[1]+1]!=0  or mossa=="a" and campo[pos[0]+1][pos[1]]!=0   or mossa=="d" and campo[pos[0]-1][pos[1]]!=0 or mossa=="e" and campo[pos[0]-1][pos[1]-1]!=0   or mossa=="x" and campo[pos[0]+1][pos[1]-1]!=0 or mossa=="s" and campo[pos[0]][pos[1]+1]!=0:
                mossa=input("Inserisci una mossa valida :  w,a,s,d,e,x,r,v  ")
                
                
            
            if mossa=="w":
                  
                       
                    app=campo[pos[0]][pos[1]]
                    
                    campo[pos[0]][pos[1]]=campo[pos[0]][pos[1]-1]
                    campo[pos[0]][pos[1]-1]=app
            if mossa=="d":
                if campo[pos[0]-1][pos[1]]==7:
                    app=campo[pos[0]][pos[1]]
                    campo[pos[0]][pos[1]]=campo[pos[0]-1][pos[1]-1]
                    campo[pos[0]-1][pos[1]-1]=app
                else:
                    app=campo[pos[0]][pos[1]]
                    campo[pos[0]][pos[1]]=campo[pos[0]-1][pos[1]]
                    campo[pos[0]-1][pos[1]]=app
                       
            
            if mossa=="a":
                print(campo[pos[0]+1][pos[1]])
                if campo[pos[0]+1][pos[1]]==7:
                    app=campo[pos[0]][pos[1]]
                    campo[pos[0]][pos[1]]=campo[pos[0]+1][pos[1]-1]
                    campo[pos[0]+1][pos[1]-1]=app
                else:
                    app=campo[pos[0]][pos[1]]
                    campo[pos[0]][pos[1]]=campo[pos[0]+1][pos[1]]
                    campo[pos[0]+1][pos[1]]=app
            
            if mossa=="e":
                    app=campo[pos[0]][pos[1]]
                    campo[pos[0]][pos[1]]=campo[pos[0]-1][pos[1]-1]
                    campo[pos[0]-1][pos[1]-1]=app
            if mossa=="x":
                    app=campo[pos[0]][pos[1]]
                    campo[pos[0]][pos[1]]=campo[pos[0]+1][pos[1]-1]
                    campo[pos[0]+1][pos[1]-1]=app
            if mossa=="s":
                    if campo[pos[0]][pos[1]+1]==0:
                        app=campo[pos[0]][pos[1]]
                        campo[pos[0]][pos[1]]=campo[pos[0]][pos[1]+1]
                        campo[pos[0]][pos[1]+1]=app
            if mossa=="r":
                    if campo[pos[0]-1][pos[1]+1]==0:
                        app=campo[pos[0]][pos[1]]
                        campo[pos[0]][pos[1]]=campo[pos[0]-1][pos[1]+1]
                        campo[pos[0]-1][pos[1]+1]=app
            if mossa=="v":
                    if campo[pos[0]+1][pos[1]+1]==0:
                        app=campo[pos[0]][pos[1]]
                        campo[pos[0]][pos[1]]=campo[pos[0]+1][pos[1]+1]
                        campo[pos[0]+1][pos[1]+1]=app
            
        disegna_campo(campo)
        if controllo_pos(1,1,campo)[1]>= controllo_pos(2,1,campo)[1] and controllo_pos(1,2,campo)[1]>=controllo_pos(2,1,campo)[1] and controllo_pos(1,3,campo)[1]>=controllo_pos(2,1,campo)[1]:
                print("\033[0;31mIL GIOCATORE 2 HA VINTO")
                break
        
        
        
        
            
        
        
            
            
        turno+=1

                
        
    
#     turno+=1