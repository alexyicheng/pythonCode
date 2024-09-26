#26.09.2024
#speicher, um daten zu speichern
from xml.etree.ElementPath import xpath_tokenizer

number = 1
kommazahl = 1.5

print(type(number))
print(type(kommazahl))

#bool variablen True = 1 und False = 0
print(True + False)

#complex y = a + bx
f1 = 1 + 2j
f2 = 2 + 3j
print(f1+f2)

name = 'Hoffmann'
nianling = 18
#%s kein , erforderlich
print('Nachname: %s, Alter: %d' % (name,nianling))

#%4d Ganzzahl
a = 100
b = 506
print('%06d' % a) # anzahl der Ganzer Zahlen, wenn es nicht erfüllt ist, wird davor mit 0 ergänzt
print('%06d' % b)

c = 1.23456
print('%f' % c) #letzen 6 Stellen nach Komma , nach 6 Stellen wird aufgerundet
print('%.3f' % c)

#format {f}
name = 'Daniela'
age = 30
print(f'Ich heiße {name} und ich bin {age} Jahre alt.')