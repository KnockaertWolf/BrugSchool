import random
import time

def newPoint(x: int) -> str: 			# Functie die een willekeurig paar nummers genereert
	y = random.randint(0,50)
	data = f"{x},{y}\n"
	return data

f = open("fig1.txt", "w").close() 		# Ledig bestand

t = 0
while True:

	data = newPoint(t)				# Genereer paar waarden met functie
	f = open("fig1.txt", "a")
	f.write(data)
	f.close()						# Sla de waarde op in een bestand
	t = t + 1						
	time.sleep(1)						# Wacht 1 seconde
