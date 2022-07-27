notas = []

while True: 
	add = []
	ask = int(input("afegir asignatura? "))
	if ask == 1:
		name = input("nom? ")
		add.append(name)
	else:
		break

	noteask = int(input("vols afegir notes? "))
	if noteask == 1:
		note = float(input("nota? "))
		n = 1
		add.append(note)
		add.append(n)
		noteaskagain = int(input("vols afegir mes notes?"))
		while noteaskagain == 1:
			a=add[2]
			add.append(a)
			note = float(input("nota? "))
			n+=1
			canvi = ((a*(n-1))+note)/n
			add[2]=canvi
			add[3]=n
			if len(add) >= 9:
				add.pop(4)
			noteaskagain = int(input("vols afegir mes notes?"))
	notas.append(add)

print(notas)