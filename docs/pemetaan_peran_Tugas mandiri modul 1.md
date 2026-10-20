# Pemetaan Peran Data Engineering — Batik Kinanthi

| No. | Kebutuhan pemilik Batik Kinanthi | Peran utama | Alasan singkat | Tahap lifecycle |
|---:|---|---|---|---|
| 1 | Data penjualan dari toko, web, dan marketplace dikumpulkan ke satu tempat setiap malam | Data Engineer | Mengambil dan menyatukan data dari berbagai sumber secara andal dan terjadwal. | Ingestion |
| 2 | Dashboard omzet harian per kanal | Data Analyst | Menyajikan dan menjelaskan kinerja penjualan melalui metrik dan dashboard. | Serving |
| 3 | Prediksi kebutuhan stok kain bulan depan | Data Scientist | Membuat model prediksi berdasarkan pola historis dan faktor yang relevan. | Transformation / serving hasil model |
| 4 | Tabel pelanggan tidak boleh berisi data ganda | Data Engineer | Menerapkan aturan kualitas, deduplikasi, dan integritas data agar data konsisten. | Transformation / storage |
| 5 | Laporan motif terlaris per kota untuk rapat bulanan | Data Analyst | Mengelompokkan dan membandingkan penjualan berdasarkan motif dan kota untuk menjawab kebutuhan bisnis. | Serving |
| 6 | Rekomendasi produk untuk pelanggan di situs web | Data Scientist | Mengembangkan model atau logika rekomendasi berdasarkan perilaku dan riwayat pelanggan. | Transformation / serving hasil model |
| 7 | Data transaksi lama tetap tersimpan aman dan hemat biaya | Data Engineer | Merancang penyimpanan, retensi, backup, akses, dan pengarsipan data. | Storage |
| 8 | Analisis penyebab penurunan penjualan marketplace bulan lalu | Data Analyst | Menganalisis tren dan faktor yang berkaitan dengan penurunan untuk menjelaskan apa yang terjadi dan mengapa. | Transformation / serving |

## (a) Mengapa kebutuhan 3 dan 6 tidak bisa dikerjakan sebelum kebutuhan 1 dan 4 selesai?

Kebutuhan 3 (prediksi stok) dan 6 (rekomendasi produk) membutuhkan data historis yang cukup, konsisten, dan dapat dipercaya. Kebutuhan 1 memastikan data dari toko, web, dan marketplace terkumpul di satu tempat. Kebutuhan 4 memastikan data pelanggan tidak ganda. Jika pengumpulan dan deduplikasi belum beres, model dapat belajar dari data yang tidak lengkap atau menghitung pelanggan/transaksi yang sama lebih dari sekali. Akibatnya, prediksi stok dapat meleset dan rekomendasi produk menjadi kurang tepat. Karena itu, fondasi integrasi dan kualitas data perlu dibangun terlebih dahulu.

## (b) Risiko satu orang merangkap tiga peran di UMKM dan otomatisasi yang diprioritaskan

Jika satu orang menjadi Data Engineer, Data Scientist, dan Data Analyst sekaligus, risiko utamanya adalah beban kerja berlebihan, ketergantungan pada satu orang, kesalahan yang tidak terdeteksi karena tidak ada pemeriksaan silang, serta waktu yang terbagi antara pemeliharaan pipeline, eksperimen model, dan pembuatan laporan. Dokumentasi juga berisiko tertinggal.

Otomatisasi pertama yang sebaiknya diprioritaskan adalah pengumpulan data penjualan terjadwal, pemeriksaan kualitas dasar (data kosong, ID ganda, nilai total tidak wajar), dan pencatatan log serta notifikasi ketika pipeline gagal. Langkah ini menjaga data yang dipakai untuk laporan dan model tetap konsisten. Setelah itu, otomatisasi pembaruan tabel omzet dan dashboard dapat dilakukan.
