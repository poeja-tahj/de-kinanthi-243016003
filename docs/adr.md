4A. Reversibilitas Keputusan
A. Tabel Klasifikasi Keputusan
No.| Keputusan |One-way / Two-way| Alasan | Cara Membuatnya Lebih Reversible|
1| Menyimpan seluruh data kampus dalam format tertutup milik satu vendor |One-way door| Keputusan ini sulit dibatalkan karena data terikat pada format khusus vendor sehingga migrasi ke sistem lain membutuhkan biaya, waktu, dan proses konversi yang besar. |Menggunakan format data terbuka seperti CSV atau Parquet, menyediakan fitur ekspor data, dan melakukan backup secara berkala.|
2| Menulis ulang SIAKAD kampus sekaligus (big-bang rewrite) |One-way door| Penulisan ulang seluruh sistem sekaligus berisiko menyebabkan gangguan layanan dan kegagalan migrasi karena semua komponen berubah dalam satu waktu.| Menggunakan pendekatan Strangler Pattern, yaitu mengganti sistem lama secara bertahap sambil mempertahankan sistem lama sebagai cadangan.|
3| Menandatangani kontrak cloud selama 3 tahun dengan komitmen biaya |One-way door| Kontrak jangka panjang dengan komitmen biaya membuat kampus terikat pada pengeluaran tertentu dan dapat dikenai penalti jika mengakhiri kontrak lebih awal.| Menegosiasikan kontrak dengan opsi penghentian, evaluasi berkala, batas komitmen biaya, dan klausul migrasi ke penyedia cloud lain.|
4| Memilih Parquet sebagai format penyimpanan data analitik |Two-way door| Keputusan ini relatif mudah dibatalkan karena data Parquet dapat dikonversi ke format lain dengan bantuan berbagai tools pengolahan data. |Memisahkan format penyimpanan dari aplikasi yang menggunakannya, menyimpan skema data secara terdokumentasi, dan menguji proses konversi secara berkala.|

4A. Jawaban Pertanyaan
(1) Mengapa keputusan two-way door boleh diambil lebih cepat?
Keputusan two-way door boleh diambil lebih cepat karena keputusan tersebut relatif mudah dibatalkan atau diubah apabila hasilnya tidak sesuai dengan kebutuhan. Dengan demikian, tim tidak perlu menghabiskan terlalu banyak waktu untuk menganalisis semua kemungkinan sebelum bertindak.
Pendekatan ini memungkinkan tim melakukan eksperimen, memperoleh umpan balik lebih awal, dan memperbaiki keputusan berdasarkan pengalaman nyata. Namun, keputusan tetap perlu mempertimbangkan risiko dan dampaknya agar perubahan tidak menimbulkan kerugian yang besar.
(2) Strangler Pattern pada proyek brownfield termasuk strategi apa dari sudut reversibilitas?
Strangler Pattern termasuk strategi meningkatkan reversibilitas melalui migrasi bertahap. Dalam proyek brownfield, yaitu pengembangan atau perubahan sistem yang sudah berjalan, pendekatan ini memungkinkan sistem baru dibangun secara bertahap untuk menggantikan fungsi sistem lama.
Selama proses migrasi, sistem lama tetap dapat digunakan untuk bagian yang belum dipindahkan. Jika sistem baru mengalami masalah, lalu lintas pengguna dapat dialihkan kembali ke sistem lama selama mekanisme tersebut sudah dirancang dan diuji.
Dengan demikian, risiko perubahan dapat dikurangi karena tim tidak perlu mengganti seluruh sistem sekaligus. Pendekatan ini juga mempermudah pengujian, evaluasi, dan pembatalan perubahan pada setiap tahap migrasi.

4A.Architecture Decision Record (ADR)
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

4B.Plan for failure: availability, RPO, dan retry

1. Mengapa availability total lebih rendah daripada komponen terlemahnya?
   Availability total lebih rendah karena aplikasi, database, dan jaringan harus berfungsi bersama. Jika salah satu komponen mengalami gangguan, sistem secara keseluruhan dapat terganggu. Availability total dihitung dengan mengalikan availability setiap komponen, sehingga hasilnya menjadi 99,30% dengan downtime sekitar 61,2 jam per tahun.
2. Tabel RPO, interval backup, dan alasan
   Jenis data | RPO wajar| Interval backup Alasan
   (a) Transaksi pembayaran toko | 1 menit |Setiap 1 menit| Transaksi pembayaran sangat penting sehingga kehilangan data harus diminimalkan. Waktu pemulihan harus singkat agar pelanggan dapat kembali bertransaksi. Biaya backup lebih tinggi dapat diterima untuk mengurangi risiko kerugian.
   (b) Log klik website | 15 menit |Setiap 15 menit| Kehilangan sebagian log klik masih dapat ditoleransi. Interval ini menyeimbangkan kebutuhan analisis data dengan biaya backup.
   (c) Laporan internal mingguan | 24 jam |Setiap 24 jam |Laporan tidak berubah sesering transaksi. Backup harian lebih hemat biaya dan kehilangan perubahan selama satu hari masih dapat ditoleransi.
