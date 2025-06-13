
# 🧾 Aplikasi Keuangan Sederhana

Aplikasi desktop berbasis Python dengan antarmuka grafis (GUI) menggunakan Tkinter dan database SQLite. Aplikasi ini dirancang untuk membantu mencatat transaksi, mengelola data barang dan anggota, serta menampilkan laporan keuangan.

---

## 📌 Fitur Utama

- 📦 Tambah & kelola data barang
- 👥 Tambah & kelola data anggota
- 💰 Input transaksi penjualan
- 📊 Laporan keuangan:
  - Menghitung total keuntungan
  - Menampilkan jumlah transaksi per anggota
  - Menghitung nilai sisa stok barang

---

## 📁 Struktur Folder

```
aplikasi_keuangan/
├── main.py                  # File utama untuk menjalankan aplikasi
├── database/
│   └── db.py               # Inisialisasi dan koneksi database SQLite
├── models/                 # (Kosong, disiapkan untuk model lanjutan)
├── views/
│   ├── tambah_barang.py    # Form input barang
│   ├── tambah_anggota.py   # Form input anggota
│   ├── input_transaksi.py  # Form input transaksi
│   └── laporan.py          # Menampilkan laporan
├── utils/
│   └── kalkulasi.py        # Fungsi perhitungan (keuntungan, sisa stok, dll)
└── README.md               # Dokumentasi ini
```

---

## ▶️ Cara Menjalankan

1. **Pastikan Python sudah terinstall**
   ```bash
   python --version
   ```

2. **Masuk ke folder proyek**
   ```bash
   cd aplikasi_keuangan
   ```

3. **Jalankan aplikasi**
   ```bash
   python main.py
   ```

Tidak perlu menginstall library tambahan karena hanya menggunakan modul bawaan: `tkinter` dan `sqlite3`.

---

## 💡 Catatan

- Pastikan struktur folder sesuai.
- Jika menggunakan Linux dan `tkinter` belum tersedia, install dengan:
  ```bash
  sudo apt install python3-tk
  ```

---

## 📃 Lisensi

Proyek ini bersifat open-source dan bebas digunakan untuk keperluan belajar, pengembangan pribadi, atau tugas kuliah.

---

## ✍️ Dibuat oleh

> Moh. Radithyo Surya Martuah  
> Prodi Sistem Informasi  
> 2025
