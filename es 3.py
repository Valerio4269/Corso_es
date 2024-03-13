dizionario_boh = {
    "I"  : "S001",
    "II" : "S002",
    "III": "S001",
    "IV" : "S005",
    "V"  : "S005",
    "VI" : "S009",
    "VII": "S007"
}
lista=[]


lista1=[]
for x in dizionario_boh:
    flag=True
    lista1.append(dizionario_boh[x])
cont=0
for x in dizionario_boh:
    cont+=1
    for y in range(cont,len(lista1)):
                if dizionario_boh[x]==lista1[y]:
                    flag=False
    if flag==True:
	     lista.append(dizionario_boh[x])
        

print(lista)
	




