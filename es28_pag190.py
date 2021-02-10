cap_città={}

while True:
    città=input("Scrivi il nome della città (Scrivere STOP per fermare il programma): ")
    if città=="STOP":
        break
    else:
        cap=input("Scrivi il CAP della città scelta: ")
        cap_città[città]=cap

domanda=input("Di che città vuoi sapere il CAP? ")
if domanda in cap_città:
    print("Il CAP di", domanda, "è", cap_città[domanda])
else:
    print("La città che hai scelto non è presente nell'elenco")