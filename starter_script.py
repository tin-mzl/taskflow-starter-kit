#!/usr/bin/env python3
# starter_script.py
# Crée une petite base SQLite et exporte un CSV d'exemple.
import sqlite3, csv, os

DB = 'starter_tasks.db'
CSV = 'tasks.csv'

def create_db():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      title TEXT NOT NULL,
      priority INTEGER DEFAULT 1,
      date_limite TEXT,
      done INTEGER DEFAULT 0
    )''')
    sample = [
        ('Corriger l\'erreur de build', 3, '2025-11-01', 0),
        ('Ajouter la validation date_limite', 2, '2025-11-05', 0),
        ('Écrire README de release', 1, '2025-11-10', 0),
        ('Nettoyer la DB de test', 1, '', 0),
        ('Préparer la page de vente', 2, '', 0)
    ]
    cur.executemany('INSERT INTO tasks (title, priority, date_limite, done) VALUES (?,?,?,?)', sample)
    conn.commit()
    conn.close()

def export_csv():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    rows = cur.execute('SELECT id,title,priority,date_limite,done FROM tasks').fetchall()
    with open(CSV, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['id','title','priority','date_limite','done'])
        writer.writerows(rows)
    conn.close()

if __name__ == '__main__':
    if os.path.exists(DB):
        os.remove(DB)
    create_db()
    export_csv()
    print('Fichiers créés :', DB, 'et', CSV)
    print('Lance : python starter_script.py')
