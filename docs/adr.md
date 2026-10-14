4A. Reversibilitas Keputusan
A. Tabel Klasifikasi Keputusan
No.| Keputusan |One-way / Two-way| Alasan Cara Membuatnya Lebih Reversible|
1| Menyimpan seluruh data kampus dalam format tertutup milik satu vendor |One-way door| Keputusan ini sulit dibatalkan karena data terikat pada format khusus vendor sehingga migrasi ke sistem lain membutuhkan biaya, waktu, dan proses konversi yang besar. Menggunakan format data terbuka seperti CSV atau Parquet, menyediakan fitur ekspor data, dan melakukan backup secara berkala.|
2| Menulis ulang SIAKAD kampus sekaligus (big-bang rewrite) |One-way door| Penulisan ulang seluruh sistem sekaligus berisiko menyebabkan gangguan layanan dan kegagalan migrasi karena semua komponen berubah dalam satu waktu. Menggunakan pendekatan Strangler Pattern, yaitu mengganti sistem lama secara bertahap sambil mempertahankan sistem lama sebagai cadangan.|
3| Menandatangani kontrak cloud selama 3 tahun dengan komitmen biaya |One-way door| Kontrak jangka panjang dengan komitmen biaya membuat kampus terikat pada pengeluaran tertentu dan dapat dikenai penalti jika mengakhiri kontrak lebih awal. Menegosiasikan kontrak dengan opsi penghentian, evaluasi berkala, batas komitmen biaya, dan klausul migrasi ke penyedia cloud lain.|
4| Memilih Parquet sebagai format penyimpanan data analitik |Two-way door| Keputusan ini relatif mudah dibatalkan karena data Parquet dapat dikonversi ke format lain dengan bantuan berbagai tools pengolahan data. Memisahkan format penyimpanan dari aplikasi yang menggunakannya, menyimpan skema data secara terdokumentasi, dan menguji proses konversi secara berkala.|

B. Jawaban Pertanyaan
(1) Mengapa keputusan two-way door boleh diambil lebih cepat?
Keputusan two-way door boleh diambil lebih cepat karena keputusan tersebut relatif mudah dibatalkan atau diubah apabila hasilnya tidak sesuai dengan kebutuhan. Dengan demikian, tim tidak perlu menghabiskan terlalu banyak waktu untuk menganalisis semua kemungkinan sebelum bertindak.
Pendekatan ini memungkinkan tim melakukan eksperimen, memperoleh umpan balik lebih awal, dan memperbaiki keputusan berdasarkan pengalaman nyata. Namun, keputusan tetap perlu mempertimbangkan risiko dan dampaknya agar perubahan tidak menimbulkan kerugian yang besar.
(2) Strangler Pattern pada proyek brownfield termasuk strategi apa dari sudut reversibilitas?
Strangler Pattern termasuk strategi meningkatkan reversibilitas melalui migrasi bertahap. Dalam proyek brownfield, yaitu pengembangan atau perubahan sistem yang sudah berjalan, pendekatan ini memungkinkan sistem baru dibangun secara bertahap untuk menggantikan fungsi sistem lama.
Selama proses migrasi, sistem lama tetap dapat digunakan untuk bagian yang belum dipindahkan. Jika sistem baru mengalami masalah, lalu lintas pengguna dapat dialihkan kembali ke sistem lama selama mekanisme tersebut sudah dirancang dan diuji.
Dengan demikian, risiko perubahan dapat dikurangi karena tim tidak perlu mengganti seluruh sistem sekaligus. Pendekatan ini juga mempermudah pengujian, evaluasi, dan pembatalan perubahan pada setiap tahap migrasi.

4C. Architecture Decision Record (ADR)
ADR-001: Pemilihan Format Penyimpanan Data Analitik Kampus

Status:Diusulkan

Konteks:
Kampus memiliki data akademik yang berasal dari berbagai sistem, seperti Sistem Informasi Akademik (SIAKAD), keuangan, dan administrasi mahasiswa. Data tersebut perlu disimpan dan diolah untuk menghasilkan laporan serta mendukung analisis data.

Format penyimpanan harus mampu menghemat ruang penyimpanan, mendukung pemrosesan data dalam jumlah besar, dan mempermudah integrasi dengan berbagai tools analitik. Selain itu, kampus perlu menghindari ketergantungan berlebihan pada satu vendor agar migrasi ke teknologi lain tetap memungkinkan.

Opsi:

1. Opsi A CSV
   - Biaya: Rendah karena mudah dibuat dan dibaca menggunakan berbagai aplikasi.
   - Latensi: Relatif lebih tinggi untuk analisis kolom tertentu pada data berukuran besar karena umumnya perlu membaca dan mem-parsing teks.
   - Kompleksitas: Rendah, tetapi tipe data dan skema perlu dikelola secara terpisah.

2. Opsi B Parquet
   - Biaya: Relatif efisien dalam penggunaan ruang penyimpanan karena mendukung kompresi.
   - Latensi: Baik untuk analitik karena mendukung penyimpanan kolumnar dan pembacaan kolom yang diperlukan saja.
   - Kompleksitas: Sedang karena memerlukan tools atau library yang mendukung format Parquet.

3. Opsi C Format tertutup milik vendor
   - Biaya: Dapat terlihat efisien pada awal penggunaan, tetapi berpotensi menimbulkan biaya lisensi dan migrasi.
   - Latensi: Dapat optimal dalam ekosistem vendor terkait, bergantung pada implementasinya.
   - Kompleksitas: Berpotensi tinggi ketika data harus diintegrasikan dengan sistem lain atau dipindahkan ke vendor berbeda.

Keputusan:
Memilih Parquet sebagai format utama penyimpanan data analitik kampus karena mendukung penyimpanan kolumnar, kompresi, dan pembacaan data secara efisien. Format ini juga didukung oleh berbagai tools pengolahan data sehingga ketergantungan terhadap satu vendor dapat dikurangi.

CSV tetap dapat digunakan untuk pertukaran data sederhana dan kebutuhan ekspor yang mudah dibaca manusia.

Tipe:Two-way door

Konsekuensi:

- Penggunaan ruang penyimpanan dapat lebih efisien untuk data analitik dibandingkan CSV, bergantung pada karakteristik data.
- Pemrosesan analitik dapat lebih efisien karena hanya kolom yang diperlukan yang perlu dibaca.
- Tim perlu mengelola skema data, kompatibilitas tools, dan proses konversi data.
- Data perlu didokumentasikan dan dicadangkan untuk menjaga integritas serta mempermudah pemulihan.

Risiko:
Perubahan skema, ketidakcocokan versi tools, atau kebutuhan integrasi dengan sistem lama dapat menimbulkan kendala dalam pengolahan data.

Exit Plan:
Apabila Parquet tidak lagi sesuai dengan kebutuhan kampus, data akan diekspor ke format alternatif seperti CSV atau format terbuka lainnya. Sebelum migrasi dilakukan, tim akan menguji kesesuaian skema, jumlah baris, tipe data, dan integritas data. Migrasi dilaksanakan secara bertahap agar sistem analitik yang sedang berjalan tidak terganggu.
