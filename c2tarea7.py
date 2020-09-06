#10.2 Write a program to read through the mbox-short.txt and figure out the
#distribution by hour of the day for each of the messages. You can pull the
#hour out from the 'From ' line by finding the time and then splitting the
#string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts,
#sorted by hour as shown below.

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
fh = open(name)

#seleccionar
lista=list()

for line in fh:
    if not line.startswith("From "):
        continue        
    words=line.split()
    WORDS=words[5]
    horas=WORDS.split(':')
    HORAS=horas[0]
    lista.append(HORAS)

#contador
counts=dict()
for h in lista:
    counts[h] = counts.get(h,0) + 1

#ordenar
LISTA=list()
for h,c in counts.items():
    newtp=(h,c)
    LISTA.append(newtp)
    LISTA=sorted(LISTA)

#respuesta
for h,c in LISTA[:]:
    print(h,c)
#terminado from scratch:)
    
    

       
#for h,c in counts.items():
    
    
    
