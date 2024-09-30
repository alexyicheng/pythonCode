# 28.09.2024

# # tuple
# # unterstützt nur die Funktion Suche(Abfrage)
# # unterstützt keine Hinzufügen-, löschen- und ersetzen-Funktion
# # wenn nur ein Element gebe, ein Komma muss gesetzen werden
# tua = (1,2,3,'a','b')
# print(type(tua))
# print(tua.index(2))
# print(tua.count(1))
# print(len(tua))
#
# name = 'Sophia'
# age = 23
# # option 1
# # print(f'{name} ist {age} Jahre Alt')
# # option 2
# print('%s ist %d Jahre alt' % (name,age))
#
# # dictionary
# dic = {'name':'Felix','age':11}
# print(type(dic))
#
# # 'name' kann nicht mehrfach vorkommen, werte werden überschreiben
# # dic_2 = {'name':'Dennis','name':'Thomas'}
# # print(dic_2)
#
# # Element in Dictionary abfragen
# # option 1
# print(dic['name'])
# # option 2
# print(dic.get('name'))
# # Wenn das Element nicht in der Dictionary drin ist, gibt den Werte None zurück
# print(dic.get('tel','gibt es nicht'))
#
# # Element ändern
# dic['age'] = 85
#
# #Element hinzufügen
# # option 1
# geschlecht = {'Geschlecht':'m'}
# dic.update(geschlecht)
# print(dic)
# # option 2 - bei neuem Element wird die fehlenden Informationen automatisch ergänzt
# dic['age'] = 11
# print(dic)
#
# # Element löschen
# # del dic['age']
# # print(dic)
#
# #dictionary entleeren
# # dic.clear()
# # print(dic)
#
# #pop() bestimmtes Element löschen
# # dic.pop('age')
# # print(dic)
# # popitem() - immer das letztes Element aus der Dictionary löschen
# # dic.popitem()
# # print(dic)
#
# new_dic = {'Name':'Jojo','Alter':5,'tel':'01112515'}
# print(len(new_dic)) # Es gibt 3 Elemente zurück
#
# for item in new_dic.keys():
#     print(item)
#
# for item in new_dic.values():
#     print(item)
#
# for item in new_dic.items():
#     print(item,type(item)) # item is tuple

#set
s1 = {1,2,3}
print(s1) # Reihenfolge der Ergebnisse ist immer gleich
s2 = {'a','b','c','d','e','f'}
print(s2) # Reihenfolge der Ergebnisse ist immer ungleich (Hash)

# set Element hinzufügen

# s2.add('z') # jedes Mal kann man nur ein Element hinzufügen
# print('new set s2:',s2)

# set Element update
# einzel Element hinzufügen
#s2.update({'name':'Alpfa'})

#s2.update('xyz')
#s2.update((5,6,7))
# s2.update([8,9,10])
# print(s2)


# set remove
s2.remove('a')
print(s2)

#set pop
s2.pop()
print(s2) # Immer das erste Element entfernen

#set discard
s2.discard('b')
print(s2)


#Schnittstelle
a = {1,2,3,4}
b = {3,4,5}
print(a&b)

# Zusammenfassen
# alle Elemente zusammenfassen ohne Dubletten
a = {1,2,3,4}
b = {3,4,5,6}
print(a|b)





