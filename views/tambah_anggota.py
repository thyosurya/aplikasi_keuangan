import tkinter as tk
from tkinter import messagebox
from database.db import get_connection

def tambah_anggota():
    def simpan():
        nama = ent_nama.get()
        if not nama.strip():
            messagebox.showerror("Error", "Nama tidak boleh kosong")
            return

        conn = get_connection()
        c = conn.cursor()
        c.execute("INSERT INTO anggota (nama) VALUES (?)", (nama,))
        conn.commit()
        conn.close()
        win.destroy()
        messagebox.showinfo("Sukses", "Anggota berhasil ditambahkan")

    win = tk.Toplevel()
    win.title("Tambah Anggota")
    tk.Label(win, text="Nama").grid(row=0, column=0)
    ent_nama = tk.Entry(win)
    ent_nama.grid(row=0, column=1)
    tk.Button(win, text="Simpan", command=simpan).grid(row=1, columnspan=2)
