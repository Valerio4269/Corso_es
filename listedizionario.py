lista=[
    {'student_id': 1, 'name': 'Jean Castro', 'class': 'V'},
    {'student_id': 2, 'name': 'Lula Powell', 'class': 'V'},
    {'student_id': 3, 'name': 'Brian Howell', 'class': 'VI'},
    {'student_id': 4, 'name': 'Lynne Foster', 'class': 'VI'},
    {'student_id': 5, 'name': 'Zachary Simon', 'class': 'VII'}
]


lista1=[]


for x in range(len(lista)):
    lista1.append([])
    for y in lista[x]:
        lista1[x].append(lista[x][y])

print(lista1)