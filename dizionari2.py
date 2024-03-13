
def rimuovi(lista,x,y):
    
    lista[x].pop(y)
    return lista




lista=[
    {"nome":"Carlo" ,"Materia":"Italiano","voto1":6,"voto2":8},
    {"nome":"Sergio" ,"Materia":"Italiano","voto1":6,"voto2":6},
    {"nome":"Andra" ,"Materia":"Italiano","voto1":6,"voto2":8}
]
tot=0
for x in range(len(lista)):
    for y in lista[x]:
        if "voto" in y:
            tot=tot+lista[x][y]
            lista1=rimuovi(lista,x)
            
            
    tot=tot/2
    lista1[x].update({"media":tot})
    
    tot=0

print(lista1)