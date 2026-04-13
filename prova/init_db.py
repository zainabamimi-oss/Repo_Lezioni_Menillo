"""
init_db.py – Crea e popola il database SQLite con i dati di esempio.
Esegui una sola volta: python init_db.py
"""

import sqlite3

DB_PATH = "database.db"

# ── Schema ─────────────────────────────────────────────────────────────────
SCHEMA = """
CREATE TABLE IF NOT EXISTS corsi (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    nome            TEXT NOT NULL,
    categoria       TEXT NOT NULL,          -- Informatica / Design / Lingue
    livello         TEXT NOT NULL,          -- Base / Intermedio / Avanzato
    durata          INTEGER NOT NULL,       -- ore totali
    immagine        TEXT,                   -- URL immagine
    descrizione     TEXT,
    descrizione_breve TEXT
);

CREATE TABLE IF NOT EXISTS obiettivi (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    corso_id    INTEGER NOT NULL REFERENCES corsi(id),
    descrizione TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS moduli (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    corso_id    INTEGER NOT NULL REFERENCES corsi(id),
    ordine      INTEGER NOT NULL,
    titolo      TEXT NOT NULL,
    ore         INTEGER NOT NULL,
    descrizione TEXT
);

CREATE TABLE IF NOT EXISTS sessioni (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    corso_id    INTEGER NOT NULL REFERENCES corsi(id),
    data_inizio TEXT NOT NULL,   -- formato YYYY-MM-DD
    data_fine   TEXT NOT NULL,
    orario      TEXT,            -- es. "09:00 – 13:00"
    luogo       TEXT,
    max_posti   INTEGER NOT NULL,
    posti_liberi INTEGER NOT NULL
);
"""

# ── Dati ───────────────────────────────────────────────────────────────────
CORSI = [
    (1, "Programmazione", "Informatica", "Intermedio", 120,
     "https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=800&q=80",
     "Corso completo di programmazione software che copre i fondamenti dell'ingegneria del codice, algoritmi avanzati e best practices per lo sviluppo di applicazioni enterprise moderne e scalabili con Python e JavaScript.",
     "Fondamenti di programmazione con Python e JavaScript. Algoritmi, strutture dati e sviluppo di applicazioni web moderne."),

    (2, "Grafica", "Design", "Base", 80,
     "https://images.unsplash.com/photo-1561070791-2526d30994b5?w=800&q=80",
     "Introduzione completa al design grafico digitale: teoria del colore, tipografia, composizione visiva e utilizzo professionale degli strumenti Adobe Creative Suite.",
     "Teoria del colore, tipografia e composizione visiva. Adobe Photoshop, Illustrator e Figma per progetti professionali."),

    (3, "Design Industriale", "Design", "Avanzato", 200,
     "https://images.unsplash.com/photo-1581091226033-d5c48150dbaa?w=800&q=80",
     "Formazione specialistica nel design industriale e product design: modellazione 3D parametrica con SolidWorks, prototipazione rapida con stampa 3D, analisi dei materiali e processi di manufacturing.",
     "Modellazione 3D, prototipazione rapida e design thinking per la progettazione di prodotti industriali innovativi."),

    (4, "Sistemista Reti", "Informatica", "Avanzato", 160,
     "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=800&q=80",
     "Corso tecnico avanzato per sistemisti di rete: architetture TCP/IP, configurazione Cisco CLI, sicurezza informatica, VPN, firewall e gestione di infrastrutture IT enterprise. Preparazione all'esame Cisco CCNA 200-301.",
     "Architetture di rete, Cisco CLI, sicurezza, VPN e gestione infrastrutture IT. Preparazione certificazione CCNA."),

    (5, "Inglese", "Lingue", "Intermedio", 100,
     "https://images.unsplash.com/photo-1546410531-bb4caa6b424d?w=800&q=80",
     "Corso di inglese business-oriented per lo sviluppo di competenze comunicative avanzate in contesti professionali internazionali: email formali, presentazioni, negoziazioni e corrispondenza commerciale.",
     "Business English certificato B2/C1. Presentazioni, negoziazioni e comunicazione professionale con docenti madrelingua."),
]

