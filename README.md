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

</details>
Tugas 4
<details>

# Implementasi step by step
 **Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna mengakses aplikasi dengan data pribadi**

  1. **Registrasi**

Buka file `views.py` yang ada di folder `main` dan buat fungsi baru dengan nama `register` dan memiliki parameter `request`. Lalu import `redirect`, `UserCreationForm`, dan `messages`. Kita bisa buat fungsi `register` untuk membuat user baru dengan isi:
    
    ```python
    def register(request):
      form = UserCreationForm()

      if request.method == "POST":
          form = UserCreationForm(request.POST)
          if form.is_valid():
              form.save()
              messages.success(request, 'Your account has been successfully created!')
              return redirect('main:login')
      context = {'form':form}
      return render(request, 'register.html', context)
    ```
`form = UserCreationForm(request.POST)` untuk membuat variabel `form` yang dimana ia adalah hasil dari method built-in Django yaitu `UserCreationForm` . Setelah user berhasil mendaftar, user akan kembali dari halaman register, jadi, kita menambahkan kode `return redirect('main:show_main')`.

Halaman register akan kita buat dengan file `register.html` yang ada di folder `main/templates`.

    ```html
    {% extends 'base.html' %}
    
    {% block meta %}
        <title>Register</title>
    {% endblock meta %}
    
    {% block content %}  
    
    <div class = "login">
    
          <h1>Register</h1>  
    
            <form method="POST" >  
                {% csrf_token %}  
                <table>  
                    {{ form.as_table }}  
                    <tr>  
                        <td></td>
                        <td><input type="submit" name="submit" value="Daftar"/></td>  
                    </tr>  
                </table>  
            </form>
    
        {% if messages %}  
            <ul>   
                {% for message in messages %}  
                    <li>{{ message }}</li>  
                    {% endfor %}  
            </ul>   
        {% endif %}
    
    </div>  
    
    {% endblock content %}
    ```
Tambahkan path url milik halaman register ke file `urls.py` pada direktori `main` dengan mengimpor fungsi `register` dari `views.py` dan tambahkan `path('register/', register, name='register')` pada variabel `urlpatterns`.


  2. **Login**

    Tetap di file yang sama kita akan buat fungsi baru dengan nama `login_user` yang menerima parameter `request` juga. Lalu impor `login` dari `authenticate`. Fungsi `login` ini untuk mengakses app sesuai dari info user yang dibuat dari `registrasi`.
    ```
    def login_user(request):
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('main:show_main')
            else:
                messages.info(request, 'Sorry, incorrect username or password. Please try again.')
        context = {}
        return render(request, 'login.html', context)
    ```
    `authenticate(request, username=username, password=password` berguna untuk melakukan autentikasi user dengan menggunakan username dan password yang diterima dari `request` yang dikirim user saat ingin login.
    Halaman login akan kita buat dengan file `login.html` yang ada di folder `main/templates` dengan isi:
    ```
    {% extends 'base.html' %}
    
    {% block meta %}
        <title>Login</title>
    {% endblock meta %}
    
    {% block content %}

    <div class = "login">
    
        <h1>Login</h1>
    
        <form method="POST" action="">
            {% csrf_token %}
            <table>
                <tr>
                    <td>Username: </td>
                    <td><input type="text" name="username" placeholder="Username" class="form-control"></td>
                </tr>
                        
                <tr>
                    <td>Password: </td>
                    <td><input type="password" name="password" placeholder="Password" class="form-control"></td>
                </tr>
    
                <tr>
                    <td></td>
                    <td><input class="btn login_btn" type="submit" value="Login"></td>
                </tr>
            </table>
        </form>
    
        {% if messages %}
            <ul>
                {% for message in messages %}
                    <li>{{ message }}</li>
                {% endfor %}
            </ul>
        {% endif %}     
            
        Don't have an account yet? <a href="{% url 'main:register' %}">Register Now</a>
    
    </div>

    {% endblock content %}
    ```

Tambahkan path url halaman login seperti cara pada tahap `register`.

  3. **Logout**
    
Buka file `views.py` yang ada di folder `main` dan buat fungsi baru dengan nama `logout_user` yang menerima parameter `request`. Lalu impor `logout`. Isi dari fungsi `logout_user` adalah:

    ```python

    def logout_user(request):
        logout(request)
        return redirect('main:login')

    ```
