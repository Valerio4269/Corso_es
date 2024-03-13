voti_di_carlo = {
    "italiano"         :  6,
    "matematica"       :  9,
    "storia"           :  5,
    "geografia"        :  7,
    "educazione_fisica": 10,
    "storia_dell_arte" :  7
}
min=100000
max=0
for x in voti_di_carlo:
	if voti_di_carlo[x]<min:
		min=voti_di_carlo[x]
	if voti_di_carlo[x]>max:
		max=voti_di_carlo[x]

print(min,max)
