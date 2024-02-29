
def somma(num,num2):
    return int(num)+int(num2)
def sottrazione(num,num2):
    tot=int(num)-int(num2)
    return tot
def moltiplicazione(num,num2):
    tot=int(num)*int(num2)
    return tot
def divisione(num,num2):
    tot=int(num)/int(num2)
    return tot
def calcolo(stringa,num,posizione):
    print(num, "nuemri da calcolare")
    for x in range(len(num)-1):
        if stringa[posizione[x]]=='+': 
            
            tot=somma(num[0],num[1])
            
            num.remove(num[0])
            
            num.remove(num[0])
            
            num.insert(0,tot)
            print(num)
            print(x)
        if stringa[posizione[x]]=='-':
            tot=sottrazione(num[0],num[1])
            
            num.remove(num[0])
            
            num.remove(num[0])
            
            num.insert(0,tot)
            print(num)
            print(x)
        if stringa[posizione[x]]=='*':
            tot=moltiplicazione(num[0],num[1])
            
            num.remove(num[0])
            
            num.remove(num[0])
            
            num.insert(0,tot)
            print(num,"numero")
            
        if stringa[posizione[x]]=='/':
            if flag1==True:
                app2=num[1]
                num.remove(num[1])
                num.insert(0,app2)
            tot=divisione(num[0],num[1])
            
            num.remove(num[0])
            
            num.remove(num[0])
            
            num.insert(0,tot)
    print(len(num))
    return num

stringa=input("Inserisci l'operazione da svolgere ")
num=[]
app=""
tot=0
priorita=0
flag=False
flag1=False
posizione=[]
parentesi=[]
posizioneP=[]
P=False
for x in range(len(stringa)):
    if stringa[x]=='0' or stringa[x]=='1' or stringa[x]=='2' or stringa[x]=='3' or stringa[x]=='4' or stringa[x]=='5' or stringa[x]=='6' or stringa[x]=='7' or stringa[x]=='8' or stringa[x]=='9':
        app=app+stringa[x]
    elif stringa[x]=='*':
        if P==False: 
            if priorita==2:
                flag1=True
                
            num.insert(0,app)
        else:
            if priorita==2:
                flag1=True
                
            parentesi.insert(0,app)
            
        app=""
        flag=True
        priorita=3
        if P==False:
            posizione.insert(0,x)
        else:
            posizioneP.insert(0,x)
    elif stringa[x]=='+':
        if P==False:
            if priorita==3:
                num.insert(1,app)
            elif priorita==2:
                num.insert(1,app)
            else:
                num.insert(len(num),app)
        else:
            if priorita==3:
                parentesi.insert(1,app)
            elif priorita==2:
                parentesi.insert(1,app)
            else:
                parentesi.insert(len(num),app)
            
        app=""
        priorita=1
        if P==False:
            posizione.insert(len(posizione),x)
        else:
            posizioneP.insert(len(posizioneP),x)

    elif stringa[x]=='-':
        if P==False:
            if priorita==3:
                num.insert(1,app)
            elif priorita==2:
                num.insert(1,app)
            else:
                num.insert(len(num),app)
        else:
             if priorita==3:
                parentesi.insert(1,app)
             elif priorita==2:
                parentesi.insert(1,app)
             else:
                parentesi.insert(len(num),app)   
        priorita=1
        app=""
        if P==False:
            posizione.insert(len(posizione),x)
        if P==True:
            posizioneP.insert(len(posizioneP),x)

    elif stringa[x]=='/':
        if P==False:
            if priorita==3:
                num.insert(1,app)
                posizione.insert(1,x)
            else:
                num.insert(0,app)
                posizione.insert(0,x)
        else:
            if priorita==3:
                parentesi.insert(1,app)
                posizioneP.insert(1,x)
            else:
                parentesi.insert(0,app)
                posizioneP.insert(0,x)
        priorita=2
        app=""
    elif stringa[x]=='(':
        P=True
        
    elif stringa[x]==')':
        print(app)
        parentesi.insert(len(parentesi),app)
        print(parentesi,"sdsjdshdsjdffgfgfg")
        print (len(num),"len")
        num.insert(len(num),str(calcolo(stringa,parentesi,posizioneP)[0]))
         
        P=False
        app=""
               
if P==False:
    if x==len(stringa)-1 and priorita==1:
         num.insert(len(num),app)
    elif x==len(stringa)-1 and priorita==3:
        num.insert(1,app)
    elif x==len(stringa)-1 and priorita==2 and flag==True:
        num.insert(2,app)
    elif x==len(stringa)-1 and priorita==2 and flag==False:
        num.insert(1,app)
# else:
#     if x==len(stringa)-1 and priorita==1:
#          parentesi.insert(len(num),app)
#     elif x==len(stringa)-1 and priorita==3:
#         parentesi.insert(1,app)
#     elif x==len(stringa)-1 and priorita==2 and flag==True:
#         parentesi.insert(2,app)
#     elif x==len(stringa)-1 and priorita==2 and flag==False:
#         parentesi.insert(1,app)        
print(posizioneP,"ssdsd")
print(posizione)
print(num)
y=0
print(len(num),"len")

print(num.index('8'),"vuoto")
    
    
    
num.remove('')
    
    
print(calcolo(stringa,num,posizione))
print(parentesi)