OBIETTIVI = [
    # Corso 1 – Programmazione
    (1, "Padroneggiare Python 3 e JavaScript ES6+"),
    (1, "Progettare algoritmi efficienti e strutture dati"),
    (1, "Sviluppare REST API con Flask e MySQL"),
    (1, "Creare interfacce web dinamiche con DOM manipulation"),
    (1, "Applicare principi OOP e design pattern"),
    (1, "Usare Git per il versionamento del codice"),
    # Corso 2 – Grafica
    (2, "Applicare teoria del colore, composizione e tipografia"),
    (2, "Usare Photoshop per ritocco e compositing"),
    (2, "Creare grafica vettoriale con Illustrator"),
    (2, "Progettare interfacce con Figma"),
    (2, "Sviluppare un'identità di marca completa"),
    (2, "Esportare file per stampa e digitale"),
    # Corso 3 – Design Industriale
    (3, "Leggere e produrre disegni tecnici ISO"),
    (3, "Modellare solidi e superfici in SolidWorks"),
    (3, "Applicare metodologia design thinking"),
    (3, "Stampare prototipi FDM e SLA"),
    (3, "Analizzare fattibilità produttiva e materiali"),
    (3, "Presentare con render e tavole professionali"),
    # Corso 4 – Sistemista Reti
    (4, "Padroneggiare il modello OSI e TCP/IP"),
    (4, "Configurare router e switch Cisco via CLI"),
    (4, "Implementare VLAN, OSPF e BGP"),
    (4, "Gestire server Linux: DNS, DHCP, Apache"),
    (4, "Configurare VPN IPsec e OpenVPN"),
    (4, "Monitorare la rete con Wireshark e Nagios"),
    # Corso 5 – Inglese
    (5, "Comunicare con sicurezza in inglese professionale"),
    (5, "Scrivere email, report e presentazioni formali"),
    (5, "Condurre meeting e videoconferenze internazionali"),
    (5, "Negoziare accordi commerciali in inglese"),
    (5, "Superare l'esame Cambridge B2 o C1"),
    (5, "Ampliare il vocabolario tecnico di settore"),
]

MODULI = [
    # Corso 1
    (1, 1, "Fondamenti Python", 24, "Variabili, tipi, funzioni, liste, dizionari e controllo del flusso."),
    (1, 2, "Algoritmi e strutture dati", 20, "Array, stack, queue, grafi. Complessità computazionale O(n)."),
    (1, 3, "OOP e Design Pattern", 20, "Classi, ereditarietà, polimorfismo, pattern MVC."),
    (1, 4, "Web con Flask + MySQL", 36, "Routing, Jinja2, connessione DB, query, sessioni e autenticazione."),
    (1, 5, "JavaScript e DOM", 20, "ES6+, fetch API, manipolazione DOM, eventi e AJAX."),
    # Corso 2
    (2, 1, "Fondamenti visivi", 12, "Teoria del colore, tipografia, composizione e principi gestalt."),
    (2, 2, "Adobe Photoshop", 20, "Livelli, maschere, retouching, compositing e workflow non-distruttivo."),
    (2, 3, "Adobe Illustrator", 20, "Curve di Bezier, pathfinder, pattern, loghi e icone scalabili."),
    (2, 4, "UI/UX con Figma", 20, "Wireframe, design system, componenti e prototipazione interattiva."),
    (2, 5, "Progetto finale", 8, "Brand identity completa: logo, palette, tipografia e brand manual."),
    # Corso 3
    (3, 1, "Disegno tecnico", 24, "Proiezioni, sezioni, quotatura ISO e tolleranze."),
    (3, 2, "SolidWorks Base", 40, "Sketch vincolato, feature solide, assembly e distinta base."),
    (3, 3, "SolidWorks Avanzato", 60, "Superfici, sheet metal, simulazione FEA base."),
    (3, 4, "Prototipazione rapida", 40, "Stampa 3D FDM/SLA, post-processing e test funzionali."),
    (3, 5, "Progetto finale", 36, "Sviluppo autonomo con supervisione e presentazione a giuria."),
    # Corso 4
    (4, 1, "Fondamenti TCP/IP", 28, "OSI, indirizzamento IPv4/IPv6, subnetting CIDR e routing statico."),
    (4, 2, "Switching e VLAN", 32, "Cisco CLI, VLAN, trunking 802.1Q, STP/RSTP e sicurezza layer 2."),
    (4, 3, "Routing avanzato", 36, "OSPF, BGP, ridondanza HSRP/VRRP. Simulazione reti enterprise."),
    (4, 4, "Linux Server", 32, "Ubuntu Server, DNS, DHCP, Apache, SSH hardening e gestione utenti."),
    (4, 5, "Sicurezza e VPN", 32, "Firewall iptables, fail2ban, OpenVPN, IPsec e analisi con Wireshark."),
    # Corso 5
    (5, 1, "Business Vocabulary", 20, "Lessico professionale per finance, marketing e management."),
    (5, 2, "Written Communication", 24, "Email formali, report aziendali e proposte commerciali."),
    (5, 3, "Oral Communication", 28, "Presentazioni pubbliche, meeting management e video call."),
    (5, 4, "Negotiation & Diplomacy", 16, "Linguaggio negoziale, gestione conflitti e role-play."),
    (5, 5, "Cambridge Exam Prep", 12, "Simulazioni complete delle prove B2/C1 ufficiali."),
]

