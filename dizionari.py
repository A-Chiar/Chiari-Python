formaggi = {"nome" : "Parmigiano",
            "stagionatura":"20 mesi"}

print(formaggi["nome"])


studente = {"nome" : "Alice",
            "età": 20,
            "sesso": "Femmina"
            }

print(studente["nome"])
studente["città"] = "Roma"
print(studente)

print(studente.keys())
print(studente.values())

print(studente.get("nome"))
print(studente.items())

print(studente.get("cane"))