`logout(request)` akan menghapus sesi pengguna yang saat ini sudah masuk. Lalu user akan kembali ke halaman login dengan `return redirect('main:login')`.

Tambahkan:

    ```html
    ...
    <a href="{% url 'main:logout' %}">
        <button>
            Logout
        </button>
    </a>
    ...

    ```

Setelah hyperlink tag untuk Add New Product yang ada di file `main.html`.
Tambahkan path url milik halaman logout ke file `urls.py` pada direktori `main` dengan mengimpor fungsi `logout_user` dari `views.py` dan tambahkan `path('logout/', logout_user, name='logout')` pada variabel `urlpatterns`.

### Testing Dummy Account

 Membuat 3 akun melalui `Register Now` pada halaman login dan mengisi data `Skin Order` melalui `Make Order` pada halaman main masing akun 3 kali.

-  **Menghubungkan model Item dengan User**

  Buka `models.py` yang ada di direktori `main` lalu impor `User` dari `django.contrib.auth.models`. Pada model `Product` yang ada tambahkan kode 

  ```python
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  ``` 
  untuk menghubungkan data model dengan user (relationship).
  
    ```python
    class Pesanan(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        ...
    ```
  
  Buka `views.py` yang ada di direktori `main` dan modifikasi fungsi `create_product` menjadi:

    ```python
    def create_product(request):
    form = PesananForm(request.POST or None)
    
    if form.is_valid() and request.method == "POST":
      product = form.save(commit=False)
      product.user = request.user
      product.save()
      return HttpResponseRedirect(reverse('main:show_main'))
    ...
    ```

  `commit=False` berfungsi supaya Django tidak langsung menyimpan objek yang dibuat dari form ke database sehingga kita dapat memodifikasi objek tersebut dahulu. Kita mengisi field `user` dengan objek `User` dari return nilai `request.user` yang sudah terautentikasi untuk menandakan bahwa objek tersebut milik pengguna yang sedang login.
  Ubah fungsi `show_main` menjadi:

    ```python
    def show_main(request):
        pesanans = Pesanan.objects.filter(user=request.user)
    
        context = {
            'name': request.user.username,
        ...
        }
    ...
    ```

  Hal ini dilakukan agar objek `Pesanan` yang terasosiasi dengan user yang sedang login dapat ditampilkan. Kita menyaring seluruh objek dan hanya mengambil `Product` yang field `user` terisi dengan objek `User` yang sama dengan user yang sedang login. Untuk menampilkan username user yang login pada halaman main kita menggunakan `request.user.username`.
  Kita lakukan migrasi model dengan `python manage.py makemigration`.

-  **Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi**

  Buka file `views.py` yang ada di direktori `main` dan impor `HttpResponseRedirect`, `reverse`, dan `datetime`. Kita tambahkan fungsi untuk menambahkan cookie yang bernama `last_login` pada fungsi `login_user`, fungsi `last_login` digunakan untuk mengetahui kapan terakhir kali user login. Cara ini dilakukan dengan mengganti kode yang ada pada conditional `if user is not None` menjadi:

   ```
   ...
   if user is not None:
       login(request, user)
       response = HttpResponseRedirect(reverse("main:show_main")) 
       response.set_cookie('last_login', str(datetime.datetime.now()))
       return response
   ...
   ```

  `login(request, user)` berguna supaya logint terlebih dahulu. Untuk membuat response, kita menggunakan variabel `response` dan mengisinya dengan `HttpResponseRedirect(reverse("main:show_main"))`. `response.setcookie('last_login', str(datetime.datetime.now()))` berfungsi untuk membuat cookie `last_login` dan menambahkannya ke response tadi.
  Pada fungsi `show_main` tambahkan `'last_login': request.COOKIES['last_login']` pada variabel `context` supaya kita bisa menambahkan informasi cookie last_login pada response yang akan ditampilkan di web `main.html`.
  Untuk menghapus cookie `last_login` ketika user `logout` kita modifikasi code `logout_user` menjadi:

   ```python
   def logout_user(request):
      logout(request)
      response = HttpResponseRedirect(reverse('main:login'))
      response.delete_cookie('last_login')
      return response
   ```
  Lalu pada `main.html` tambahkan:
   ```html
   ...
  <h4>Sesi terakhir login: {{ last_login }}</h4>
   ...
   ```
  sebelum tabel pesanan untuk menampilkan data last login.

-  **Mengerjakan Bonus**

Pertama-tama, buat widget button pada `main.html`

