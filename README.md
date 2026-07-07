# TV Time Memory

Progetto per trasformare un export TV Time in una visualizzazione web personale: prima si audita l'export, poi si decide quali storie raccontare con i dati.

## Struttura

```text
film-polpetta/
  data/
    raw/          # CSV originali esportati da TV Time
    processed/    # Output generati dagli script
  docs/
    DATA_AUDIT.md        # Report tecnico dell'audit dati
    DISCOVERY_SUMMARY.md # Sintesi prodotto e viste consigliate
    VIEW_IDEAS.md        # Idee di visualizzazione
  scripts/
    profile_export.py
    build_site_data.py
  site/           # Spazio per il sito quando avremo scelto cosa mostrare
```

## Come usare l'audit

1. Lascia i CSV dell'export in `data/raw/`, oppure passa allo script un altro percorso.
2. Da questa cartella esegui:

```powershell
python .\scripts\profile_export.py
```

oppure:

```powershell
python .\scripts\profile_export.py "C:\path\to\other-export"
```

3. Lo script aggiorna:

- `docs/DATA_AUDIT.md`, leggibile a colpo d'occhio.
- `data/processed/export_profile.json`, utile per costruire il sito.

## Come usare il sito

Genera il dataset pulito per il sito:

```powershell
python .\scripts\build_site_data.py
```

Scarica o aggiorna i poster locali da TVMaze:

```powershell
python .\scripts\fetch_show_posters.py
```

Rigenera icone e immagine social preview:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\generate_brand_assets.ps1
```

Avvia una preview locale:

```powershell
python -m http.server 4173 -d .\site
```

Poi apri:

```text
http://localhost:4173
```

Nota: i meta tag Open Graph/Twitter usano asset locali. Quando il sito verra pubblicato su un dominio, si potranno trasformare `og:image` e l'eventuale URL canonico in URL assoluti.

## Audit corrente

L'audit reale e' stato generato da:

```text
C:\Users\danyp\Documents\Programmazione\Github\Repo\film-polpetta\data\raw
```

Leggi prima `docs/DISCOVERY_SUMMARY.md` per la sintesi prodotto, poi `docs/DATA_AUDIT.md` per il dettaglio tecnico.

## Cosa cerchiamo nei dati

L'audit serve a rispondere a domande pratiche:

- Quali entita esistono davvero nell'export: serie, episodi, film, watchlist, commenti, rating, amici, stati?
- Quali colonne sono affidabili e complete?
- Ci sono date abbastanza buone per creare una timeline?
- Ci sono ID condivisi per collegare file diversi?
- Quali informazioni sono personali e belle da mostrare senza sembrare una tabella amministrativa?

Il prossimo passo e' scegliere insieme 3-5 viste principali e poi costruire il sito.
