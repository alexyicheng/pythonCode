#27.09.2024
#Schleifen

#while Schleife
# i = 1
# while i < 4:
#     print('allow to make misstake')
#     i += 1

#endlose Schleife
# while True: #Bedingung = True
#     print('immer 18 Jahre Alt')
# while False:
#     print('Programm startet nie')


# i = 1
# s = 0 # summe
# while i < 101:
#     s += i # s = s + i
#     i += 1 # i = i + 1
# print('Die Summe von 1 bis 100 ist', s)


# b = 1
# while b < 3:
#     print(f'Das ist die {b}.Schleife')
#     j = 1
#     while j < 2:
#         print(f'inner Schleif{j}.Schleife')
#         j += 1
#     b += 1

#for Schleife
# zitiao = 'HelloPython'
# #print(type(zitiao))
# for c in zitiao: #gilt für nur String - um einzelne Element zu nehmen
#     print(c)

# s = 0
# for i in range(1,101):
#     s += i
#     i += 1
# print('Die Summe von 1 bis 100 ist', s)

i = 1
while 1 < 5:
    print(f'ich habe {i}.Pfirsich gegessen')
    if i == 3:
        print('satt')
        break
    i += 1

i = 1
while i < 5:
    print(f'ich habe {i}.Banana gegessen')
    if i == 3:
        print(f'Eh, voll eklig, schon schlecht geworden, als ich {i}. Banana off gemacht habe')
        i += 1 # continue - unbedingt variable ändern, ansondern wird es zu eine Endlose - Schleife
        continue
    i += 1
