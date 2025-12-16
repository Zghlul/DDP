import streamlit as st

st.sidebar.title ("Menu")
Menu = st.sidebar.radio ("---", ["Home","Zakat Simpanan", "Zakat Penghasilan", "Zakat Peternakan"])

# Menu navigasi
if Menu == "Home":
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

# ZAKAT SIMPANAN
elif Menu == "Zakat Simpanan":
    st.title("Menghitung zakat Simpanan, Emas Dan Perak 🪙")
    st.write ("Hitung zakat emas dan perak sesuai syari'at")
    st.write ('---')

    # Nama Muzzaki
    col1, col2 = st.columns(2)
    with col1 :
        nama = st.text_input ('Nama Muzzaki')
        nomor = st.text_input ('Nomor Hp')
    with col2 :
        domisili = st.text_input('Domisili')
        tanggal = st.date_input('tanggal')
    st.write ('---')

    # Harga emas dan perak
    harga_emas = st.number_input ('Masukan harga emas per gramm (Rp)', min_value=0, step=1000, format="%d")
    harga_perak = st.number_input ('Masukan harga perak Per gram (Rp)', min_value=0, step=1000, format="%d")

    # Masukan jumlah emas dan perak
    emas = st.number_input ('Jumlah Emas (gram)', min_value=0, step=1000, format="%d")
    perak = st.number_input ('Jumlah perak (gram)', min_value=0, step=1000, format="%d")

    # rumus : harga * berat * 2,5%

    if st.button ("Hitung Zakat") :
        nisab_emas = 85 # gram
        nisab_perak = 595 # gram
        total_emas = emas * harga_emas
        total_perak = perak * harga_perak

        # zakat yang di keluarkan
        zakat_emas = total_emas * 0.025 if emas >= nisab_emas else 0
        zakat_perak = total_perak * 0.025 if perak >= nisab_perak else 0

        st.subheader ('Hasil perhitungan')
        # emas
        if emas >= nisab_emas :
            st.success (f'Nama {nama}, Nomor hp {nomor}, Domisili {domisili}. ')
            st.success (f'✅ Di nyatakan bahwa Emas anda mencapai nisab. Jumlah Zakat emas yang harus dikeluarkan Rp {zakat_emas:,.0f}')
        else :
            st.success (f'Nama {nama}, Nomor hp {nomor}, Domisili {domisili}. ')
            st.warning (f'⚠️ Emas anda belom mencapai nisab (minimal 85 gram). Maka tidak wajib zakat')
        # perak
        if perak >= nisab_perak :
            st.success (f'Nama {nama}, Nomor hp {nomor}, Domisili {domisili}. ')
            st.success (f'✅ Perak Anda sudah mencapai nisab. Jumlah Zakat perak yang harus dikeluarkan Rp {zakat_perak:,.0f}')
        else :
            st.success (f'Nama {nama}, Nomor hp {nomor}, Domisili {domisili}. ')
            st.warning (f'⚠️ Perak Anda belom mencapai nisab (minimal 595 gram). Maka Tidak wajib zakat')

