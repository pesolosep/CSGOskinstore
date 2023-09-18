[!Link Aplikasi!] (https://pesolcsgoskinstore.adaptable.app/main)
# Tugas 2
Untuk Tugas 2 PBP, saya membuat aplikasi bertemakan website penjualan skin game yaitu CSGO. Aplikasi berjudul PESOl's CSGO Skin Store dapat dilihat pada [link ini] (https://pesolcsgoskinstore.adaptable.app/main).

#### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

1. Membuat sebuah proyek Django baru.

Pertama, saya membuat direktori dan menyiapkan *dependencies* pada `requirements.txt` untuk menyiapkan proyek Django.

Berikut adalah isi dari berkas `requirements.txt`.
```
django
gunicorn
whitenoise
psycopg2-binary
requests
urllib3
```
Install *dependencies* tersebut dengan perintah `pip install -r requirements.txt` pada *virtual environment*. Setelah itu, proyek dibuat dengan menjalankan perintah `django-admin startproject depoAMC .` dan mengunggahnya ke repositori GitHub baru.


2. Membuat aplikasi dengan nama main pada proyek tersebut.

Pada direktori `CSGOskinstore`, saya aktifkan *virtual environment* dan membuat aplikasi baru bernama `main` dengan perintah `python manage.py startapp main`. Daftarkan `main` ke dalam proyek dengan menambahkan `'main'` pada variabel `INSTALLED_APPS` yang berada di berkas `settings.py`.
```python
INSTALLED_APPS = [
    ...,
    'main',
    ...
]
```


3. Melakukan routing pada proyek agar dapat menjalankan aplikasi main.

Akan dilakukan *rendering* tampilan HTML dengan menggunakan data yang diberikan. Pada berkas `views.py` tambahkan `import render` dan fungsi `show_main` untuk menampilkan halaman `main.html` dengan kode dibawah ini.
```python
from django.shortcuts import render

def show_main(request):
    context = {
        'username': 'Muhammad Faishal Adly Nelwan',
        'class' :'PBP C',
        'name': 'Karambit Blue Gem',
        'type': 'Knife',
        'price' : 'Rp500.000.000,00',
        'amount' : '1',
        'description' : 'The rarest skin in CSGO, effect on using this skin is as follows:\n+25% aim\n +50 damage '
    }

    return render(request, "main.html", context)


4. Membuat model pada aplikasi main dengan nama Item dan memiliki atribut wajib sebagai berikut.
    - name sebagai nama item skin dengan tipe CharField
    - type sebagai tipe senjata skin  dengan tipe TextField
    - price sebagai nominal harga item skin dengan tipe IntegerField
    - amount sebagai jumlah stok item skin dengan tipe IntegerField
    - description sebagai deskripsi item skin dengan tipe TextField
    
Jika saya ingin menggunakan database, saya perlu membuat model yang akan menjadi penghubung antara Python dan database saya. Model ini akan berada di dalam file `models.py` di dalam aplikasi "main". Sebagai contoh, jika saya ingin membuat database yang berisi informasi tentang barang dengan atribut name, type, price, amount, dan description, saya dapat membuat model seperti ini:

```python
from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=255)
    type = models.TextField()
    price = models.IntegerField()
    amount =  models.IntegerField()
    description = models.TextField()
```

Namun, untuk menghubungkan model ini dengan tampilan, saya perlu melakukan lebih banyak konfigurasi yang akan dibahas dalam tutorial PBP selanjutnya.

5. Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.

```
```
Pada `main.html`, saya meletakkan variabel yang dapat digantikan oleh data yang telah diambil dari key dictionary function show_main `views.py` context pada seperti dibawah ini.
```
```
```html

<hr>
<p>Nama :</p>
<p>{{username}}</p>
<p>Class :</p>
<p>{{class}}</p>
<p></p>
<h5>Skin Name: </h5>
<p>{{name}}</p> 
<h5>Type: </h5>
<p>{{ type }}</p> 
<h5>Price: </h5>
<p>{{ price }}</p> 
<h5>Amount: </h5>
<p>{{ amount }}</p> 
<h5>Description: </h5>
<p>{{ description }}</p> 
```
```
```
6. Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.

Saya akan membuat berrkas `urls.py`pada aplikasi main yang akan bertanggung jawab untuk mengatur rute URL yang terkait dengan aplikasi main. Lalu saya kan mengimpor path dari django.urls untuk mendefinisikan pola URL. Lalu saya menggunakan fungsi show_main dari modul main.views sebagai tampilan yang akan ditampilkan ketika URL terkait diakses.
Nama app_name diberikan untuk memberikan nama unik pada pola URL dalam aplikasi.
```

```
```python
from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]
```

```
```
7. Melakukan deployment ke Adaptable terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet

```
```
Terakhir, jika saya ingin mendeploy proyek saya ke Adaptable, pastikan repositori proyek saya sudah berada di GitHub dan bersifat public. Selanjutnya, di Adaptable, pilih opsi "deploy a new app" dan pilih repositori yang sesuai dengan proyek yang akan saya deploy. Pilih template "Python App Template" dan tentukan jenis database yang saya inginkan, disini saya akan memilih "PostgreSQL".


Pastikan untuk sesuaikan versi Python dengan versi yang digunakan di lingkungan lokal saya dengan menjalankan `python --version` di terminal lokal. Selanjutnya, masukkan perintah `python manage.py migrate && gunicorn CSGOskinstore.wsgi`dimana CSGOskinstore itu nama repository ke dalam kolom "Start Command". Akhirnya, tentukan nama aplikasi saya dan centang opsi "HTTP Listener on PORT".

```
```
#### Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

![Alt text](/images/baganMVT.jpg)


Ketika ada permintaan dari luar, Django akan mencoba mencari pola URL yang ada dalam file urls.py. Setelah menemukan pola URL yang sesuai dengan yang telah kita tulis, Django akan mengakses fungsi yang sesuai dalam file views.py sesuai dengan pola URL yang dituju. Di dalam fungsi yang dipanggil, kita memiliki kemampuan untuk menulis, membaca, menghapus, dan memperbarui basis data. Setelah itu, kita dapat mengirimkan halaman HTML yang akan dirender oleh browser pengguna.

Virtual environment digunakan untuk mengisolasi dependensi proyek, mencegah konflik, menjaga kebersihan sistem, dan memungkinkan portabilitas. Meskipun mungkin bisa membuat aplikasi web Django tanpa virtual environment, secara umum virutal environment digunakan untuk mencegah masalah dependensi dan konflik.
#### Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

Virtual environment digunakan untuk mengisolasi dependensi proyek, mencegah konflik, menjaga kebersihan sistem, dan memungkinkan portabilitas. Meskipun mungkin bisa membuat aplikasi web Django tanpa virtual environment, secara umum virutal environment digunakan untuk mencegah masalah dependensi dan konflik.
#### Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya
- MVC (Model-View-Controller): Memisahkan data (Model), tampilan (View), dan logika pengendalian (Controller).
- MVT (Model-View-Template): Sama seperti MVC, dengan Template yang memisahkan tampilan.
- MVVM (Model-View-ViewModel): Memisahkan Model, tampilan (View), dan ViewModel yang menghubungkan keduanya, umumnya digunakan dalam - aplikasi UI dinamis seperti aplikasi mobile.
