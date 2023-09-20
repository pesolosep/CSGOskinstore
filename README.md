[!Link Aplikasi!] (https://pesolcsgoskinstore.vercel.app/)


</details>
Tugas 2
<details>


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
    skinType = models.TextField("-")
    price = models.IntegerField(default = 0)
    amount =  models.IntegerField(default = 0)
    tradeLink = models.TextField(default ="")
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
7. Melakukan deployment ke Digital Ocean terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet

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










</details>
Tugas 3
<details>

# Cara Implementasi

## Mengganti SQL menjadi PostgreSQL
Karena saya tidak isi form untuk memakai PaaS Fasilkom, maka saya harus deploy melalui PaaS lain :D. Platform yang saya akan pakai adalah `vercel.app` . Untuk memakai platform tersebut, saya perlu membuat database SQL terbaru memakai `railway.app` . Disitu saya akan mendapat database Postgres pribadi, dari situ saya akan mengconnect nya dengan mengubah variabel `DATABASE` pada `settings.py` .

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'railway',
        'USER' : 'postgres',
        'PASSWORD' : 'RNyPzc7grbq4ifbXtAmO',
        'HOST' : 'containers-us-west-39.railway.app',
        'PORT' : '6005'
    }
}
```

Dengan mengubah database saya, saya bisa mendeploy deh project ini ke vercel :D .
## Membuat Form (`forms.py`)

`APP/forms.py` akan mengimplementasikan library `django.forms`, dimana akan digunakan untuk proses pembuatan form kita (pesanan baru dalam konteks website). Seluruh html sudah dihandle oleh library form tersebut. Isi `APP/forms.py` dari aplikasi saya adalah.
```python
from main.models import Item
class ItemForm(ModelForm):
    class Meta:
        model = Pesanan 
        fields = ["name", "skinType","amount","description"]
```
dimana `name`, `skinType`, `amount`, dan `description` adalah field yang ada pada model `Pesanan` yang sudah didefinisikan.

## Merender form yang dibuat

Untuk merender form yang sudah kita buat, kita dapat menggunakan kemudahan library django. Pada `html` yang akan kita buat, kita dapat menulis.
```html
<form method="POST">
    {% csrf_token %}
    <table>
        {{ form.as_table }}
        <tr>
            <td></td>
            <td>
                <input type="submit" value="Add Pesanan"/>
            </td>
        </tr>
    </table>
</form>
```
`csrf_token` token wajib didefinisikan setiap definisi form, hal ini terkait dengan keamanan. `form.as_table` akan merender form secara keseluruhan kecuali button submit yang perlu kita tulis sendiri (tulisan button kita buat pada main.html).

## Menambah estetik pada tampilan produk dan tabel pesanan

Saya menggunakan tag </style> untuk menambahkan gaya dalam elemen tampilan produk yaitu skin dan tabel pesanannya melalui kode berikut:

```html
 <style>
        body {
           font-family: Arial, sans-serif;
           
       }

       h1 {
           text-align: center;
           margin-top: 20px;
       }
       
       .product-info {
           display: flex;
           justify-content: center;
           align-items: center;
           padding: 20px;
           border-radius: 50px;
           box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
           margin-bottom: 20px;
           background-color: #f9f9f9;

       }

       .product-details {
           margin-left: 20px;
           font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
           font-size: large;
       }

       .product-info img {
           max-width: 200px;
           height: auto;
       }

       table {
           width: 100%;
           border-collapse: collapse;
           margin-bottom: 20px;
       }

       /* Styling header tabel */
       th {
           background-color: #f2f2f2;
           text-align: left;
           padding: 8px;
       }

       /* Styling sel pada tabel */
       td {
           padding: 8px;
           border-bottom: 1px solid #ddd;
       }

       /* Styling the "Add New Product Button"*/
       .center-button {
           display: flex;
           justify-content: center;
           align-items: center;
           margin-top: 20px;
       }

       .rounded-button {
           background-color: #008CBA;
           color: white;
           border: none;
           padding: 10px 20px;
           cursor: pointer;
           border-radius: 15px; 
           text-decoration: none; 
       }

       /* Efek Hover pada bagian button*/
       .rounded-button:hover { 
           background-color: #005f7f;
       }
       
   </style>
```

lalu untuk command menampilkan dalam produknya saya memakai tag <\div> untuk menandakan class apa yang saya pakai untuk menampilkan elemen-elemen pada halamannya. Berikut kodenya:

```html
<div class="container"></div>
<div class="product-info">
    <img src="https://www.simpleimageresizer.com/_uploads/photos/a38db52e/blue-gem-karambit_500x281.jpg" width="350">
    <div class="product-details">