```html
...
            <td>
                <form method="post" action="{% url 'main:add_amount' pesanan.id %}">
                    {% csrf_token %}
                    <button type="submit">+</button>
                </form>
            </td>
    
            <td>
                <form method="post" action="{% url 'main:decrease_amount' pesanan.id %}">
                    {% csrf_token %}
                    <button type="submit">-</button>
                </form>
            </td>
    
            <td>
                <form method="post" action="{% url 'main:delete_object' pesanan.id %}">
                    {% csrf_token %}
                    <button type="submit">DEL</button>
                </form>
            </td>
...
```

Button tersebut akan mengarah ke url `decrease_amount/ID` atau `add_amount/ID` dimana `ID` adalah id item yang akan diubah (yang kemarin kita akses di JSON/xml). Implementasi `add_amount/ID`, `decrease_amount/ID` dan `delete_object/ID`  dilakukan di `views.py`.

```python
@login_required(login_url='/login')
@login_required(login_url='/login')
def add_amount(request, id):
    pesanans = Pesanan.objects.filter(user=request.user).filter(pk=id).first() #first() is for effieciency as it only retrieve one requested object
    pesanans.amount +=1
    pesanans.save(update_fields=['amount'])
    return HttpResponseRedirect(reverse('main:show_main'))


@login_required(login_url='/login')
def decrease_amount(request, id):
    pesanans = Pesanan.objects.filter(user=request.user).filter(pk=id).first() #first() is for effieciency as it only retrieve one requested object
    if pesanans.amount >0: #so the amount will never be minus
        pesanans.amount -=1 
    pesanans.save(update_fields=['amount'])

    return HttpResponseRedirect(reverse('main:show_main'))

@login_required(login_url='/login')
def delete_object(request, id):
    Pesanan.objects.filter(user=request.user).filter(pk=id).delete() #first() is for effieciency as it only retrieve one requested object
    return HttpResponseRedirect(reverse('main:show_main'))

```
Dimana kita mengubah nilai dan mengupdate database yang kemudian kembali ke page main. 

## Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya?
Django UserCreationForm adalah suatu `built-in form` yang disediakan oleh framework web `Django`. Form ini dirancang khusus untuk memudahkan proses pembuatan user dalam aplikasi web yang memerlukan autentikasi. Dengan menggunakan UserCreationForm, Anda dapat membuat formulir registrasi pengguna dengan `cepat` tanpa perlu `menulis kode form` secara `manual`.

`Kelebihan `dari UserCreationForm:

- Kemudahan Penggunaan: Form ini menyederhanakan proses pembuatan user dalam `Django`. Anda hanya perlu mengimpor form ini dan menambahkannya ke `view` Anda untuk membuat halaman registrasi pengguna.

- Validasi Bawaan: Form ini dilengkapi dengan validasi bawaan, seperti memeriksa apakah `username unik` dan apakah `password yang dimasukkan cukup kuat`.

- Kustomisasi: Anda dapat mengkustomisasi tampilan form ini sesuai kebutuhan aplikasi Anda dengan menambahkan atau menghapus `field` atau mengubah pesan kesalahan yang ditampilkan.

- Integrasi dengan Model Pengguna Django: UserCreationForm terintegrasi dengan baik dengan model `User` `Django` , sehingga Anda tidak perlu melakukan banyak konfigurasi tambahan.

Namun, seperti halnya dengan banyak fitur dalam Django, ada beberapa `kekurangan` yang perlu dipertimbangkan:

