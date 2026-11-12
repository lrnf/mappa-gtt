import json
import requests

def genera_dati_live():
    # Qui andrà la logica per interrogare l'endpoint GTFS-RT o il proxy dei dati live di Torino.
    # Per adesso, impostiamo la struttura dizionario che il tuo index.html si aspetta:
    # { "codice_palina": [ { "linea": "...", "destinazione": "...", "orario": "..." }, ... ] }
    
    dati_live = {
        "1234": [
            { "linea": "3", "destinazione": "Corso Tortona", "orario": "In arrivo" },
            { "linea": "15", "destinazione": "Sassi", "orario": "4 min" }
        ],
        "5678": [
            { "linea": "68", "destinazione": "Via Frejus", "orario": "2 min" }
        ]
    }
    
    # Scrive il file live.json formattato correttamente nella root del sito
    with open('live.json', 'w', encoding='utf-8') as f:
        json.dump(dati_live, f, ensure_ascii=False, indent=2)
    
    print("File live.json aggiornato con successo!")

if __name__ == '__main__':
    genera_dati_live()