import tkinter as tk
from tkinter import messagebox
from database.db import get_connection

def tambah_barang():
    def simpan():
        nama = ent_nama.get()
        stok = int(ent_stok.get())
        modal = float(ent_modal.get())
        jual = float(ent_jual.get())
        conn = get_connection()
        c = conn.cursor()
        c.execute("INSERT INTO barang (nama, stok, modal, harga_jual) VALUES (?, ?, ?, ?)",
                  (nama, stok, modal, jual))
        conn.commit()
        conn.close()
        win.destroy()
        messagebox.showinfo("Sukses", "Barang berhasil ditambahkan")

    win = tk.Toplevel()
    win.title("Tambah Barang")
    tk.Label(win, text="Nama").grid(row=0, column=0)
    tk.Label(win, text="Stok").grid(row=1, column=0)
    tk.Label(win, text="Modal").grid(row=2, column=0)
    tk.Label(win, text="Harga Jual").grid(row=3, column=0)
    ent_nama = tk.Entry(win)
    ent_stok = tk.Entry(win)
    ent_modal = tk.Entry(win)
    ent_jual = tk.Entry(win)
    ent_nama.grid(row=0, column=1)
    ent_stok.grid(row=1, column=1)
    ent_modal.grid(row=2, column=1)
    ent_jual.grid(row=3, column=1)
    tk.Button(win, text="Simpan", command=simpan).grid(row=4, columnspan=2)
