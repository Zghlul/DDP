import streamlit as st
import rumuszakat
from datetime import date

st.set_page_config(page_title="Kalkulator Zakat", layout="centered")
st.title("Zakat Mal")

# ======================
# NAVIGASI
# ======================
menu = st.sidebar.radio(
    "Menu",
    ["Home", "Zakat Emas & Perak", "Zakat Penghasilan", "Zakat Peternakan"]
)

# ======================
# FUNGSI WAJIB IDENTITAS
# ======================
def input_identitas():
    col1, col2 = st.columns(2)
    with col1:
        nama = st.text_input("Nama Muzakki *")
        nomor = st.text_input("Nomor HP *")
    with col2:
        domisili = st.text_input("Domisili *")
        tanggal = st.date_input("Tanggal", value=date.today())
    return nama, nomor, domisili, tanggal


def validasi_identitas(nama, nomor, domisili):
    return all([nama.strip(), nomor.strip(), domisili.strip()])


def tampilkan_identitas(nama, nomor, domisili, tanggal):
    st.info(
        f"""
**DATA MUZAKKI**
- Nama      : {nama}
- Nomor HP  : {nomor}
- Domisili  : {domisili}
- Tanggal   : {tanggal}
"""
    )


# ======================
# HOME
# ======================
if menu == "Home":
    st.title("APLIKASI SEDERHANA PERHITUNGN ZAKAT MAL")
    st.write ("----")
    st.header ("Welcome to zakat")
    st.text ("Zakat mal dikeluarkan saat harta telah mencapai batas minimum (nisab) dan telah dimiliki selama satu tahun penuh (haul)")
    st.write ('---')
    st.image ('https://baznasdepok.id/wp-content/uploads/2025/06/bayar-zakat-fitrah-secara-online-di-ziswaf-ct-arsa-praktis-banget-bun_169.jpeg', caption='Mau tunaikan zakat tapi tidak tau cara menghitungnya? Disini aja', width=700)
    st.write ('---')
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write('1. Zakat Emas Dan Perak')
        st.image('https://storage.googleapis.com/pyd-upload/website/thumbnail/article/1729159470697_zakat-emas-perak-judul.webp',
                 caption= 'Zakat emas dan perak adalah kewajiban zakat yang dikenakan atas kepemilikan emas dan perak yang telah mencapai nisab (batas minimum) dan haul (satu tahun kepemilikan).')
    with col2:
        st.write('2. Zakat Penghasilan ')
        st.image ('https://zakat.or.id/wp-content/uploads/2012/04/91f0a6b83ccef31beeb055f8ee34930e-768x512.jpg',
                  caption='Zakat penghasilan (atau zakat profesi) adalah zakat wajib atas pendapatan halal rutin seperti gaji, honor, atau jasa, yang dikeluarkan sebesar 2,5% jika penghasilan sudah mencapai nishab 85 gram emas per tahun') 
    with col3:
        st.write('3. Zakat Peternakan')
        st.image('https://awsimages.detik.net.id/community/media/visual/2022/08/11/kambing-makan-rumput-kering-untuk-cegah-kebakaran-hutan-3.jpeg?w=600&q=90',
                 caption='Zakat peternakan adalah kewajiban zakat atas hewan ternak (seperti sapi, kambing, domba, dan unta) yang telah mencapai jumlah minimal tertentu (nisab) dan dimiliki selama satu tahun (haul). ')

# ======================
# ZAKAT EMAS & PERAK
# ======================
elif menu == "Zakat Emas & Perak":
    st.header("Zakat Emas & Perak")

    nama, nomor, domisili, tanggal = input_identitas()
    st.divider()

    emas = st.number_input("Berat emas (gram)", min_value=0.0, step=85.0)
    harga_emas = st.number_input("Harga emas per gram (Rp)", min_value=0, step=100000)

    perak = st.number_input("Berat perak (gram)", min_value=0.0, step=595.0)
    harga_perak = st.number_input("Harga perak per gram (Rp)", min_value=0, step=100000)

    if st.button("Hitung Zakat", key="btn_emas"):
        if not validasi_identitas(nama, nomor, domisili):
            st.error("❗ Nama, Nomor HP, dan Domisili wajib diisi")
        else:
            tampilkan_identitas(nama, nomor, domisili, tanggal)

            zakat_emas = rumuszakat.hitung_zakat_emas(emas, harga_emas)
            zakat_perak = rumuszakat.hitung_zakat_perak(perak, harga_perak)

            if zakat_emas > 0:
                st.success(f"✅ Zakat emas: Rp {zakat_emas:,.0f}")
            else:
                st.warning("⚠️ Emas belum mencapai nisab (85 gram)")

            if zakat_perak > 0:
                st.success(f"✅ Zakat perak: Rp {zakat_perak:,.0f}")
            else:
                st.warning("⚠️ Perak belum mencapai nisab (595 gram)")

# ======================
# ZAKAT PENGHASILAN
# ======================
elif menu == "Zakat Penghasilan":
    st.header("Zakat Penghasilan")

    nama, nomor, domisili, tanggal = input_identitas()
    st.divider()

    income = st.number_input("Penghasilan", min_value=0.0, step=100_000.0)
    expenses = st.number_input("Pengeluaran", min_value=0.0, step=100_000.0)
    period = st.selectbox("Periode", ["Bulanan", "Tahunan"])

    if st.button("Hitung Zakat", key="btn_penghasilan"):
        if not validasi_identitas(nama, nomor, domisili):
            st.error("❗ Nama, Nomor HP, dan Domisili wajib diisi")
        else:
            tampilkan_identitas(nama, nomor, domisili, tanggal)

            hasil = rumuszakat.hitung_zakat_penghasilan(
                income, expenses, period
            )

            if hasil > 0:
                st.success(f"✅ Zakat yang harus dibayar: Rp {hasil:,.2f}")
            else:
                st.warning("⚠️ Penghasilan belum mencapai nisab")

# ======================
# ZAKAT PETERNAKAN
# ======================
elif menu == "Zakat Peternakan":
    st.header("Zakat Peternakan")

    nama, nomor, domisili, tanggal = input_identitas()
    st.divider()

    jenis = st.selectbox("Jenis ternak", ["Sapi / Kerbau", "Kambing / Domba"])
    jumlah = st.number_input("Jumlah ternak", min_value=0, step=1)

    if st.button("Hitung Zakat", key="btn_peternakan"):
        if not validasi_identitas(nama, nomor, domisili):
            st.error("❗ Nama, Nomor HP, dan Domisili wajib diisi")
        else:
            tampilkan_identitas(nama, nomor, domisili, tanggal)

            if jenis == "Sapi / Kerbau":
                hasil = rumuszakat.zakat_sapi(jumlah)
            else:
                hasil = rumuszakat.zakat_kambing(jumlah)

            if hasil:
                st.success(f"✅ Zakat yang harus ditunaikan: {hasil}")
            else:
                st.warning("⚠️ Jumlah ternak belum mencapai nisab")

# ======================
# FOOTER
# ======================
st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #0f172a;
        color: #f8fafc;
        text-align: center;
        padding: 10px 0;
        font-size: 14px;
        z-index: 100;
    }
    </style>

    <div class="footer">
        📞 <b>Kontak</b> : 085715118015 &nbsp; | &nbsp;
        📧 <b>Email</b> : farelzaghlul@gmail.com &nbsp; | &nbsp;
        📍 <b>Alamat</b> : STT Nurul Fikri
    </div>
    """,
    unsafe_allow_html=True
)
