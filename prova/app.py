import sqlite3
from flask import Flask, render_template, abort

app = Flask(__name__)
DB_PATH = "database.db"


def get_db():
    """Apre e restituisce una connessione al database."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row   # risultati accessibili come dizionari
    return conn


# ─────────────────────────────────────────────
# Route 1 – Home page
# ─────────────────────────────────────────────
@app.route("/")
def index():
    conn = get_db()
    # Primi 3 corsi per la preview in homepage
    corsi = conn.execute(
        "SELECT * FROM corsi ORDER BY id LIMIT 3"
    ).fetchall()
    conn.close()
    return render_template("index.html", corsi=corsi)


# ─────────────────────────────────────────────
# Route 2 – Catalogo corsi
# ─────────────────────────────────────────────
@app.route("/corsi")
def corsi():
    conn = get_db()
    tutti_i_corsi = conn.execute("SELECT * FROM corsi ORDER BY id").fetchall()
    conn.close()
    return render_template("corsi.html", corsi=tutti_i_corsi)


# ─────────────────────────────────────────────
# Route 3 – Dettaglio singolo corso
# ─────────────────────────────────────────────
@app.route("/corsi/<int:id>")
def dettaglio(id):
    conn = get_db()

    corso = conn.execute(
        "SELECT * FROM corsi WHERE id = ?", (id,)
    ).fetchone()

    if corso is None:
        conn.close()
        abort(404)

    sessioni = conn.execute(
        "SELECT * FROM sessioni WHERE corso_id = ? ORDER BY data_inizio",
        (id,)
    ).fetchall()

    moduli = conn.execute(
        "SELECT * FROM moduli WHERE corso_id = ? ORDER BY ordine",
        (id,)
    ).fetchall()

    obiettivi = conn.execute(
        "SELECT descrizione FROM obiettivi WHERE corso_id = ? ORDER BY id",
        (id,)
    ).fetchall()

    # Corsi correlati (stessa categoria, escluso il corrente)
    correlati = conn.execute(
        "SELECT * FROM corsi WHERE categoria = ? AND id != ? LIMIT 3",
        (corso["categoria"], id)
    ).fetchall()

    conn.close()

    return render_template(
        "dettaglio.html",
        corso=corso,
        sessioni=sessioni,
        moduli=moduli,
        obiettivi=obiettivi,
        correlati=correlati,
    )


# ─────────────────────────────────────────────
# Pagina 404 personalizzata
# ─────────────────────────────────────────────
@app.errorhandler(404)
def not_found(e):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True)
