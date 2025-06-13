from database.db import get_connection

def hitung_keuntungan():
    conn = get_connection()
    c = conn.cursor()
    c.execute("""
        SELECT t.jumlah, b.modal, b.harga_jual
        FROM transaksi t JOIN barang b ON t.id_barang = b.id
    """)
    data = c.fetchall()
    conn.close()
    return sum((jual - modal) * jumlah for jumlah, modal, jual in data)

def nilai_sisa_stok():
    conn = get_connection()
    c = conn.cursor()
    c.execute("SELECT stok, modal FROM barang")
    data = c.fetchall()
    conn.close()
    return sum(stok * modal for stok, modal in data)

def jumlah_transaksi_per_anggota():
    conn = get_connection()
    c = conn.cursor()
    c.execute("""
        SELECT a.nama, COUNT(t.id) as total
        FROM transaksi t JOIN anggota a ON t.id_anggota = a.id
        GROUP BY a.id
    """)
    hasil = c.fetchall()
    conn.close()
    return hasil
