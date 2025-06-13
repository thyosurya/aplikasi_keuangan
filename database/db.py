import sqlite3

def get_connection():
    return sqlite3.connect("keuangan.db")

def init_db():
    conn = get_connection()
    c = conn.cursor()

    c.execute("""CREATE TABLE IF NOT EXISTS barang (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nama TEXT,
        stok INTEGER,
        modal REAL,
        harga_jual REAL
    )""")

    c.execute("""CREATE TABLE IF NOT EXISTS anggota (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nama TEXT
    )""")

    c.execute("""CREATE TABLE IF NOT EXISTS transaksi (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        id_barang INTEGER,
        id_anggota INTEGER,
        jumlah INTEGER,
        tanggal TEXT,
        FOREIGN KEY(id_barang) REFERENCES barang(id),
        FOREIGN KEY(id_anggota) REFERENCES anggota(id)
    )""")

    conn.commit()
    conn.close()
