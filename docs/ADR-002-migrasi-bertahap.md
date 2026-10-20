ADR-002: Mengganti Sistem SIAKAD Secara Bertahap



a)Status: Diusulkan



b)Konteks:

SIAKAD merupakan sistem yang digunakan untuk mendukung kegiatan akademik kampus. Jika sistem perlu diperbarui, penulisan ulang seluruh sistem sekaligus berisiko menyebabkan gangguan layanan, kegagalan migrasi, dan kesulitan menemukan sumber masalah.



c)Keputusan:

Kampus memilih pendekatan Strangler Pattern, yaitu mengganti fungsi sistem lama secara bertahap dengan fungsi pada sistem baru. Sistem lama tetap digunakan untuk bagian yang belum dimigrasikan.



d)Klasifikasi Keputusan: One-way door untuk keputusan melakukan big-bang rewrite yang dihindari; sedangkan penerapan Strangler Pattern merupakan strategi yang lebih reversible.

Penulisan ulang seluruh SIAKAD sekaligus dikategorikan sebagai one-way door karena perubahan besar dilakukan dalam satu waktu dan pemulihannya berpotensi mahal. Sebaliknya, migrasi bertahap memungkinkan setiap bagian diuji dan dievaluasi sebelum melanjutkan ke tahap berikutnya.



e)Konsekuensi:

\- Risiko gangguan layanan dapat dikurangi karena perubahan dilakukan secara bertahap.

\- Sistem lama masih dapat mendukung fungsi yang belum dipindahkan.

\- Tim dapat menguji dan mengevaluasi sistem baru pada setiap tahap.

\- Pengelolaan dua sistem selama masa transisi membutuhkan koordinasi dan biaya tambahan.



f)Risiko:

Integrasi antara sistem lama dan sistem baru dapat menimbulkan ketidaksesuaian data, perbedaan proses bisnis, atau kesalahan ketika pengguna berpindah dari satu sistem ke sistem lain.



g)Exit Plan:

Jika fungsi baru mengalami masalah, alur pengguna dapat dialihkan kembali ke fungsi sistem lama selama mekanisme pengalihan dan pemulihan tersebut sudah dirancang serta diuji. Migrasi dilanjutkan setelah masalah diperbaiki dan hasil pengujian memenuhi kebutuhan.



h)Cara Meningkatkan Reversibilitas:

Memigrasikan fungsi secara bertahap, menguji setiap perubahan, mempertahankan sistem lama selama masa transisi, serta menyiapkan backup dan prosedur rollback.

