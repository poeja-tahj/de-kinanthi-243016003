SELECT 'pelanggan' AS tabel, COUNT(*) FROM pelanggan
UNION ALL SELECT 'produk', COUNT(*) FROM produk
UNION ALL SELECT 'transaksi', COUNT(*) FROM transaksi
UNION ALL SELECT 'detail_transaksi', COUNT(*) FROM detail_transaksi;

SELECT kanal, COUNT(*) AS jumlah_transaksi, SUM(total) AS omzet
FROM transaksi
GROUP BY kanal
ORDER BY omzet DESC;

SELECT p.nama, SUM(d.jumlah) AS terjual
FROM detail_transaksi d
JOIN produk p ON p.id_produk = d.id_produk
GROUP BY p.nama
ORDER BY terjual DESC
LIMIT 5;

SELECT COUNT(*) AS jumlah_transaksi
FROM transaksi;

SELECT
    SUM(jumlah_transaksi) AS total_transaksi,
    SUM(omzet) AS total_omzet
FROM mart_omzet_harian;

SELECT table_schema, table_name
FROM information_schema.tables
WHERE table_name = 'mart_omzet_harian';

SELECT *
FROM public.mart_omzet_harian
LIMIT 10;

SELECT
    SUM(jumlah_transaksi) AS total_transaksi,
    SUM(omzet) AS total_omzet
FROM public.mart_omzet_harian;

INSERT INTO transaksi
    (id_transaksi, id_pelanggan, tanggal, kanal, total)
VALUES
    (5001, 1, NOW(), 'web', -50000);

DELETE FROM transaksi
WHERE id_transaksi = 5001;

SELECT COUNT(*) AS jumlah_transaksi
FROM transaksi;