# ZAKAT PENGHASILAN    
elif Menu == 'Zakat Penghasilan':
    st.title('Menghitung zakat penghasilan atau profesi 💰')
    st.write ("Hitung zakat penghasilan (zakat profesi) dengan cepat. Zakat dihitung 2.5% dari penghasilan bersih tahunan jika melewati nisab (85 gram emas).")
    st.write ('---')

    # Nama Muzzaki
    col1, col2 = st.columns(2)
    with col1 :
        nama = st.text_input ('Nama Muzzaki')
        nomor = st.text_input ('Nomor Hp')
    with col2 :
        domisili = st.text_input('Domisili')
        tanggal = st.date_input('tanggal')
    st.write ('---')

    col1, col2 = st.columns(2)
    with col1 :
         # penghasilan perbulan dan tahunan
         income = st.number_input("Penghasilan (per periode)", min_value=0.0, step=10000.0, format="%.2f",
                             help="Masukkan jumlah penghasilan (gaji, honor, dsb) untuk periode yang dipilih")
    with col2 :
         # biaya hidup
         expenses = st.number_input("Biaya / kebutuhan pokok (per periode)", min_value=0.0, step=10000.0, format="%.2f",
                               help="Biaya hidup atau pengeluaran yang mengurangi penghasilan")
    
    period = st.selectbox("Periode input", options=["Bulanan", "Tahunan"], index=0,
                          help="Pilih apakah nilai diisi per bulan atau per tahun")
    # pengaturan nisab
    st.write ('---')
    st.header("Pengaturan Nisab")
    st.write("Nisab dihitung dari harga emas 85 gram nilai setara per tahun sekitar Rp 85.685.972 dan Rp 7.140.498 per bulan")
    per_bulan = 7140498
    per_tahun = 85685972

    # perhitungan
    PERIOD_MULTIPLIER = 12 if period == "Bulanan" else 1

    if st.button ("Hitung Zakat") :
        zakat = income - expenses
        penghasilan_bersih_pertahun = zakat * PERIOD_MULTIPLIER
        rumus_zakat = 0.025 # 2.5%

        zakat_tahunan = penghasilan_bersih_pertahun * rumus_zakat if per_tahun else 0.0
        zakat_per_periode = zakat_tahunan / PERIOD_MULTIPLIER

        st.subheader ('Hasil perhitungan')
        if penghasilan_bersih_pertahun >= per_tahun :
            st.success (f'Nama {nama}, Nomor hp {nomor}, Domisili {domisili}. ')
            st.success (f'✅ Zakat yang harus anda keluarkan sejumlah Rp {zakat_per_periode:,.2f}')
        else :
            st.success (f'Nama {nama}, Nomor hp {nomor}, Domisili {domisili}. ')
            st.warning (f'⚠️ Anda belum mencapai nisab seharga emas (85 gram)')
# zakat peternakan
elif Menu == "Zakat Peternakan":
    st.title ('Menghitung zakat peternakan kambing dan sapi 🐐')
    st.write ("Menghitung zakat ternakan sesuai syari'at")
    st.write ('---')

     # Nama Muzzaki
    col1, col2 = st.columns(2)
    with col1 :
        nama = st.text_input ('Nama Muzzaki')
        nomor = st.text_input ('Nomor Hp')
    with col2 :
        domisili = st.text_input('Domisili')
        tanggal = st.date_input('tanggal')
    st.write ('---')

    # jenis dan jumlah hewan
    jenis = st.selectbox (
        "pilih jenis ternak",
        ['Kambing / Domba', 'Sapi / Kerbau']
    )    
    jumlah = st.number_input ("Masukan jumlah ternak anda", min_value=0, step=1)

    # rumus zakat sapi dan kambing
    def zakat_sapi(jumlah):
        if jumlah < 30:
            return ""
        hasil = []
        sisa = jumlah
        jumlah_40 = sisa // 40
        sisa = sisa % 40

        jumlah_30 = sisa // 30
        sisa = sisa % 30 

        if jumlah_30 == 0 and jumlah_40 == 0:
            if 30 <= jumlah <= 39:
                return "1 ekor sapi / kerbau tabi umur 1 tahun"
            elif 40 <= jumlah <= 59:
                return "1 ekor sapi / kerbau musinnah umur 2 tahun"
            
        if jumlah_30 > 0:
            hasil.append(f"{jumlah_30} ekor sapi / kerbau tabi umur 1 tahun")

        if jumlah_40 > 0:
            hasil.append(f"{jumlah_40} ekor sapi / kerbau musinnah umur 2 tahun")
        return " dan" .join(hasil)

    def zakat_kambing(jumlah):
        if jumlah < 40:
            return ""
        elif 40 <= jumlah <= 120:
            return "1 ekor kambing / domba"
        elif 121 <= jumlah <= 200:
            return "2 ekor kambing / domba"
        elif 201 <= jumlah <= 300:
            return "3 ekor kambing / domba"
        elif 301 <= jumlah <= 400:
            return "4 ekor kambing / domba"
        else:
            tambahan = (jumlah - 401) // 100 + 1
            total = 4 + tambahan
            return f"{total} ekor kambing / domba umur 1 tahun"
        
    if st.button("Hitung Zakat"):
        if jenis == "Sapi / Kerbau":
            hasil = zakat_sapi(jumlah)
        elif jenis == "Kambing / Domba":
            hasil = zakat_kambing(jumlah)

        if hasil :
            st.success (f'Nama {nama}, Nomor hp {nomor}, Domisili {domisili}')
            st.success (f'✅ Zakat yang harus anda tunaikan adalah {hasil}')
        else:
            st.success (f'Nama {nama}, Nomor hp {nomor}, Domisili {domisili},')
            st.warning(f'⚠️ Maaf, hewan ternak anda belum mencapai nisab. Tidak wajib zakat')

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