SESSIONI = [
    # Corso 1
    (1, "2025-04-15", "2025-06-15", "09:00 – 13:00", "Sede Milano – Aula A", 20, 12),
    (1, "2025-09-01", "2025-11-01", "14:00 – 18:00", "Online – Zoom", 25, 8),
    (1, "2025-10-10", "2025-12-10", "09:00 – 17:00", "Sede Roma – Lab 3", 15, 0),
    # Corso 2
    (2, "2025-05-01", "2025-06-20", "14:00 – 18:00", "Sede Milano – Lab Design", 18, 5),
    (2, "2025-09-15", "2025-11-05", "09:00 – 13:00", "Online – Teams", 20, 14),
    # Corso 3
    (3, "2025-04-20", "2025-08-20", "09:00 – 17:00", "Sede Torino – FabLab", 12, 3),
    (3, "2025-10-01", "2026-02-01", "09:00 – 17:00", "Sede Torino – FabLab", 12, 10),
    # Corso 4
    (4, "2025-05-15", "2025-09-15", "18:00 – 22:00", "Sede Milano – Lab Reti", 16, 7),
    (4, "2025-09-20", "2026-01-20", "09:00 – 13:00", "Online – Piattaforma dedicata", 20, 18),
    (4, "2025-11-01", "2026-03-01", "14:00 – 18:00", "Sede Roma – Data Center", 14, 0),
    # Corso 5
    (5, "2025-04-10", "2025-07-10", "18:30 – 20:30", "Sede Milano – Aula Lingue", 12, 4),
    (5, "2025-09-05", "2025-12-05", "18:30 – 20:30", "Online – Virtual Classroom", 15, 11),
]


def init():
    conn = sqlite3.connect(DB_PATH)
    conn.executescript(SCHEMA)

    conn.executemany(
        "INSERT OR REPLACE INTO corsi (id,nome,categoria,livello,durata,immagine,descrizione,descrizione_breve) VALUES (?,?,?,?,?,?,?,?)",
        CORSI,
    )
    conn.executemany(
        "INSERT INTO obiettivi (corso_id, descrizione) VALUES (?,?)",
        OBIETTIVI,
    )
    conn.executemany(
        "INSERT INTO moduli (corso_id, ordine, titolo, ore, descrizione) VALUES (?,?,?,?,?)",
        MODULI,
    )
    conn.executemany(
        "INSERT INTO sessioni (corso_id,data_inizio,data_fine,orario,luogo,max_posti,posti_liberi) VALUES (?,?,?,?,?,?,?)",
        SESSIONI,
    )

    conn.commit()
    conn.close()
    print("✅ Database inizializzato con successo!")


if __name__ == "__main__":
    init()
