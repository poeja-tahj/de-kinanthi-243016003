3A.Pemetaan Peran Data Engineering Batik Kinanthi

| No.|Kebutuhan Pemilik Batik Kinanthi | Peran Utama | Alasan Singkat | Tahap Lifecycle |
| 1 | Data penjualan dari toko, web, dan marketplace dikumpulkan ke satu tempat setiap malam | Data Engineer | Memindahkan dan menyatukan data dari banyak sumber secara otomatis | Ingestion |
| 2 | Dashboard omzet harian per kanal | Data Analyst | Menganalisis omzet setiap kanal dan menyajikan hasilnya dalam dashboard agar mudah dipahami | Serving |
| 3 | Prediksi kebutuhan stok kain bulan depan | Data Scientist | Membangun model prediksi berdasarkan pola penjualan dan data historis | Transformation |
| 4 | Tabel pelanggan tidak boleh berisi data ganda | Data Engineer | Menerapkan pemeriksaan kualitas dan proses deduplikasi agar data pelanggan tetap konsisten | Transformation |
| 5 | Laporan motif terlaris per kota untuk rapat bulanan | Data Analyst | Mengolah dan menganalisis penjualan berdasarkan motif dan kota untuk menghasilkan laporan | Serving |
| 6 | Rekomendasi produk untuk pelanggan di situs web | Data Scientist | Mengembangkan model rekomendasi berdasarkan pola pembelian atau preferensi pelanggan | Serving |
| 7 | Data transaksi lama tetap tersimpan aman dan hemat biaya | Data Engineer | Mengelola penyimpanan, pencadangan, dan pengarsipan data historis secara efisien | Storage |
| 8 | Analisis penyebab penurunan penjualan marketplace bulan lalu | Data Analyst | Membandingkan data penjualan dan mencari faktor yang berkaitan dengan penurunan penjualan | Transformation |

Kesimpulan :
Data Engineer berfokus pada pengumpulan, kualitas, dan penyimpanan data. Data Scientist berfokus pada pengembangan model prediksi dan rekomendasi. Data Analyst berfokus pada analisis data, pencarian penyebab masalah bisnis, serta penyajian informasi dalam bentuk laporan dan dashboard.

3B.Identifikasi Undercurrents pada Mini Pipeline Batik Kinanthi

| Undercurrent | Bukti Penerapan di Kode | Kekurangan | Usulan Perbaikan |
| Security | Kredensial database dibaca dari file `.env` menggunakan `load_dotenv()`. | Pipeline menggunakan akun `de_user` yang memiliki hak akses terlalu luas. | Membuat akun khusus pipeline dengan hak baca pada tabel transaksi dan hak tulis pada tabel `mart_omzet_harian` saja. |
| Data management | Fungsi `check_quality()` memeriksa kualitas data, sedangkan `store_raw()` menyimpan data mentah ke CSV. | Pemeriksaan kualitas masih sederhana dan belum mencakup semua kemungkinan data tidak valid. | Menambahkan validasi skema, pemeriksaan data duplikat, pencatatan asal data, dan aturan retensi data. |
| DataOps | Logging menggunakan `logging` untuk mencatat awal pipeline, jumlah baris, hasil pemeriksaan kualitas, dan penyelesaian proses. | Belum tersedia pengujian otomatis, pemantauan terpusat, dan notifikasi kegagalan. | Menambahkan pengujian otomatis, pemantauan pipeline, serta notifikasi ketika proses gagal. |
| Data architecture | Pipeline memisahkan fungsi `ingest()`, `store_raw()`, `transform()`, dan `serve()`. | Struktur pipeline masih sederhana dan belum mendefinisikan kontrak data serta pengelolaan skema secara eksplisit. | Menetapkan skema dan kontrak data yang jelas agar perubahan struktur data dapat dideteksi sebelum proses berikutnya. |
| Orchestration | Fungsi `main()` mengatur urutan ingestion, storage, pemeriksaan kualitas, transformation, dan serving. | Pipeline dijalankan secara manual dan belum memiliki penjadwalan atau mekanisme retry otomatis. | Menambahkan penjadwalan harian, retry untuk kegagalan sementara, dan pencatatan status setiap proses. |
| Software engineering | Kode dipisahkan menjadi beberapa fungsi dan menggunakan type hints pada sejumlah fungsi. | Belum ada pengujian unit yang memadai untuk memastikan setiap fungsi berjalan sesuai harapan. | Menambahkan unit test, penanganan error yang konsisten, dan dokumentasi fungsi. |

Kesimpulan:
Enam undercurrents tersebut membantu menjaga pipeline data agar aman, berkualitas, terstruktur, mudah dipantau, dan mudah dipelihara. Walaupun mini pipeline Batik Kinanthi sudah memisahkan beberapa tahap pemrosesan dan memiliki pemeriksaan kualitas, sistem masih dapat ditingkatkan melalui pembatasan akses, pengujian otomatis, penjadwalan, dan pemantauan kegagalan.