- Ketidakcukupan Kustomisasi: Meskipun Anda dapat mengkustomisasi UserCreationForm, dalam beberapa kasus (misal menyimpan data password user :DD #kejahatan), Anda mungkin perlu membuat form registrasi yang sangat kustom. Dalam hal ini, Anda mungkin perlu menulis form sendiri secara manual.

- Tampilan Default yang Mungkin Tidak Sesuai: Tampilan default dari UserCreationForm mungkin tidak cocok dengan desain atau gaya visual aplikasi Anda. Anda perlu melakukan penyesuaian tampilan dengan `HTML` dan `CSS `tambahan.

- Ketergantungan pada Model Pengguna Bawaan: Jika Anda ingin menggunakan model pengguna yang berbeda atau mengganti model pengguna bawaan `Django`, Anda mungkin perlu menyesuaikan UserCreationForm, yang bisa menjadi `rumit`.

- Kompleksitas Ketika Menggabungkan Fitur Tambahan: Ketika Anda ingin menggabungkan fitur tambahan seperti konfirmasi username atau metode autentikasi sosial, Anda mungkin perlu menulis kode tambahan dan berurusan dengan validasi yang lebih rumit.

Jadi, meskipun UserCreationForm sangat berguna dalam banyak kasus, terutama untuk proyek-proyek dengan kebutuhan dasar autentikasi pengguna, Anda harus mempertimbangkan kebutuhan kustomisasi dan kompleksitas aplikasi Anda sebelum memutuskan apakah akan menggunakannya atau tidak.

## Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?

Autentikasi dan otorisasi adalah dua konsep penting dalam pengembangan aplikasi web, termasuk dalam konteks `Django`. Keduanya memiliki peran yang berbeda dalam mengelola akses pengguna ke sumber daya aplikasi Anda:

- Autentikasi:

Autentikasi adalah `proses verifikasi identitas pengguna`. Ini berarti memastikan bahwa pengguna yang mencoba mengakses aplikasi adalah orang yang dia klaim. Proses autentikasi biasanya melibatkan verifikasi kombinasi nama pengguna (username) atau alamat email dan kata sandi (password). Tujuan autentikasi adalah untuk memastikan bahwa hanya pengguna yang sah yang dapat masuk ke dalam sistem.

Dalam `Django`, autentikasi seringkali dilakukan dengan menggunakan `built-in user system`, di mana pengguna harus memasukkan nama pengguna dan kata sandi mereka untuk mengakses bagian tertentu dari aplikasi.

- Otorisasi:

Otorisasi adalah `proses yang mengatur apa yang diizinkan atau dilarang oleh pengguna` yang `sudah diautentikasi `untuk dilakukan dalam aplikasi. Ini berkaitan dengan hak akses dan izin. Otorisasi menentukan apakah seorang pengguna memiliki hak untuk melihat, membuat, mengedit, atau menghapus sumber daya tertentu dalam aplikasi. Dalam Django, ini sering diimplementasikan dengan menggunakan decorator seperti` @login_required` untuk melindungi tampilan (views) atau dengan menggunakan class-based views yang memiliki mixin otorisasi.

Otorisasi memastikan bahwa pengguna hanya dapat melakukan tindakan yang sesuai dengan peran atau hak akses yang telah diberikan kepada mereka. Ini membantu menjaga keamanan dan integritas data aplikasi.

Keduanya penting karena:

- Keamanan: Autentikasi membantu mencegah akses tidak sah ke sistem Anda. Tanpa autentikasi yang kuat, seseorang bisa berpura-pura menjadi pengguna yang sah dan mengakses informasi atau melakukan tindakan yang seharusnya tidak diizinkan.

- Kontrol Akses: Otorisasi memastikan bahwa pengguna hanya dapat melakukan tindakan yang sesuai dengan peran atau izin yang dimiliki. Ini membantu menjaga integritas data dan mencegah tindakan yang tidak diinginkan.

- Pengelolaan Identitas Pengguna: Autentikasi membantu dalam pengelolaan identitas pengguna dan mengidentifikasi pengguna yang masuk ke dalam sistem. Ini penting untuk personalisasi pengalaman pengguna dan pelacakan aktivitas pengguna.

- Dalam Django, kerangka kerja ini menyediakan alat dan mekanisme yang kuat untuk mengimplementasikan autentikasi dan otorisasi, sehingga memudahkan pengembang dalam melindungi aplikasi mereka dan mengendalikan akses pengguna dengan lebih baik.

##  Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?

`Cookies` adalah sejenis mekanisme penyimpanan data yang digunakan dalam konteks aplikasi web untuk menyimpan informasi di sisi klien (browser) pengguna. Informasi ini kemudian dapat diakses dan digunakan oleh server web dalam setiap permintaan selanjutnya yang dibuat oleh klien. `Cookies` biasanya digunakan untuk berbagai tujuan, termasuk mengidentifikasi sesi pengguna, menyimpan preferensi pengguna, pelacakan perilaku pengguna, dan banyak lagi.

Django menggunakan `cookies `untuk mengelola data sesi pengguna. Ini terkait dengan pembuatan dan penggunaan `cookie session`. `Cookie session` adalah `cookie` khusus yang digunakan oleh `Django `untuk menyimpan data sesi pengguna. Data sesi adalah informasi yang berhubungan dengan pengguna tertentu selama sesi mereka di aplikasi web, seperti data login, preferensi, atau item keranjang belanja.

Berikut adalah bagaimana Django menggunakan `cookies` untuk `mengelola data sesi pengguna`:

- Pembuatan Cookie Sesi: Saat pengguna mengakses aplikasi web yang menggunakan Django, server Django akan membuat cookie sesi baru. Cookie ini berisi identifikasi unik (ID sesi) yang biasanya merupakan string acak. ID sesi ini digunakan untuk mengidentifikasi sesi pengguna.

- Penyimpanan Data Sesi: Data sesi pengguna, seperti informasi login atau item keranjang belanja, disimpan di server Django. Namun, yang dikirimkan ke klien adalah hanya ID sesi yang disimpan dalam cookie.

- Pengambilan Data Sesi: Setiap kali pengguna membuat permintaan ke aplikasi web (misalnya, mengklik tautan atau mengirim formulir), browser klien akan mengirimkan cookie sesi yang berisi ID sesi ke server. Dengan menggunakan ID sesi ini, server Django dapat mengidentifikasi sesi pengguna yang sesuai.

- Pemulihan Data Sesi: Setelah mengidentifikasi sesi pengguna, server Django dapat memulihkan data sesi pengguna dari penyimpanan server dan menggunakan data tersebut untuk memberikan pengalaman yang sesuai kepada pengguna, seperti menampilkan nama pengguna setelah login.

Django menyediakan dukungan untuk mengelola cookie sesi dengan mudah melalui middleware bawaan. Anda dapat mengonfigurasi berbagai opsi terkait cookie sesi, seperti waktu kadaluwarsa, domain, dan secure (untuk mengirim cookie hanya melalui koneksi HTTPS), sesuai dengan kebutuhan aplikasi Anda.

Penggunaan cookie sesi `sangat penting` dalam pengembangan aplikasi web karena memungkinkan Anda untuk melacak informasi pengguna selama sesi mereka dan memberikan pengalaman yang personal dan aman. Selain itu, ini menghindari kebutuhan untuk menyimpan data pengguna di sisi klien, yang dapat memiliki risiko keamanan yang lebih besar.

## Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?

Penggunaan `cookies` dalam pengembangan web dapat menjadi aman jika dilakukan dengan benar dan dengan memperhatikan aspek keamanan. Namun, ada beberapa risiko potensial yang perlu diwaspadai terkait dengan penggunaan `cookies`. Berikut adalah beberapa risiko tersebut:

1. **Penyadapan Data:** Cookies dapat dipotong atau disadap oleh pihak ketiga yang tidak sah jika tidak diatur dengan benar. Ini dapat menyebabkan pencurian informasi sensitif, seperti token autentikasi, sesi pengguna, atau data pribadi.

2. **Penggunaan yang Tidak Aman:** Jika cookies digunakan untuk menyimpan data sensitif (seperti kata sandi) atau jika mereka dikirim melalui koneksi yang tidak aman (tanpa HTTPS), informasi tersebut bisa menjadi rentan terhadap serangan.

3. **Tracking:** Cookies sering digunakan untuk pelacakan perilaku pengguna secara online. Ini dapat menjadi masalah privasi jika pengguna tidak memberikan izin atau pemilihan privasi yang jelas.

4. **Ketidaksesuaian dengan Privacy Regulations:** Beberapa wilayah memiliki peraturan yang mengatur penggunaan cookies, seperti GDPR di Uni Eropa. Melanggar peraturan tersebut dapat berdampak pada reputasi dan denda perusahaan.

5. **Cross-Site Scripting (XSS):** Jika aplikasi web Anda rentan terhadap serangan XSS, cookie pengguna bisa dicuri oleh penyerang dan digunakan untuk mencuri sesi pengguna.

6. **Cross-Site Request Forgery (CSRF):** Penyerang dapat menggunakan cookie yang ada di peramban pengguna untuk membuat permintaan palsu ke aplikasi Anda jika tidak ada perlindungan CSRF yang memadai.

Untuk mengamankan penggunaan cookies dalam pengembangan web, Anda dapat mengikuti beberapa praktik terbaik:

- **Gunakan HTTPS:** Selalu gunakan koneksi HTTPS yang aman untuk mentransmisikan cookies, terutama jika cookies mengandung data sensitif.

- **AturSame-Origin Policies:** Pastikan cookie hanya dapat diakses oleh halaman yang memiliki asal yang sama (sama dengan domain yang mengeluarkan cookie).

- **Lakukan Validasi Input:** Selalu validasi dan bersihkan input pengguna untuk mencegah serangan XSS.

- **Beri Izin Pengguna:** Berikan pengguna kontrol atas cookie yang mereka terima dengan memberikan pilihan privasi yang jelas.

- **Ikuti Peraturan Privasi:** Jika Anda mengumpulkan data pribadi melalui cookies, pastikan untuk mematuhi peraturan privasi yang berlaku, seperti GDPR atau CCPA.

- **Pantau Keamanan:** Pantau aktivitas yang mencurigakan terkait dengan cookies dan tindakan keamanan lainnya secara teratur.

Saat mengembangkan aplikasi web, `selalu ` pertimbangkan `keamanan cookies` sebagai bagian penting dari strategi keamanan Anda. Penerapan yang benar akan membantu mengurangi risiko dan menjaga data pengguna yang aman.

</details>
Tugas 5
<details>

## Cara Implementasi
- **Kustomisasi halaman login, register, dan tambah inventori semenarik mungkin**
      
Sebelum melakukan desain pada HTML, perlu menambahkan link CSS framework dalam case ini adalah Bootstrap dan Java Scriptke dalam `templates/base.html` dan menambahkan tag `<meta name="viewport">` . Untuk menambahkannya bisa dengan menambahkan:

```html
<head>
    {% block meta %}
        ...
    {% endblock meta %}

    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">

    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/umd/popper.min.js" integrity="sha384-I7E8VVD/ismYTF4hNIPjVp/Zjvgyol6VFvRkX/vR+Vc4jQkC+hVqc2pM8ODewa9r" crossorigin="anonymous"></script>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.min.js" integrity="sha384-BBtl+eGJRgqQAUMxJ7pMwbEyER4l1g+O15P+16Ep7Q9Q+zqX6gSbd85u4mG4QzX+" crossorigin="anonymous"></script>
</head>

```
Pada halaman login, register, dan tambah inventori, desain yang saya buat kurang lebih sama, saya menggunakan inline css dengan memanggil `<style>` pada bagian atas html serta dipadukan dengan framework bootstrap. Saya menggunakan inline CSS karena menurut saya ini yang mudah disetup dan digunakan untuk pemula. Berikut adalah inline CSS yang saya tambahkan:
```html
<style>
    body {
        background-image: url('https://cdn.akamai.steamstatic.com/apps/csgo/images/dreams/hyper_awp_1.png');
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        margin: 0;
        padding: 0;
        display: flex;
        justify-content: center;
        align-items: center;
        min-height: 100vh;
        position: relative; 
    }

    .logo {
        position: absolute;
        top: 12px;
        left: 22px;
        z-index: 2;
        font-size: 36px;
        font-family: 'Helvetica', sans-serif;
        color: rgb(108, 20, 162);
    }

    .showcase h1,
    .showcase a {
        font-family: 'Helvetica', sans-serif;
        color: black;
        font-weight: bold;
    }

    .showcase {
        text-align: center;
        background-color: #d3d3d3ac;
        border-radius: 16px;
        padding-top: 30px;
        padding: 40px;
        width: 600px;
        text-align: left;
        backdrop-filter: blur(6px);
    }

    form {
        font-family: 'Helvetica', sans-serif;
        font-weight: 600;
    }

    input,
    textarea {
        width: 100%;
        padding: 0.4rem;
        border: 1px solid #ccc;
        border-radius: 5px;
    }

    .text-title {
        text-align: left; 
        font-size:35px;
        font-weight: 600;
        padding-bottom: 19px;
        padding-top: 5px;
    }

    .submit-button{
        font-size: 16px;
        display: inline-flex;
        height: 40px;
        width: 100%;
        padding: 8px 48px;
        justify-content: center;
        align-items: center;
        gap: 16px;
        border-radius: 8px;
        background: var(--primary-blue, rgb(108, 20, 162));
        color: #ffffff;
        text-decoration: none;
        border: none;
        cursor: pointer;
    }

</style>

```

      
 -  **Kustomisasi halaman daftar inventori menjadi lebih berwarna maupun menggunakan apporach lain seperti menggunakan Card**

Berikut inline CSS pada file main.html saya

```html
<style>
....
.rounded-button {
    background-color: #6c00ba;
    color: white;
    border: none;
    padding: 10px 20px;
    cursor: pointer;
    border-radius: 15px; 
    text-decoration: none; 
}

/* Efek Hover pada bagian button*/
.rounded-button:hover { 
    background-color: #43085e;
}



....
</style>

```

 - **Memberikan warna yang berbeda (teks atau background) pada baris terakhir dari item pada inventori anda menggunakan CSS**

Untuk menambahkan penanda berbeda di akhir tabel, saya menambahkan CSS untuk last child pada `tr` dengan kode berikut:

```html
<style>
...
table tr:last-child td {
background-color: rgb(159, 134, 188);
color: #ffffff;
}
...
</style>

```

   

##  Manfaat dari setiap element selector dan kapan waktu yang tepat untuk menggunakannya

1. **Element Selector (Tag Selector):**

    * Manfaat: Memilih semua elemen dengan tag yang spesifik
    * Waktu Penggunaan: Ketika ingin menerapkan gaya yang sama pada semua elemen dengan tag tertentu.

2. **Descendant Selector (Space):**
    
    * Manfaat: Memilih elemen yang merupakan anak atau keturunan dari elemen tertentu.
    * Waktu Penggunaan: Ketika ingin menerapkan gaya pada elemen yang berada di dalam elemen tertentu.

3. **ID Selector (#nama-id):**

    * Manfaat: Memilih elemen dengan ID yang spesifik.
    * Waktu Penggunaan: ketika ingin menerapkan gaya atau perilaku unik pada satu elemen tertentu.

4. **Class Selector (.nama-kelas):**

    * Manfaat: Memilih elemen berdasarkan kelas yang diberikan
    * Waktu Penggunaan: Ketika ingin menerapkan gaya yang sama pada beberapa elemen atau grup elemen.

5. **Universal Selector (*):**
    
    * Manfaat: Memilih semua elemen di halaman.
    * Waktu Penggunaan: Ketika mereset atau menetapkan gaya default untuk semua elemen di halaman.

6. **Adjacent Sibling Selector (+):**

    * Manfaat: Memilih elemen yang sejajar (saudara sejajar) dari elemen tertentu.
    * Waktu Penggunaan: Ketika ingin menerapkan gaya pada elemen yang berada tepat setelah elemen lain dari jenis yang sama.

7. **Pseudo-Class Selector (:pseudo-class):**

    * Manfaat: Memilih elemen berdasarkan keadaan atau perilaku tertentu (seperti :hover, :active, dsb.)
    * Waktu Penggunaan: Ketika ingin menerapkan gaya berdasarkan interaksi pengguna atau keadaan elemen.

## Penjelasan HTML5 Tag
HTML5 adalah versi terbaru dari HTML. Beberapa tag HTML5 yang dapat digunakan adalah:

1. `<canvas>` digunakan untuk membuat gambar, grafik, dan animasi dengan bantuan JavaScript.
2. `<video>` digunakan untuk memperlihatkan video pada halaman web.
3. `<nav>` digunakan untuk membuat bagian navigasi situs web
4. `<audio>` digunakan untuk memperlihatkan file audio pada halaman web.
5. `<img>` digunakan untuk memperlihatkan gambar dalam halaman web.
6. `<a>` digunakan untuk membuat hyperlink ke halaman web lain, file, dan sebagainya.

## Perbedaan *margin* dan *padding*
Margin mengatur jarak suatu elemen terhadap elemen-elemen lainnya, sedangkan padding mengatur jarak elemen yang berada di dalam suatu elemen terhadap border dari elemen tersebut.

<div style='display: flex;'>
    <img src='https://hackmd.io/_uploads/B1QiTx9ya.png' width=100%>

</div>

## Perbedaan TailwindCSS dengan Bootstrap

Bootstrap menyediakan komponen-komponen yang sudah jadi sehingga tinggal kita pakai sedangkan tailwind menyediakan template-template lebih dasar yang harus kita gabungkan terlebih dulu untuk memakainya. Sehingga perbedaannya adalah **tailwind** unggul pada kustomisasi namun lemah pada **kecepatan implementasi** sedangkan **bootstrap** unggul pada **kecepatan implementasi** namun lengah pada **kustomisasi**.

Waktu terbaik menggunakan **tailwind** adalah disaat kita diminta membuat website dengan desain kompleks dengan jangka waktu yang **lama**. Sedangkan bootstrap adalah ketika kita diminta membuat website **simpel** dengan jangka waktu yang **pendek**.

