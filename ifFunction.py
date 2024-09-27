# 27.09.2024
#if Funktion

print(not 3>9)

# fruit = input('Geben Sie bitte Pfirsich auf Englisch ein:')
# if fruit == 'peach':
#     print('peach')
# else:
#     print('nein')

a = 8
b = 5
# richtiges Ergebnis                        #falsches Ergebnis
print('a ist größer als b') if (a>b) else print('b ist größer als a')

erg = 0
if 11 < erg < 50:
    print('mangelhaft')
elif 50 <= erg < 80:
    print('befriedigend')
elif erg < 11:
    print('unmangelhaft')
else:
    print('sehr gut')


#In Corona-Zeiten -> Körpertemperatur messen
ticket = True # True gültiges Ticket #False ungültiges Ticket
temp = 36.5

if ticket == True:
    print('Yeah, i am in.-->', end = '')
    if 36.2 < temp < 37.2  :
        print('Keinen Feber')
    else:
        print('Isolieren')
else:
    print('Leider darfst du nicht mit fahren.')
