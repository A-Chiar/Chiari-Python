#chiedo input
num1 = int(input("inserisci un numero "))
num2 = int(input("inserisci un altro numero "))

#creo menù
addizione = print("1. addizione")
sottrazione = print("2. sottrazione")
moltiplicazione = print("3. moltiplicazione")
divisione = print("4. divisione")
menù = int(input("scegli un'operazione "))

#creo operazioni con if
if menù == 1:
    print(num1 + num2)
elif menù == 2:
    print(num1 -num2)
elif menù == 3:
    print(num1 * num2)
elif menù == 4:
    if num1 == 0 or num2 == 0:
        print("Errore: Divisione per zero")
    elif num1 != 0 and num2 != 0:
        print(num1/num2)
 

    