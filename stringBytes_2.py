#28.09.2024

# name = 'Dagema'
# print(name.find('a'))
# print(name.find('ge'))
# print(name.find('g',3,5)) # Wenn keine Werte findet, gibt -1 zurück
#
# #print(name.index('g',3,5)) # Wenn keine Werte gefinden wird, gibt index eine Fehlermeldung zurück statt -1
#
# print(name.count('a'))
#
# st =  'Tim Duncan'
# print(st.startswith('Tim'))
# print(st.endswith('can'))
#
# text = 'Was für ein Tag'
# #replace(old, new, how many times)
# print(text.replace('a','Y',1))
#
# print(text.lower())
# print(text.upper())
#
# text_2 = 'abcedef'
# # Nur der erster Buchstabe wird groß geschrieben
# print(text_2.capitalize())
#
# li = [1,2,3,4,5,'voll']
# for i in li:
#     print(i)
#
# li.append('four') # füge das gesamte Element hinzu
# print(li)
# # z.B. 4 kann nicht mit extend hinzugefügt werden
# li.extend('four') # fügt jedes einzelne Element hinzu
# print(li)
#
# #Wenn keine Position angeben ist, gibt Fehler zurück
# li.insert(0,'first') # muss die position angeben, an welche Stelle das Element hinzugefügt würden soll und alle Elemente wird nachhinterverschoben
#
# # name_list = ['Nicole','Daniela','Armin']
# # name = input('Please insert your name into the list')
# # while True:
# #     if name in name_list:
# #         print(f'{name} exists already')
# #     else:
# #         print(f'{name} inserts into the name_list')
# #         name_list.append(name)
# #         print(name_list)
# #         break
#
# # pop löscht immer das letzte Element der Liste
# li = ['a','n','e']
# li.pop()
# li.pop(2) #löschen nur über den Index der Liste
# print(li)
#
# # löscht das Element aus der Liste über Element
# li = ['a','n','e','n']
# li.remove('n') # nur das erste Element wird gelöscht
#
# zahl_list = [1,5,67,8,3,11]
# zahl_list.sort() # orden von klein bis groß
# zahl_list.reverse()

odd_list = []
[odd_list.append(i) for i in range(1,11) if i % 2 != 0]
print(odd_list)

li = [1,2,3,[4,5,6]]
print(li[3][1])