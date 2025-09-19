import sys

numeratore = int(sys.argv[1]) 
denominatore = int(sys.argv[2]) 

try:
    risultato = numeratore / denominatore
except ZeroDivisionError:
    print("Errore: Divisione per zero non permessa.")
else:
    print(f"Risultato: {risultato}")
finally:
    print("Esecuzione del blocco finally completata.")
