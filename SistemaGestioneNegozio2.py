'''TRACCIA: Gestione dell'Inventario:
Gli articoli in magazzino sono elencati con il nome, il prezzo e la quantità.
È possibile aggiungere nuovi articoli all'inventario.
Gli articoli possono essere rimossi o aggiornati (ad es., cambiare prezzo o quantità).'''

#è una soluzione molto poco elegante e limitata, ma almeno funziona
'''Xcreo una lista con all'interno dei dizionari, ogni dizionario corrisponde a un articolo:X'''
'''inventario =[({"nome":"matita",
            "prezzo": 2,
            "quantità" : 3}),
            ({"nome": "penna",
            "prezzo": 2,
            "quantità": 10}),
            ({"nome":"foglio",
            "prezzo": 3,
            "quantità": 4}),
            ({"nome": "agenda",
            "prezzo":2,
            "quantità": 5})]'''
menù = input("salve, si vuole 1. visualizzare 2. aggiungere articolo 3. modificare informazioni articoli? ")
#creare una lista
inventario = [("matita, 2, 3"),
            ("penna, 2, 10"),
            ("foglio, 3, 4"),
            ("agenda, 2,5")]

if menù == "1":
    print("Gli articoli verrano stampati con il seguente ordine: nome articolo, prezzo, quantità")
    print(inventario)
elif menù== "2":
    aggiunta =  input("che articoli si vogliono inserire? Definire: nome articolo, prezzo, quantità"),
    #da specificare nome articolo, prezzo e quantità
    inventario.append(aggiunta)
    print(inventario)
elif menù == "3":
    print(inventario)
    modificaposizione = int(input("che posizione si desidera cambiare?")) #è necessario che sia un intero, essendo una posizione
    modificavalore = input("che valore si desidera cambiare?")
    inventario[modificaposizione] = modificavalore
    print(inventario)
else:
    print("uscita da inventario")




