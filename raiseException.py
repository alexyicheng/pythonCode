#02.10.2024

# raise - stop programm

#länger des Passworts prüfen
#password muss länger als 6 zeichen sein, ansonsten gibt eine Fehlermeldung zurück
def login():
    pwd = input('Bitte geben sie Ihr Passwort ein')
    if len(pwd) > 5:
        return 'erfolgreich'
    raise Exception('Passwort muss mindestens 6 Zeichen besitzen')
#print(login())


# try - fails das Programm ein Fehler auftaucht, wird der Fehler aufgefangen, damit das Programm weiter ausgeführt werden kann
try:
    print(login())
except Exception as e:
    print(e)

