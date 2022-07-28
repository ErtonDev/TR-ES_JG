notas = []
add = ["id", "nombre", 0, 0, 0, 0, 0]
n60 = 0
n40 = 0
m60 = 0
m40 = 0
m = 0

while True:
	a = "del 60 o 40?"
	if a == "del 60":
		b = "nota"
		n60 += 1
		add[3] = n60
		m60 = ((m60*(n60-1))+b)/n60
		add[2] = m60
	elif a == "del 40":
		b = "nota"
		n40 += 1
		add[5] = n40
		m40 = ((m40*(n40-1))+b)/n40
		add[4] = m40

	add.append(m)
	m = m60*0.6 + m40*0.4
	add[6] = m

	if len(add) >= 12:
		add.pop(7)

	print(add)