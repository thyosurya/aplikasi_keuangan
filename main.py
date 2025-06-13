import tkinter as tk
from database.db import init_db
from views.tambah_barang import tambah_barang

# Tambahkan import lainnya setelah selesai

from views.tambah_anggota import tambah_anggota
from views.input_transaksi import input_transaksi
from views.laporan import tampilkan_laporan

root = tk.Tk()
root.title("Aplikasi Keuangan Modular")
root.geometry("400x300")

tk.Label(root, text="Menu Utama", font=("Helvetica", 16)).pack(pady=10)
tk.Button(root, text="Tambah Barang", command=tambah_barang, width=25).pack(pady=5)
tk.Button(root, text="Tambah Anggota", command=tambah_anggota, width=25).pack(pady=5)
tk.Button(root, text="Input Transaksi", command=input_transaksi, width=25).pack(pady=5)
tk.Button(root, text="Lihat Laporan", command=tampilkan_laporan, width=25).pack(pady=5)

init_db()
root.mainloop()



