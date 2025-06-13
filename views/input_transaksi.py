import tkinter as tk
from tkinter import ttk, messagebox
from database.db import get_connection
from datetime import datetime

def input_transaksi():
    def simpan():
        try:
            id_barang = int(combo_barang.get().split(' - ')[0])
            id_anggota = int(combo_anggota.get().split(' - ')[0])
            jumlah = int(ent_jumlah.get())
        except Exception as e:
            messagebox.showerror("Error", f"Input tidak valid: {e}")
            return

        conn = get_connection()
        c = conn.cursor()
        tanggal = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        c.execute("INSERT INTO transaksi (id_barang, id_anggota, jumlah, tanggal) VALUES (?, ?, ?, ?)",
                  (id_barang, id_anggota, jumlah, tanggal))
        c.execute("UPDATE barang SET stok = stok - ? WHERE id = ?", (jumlah, id_barang))
        conn.commit()
        conn.close()
        win.destroy()
        messagebox.showinfo("Sukses", "Transaksi berhasil dicatat")

    win = tk.Toplevel()
    win.title("Input Transaksi")

    tk.Label(win, text="Barang").grid(row=0, column=0)
    tk.Label(win, text="Anggota").grid(row=1, column=0)
    tk.Label(win, text="Jumlah").grid(row=2, column=0)

    conn = get_connection()
    c = conn.cursor()

    c.execute("SELECT id, nama FROM barang")
    barang_list = [f"{id} - {nama}" for id, nama in c.fetchall()]
    combo_barang = ttk.Combobox(win, values=barang_list, state="readonly")
    combo_barang.grid(row=0, column=1)

    c.execute("SELECT id, nama FROM anggota")
    anggota_list = [f"{id} - {nama}" for id, nama in c.fetchall()]
    combo_anggota = ttk.Combobox(win, values=anggota_list, state="readonly")
    combo_anggota.grid(row=1, column=1)

    conn.close()

    ent_jumlah = tk.Entry(win)
    ent_jumlah.grid(row=2, column=1)

    tk.Button(win, text="Simpan", command=simpan).grid(row=3, columnspan=2)
