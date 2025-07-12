from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

def get_livros():
    conn = sqlite3.connect('livros.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS livros (id INTEGER PRIMARY KEY, titulo TEXT)')
    cursor.execute('INSERT OR IGNORE INTO livros (id, titulo) VALUES (1, "Noites Brancas"), (2, "Dom Casmurro")')
    conn.commit()
    livros = cursor.execute('SELECT * FROM livros').fetchall()
    conn.close()
    return [{'id': row[0], 'titulo': row[1]} for row in livros]

@app.route('/livros')
def listar_livros():
    return jsonify(get_livros())

if __name__ == '__main__':
    app.run(debug=True)
