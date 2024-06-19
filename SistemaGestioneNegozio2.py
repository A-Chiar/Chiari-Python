'''TRACCIA: Gestione dell'Inventario:
Gli articoli in magazzino sono elencati con il nome, il prezzo e la quantità.
È possibile aggiungere nuovi articoli all'inventario.
Gli articoli possono essere rimossi o aggiornati (ad es., cambiare prezzo o quantità).'''
menù = input("salve, si vuole 1. visualizzare 2. aggiungere articolo 3. modificare informazioni articoli? ")
#creo una lista con all'interno dei dizionari, ogni dizionario corrisponde a un articolo:
inventario =[({"nome":"matita",
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
            "quantità": 5})]

if menù == "1":
    print(inventario)
    #almeno questo funziona
elif menù== "2":
    aggiunta =  input("che articoli si vogliono inserire? "),
    #da specificare nome articolo, prezzo e quantità
    inventario.append({aggiunta})
    print(inventario)
    #l'ultimo valore non viene aggiunto come chiave-valore, ma solo come una serie di valori
elif menù == "3":
    #non funziona
    print(inventario)
    modificaposizione = input("che posizione si desidera cambiare?")
    modificavalore = input("che valore si desidera cambiare?")
    inventario[modificaposizione] = {modificavalore}
else:
    print("uscita da inventario")




