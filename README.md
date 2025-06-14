# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding

Jaya Jaya Institut merupakan salah satu institusi pendidikan perguruan yang telah berdiri sejak tahun 2000. Hingga saat ini ia telah mencetak banyak lulusan dengan reputasi yang sangat baik. Akan tetapi, terdapat banyak juga siswa yang tidak menyelesaikan pendidikannya alias dropout.

Jumlah dropout yang tinggi ini tentunya menjadi salah satu masalah yang besar untuk sebuah institusi pendidikan. Oleh karena itu, Jaya Jaya Institut ingin mendeteksi secepat mungkin siswa yang mungkin akan melakukan dropout sehingga dapat diberi bimbingan khusus.

Nah, sebagai calon data scientist masa depan Anda diminta untuk membantu Jaya Jaya Institut dalam menyelesaikan permasalahannya. Mereka telah menyediakan dataset yang dapat Anda digunaka
n. Selain itu, mereka juga meminta Anda untuk membuatkan dashboard agar mereka mudah dalam memahami data dan memonitor performa siswa.

### Permasalahan Bisnis

1. Apa saja faktor yang mempengaruhi status mahasiswa itu Droput?
2. Bagaimana cara mengatasi tingginya Droput pada Jaya Jaya Institut?
3. Bagaimana cara memprediksi status mahasiswa (DropOut, Graduated, Enrolled) pada Jaya jaya Institut?

### Cakupan Proyek

1. Mengetahui faktor apa saja yang mempengaruhi droput pada Jaya Jaya Institut
2. Mendapatkan solusi untuk mengatasi mahasiswa droput pada Jaya Jaya Institut
3. Mampu memprediksi status mahasiswa (DropOut, Graduated, Enrolled) pada Jaya jaya Institut

### Persiapan

Sumber data: (https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/refs/heads/main/students_performance/data.csv)

Setup environment:
Install library atau modul menggunakan file _requirements.txt_

```
pip install -r requirements.txt
```

Lalu, jalankan cell dalam notebook secara berurutan

## Business Dashboard

### Menjalankan Dashboard Metabase

Import file metabase yang ada di dalam folder submission

Email : example123@test.com <br>
Pass: gqChaq022ET_Wn

## Menjalankan Sistem Machine Learning

Pertama, Install library atau modul menggunakan file _requirements.txt_

```
pip install -r requirements.txt
```

Kedua, Jalankan script pythonnya:

```
streamlit run students_scoring_app.py
```

Selanjutnya bukalah aplikasi sederhana tersebut menggunakan alamat http://localhost:8501/ atau lihatlah pada terminal menyesuaikan komputer/laptop masing-masing

Lalu, masukkan inputan yang di minta dan tekan predict, maka akan muncul hasil prediksinya

adapun link streamlit cloudnya:
https://studentsperformanceprediction-fathir.streamlit.app/

## Conclusion

Dari hasil EDA, didapatkan beberapa hal berikut:

1. Mahasiswa droput cenderung memiliki nilai ujian masuk dan nilai ujian sebelumnya lebih rendah dari mahasiswa dengan status graduated dan enrolled.
2. mahasiswa droput itu dominasinya berstatus single, tidak memegang beasiswa, bukan mahasiswa intenational, tidak memerlukan perhatian edukasi khusus
3. Selain itu, mahasiswa droput memiliki proporsi mahasiswa displaced(pindahan) terbanyak, pproporsi pembayaran tuition yang tidak tepat terbanyak dibanding yang lain(meskipun pembayaran tepat waktu)

Selanjutnya dari hasil ektrak feature importance model prediksi, umur dan grade menjadi top variabel yang berpengaruh di model.

### Rekomendasi Action Items (Optional)

Berikan beberapa rekomendasi action items yang harus dilakukan Institusi guna menyelesaikan permasalahan atau mencapai target mereka.

1. Memberikan perhatian khusus kepada mahasiswa yang memiliki nilai yang rendah, perlu ditelusuri alasan dan memberikan solusi atau bantuan jika diperlukan
2. Karna didominasi oleh mahasiswa lokal, perlu dikaji lebih lanjut alasannya mungkin dengan melakukan survei khusus untuk mahasiswa lokal yang droput untuk mengetahui alasan lebih detail
3. Memberi alert kepada mahasiswa yg membayar tuition yang tidak tepat waktu. perlu ditanya alasannya lebih detail
4. Membuka forum atau diskusi internal institusi untuk lebih memperdalam permasalahan ini dengan berdasarkan hasil analisis data ini
