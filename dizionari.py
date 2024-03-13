
valori = {
    'chiave1': [10, 20, 30],
    'chiave2': [40, 50],
    'chiave3': [60, 70, 80, 90],
    'chiave4': [100],
    'chiave5': [110, 120, 130],
    'chiave6': [110, 120, 130,12,34],
    'chiave7': [101],
}
min=100000
for x in valori:
    if len(valori[x])<min:
        min=len(valori[x])
        app=x
    
for x in valori:
    if len(valori[x])==min:
        print(x)  
        
    

