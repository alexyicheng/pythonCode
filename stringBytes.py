#27.09.2024
#decode encode

a = 'Python'
print(a,type(a))
a1 = a.encode() # verschlüsseln
print(a1,type(a1))
a2 = a1.decode() # entschlüsseln
print(a2,type(a2))

st = 'Kobe MJ'
st1 = st.encode('utf-8') # verschlüsseln in utf-8 format
print(st1,type(st1))
st2 = st1.decode('utf-8') # entschlüsseln in utf-8 format
print(st2,type(st2))

Vorname = 'Derrick'
Nachname = 'Rose'
print(Vorname,Nachname,sep=' ')

print('Lalala Land \n'*5)

print('d' in Vorname)
print('D' not in Nachname)
print('Ro' in Nachname)

name = 'Name'
for i in range(0,len(name)):
    print(f'{i}.Buchstaben ist',name[i])


stringlist = 'abcdefghijk'
#[start:end:step]
print(stringlist[0:4]) # abed
print(stringlist[4:7]) # efg
print(stringlist[3:]) # defghijk
print(stringlist[:6]) #   abcdef





