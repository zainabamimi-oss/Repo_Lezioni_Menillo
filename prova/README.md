# Prova – Piattaforma Formativa

Sito web Flask per la gestione e visualizzazione di corsi aziendali.

---

## Struttura del progetto

```
prova/
├── app.py              ← applicazione Flask (le 3 route)
├── init_db.py          ← crea e popola il database SQLite
├── database.db         ← generato da init_db.py
├── requirements.txt
├── templates/
│   ├── base.html       ← layout comune (navbar, footer)
│   ├── index.html      ← home page  →  route GET /
│   ├── corsi.html      ← catalogo   →  route GET /corsi
│   ├── dettaglio.html  ← dettaglio  →  route GET /corsi/<id>
│   └── 404.html        ← errore
└── static/
    ├── css/style.css
    └── js/main.js
```

---

## Avvio rapido

```bash
# 1. Installa le dipendenze
pip install -r requirements.txt

# 2. Crea il database (solo la prima volta)
python init_db.py

# 3. Avvia il server di sviluppo
python app.py
```

Il sito sarà disponibile su → http://127.0.0.1:5000

---

## Route implementate

| URL           | Metodo | Funzione     | Descrizione                                       |
|---------------|--------|--------------|---------------------------------------------------|
| `/`           | GET    | `index()`    | Home page con i primi 3 corsi in anteprima        |
| `/corsi`      | GET    | `corsi()`    | Catalogo completo con tutti i corsi dal DB        |
| `/corsi/<id>` | GET    | `dettaglio()`| Dettaglio corso: descrizione, moduli e sessioni   |

Ogni route:
1. Apre la connessione al database con `get_db()`
2. Esegue la query necessaria
3. Passa i dati al template Jinja2 con `render_template()`
4. Chiude la connessione

---

## 🔤 Come cambiare il nome del sito

Il nome **"Prova"** appare in **4 punti**. Cerca e sostituisci la stringa `Prova` in:

| File                    | Posizione                            |
|-------------------------|--------------------------------------|
| `templates/base.html`   | Logo nella navbar (riga ~18)         |
| `templates/base.html`   | Logo nel footer (riga ~45)           |
| `templates/base.html`   | Copyright nel footer (riga ~58)      |
| `templates/base.html`   | Tag `<title>` dei vari `{% block %}` |

In pratica basta aprire **`templates/base.html`** e fare un semplice
**Trova & Sostituisci** di `Prova` con il nome definitivo.  
I `{% block title %}` nei singoli template ereditano da base.html, quindi
si aggiornano automaticamente.

---

## Database – Tabelle principali

| Tabella    | Colonne principali                                             |
|------------|----------------------------------------------------------------|
| `corsi`    | id, nome, categoria, livello, durata, immagine, descrizione    |
| `sessioni` | id, corso_id, data_inizio, data_fine, orario, luogo, max_posti, posti_liberi |
| `moduli`   | id, corso_id, ordine, titolo, ore, descrizione                 |
| `obiettivi`| id, corso_id, descrizione                                      |
