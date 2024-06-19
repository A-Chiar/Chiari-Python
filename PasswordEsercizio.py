#input utente
UtenteInput= input("Inserire il nome utente ")
PassInput= input("Inserire password ")
CambioPass = input("Si desidera cambiare password? Rispondere True o False")
CambioUtente =  input("Si desidera cambiare nome utente? Rispondere True o False")

#prove con dizionario errate
#ChiavePassword = {"admin":'12345'}
#print(ChiavePassword.keys())

Utente = "admin"
Pass = "12345"
if UtenteInput == Utente:
    pass
if PassInput == Pass:
    print("Pass corretta")
    print("Benvenuto " + UtenteInput)
else:
    print("Credenziali non corrette")


#prove con dizionario errate
'''if UtenteInput == ChiavePassword["admin"]:
    print("Nome Utente corretto")
elif PassInput == ChiavePassword.values():
    print("Pass corretta")
    print("Benvenuto " + UtenteInput)
#elif CambioDati == True:
else:
    print("Credenziali non corrette")'''



