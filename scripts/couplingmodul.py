"""Demonstrasi loose coupling dan replay DLQ yang idempotent."""
from copy import deepcopy

stok, analitik = [], []
email_terkirim = []
fraud_alert = []

def kurangi_stok(event):
    # Idempotent: event yang sama tidak diproses dua kali.
    if event["id"] not in stok:
        stok.append(event["id"])

def catat_analitik(event):
    if event["id"] not in analitik:
        analitik.append(event["id"])

def kirim_email(event):
    if event["id"] == 2 and not event.get("email_diperbaiki", False):
        raise ConnectionError("layanan email down")
    if event["id"] not in email_terkirim:
        email_terkirim.append(event["id"])

def cek_fraud(event):
    if event["id"] % 2 == 0:
        fraud_alert.append(event["id"])
        print(f"PERINGATAN FRAUD: pesanan {event['id']} bernomor genap")

class Router:
    def __init__(self):
        self.pelanggan = {}
        self.dlq = []

    def subscribe(self, topik, handler):
        self.pelanggan.setdefault(topik, []).append(handler)

    def publish(self, topik, event):
        for handler in self.pelanggan.get(topik, []):
            try:
                handler(event)
            except Exception as err:
                self.dlq.append({
                    "topik": topik,
                    "handler": handler.__name__,
                    "event": deepcopy(event),
                    "error": str(err),
                })

    def ulang_dlq(self):
        """Coba ulang hanya consumer yang gagal; consumer sukses tidak dipanggil ulang."""
        masih_gagal = []
        for item in self.dlq:
            handler = next(
                (h for h in self.pelanggan.get(item["topik"], [])
                 if h.__name__ == item["handler"]),
                None,
            )
            if handler is None:
                masih_gagal.append(item)
                continue
            try:
                handler(item["event"])
                print(f"DLQ berhasil diproses ulang: {item['handler']} untuk pesanan {item['event']['id']}")
            except Exception as err:
                item["error"] = str(err)
                masih_gagal.append(item)
        self.dlq = masih_gagal

if __name__ == "__main__":
    router = Router()
    for consumer in (kurangi_stok, kirim_email, catat_analitik):
        router.subscribe("pesanan_baru", consumer)

    for nomor in (1, 2, 3):
        router.publish("pesanan_baru", {"id": nomor})

    print("Sebelum replay:")
    print("stok:", stok, "| email:", email_terkirim, "| analitik:", analitik)
    print("DLQ:", router.dlq)

    # Simulasi layanan email pulih. Event yang gagal diubah agar retry berhasil.
    for item in router.dlq:
        if item["handler"] == "kirim_email":
            item["event"]["email_diperbaiki"] = True

    router.ulang_dlq()
    print("Sesudah replay:")
    print("stok:", stok, "| email:", email_terkirim, "| analitik:", analitik)
    print("DLQ tersisa:", router.dlq)

    # Consumer baru dapat ditambahkan tanpa mengubah producer.
    router.subscribe("pesanan_baru", cek_fraud)
    router.publish("pesanan_baru", {"id": 4})
    print("peringatan fraud:", fraud_alert)