3. Mengapa RPO mendekati nol jauh lebih mahal? Mengapa harus ditanyakan kepada stakeholder bisnis?
   RPO mendekati nol membutuhkan backup yang lebih sering, replikasi data, serta infrastruktur yang lebih andal. Hal tersebut meningkatkan biaya penyimpanan, jaringan, dan komputasi. Dalam FinOps, pengeluaran teknologi harus disesuaikan dengan manfaat bisnis dan risiko kehilangan data.
   RPO dan RTO perlu ditanyakan kepada stakeholder bisnis karena setiap data memiliki tingkat kepentingan berbeda. Stakeholder menentukan batas kehilangan data dan waktu pemulihan yang dapat diterima berdasarkan dampaknya terhadap operasional, pelanggan, pendapatan, dan anggaran.
4. Apa risiko retry tanpa batas terhadap komponen yang sedang bermasalah?
   Retry tanpa batas dapat menambah beban komponen yang sedang bermasalah karena permintaan terus dikirim berulang kali. Akibatnya, antrean permintaan menumpuk, penggunaan sumber daya meningkat, dan gangguan dapat semakin parah. Retry juga berisiko menyebabkan transaksi terduplikasi. Karena itu, retry perlu dibatasi dengan jumlah percobaan maksimal, jeda bertahap (exponential backoff), dan mekanisme circuit breaker.

44C. Tight vs Loose Coupling dan Dead-Letter Queue

1. Perbandingan Desain A dan Desain B
   Desain A (Tightly Coupled)

Pada Desain A, pesanan nomor 2 mengalami pemrosesan sebagian. Stok sudah dikurangi, tetapi layanan email mengalami kegagalan sehingga proses pencatatan analitik tidak dijalankan. Hal ini terjadi karena semua proses dipanggil secara berurutan dalam satu fungsi. Pesanan nomor 1 dan 3 berhasil diproses.

Hasilnya:

- Stok: `[1, 2, 3]`
- Analitik: `[1, 3]`

Desain B (Loosely Coupled)

Pada Desain B, pesanan nomor 2 tetap diterima meskipun layanan email gagal. Proses pengurangan stok dan pencatatan analitik tetap berjalan karena setiap consumer menangani peristiwa secara terpisah.

Dead-letter queue berisi satu pesan gagal, yaitu:

- Handler: `kirim_email`
- Event: pesanan dengan ID `2`
- Error: `layanan email down`

Hasilnya:

- Stok: `[1, 2, 3]`
- Analitik: `[1, 2, 3]`

2. Penambahan Consumer Baru `cek_fraud`

Consumer `cek_fraud` ditambahkan untuk mencetak peringatan apabila ID pesanan bernilai genap. Berdasarkan hasil program, consumer tersebut mencetak peringatan untuk pesanan nomor 2.

Pada Desain B, consumer baru dapat ditambahkan dengan berlangganan pada topik `pesanan_baru` tanpa mengubah kode producer. Sementara itu, pada Desain A, fungsi pemrosesan pesanan harus diubah untuk memanggil fungsi `cek_fraud` secara langsung.

Dengan demikian, Desain B lebih fleksibel dan mempermudah penambahan layanan baru.

3. Apa harga yang dibayar Desain B?

Desain B memiliki beberapa konsekuensi:

- Konsistensi: Data pada setiap layanan tidak selalu diperbarui secara bersamaan karena setiap consumer dapat memproses peristiwa pada waktu berbeda.
- Urutan: Urutan pemrosesan antarconsumer tidak selalu terjamin. Pengaturan tambahan diperlukan apabila urutan tertentu wajib dipertahankan.
- Debugging: Penelusuran kesalahan lebih kompleks karena peristiwa melewati beberapa komponen. Sistem memerlukan pencatatan log, pemantauan, dan pemeriksaan dead-letter queue.

Selain itu, Desain B membutuhkan sumber daya dan biaya tambahan untuk pengelolaan router, antrean pesan, dan penanganan kegagalan.

4. Apa padanan router pada skala organisasi?

Pada skala organisasi, router dapat dianalogikan dengan teknologi perantara pesan atau message broker, seperti:

1. Apache Kafka: Digunakan untuk mengalirkan dan menyimpan peristiwa dalam jumlah besar serta mendukung pemrosesan data secara berkelanjutan.
2. Google Cloud Pub/Sub: Menghubungkan producer dan consumer melalui sistem pesan berbasis topik.
3. Amazon SNS/SQS: SNS mendistribusikan notifikasi, sedangkan SQS menyediakan antrean pesan untuk diproses oleh consumer.
4. RabbitMQ: Meneruskan pesan dari producer ke antrean consumer melalui mekanisme exchange dan routing.

Teknologi tersebut membantu memisahkan layanan, meningkatkan fleksibilitas sistem, dan mendukung penanganan kegagalan. Pemilihannya disesuaikan dengan kebutuhan organisasi, seperti volume pesan, latensi, keandalan, dan biaya operasional.

Kesimpulan

Desain A lebih sederhana, tetapi kegagalan satu proses dapat menghentikan proses berikutnya. Desain B lebih fleksibel karena setiap consumer dapat bekerja secara terpisah dan pesan gagal dapat dicatat dalam dead-letter queue. Meskipun membutuhkan pengelolaan yang lebih kompleks, Desain B lebih sesuai untuk sistem yang memiliki banyak layanan dan perlu dikembangkan secara bertahap.
