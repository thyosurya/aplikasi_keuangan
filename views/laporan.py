import tkinter as tk
from utils.kalkulasi import hitung_keuntungan, nilai_sisa_stok, jumlah_transaksi_per_anggota

def tampilkan_laporan():
    win = tk.Toplevel()
    win.title("Laporan Keuangan")

    keuntungan = hitung_keuntungan()
    stok_sisa = nilai_sisa_stok()
    data_transaksi = jumlah_transaksi_per_anggota()

    tk.Label(win, text=f"📈 Total Keuntungan: Rp {keuntungan:,.2f}", font=("Arial", 12)).pack(pady=5)
    tk.Label(win, text=f"📦 Nilai Sisa Stok: Rp {stok_sisa:,.2f}", font=("Arial", 12)).pack(pady=5)
    tk.Label(win, text="👥 Jumlah Transaksi per Anggota:", font=("Arial", 12, "bold")).pack(pady=10)

    if data_transaksi:
        for nama, total in data_transaksi:
            tk.Label(win, text=f"- {nama}: {total} transaksi").pack()
    else:
        tk.Label(win, text="Belum ada transaksi").pack()
