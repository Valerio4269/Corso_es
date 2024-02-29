
import random
parole = [
    "finis",
    "banca",
    "verbo",
    "stare",
    "pieno",
    "felce",
    "fogna",
    "vitro",
    "denti",
    "salto",
    "fusci",
    "barca",
    "terra",
    "notte",
    "fulvo",
    "acqua",
    "nervo",
    "prato",
    "scala",
    "canto",
    "bello",
    "macco",
    "polso",
    "mucce",
    "gente",
    "sciar",
    "rubro",
    "culla",
    "fagro",
    "forse"
]
str="-----"
str1=""
cont=0

indovina=parole[random.randint(0,29)]

while cont<6:
    
    print(indovina)
    parola=input("Inserisci una parola o lettera ")
     
    cont+=1
    for x in range(len(parola)):
        if parola[x]==indovina[x]:
    # str = "pippo"
    # str = str[:1]+"a"+str[2:]
    # print(str)
            str=str[:x]+indovina[x]+str[x+1:]
            
            str1=str1+parola[x]
        elif  parola[x] in indovina:
                str1=str1+"\u001b[92m"+parola[x]+"\u001b[0m"
            
        else:
            str1=str1+"\u001b[31m"+parola[x]+"\u001b[0m"
            
            
       
    
     
            
    print(str)

    
    print(str1)
    str1=""
    
    
    
    if str==indovina:
        print("COMPLIMENTI HAI INDOVINATO ")
        break

if cont==6:
    print("NON HAI INDOVINATO MI DISPIACE")
    