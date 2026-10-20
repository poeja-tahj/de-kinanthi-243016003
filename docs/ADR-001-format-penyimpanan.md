ADR-001: Menghindari Format Penyimpanan Tertutup Milik Vendor



a)Status:Diusulkan



b)Konteks:

Kampus memiliki data akademik dari berbagai sistem, seperti Sistem Informasi Akademik (SIAKAD), keuangan, dan administrasi mahasiswa. Data perlu disimpan agar dapat digunakan untuk pelaporan, analisis, dan integrasi dengan sistem lain. Penggunaan format tertutup milik satu vendor dapat menimbulkan ketergantungan terhadap vendor tersebut.



c)Keputusan:

Kampus menghindari penggunaan format tertutup milik satu vendor sebagai satu-satunya format penyimpanan data. Kampus memilih format terbuka, seperti CSV atau Parquet, sesuai dengan kebutuhan penggunaan data.



d)Klasifikasi Keputusan: One-way door.

Keputusan ini dikategorikan sebagai one-way door apabila seluruh data terlanjur disimpan dalam format khusus vendor dan migrasi membutuhkan biaya, waktu, serta proses konversi yang besar. Oleh karena itu, keputusan perlu dipertimbangkan secara matang sejak awal.



e)Konsekuensi:

\- Data lebih mudah dipindahkan dan digunakan oleh berbagai tools yang mendukung format terbuka.

\- Ketergantungan pada satu vendor dapat dikurangi.

\- Tim perlu mengelola skema data dan memastikan kompatibilitas antarperangkat.

\- Proses ekspor dan backup perlu dilakukan secara teratur.



f)Risiko:

Perbedaan skema, tipe data, atau dukungan format pada aplikasi tertentu dapat menimbulkan kendala ketika data dipindahkan atau digunakan oleh sistem lain.



g)Exit Plan:

Jika format yang digunakan tidak lagi memenuhi kebutuhan, kampus melakukan ekspor dan konversi data ke format alternatif. Sebelum migrasi, tim memeriksa skema, jumlah baris, tipe data, dan integritas data serta melakukan backup agar proses migrasi dapat dipulihkan jika terjadi masalah.



h)Cara Meningkatkan Reversibilitas

Menggunakan format terbuka, menyediakan fitur ekspor data, mendokumentasikan skema, dan melakukan backup secara berkala.

