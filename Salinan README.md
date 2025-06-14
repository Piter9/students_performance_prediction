# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding

Jaya Jaya Maju merupakan salah satu perusahaan multinasional yang telah berdiri sejak tahun 2000. Ia memiliki lebih dari 1000 karyawan yang tersebar di seluruh penjuru negeri.

Walaupun telah menjadi menjadi perusahaan yang cukup besar, Jaya Jaya Maju masih cukup kesulitan dalam mengelola karyawan. Hal ini berimbas tingginya attrition rate (rasio jumlah karyawan yang keluar dengan total karyawan keseluruhan) hingga lebih dari 10%.

Untuk mencegah hal ini semakin parah, manajer departemen HR ingin meminta bantuan Anda mengidentifikasi berbagai faktor yang mempengaruhi tingginya attrition rate tersebut. Selain itu, ia juga meminta Anda untuk membuat business dashboard untuk membantunya memonitori berbagai faktor tersebut. Selain itu, mereka juga telah menyediakan dataset yang dapat Anda gunakan

### Permasalahan Bisnis

1. Apa saja faktor yang mempengaruhi tingginya attrition rate pada perusahaan Jaya Jaya Maju?
2. Bagaimana cara mengatasi tingginya attrition rate pada perusahaan Jaya Jaya Maju?

### Cakupan Proyek

1. Mengetahui faktor apa saja yang mempengaruhi tingginya attrition rate pada perusahaan Jaya Jaya Maju?
2. Mendapatkan solusi untuk mengatasi tingginya attrition rate pada perusahaan Jaya Jaya Maju

### Persiapan

Sumber data: (https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/refs/heads/main/employee/employee_data.csv')

Setup environment:
Install library atau modul menggunakan file _requirements.txt_

```
pip install -r requirements.txt
```

Lalu, jalankan cell dalam notebook secara berurutan

#### Menjalankan Model Prediksi

Pertama, Install library atau modul menggunakan file _requirements.txt_

```
pip install -r requirements.txt
```

Kedua, Jalankan script pythonnya:

```
python script_model.py
```

Selanjutnya bukalah aplikasi sederhana tersebut menggunakan alamat http://127.0.0.1:5000/ atau lihatlah pada terminal

Lalu, masukkan inputan yang di minta dan tekan predict, maka akan muncul hasil prediksinya

## Business Dashboard

### Menjalankan Dashboard Metabase

Import file metabase yang ada di dalam folder submission

Email : fathirmaula89@gmail.com <br>
Pass: gqChaq022ET_Wn

## Conclusion

Dari hasil EDA, didapatkan beberapa hal berikut:

1. Poin Satisfaction, baik itu environment, job maupun relationship. Menunjukkan trend dimana pekerja terindikasi attrition (keluar) itu memiliki skor saatisfaction yang rendah.
2. Kebanyakan yang attrition itu berstatus single dan Laki-laki
3. Pegawai yang terindikasi attrition memiliki rata-rata monthly income yang rendah dibanding yang tidak attritition

Selanjutnya dari hasil ektrak feature importance model prediksi, Tampak Montly income memiliki pengaruh tertinggi, diikuti oleh skor satisfaction dan status pernikahan.

### Rekomendasi Action Items (Optional)

Berikan beberapa rekomendasi action items yang harus dilakukan perusahaan guna menyelesaikan permasalahan atau mencapai target mereka.

1. Pertimbangkan lagi atau lakukan kajian ulang tentang upah untuk setiap pegawai
2. Menelusuri lebih lanjut alasan mengapa beberapa pegawai memiliki skor kepuasan yang rendah
3. Membuka forum atau diskusi internal perusahaan untuk lebih memperdalam permasalahan ini dengan berdasarkan hasil analisis data ini