<h5>Skin Name: </h5>
<p>Karambit Blue Gem</p> 
<h5>Type: </h5>
<p>Knife</p> 
<h5>Price: </h5>
<p>Rp5.000.000,00</p> 
<h5>Description: </h5>
<p>The rarest knife skin in CSGO, effect on using this skin is as follows: +25% aim +50 damage</p>

</div>
</div>

<div class="product-info">
    <img src="https://www.simpleimageresizer.com/_uploads/photos/a38db52e/fire_serpent_ak_1_500x281.jpeg" width="350">
    <div class="product-details">
<h5>Skin Name: </h5>
<p>AK-47 Fire Serpent</p> 
<h5>Type: </h5>
<p>Rifle</p> 
<h5>Price: </h5>
<p>Rp1.000.000,00</p> 
<h5>Description: </h5>
<p>Shroud's Skin, therefore giving you his skills: +50% aim reflex +30% spray control</p> 
</div>
</div>
</div>

<h1>Total skin orders : {{totalPesanan}}</h1>
<table>
    <tr>
        <th>Name</th>
        <th>Skin type</th>
        <th>Amount</th>
        <th>Steam link</th>
        <th>Date Added</th>
    </tr>

    {% comment %} Berikut cara memperlihatkan data produk di bawah baris ini {% endcomment %}

    {% for pesanan in pesanans %}
        <tr>
            <td>{{pesanan.name}}</td>
            <td>{{pesanan.skinType}}</td>
            <td>{{pesanan.amount}}</td>
            <td>{{pesanan.tradeLink}}</td>
            <td>{{pesanan.date_added}}</td>
        </tr>
    {% endfor %}
</table>

<br />
<div class="center-button">
    <a href="{% url 'main:create_product' %}" class="rounded-button">Make Order</a>
</div>
```
## Menambahkan view untuk serializer json dan xml

Serializer digunakan untuk mengirim data dalam bentuk `json` dan `xml`. Data ini dapat digunakan sebagai interface program lain (API). Dalam django, serializer diimplementasikan pada `views.py` dengan mereturn `HTTPResponse` dengan `application_type` `application/json` atau `application/xml`. Berikut contoh kodenya.
```python
from django.core import serializers
from main.models import Item
def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize('xml', data), content_type='application/xml')
```
```python
def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize('json', data), content_type='application/json')
```

## Membuat getter dengan dynamic routing

Dynamic routing digunakan untuk menyesuaikan data dengan input dari user melalui url. Contoh, jika kita ingin mendapatkan `Pesanan` **pertama** pada database kita dapat menuju url `www.outapp/1`. Implementasinya pada django dengan mengubah `urls.py` dan `views.py`. Pada `urls.py`
```python
from django.urls import path

urlpatterns = [
    ...
    path('xml/<int:id>', views.show_xmlbyid, name='xmlbyid'),
    path('json/<int:id>', views.show_jsonbyid, name='jsonbyid'),
]
```
Sedangkan pada `views.py`
```python
def show_xmlbyid(request, id: int):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize('xml', data), content_type='application/xml')

def show_jsonbyid(request, id: int):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize('json', data), content_type='application/json')
```

## Perbedaan antara POST dan GET pada Django?

**POST** adalah methodn protokol `HTTP` yang berfokus pada pengiriman data kepada server. Pengiriman data pada `POST` dikirim melalui body request `HTTP` sehingga tidak terlihat dalam `url` dan membuat datannya tidak mudah terlihat. `POST` biasanya digunakan saat melakukan update data kepada server seperti *sign up*, upload file, dan sebagainya

**Get** adalah method protokol `HTTP` yang fokus pada mengambil data dari server, misal seperti membuka laman website. Data yang dikirim akan disimpan pada `url` yang dituju. Contoh pemakaian `GET` adalah ketika kita ingin membuka website youtube misalnya, maka kita akan mengetik url youtube pada browser kita `youtube.com` , tetapi ketika kita ingin sign in account itu akan memakai metode `POST` karena data diri kita tidak akan terlihat di `URL` websitenya.

## Perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?

**HTML** digunakan untuk membuat peletakan desain kepada suatu halaman web. `HTML` lebih cocok jika client adalah manusia yang menggunakan browser (karena tampilannya mudah dibaca oleh manusia). Jika client merupakan sebuah applikasi untuk mengambil data otomatis (API), `HTML` akan lebih susah dipahami karena diperlukan parsing terlebih dahulu yang memakan waktu dan tidak efisien.
```html
<!DOCTYPE html>
<html lang="en">

<head>
	<meta charset="UTF-8" />
	<meta name="viewport" content="width=device-width, initial-scale=1.0" />


