nomi={
    "Luca": "3464578436",
    "Giovanni": "2863593125",
    "Alberto": "1069356765",
    "Matteo": "1059993255",
    "Francesco": "2957145534",
    "Lorenzo": "9003444457",
}

domanda=input("Scrivi il nome della persona di cui si vuole sapere il numero di telefono: ")
if domanda in nomi:
    print("Il numero di telefono di", domanda, "è:", nomi[domanda])
else:
    print("Questo nome non è presente nella rubrica.")