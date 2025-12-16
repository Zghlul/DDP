# rumuszakat.py

# ======================
# ZAKAT SIMPANAN (Emas & Perak)
# ======================

NISAB_EMAS = 85        # gram
NISAB_PERAK = 595      # gram
PERSEN_ZAKAT = 0.025  # 2.5%

def hitung_zakat_emas(berat, harga):
    if berat >= NISAB_EMAS:
        return berat * harga * PERSEN_ZAKAT
    return 0

def hitung_zakat_perak(berat, harga):
    if berat >= NISAB_PERAK:
        return berat * harga * PERSEN_ZAKAT
    return 0


# ======================
# ZAKAT PENGHASILAN
# ======================

NISAB_TAHUNAN = 85685972
NISAB_BULANAN = 7140498

def hitung_zakat_penghasilan(income, expenses, period):
    bersih = income - expenses
    pengali = 12 if period == "Bulanan" else 1
    bersih_tahun = bersih * pengali

    if bersih_tahun >= NISAB_TAHUNAN:
        zakat_tahun = bersih_tahun * PERSEN_ZAKAT
        return zakat_tahun / pengali
    return 0


# ======================
# ZAKAT PETERNAKAN
# ======================

def zakat_sapi(jumlah):
    if jumlah < 30:
        return ""

    hasil = []
    sisa = jumlah

    jumlah_40 = sisa // 40
    sisa %= 40

    jumlah_30 = sisa // 30

    if jumlah_30 == 0 and jumlah_40 == 0:
        if 30 <= jumlah <= 39:
            return "1 ekor sapi / kerbau tabi umur 1 tahun"
        elif 40 <= jumlah <= 59:
            return "1 ekor sapi / kerbau musinnah umur 2 tahun"

    if jumlah_30 > 0:
        hasil.append(f"{jumlah_30} ekor sapi / kerbau tabi umur 1 tahun")
    if jumlah_40 > 0:
        hasil.append(f"{jumlah_40} ekor sapi / kerbau musinnah umur 2 tahun")

    return " dan ".join(hasil)


def zakat_kambing(jumlah):
    if jumlah < 40:
        return ""
    elif jumlah <= 120:
        return "1 ekor kambing / domba"
    elif jumlah <= 200:
        return "2 ekor kambing / domba"
    elif jumlah <= 300:
        return "3 ekor kambing / domba"
    elif jumlah <= 400:
        return "4 ekor kambing / domba"
    else:
        tambahan = (jumlah - 401) // 100 + 1
        return f"{4 + tambahan} ekor kambing / domba umur 1 tahun"
