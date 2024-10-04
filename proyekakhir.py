import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Fungsi untuk menampilkan total penggunaan sepeda berdasarkan hari kerja dan akhir pekan
def show_weekday_vs_weekend_chart(day_bike):
    # Menambahkan kolom baru yang menunjukkan apakah hari tersebut weekday atau weekend
    day_bike['is_weekend'] = day_bike['weekday'].apply(lambda x: 'Weekend' if x == 0 or x == 6 else 'Weekday')

    # Mengelompokkan data berdasarkan weekday dan weekend dan menghitung total dan rata-rata penggunaan sepeda
    usage_by_day_type = day_bike.groupby('is_weekend')['cnt'].agg(['sum', 'mean']).reset_index()

    # Membuat bar chart untuk total penggunaan sepeda di weekday dan weekend
    fig, ax = plt.subplots()
    ax.bar(usage_by_day_type['is_weekend'], usage_by_day_type['sum'], color=['blue', 'green'])

    # Menambahkan judul dan label
    ax.set_title('Perbandingan Total Penggunaan Sepeda: Hari Kerja vs Akhir Pekan', fontsize=16)
    ax.set_xlabel('Jenis Hari', fontsize=12)
    ax.set_ylabel('Total Penggunaan Sepeda', fontsize=12)
    st.pyplot(fig)

    # Penjelasan di bawah chart
    st.markdown("""
    **Penjelasan:**
    Dari chart di atas, dapat dilihat bahwa total penggunaan sepeda pada hari kerja (Weekday) cenderung lebih tinggi dibandingkan dengan akhir pekan (Weekend). Meskipun penggunaan sepeda lebih banyak di hari kerja, rata-rata penggunaan per hari lebih rendah. Di sisi lain, meskipun jumlah pengguna pada akhir pekan lebih sedikit, mereka yang menggunakan sepeda lebih cenderung menghabiskan waktu lebih lama.
    """)

# Fungsi untuk menampilkan penjualan sepeda berdasarkan musim
def show_sales_by_season_chart(day_bike):
    # Mengelompokkan data berdasarkan musim dan menghitung total penjualan (cnt)
    sales_by_season = day_bike.groupby('season')['cnt'].sum().reset_index()

    # Membuat bar chart untuk total penjualan berdasarkan musim
    fig, ax = plt.subplots()
    ax.bar(sales_by_season['season'], sales_by_season['cnt'], color='purple')

    # Menambahkan judul dan label
    ax.set_title('Total Penjualan Sepeda Berdasarkan Musim', fontsize=16)
    ax.set_xlabel('Musim', fontsize=12)
    ax.set_ylabel('Total Penjualan (cnt)', fontsize=12)
    ax.set_xticks(sales_by_season['season'])
    ax.set_xticklabels(['Spring', 'Summer', 'Fall', 'Winter'])

    st.pyplot(fig)

    # Penjelasan di bawah chart
    st.markdown("""
    **Penjelasan:**
    Dari chart di atas, kita dapat melihat bahwa penjualan sepeda paling tinggi terjadi pada musim panas, sementara musim dingin menunjukkan angka penjualan yang paling rendah. Hal ini mungkin disebabkan oleh faktor cuaca, di mana orang lebih cenderung menggunakan sepeda saat cuaca hangat. Musim semi dan gugur menunjukkan penjualan yang baik, tetapi tidak setinggi musim panas.
    """)

# Fungsi untuk menampilkan halaman Beranda
def show_homepage():
    st.subheader("Selamat Datang di Beranda Dashboard")
    st.write(""" 
    Dashboard ini bertujuan untuk memberikan gambaran tentang penggunaan sepeda berdasarkan data historis. 
    Anda dapat melihat perbandingan penggunaan sepeda di hari kerja dan akhir pekan, serta penjualan sepeda berdasarkan musim.
    """)

    # Membaca dataset day.csv
    day_bike = pd.read_csv('day.csv')
    st.write("### Data dari day.csv")
    st.dataframe(day_bike)

    # Membaca dataset hour.csv
    hour_bike = pd.read_csv('hour.csv')
    st.write("### Data dari hour.csv")
    st.dataframe(hour_bike)

# Fungsi untuk menampilkan kesimpulan dengan pertanyaan dan jawaban
def show_conclusion():

    
    # Pertanyaan pertama
    st.write(""" 
    **1. Apakah ada perbedaan signifikan antara total penggunaan sepeda pada hari kerja dibandingkan dengan akhir pekan (weekday vs weekend)?**
    """)
    st.markdown(""" 
    <p style='font-size: 12px;'>
    Hari kerja cenderung memiliki jumlah pengguna yang lebih banyak secara total, tetapi penggunaan rata-rata per hari lebih rendah. Akhir pekan memiliki lebih sedikit pengguna secara total, tetapi pengguna yang ada lebih banyak menghabiskan waktu menggunakan sepeda, yang terlihat dari rata-rata penggunaan yang lebih tinggi.
    </p>
    """, unsafe_allow_html=True)
    
    # Pertanyaan kedua
    st.write(""" 
    **2. Saat musim apa penjualannya bisa meningkat drastis?**
    """)
    st.markdown(""" 
    <p style='font-size: 12px;'>
    Musim panas merupakan musim dengan tingkat penjualan sepeda yang paling tinggi. Musim dingin merupakan musim dengan penjualan sepeda paling rendah, yang mungkin disebabkan oleh cuaca yang kurang mendukung. Penjualan di musim semi dan gugur cukup baik tetapi tidak setinggi di musim panas. Data ini mengindikasikan bahwa musim dan cuaca memiliki pengaruh yang signifikan terhadap pola penjualan sepeda.
    </p>
    """, unsafe_allow_html=True)

# Main function untuk menjalankan Streamlit
def main():
    # Membaca dataset
    day_bike = pd.read_csv('day.csv')
    day_bike['dteday'] = pd.to_datetime(day_bike['dteday'])

    # Pilihan visualisasi
    st.sidebar.title("Navigasi")
    option = st.sidebar.selectbox(
        'Pilih Halaman',
        ['Beranda', 
         'Visualisasi Perbandingan Penggunaan: Weekday vs Weekend', 
         'Visualisasi Penjualan berdasarkan Musim', 
         'Kesimpulan']
    )

    # Halaman Beranda
    if option == 'Beranda':
        show_homepage()
    # Halaman Weekday vs Weekend
    elif option == 'Visualisasi Perbandingan Penggunaan: Weekday vs Weekend':
        st.subheader("Visualisasi Perbandingan Penggunaan: Weekday vs Weekend")  # Judul halaman kedua
        show_weekday_vs_weekend_chart(day_bike)
    # Halaman Penjualan Berdasarkan Musim
    elif option == 'Visualisasi Penjualan berdasarkan Musim':
        st.subheader("Visualisasi Penjualan berdasarkan Musim")  # Judul halaman ketiga
        show_sales_by_season_chart(day_bike)
    # Halaman Kesimpulan
    elif option == 'Kesimpulan':
        st.subheader("Kesimpulan")  # Judul halaman keempat
        show_conclusion()

# Jalankan aplikasi streamlit
if __name__ == "__main__":
    main()
