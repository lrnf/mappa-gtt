# Mappa Trasporti Torino

Una mappa web interattiva, leggera e ottimizzata per dispositivi mobili e desktop, pensata per esplorare la rete di trasporto pubblico di Torino. Sviluppata con Leaflet.js e basata su dati geospaziali GeoJSON.

## Caratteristiche Principali

- **Basemap Minimalista:** Sfondo pulito in scala di grigi per dare risalto ai percorsi dei mezzi.
- **Colori Ufficiali per Categoria:**
  - Metropolitana (`#E53935`)
  - Tram (`#2E7D32`)
  - Funicolare Sassi-Superga (`#6D4C41`)
  - Bus Suburbani (`#1565C0`)
  - Bus Urbani Standard (`#03A9F4`)
- **Gestione Dinamica dello Zoom:** Le fermate compaiono automaticamente superato il livello di zoom 14 per mantenere la mappa fluida.
- **Barra di Ricerca Intelligente:** Consente di cercare rapidamente inserendo il nome della fermata, il codice numerico della palina, il numero della linea o il capolinea.
- **Filtro Linee e Reset:** Cliccando su una linea si evidenzia il percorso e si filtrano le fermate pertinenti. È presente un pulsante di reset rapido per ripristinare la vista globale.
- **Integrazione Dati Live GTT:** Popup minimali e pannello inferiore contestuale (*bottom sheet*) per accedere direttamente ai transiti in tempo reale ufficiali GTT tramite il codice palina.

## Struttura del Progetto

```text
├── index.html        # Applicazione principale (HTML, CSS e logica Leaflet)
├── linee.geojson     # Tracciati geospaziali delle linee di trasporto
└── fermate.geojson   # Posizioni e metadati delle paline
