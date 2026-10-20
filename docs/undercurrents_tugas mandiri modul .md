Identifikasi Undercurrents pada `pipeline_mini.py`

| Undercurrent | Bukti penerapan di kode | Kekurangan | Usulan perbaikan |
| Security | `load_dotenv()` membaca konfigurasi dari `.env`; `DB_URL` dibentuk dari variabel lingkungan. | Contoh memakai akun `de_user` yang mungkin memiliki hak terlalu luas; rahasia tetap berisiko jika `.env` masuk Git. | Gunakan akun pipeline dengan hak minimum (hanya membaca tabel sumber dan menulis tabel mart), pastikan `.env` masuk `.gitignore`, dan rotasi password jika pernah terunggah. |
| Data management | `check_quality()` memeriksa ID transaksi ganda, `total <= 0`, dan kanal kosong. | Aturan pemeriksaan masih sedikit; belum memeriksa nilai kanal yang diizinkan, null pada ID/tanggal, relasi pelanggan, atau jumlah baris yang berubah. | Tambahkan aturan validasi skema, rentang nilai, referential integrity, serta catat hasil pemeriksaan dan jumlah baris. |
| DataOps | `logging.basicConfig()` dan `log.info()` mencatat tahap pipeline; `check_quality()` menghentikan proses jika data tidak valid. | Belum ada metrik, notifikasi kegagalan, pengujian otomatis, atau pemantauan durasi dan keberhasilan tiap tahap. | Tambahkan pengujian, status run, durasi, metrik jumlah baris, dan notifikasi saat pipeline gagal. |
| Data architecture | Fungsi `ingest()`, `store_raw()`, `transform()`, dan `serve()` memisahkan tahap; data mentah disimpan sebagai CSV dan hasil disajikan di `mart_omzet_harian`. | Penyimpanan raw lokal dapat hilang jika perangkat rusak; nama dan skema tabel belum diberi versi; proses belum dirancang untuk data bertambah besar. | Simpan raw pada object storage seperti MinIO, tetapkan kontrak/skema data, dan rancang partisi atau pemrosesan inkremental saat volume meningkat. |
| Orchestration | `main()` memanggil tahap-tahap dalam urutan yang jelas. | Pipeline hanya dijalankan manual; belum ada jadwal, timeout, retry terkontrol, atau pencatatan status run. | Jadwalkan menggunakan scheduler, tetapkan timeout dan retry terbatas, serta pastikan satu run tidak bertabrakan dengan run lain. |
| Software engineering | Pipeline memakai fungsi terpisah, nama fungsi yang jelas, dan logging; konfigurasi dibaca dari lingkungan. | Belum ada unit test, type checking, pengelolaan dependensi dengan versi yang dikunci, atau penanganan transaksi saat penulisan mart gagal. | Tambahkan unit test untuk kualitas dan transformasi, pin versi dependensi, gunakan transaksi/strategi staging untuk publikasi mart, dan lakukan review melalui pull request. |

Pertanyaan Sesi 2

1.  Mengapa `mart_omzet_harian` tetap aman saat data rusak masuk?

Urutan di `main()` adalah ingestion → simpan raw → pemeriksaan kualitas → transformasi → serving. Ketika transaksi dengan `total <= 0` ditemukan, `check_quality()` melempar `ValueError`. Eksekusi berhenti sebelum `transform()` dan `serve()` dijalankan. Karena tabel `mart_omzet_harian` baru ditulis pada tahap serving, tabel tersebut tidak ditimpa oleh hasil dari data yang gagal pemeriksaan.

2.  `data/raw/transaksi.csv` tetap diperbarui walaupun data rusak. Masalah atau berguna?

Keduanya, tergantung tujuan dan kontrolnya. Ini berguna karena salinan raw merekam data yang benar-benar diterima sehingga dapat dipakai untuk audit, penelusuran masalah, dan reproduksi kegagalan. Namun, file tersebut juga mengandung data yang tidak lolos pemeriksaan sehingga tidak boleh langsung dipakai sebagai data bersih atau sumber dashboard. Beri penanda status kualitas, batasi akses, dan pisahkan raw dari data tervalidasi. Untuk kasus ini, CSV memang diperbarui karena `store_raw()` dijalankan sebelum `check_quality()`.