</head>

<body>
    ....
```

**XML** adalah format yang machine & human readable tidak seperti `HTML`. Struktur `XML` mirip seperti `tree` yang memiliki satu root. Struktur `XML` sangat mirip dengan `HTML` pada dasarnya. Setiap `node` pada `tree` ditandai  dengan symbol `<>`. Setiap node dapat memiliki banyak `properti`. Karena format `XML` yang machine readable, `XML` sering dijadikan opsi untuk mengirim data sebagai **API**.
```xml
<django-objects version="1.0">
<object model="main.pesanan" pk="1">
<field name="name" type="CharField">Karambit Blue Gem</field>
<field name="date_added" type="DateField">2023-09-18</field>
<field name="skinType" type="TextField">-</field>
<field name="amount" type="IntegerField">0</field>
<field name="tradeLink" type="TextField">-</field>
</object>
<object model="main.pesanan" pk="2">
<field name="name" type="CharField">pesol</field>
<field name="date_added" type="DateField">2023-09-19</field>
<field name="skinType" type="TextField">-</field>
<field name="amount" type="IntegerField">0</field>
<field name="tradeLink" type="TextField">-</field>
</object>
<object model="main.pesanan" pk="3">
<field name="name" type="CharField">Faishal Nelwan</field>
<field name="date_added" type="DateField">2023-09-19</field>
<field name="skinType" type="TextField">-</field>
<field name="amount" type="IntegerField">0</field>
<field name="tradeLink" type="TextField">-</field>
</object>
<object model="main.pesanan" pk="4">
<field name="name" type="CharField">Ak-47 Fire Serpent</field>
<field name="date_added" type="DateField">2023-09-20</field>
<field name="skinType" type="TextField">Rifle</field>
<field name="amount" type="IntegerField">1</field>
<field name="tradeLink" type="TextField">-</field>
</object>
</django-objects>
``` 

**JSON** adalah format machine & human readable. Format json adalah format yang paling sering digunakan baru-baru ini. Salah satu alasannya adalah dikarenakan simplisitasnya. Json tidak memakan banyak tempat sehingga sangat mudah untuk dibaca manusia. Container pada json yang menggunakan `Dictionary` dan `List` membuatnya sangat mudah untuk dibaca mesin/programmer API.
```json
[{"model": "main.pesanan", "pk": 1, "fields": {"name": "Karambit Blue Gem", "date_added": "2023-09-18", "skinType": "-", "amount": 0, "tradeLink": "-"}}, {"model": "main.pesanan", "pk": 2, "fields": {"name": "pesol", "date_added": "2023-09-19", "skinType": "-", "amount": 0, "tradeLink": "-"}}, {"model": "main.pesanan", "pk": 3, "fields": {"name": "Faishal Nelwan", "date_added": "2023-09-19", "skinType": "-", "amount": 0, "tradeLink": "-"}}, {"model": "main.pesanan", "pk": 4, "fields": {"name": "Ak-47 Fire Serpent", "date_added": "2023-09-20", "skinType": "Rifle", "amount": 1, "tradeLink": "-"}}]
```

## Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?

**JSON** sering digunakan sebagai pertukaran data antar applikasi (API) dikarenakan sifatnya yang machine readable. Pada `JSON`, terdapat `dictionary` dan `list` sebagai kontrainer yang merupakan container yang sering dipakai oleh para pemrogram. Penulisan **JSON** lebih singkat dibandingkan `XML` membuatnya efisien secara ukuran dan lebih human readable. 

# Screenshot Postman

Gambran untuk response untuk endpoint `html`
<div style='display: flex;'>
    <img src='https://user-images.githubusercontent.com/108632813/269089388-35ada54a-d371-4d8f-a3e4-20ea049657bf.png' width=70%>
</div>

Gambaran untuk response untuk endpoint `/xml` dan `/xml/4`
<div style='display: flex;'>
    <img src='https://user-images.githubusercontent.com/108632813/269088368-aff20ebf-de5f-4310-ae1b-e87ab183a35f.png' width=70%>
    <img src='https://user-images.githubusercontent.com/108632813/269089677-71e9af26-2bf7-48a2-a089-97fa78f5b7aa.png' width=70%>
</div>

Gambaran untuk response untuk endpoint `/json` dan `/json/4`
<div style='display: flex;'>
    <img src='https://user-images.githubusercontent.com/108632813/269088162-59eb3bc6-f624-4368-b43f-77e53b3270a1.png' width=70%>
    <img src='https://user-images.githubusercontent.com/108632813/269089744-39c11bd0-165a-4482-b26e-655cc437bed0.png' width=70%>
</div>

