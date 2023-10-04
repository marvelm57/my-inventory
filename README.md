# Tugas 2

## _Step-by-step_ dalam mengimplementasikan _checklist_ Tugas 2
- Membuat direktori lokal di komputer atau laptop.
- Membuka _command_ atau _terminal_ di direktori tersebut untuk menginstall dan mengaktifkan _virtual environment_.
- Setelah _virtual environment_ sudah aktif, buat berkas requirements.txt di dalam direktori dan tambahkan beberapa _dependencies_, kemudian install _dependencies_ dengan menjalankan perintah melalui _command_ atau _terminal_.
- Buat proyek Django dengan nama yang sesuai dengan direktori lokal dengan menjalankan perintah melalui _command_ atau _terminal_. Perintah tersebut akan menghasilkan sebuah direktori baru di dalam direktori utama yang disebut dengan direktori proyek.
- Masih di dalam direktori utama dan _virtual environment_ yang aktif, buat aplikasi baru bernama main dengan menjalankan perintah melalui _command_ atau _terminal_. Perintah tersebut akan menghasilkan sebuah direktori baru yang disebut dengan direktori aplikasi.
- Untuk mendaftarkan aplikasi main ke dalam proyek, buka berkas settings.py yang ada di dalam direktori proyek dan tambahkan main ke dalam daftar aplikasi yang ada di variabel INSTALLED_APPS.
- Di dalam direktori aplikasi main, buat direktori baru dengan nama templates dan buat berkas main.html. Berkas main.html ini berisi HTML atau sebuah bahasa yang digunakan untuk membuat struktur dan tampilan konten pada halaman web.
- Selanjutnya, untuk mengimplementasi model dasar, buka berkas models.py yang ada di dalam direktori main dan isi dengan kode yang mendefinisikan model.
- Untuk mendefinisikan model, buat sebuah kelas dasar models.Models dengan nama Item dan isi kelas tersebut dengan atribut-atribut yang diinginkan, seperti _name_, _amount_, dan _description_. Setiap kali melakukan perubahan pada model, seperti menambahkan atau mengubah atribut, maka perlu melakukan migrasi untuk merefleksikan perubahan tersebut. Migrasi dapat dilakukan dengan menjalankan perintah melalui _command_ atau _terminal_.
- Selanjutnya, supaya template HTML dapat menampilkan data yang ada di model, maka view dan templates harus dihubungkan menggunakan Django. Langkah ini diawali dengan membuka berkas views.py yang berada di direktori aplikasi main dan mengimpor fungsi render dari modul django.shortcuts. Fungsi render digunakan untuk me-render tampilan HTML dengan menggunakan data yang diberikan.
- Kemudian, deklarasi fungsi show_main yang menerima parameter request dan isi fungsi tersebut dengan dictionary bernama context yang berisi data yang akan dikirimkan ke tampilan.
- Setelah itu, tambahkan kode return render(request, "main.html", context) yang berguna untuk me-render tampilan main.html dengan menggunakan fungsi render.
- Agar aplikasi main dapat diakses melalui peramban web, perlu dilakukan konfigurasi _routing_ URL aplikasi main. Langkah ini dapat dilakukan dengan membuat berkas urls.py di dalam direktori aplikasi main. Berkas urls.py ini berisi impor path dari django.urls untuk mendefinisikan pola URL, variabel app_name yang di assign value 'main', dan variable urlpatterns yang di assign sebuah list berisi fungsi path yang akan memetakan fungsi show_main dari views.py sebagai tampilan yang akan ditampilkan ketika URL terkait diakses.
- Selain mengonfigurasi _routing_ URL aplikasi main, perlu dilakukan konfigurasi _routing_ URL proyek untuk menghubungkannya ke tampilan main. Langkah ini dapat dilakukan dengan membuka berkas urls.py yang ada pada direktori proyek dan mengimpor fungsi include dari django.urls. Kemudian, tambahkan rute URL untuk mengarahkan ke tampilan main di dalam variabel urlpatterns.
- Selanjutnya, lakukan add, commit, dan push dari direktori repositori lokal ke repositori GitHub.
- Apabila repositori GitHub sudah sama dengan direktori repositori lokal, kita dapat melakukan deployment Adaptable dengan login ke akun Adaptable. Kemudian, pilih menu untuk membuat app baru. Hubungkan Adaptable dengan GitHub dan pilih repositori proyek yang telah dibuat sebagai basis aplikasi yang akan di-deploy. Pilih Python App Template sebagai template deployment dan pilih PostgreSQL sebagai tipe basis data yang akan digunakan.
- Pada bagian Start Command masukkan perintah python manage.py migrate && gunicorn <nama_direktori>.wsgi. Masukkan nama aplikasi yang juga akan menjadi nama domain situs web aplikasimu. Centang bagian HTTP Listener on PORT dan klik Deploy App untuk memulai proses deployment aplikasi.

## Bagan yang berisi request client ke web aplikasi berbasis Django beserta respon dan kaitan antara urls.py, views.py, models.py, dan berkas html.
![Screen Shot 2023-09-13 at 7 35 18 AM](https://github.com/marvelm57/my-inventory/assets/124948653/9f4f0d3d-0bca-45b9-8d8d-a95cd76d6c4a)
- Pertama, _request_ dari klien akan diteruskan oleh urls.py untuk mencocokkan dengan pola URL yang sesuai.
- Jika ada kecocokan, urls.py akan mengarahkan _request_ ke fungsi tampilan yang sesuai di views.py.
- Fungsi tampilan mungkin akan berinteraksi dengan model melalui models.py untuk mengambil atau memodifikasi data yang diperlukan.
- Fungsi tampilan kemudian akan menggunakan template HTML untuk merender tampilan yang akan dikirim sebagai respons.
- Respons akhir dikirim kembali ke klien dalam bentuk _webpage_.

## Mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
Karena _**virtual environment**_ dapat berguna untuk mengisolasi _package_ serta _dependencies_ dari aplikasi sehingga tidak bertabrakan dengan versi lain yang ada pada komputer. Kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan _**virtual environment**_, tetapi disarankan untuk menggunakan **_virtual environment_** untuk mencegah konflik antara package yang berbeda.

## Apa itu MVC, MVT, MVVM?
MVC, MVT, dan MVVM adalah konsep arsitektur yang digunakan dalam pengembangan web untuk memisahkan komponen-komponen utama dari sebuah aplikasi. Adapun perbedaan di antara ketiga konsep tersebut.
### MVC
- _**Model**_: Menyimpan data dan logika aplikasi.
- **_View_**: Merepresentasikan tampilan antarmuka dan bertanggungjawab untuk mempresentasikan data ke pengguna.
- _**Controller**_: Menerima input dari klient berupa request, kemudian berinteraksi dengan Model untuk memproses data dan mengirimkan hasilnya ke View untuk ditampilkan kepada pengguna.

### MVT
- **_Model_**: Menyimpan data dan logika aplikasi.
- **_View_**: Menampilkan data dari model dan menghubungkannya dengan template.
- **_Template_**: Menentukan tampilan antarmuka pengguna.
  
### MVVM
- _**Model**_: Menyimpan data dan logika aplikasi.
- **_View_**: Merepresentasikan tampilan antarmuka dan bertanggungjawab untuk mempresentasikan data ke pengguna
- **_ViewModel_**: Bertindak sebagai perantara antara Model dan View. Ini adalah komponen yang mengonversi data dari Model menjadi format yang dapat ditampilkan oleh View.

Perbedaan yang mencolok di antara ketiga konsep arsitektur di atas ada pada komponen _Controller_, _Template_, dan _ViewModel_. Pada konsep MVC, _Controller_ digunakan sebagai penghubung _Model_ dan _View_ dan bertanggung jawab dalam menentukan tampilan yang akan ditampilkan, kemudian View akan menampilkan tampilan antarmuka tersebut. Sedangkan, pada konsep MVT, ada komponen _Template_ yang bertanggung jawab dalam menentukan tampilan antarmuka.  Berbeda dengan konsep MVT yang menggunakan _View_ untuk menampilkan data dari model, pada konsep MVVM, terdapat komponen _ViewModel_ yang bertanggung jawab untuk meminta data dari model dan mengirimkannya ke View. Komponen ViewModel ini juga yang bertanggung jawab dalam memvalidasi user input.

# Tugas 3
## Apa perbedaan antara form POST dan form GET dalam Django?
### POST
- Digunakan untuk mengirim data, seperti _file_ atau _form data_ ke _web server_
- Dapat mengirim data dalam jumlah besar karena dikirimkan dalam badan permintaan HTTP 
- Lebih aman untuk mengirim data sensitif karena data tidak terlihat dalam URL
- Bersifat _non idempotent_

### GET
- Digunakan untuk membaca dan mengambil data, seperti _file_ atau _form data_ dari _web server_
- Hanya dapat mengirim data dalam jumlah terbatas karena sebagai parameter yang ditambahkan ke URL
- Kurang aman untuk data sensitif karena data terlihat dalam URL dan dapat dengan mudah diakses oleh pengguna
- Bersifat _idempotent_ yang berarti _request_ kedua akan diabaikan sebelum respon _request_ pertama dikirimkan

## Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?
### XML 
- Merupakan bahasa markup yang digunakan untuk menyimpan dan mengirim data dalam struktur berhierarki
- Data disimpan dalam tag yang membentuk _tree_ yang dimulai dari _root_, _branch_, hingga _leaves_
- Sering digunakan untuk pengiriman data yang terstruktur dan kompleks
- Sering digunakan untuk pengiriman data antar sistem yang berbeda

### JSON
- Merupakan format teks yang digunakan untuk menyimpan dan mengirim data dalam bentuk objek
- Data pada JSON disimpan dalam bentuk _key_ dan _value_ seperti dalam _dictionary_
- Sering digunakan dalam pengembangan web karena lebih mudah dibaca
- Sering digunakan untuk pertukaran data antara server dan klien web

### HTML
- Merupakan bahasa markup yang digunakan untuk membangun struktur halaman web
- Tidak digunakan untuk menyimpan atau mengirim data, tetapi untuk memformat dan menampilkan data
- Dapat digunakan untuk membuat tampilan halaman web yang dapat diakses oleh pengguna, seperti teks, gambar, tautan, dan lain-lain

## Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
- Memiliki sintaks yang sederhana, ringkas, dan mudah dimengerti oleh manusia
- Sangat fleksibel dalam menggambarkan berbagai jenis informasi karena dapat mewakili berbagai jenis tipe data, seperti _string_, angka, _boolean_, dan _array_
- Dapat digunakan dalam berbagai bahasa pemrograman dan lintas _platform_
- Proses pertukaran data menggunakan JSON lebih efisien dan cepat karena JSON menghasilkan data yang lebih ringan dibandingkan dengan format yang lain

## _Step-by-step_ dalam mengimplementasikan _checklist_ Tugas 3
- Buat berkas baru `forms.py` pada direktori `main` untuk membuat struktur `form` yang dapat menerima data item baru dengan menambahkan kode yang meng-_import_ `ModelForm` untuk membuat formulir berbasis model dan membuat kelas `ItemForm` yang merupakan turunan dari `ModelForm`. Kemudian, di dalam `ItemForm`, definisikan beberapa pengaturan melalui kelas `Meta`, yaitu `model = Item` untuk menunjukkan model yang digunakan untuk `form` dan `fields = ["name", "price", "description"]` untuk menunjukkan field dari model Item yang digunakan untuk `form`
- Selanjutnya, buka berkas `views.py` yang ada pada direktori `main` dan tambahkan _import_ `HttpResponseRedirect` dari `django.http`, `ItemForm` dari `main.form`, dan  `reverse` dari `django.urls`. Kemudian, buat fungsi baru bernama `create_item` pada berkas tersebut yang menerima parameter `request` dan isi dengan kode yang akan membuat dan menyimpan data item jika metode _request_ adalah `POST` dan input dari formnya valid dan kode yang akan melakukan _redirect_ setelah data `form` berhasil disimpan. Setelah itu, ubah fungsi `show_main` dengan menambahkan `items = Item.objects.all()` yang berguna untuk mengambil seluruh object item yang tersimpan pada database.
- Buka `urls.py` yang ada pada folder `main` dan _import_ fungsi `create_item`, kemudian tambahkan _path_ url ke dalam `urlpatterns` untuk mengakses fungsi `create_item` yang sudah di-_import_.
- Buat berkas HTML baru dengan nama `create_item.html` pada direktori `main/templates` yang akan menampilkan halaman `form` untuk metode `POST` yang terdiri dari judul "Add New Item", _fields_ form yang sudah dibuat pada `forms.py` sebagai tabel, dan tombol "Add Item" untuk mengirimkan _request_ ke view `create_item(request)`.
- Buka `main.html` dan tambahkan kode di dalam `{% block content %}` untuk menampilkan data item dalam bentuk tabel serta tombol "Add New Item" yang akan _redirect_ ke halaman `form`.
- Selanjutnya, untuk mengembalikan data dalam bentuk XML dan JSON, buka `views.py` yang ada pada folder `main` dan tambahkan _import_ `HttpResponse` dan `Serializer` pada bagian paling atas. `Serializer` ini digunakan untuk men-_translate_ objek model menjadi format lain, seperti XML dan JSON. Kemudian, buat dua fungsi yang menerima parameter `request` dengan nama `show_xml` dan 'show_json' dan buat sebuah variabel di dalam masing-masing fungsi tersebut yang menyimpan hasil _query_ dari seluruh data yang ada pada `Item`. Tambahkan _return function_ berupa `HttpResponse` yang berisi parameter data hasil _query_ yang sudah diserialisasi menjadi XML dan JSON pada masing-masing fungsi. Setelah itu, tambahkan parameter `content_type="application/xml"` dan `content_type="application/json"` pada masing-masing fungsi. Buka `urls.py` yang ada pada folder `main` dan _import_ fungsi yang sudah dibuat tadi, kemudian tambahkan _path_ url ke dalam `urlpattern`s untuk mengakses fungsi yang sudah di-_import_.
- Untuk mengembalikan data berdasarkan ID dalam bentuk XML dan JSON, buka `views.py` yang ada pada folder `main` dan buat dua fungsi baru yang menerima parameter `request` dan `id` dengan nama `show_xml_by_id` dan `show_json_by_id`. Buat variabel `data = Item.objects.filter(pk=id)` di dalam masing-masing fungsi tersebut yang menyimpan hasil _query_ dari data dengan id tertentu yang ada pada `Item`. Tambahkan _return function_ berupa `HttpResponse` yang berisi parameter data hasil _query_ yang sudah diserialisasi menjadi XML dan JSON pada masing-masing fungsi. Setelah itu, tambahkan parameter `content_type="application/xml"` dan `content_type="application/json"` pada masing-masing fungsi. Buka `urls.py` yang ada pada folder `main` dan _import_ fungsi yang sudah dibuat tadi, kemudian tambahkan _path_ url ke dalam `urlpatterns` untuk mengakses fungsi yang sudah di-_import_.
  
## _Screenshot_ hasil akses URL pada Postman
1. HTML
![Screen Shot 2023-09-20 at 12 20 27 AM](https://github.com/marvelm57/my-inventory/assets/124948653/cd90a7c8-ebde-4379-8297-69cf80c5d9d7)

2. XML
![Screen Shot 2023-09-20 at 12 20 56 AM](https://github.com/marvelm57/my-inventory/assets/124948653/64478963-ae2b-4521-b46a-13282d7dc70b)

3. JSON
![Screen Shot 2023-09-20 at 12 21 21 AM](https://github.com/marvelm57/my-inventory/assets/124948653/4f3802fb-e2c2-4fed-83ea-4df1a832bc3e)

4. XML _by id_
![Screen Shot 2023-09-20 at 12 21 47 AM](https://github.com/marvelm57/my-inventory/assets/124948653/ec86aef4-465e-41fc-b32d-0f5cb125d240)

5. JSON _by id_
![Screen Shot 2023-09-20 at 12 22 04 AM](https://github.com/marvelm57/my-inventory/assets/124948653/17f6a60a-e79f-4af2-9476-4a29f7153ab0)

# Tugas 4
## Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya?
UserCreationForm adalah form yang disediakan oleh Django untuk mempermudah pembuatan dan pendaftaran pengguna pada aplikasi web. Dengan form ini, pengguna baru dapat mendaftar dengan mudah karena sudah mencakup username dan password, serta berbagai validasi yang umumnya diperlukan dalam proses pendaftaran.
### Kelebihan
- Dapat menghemat waktu dalam pengembangan karena merupakan bawaan dari _framework_ sehingga tidak perlu membuat _form_ pendaftaran pengguna dari awal.
- Mencakup validasi otomatis untuk memastikan data yang dimasukkan oleh pengguna sesuai dengan persyaratan yang ditentukan, seperti memeriksa username dan password, serta memvalidasi format password yang kuat.
- Dapat menangani proses autentikasi, menyimpan data pengguna di database, dan memberikan akses ke fitur autentikasi seperti login dan logout karena terintegrasi dengan Django Authentication.

### Kekurangan
- Tidak ada _field_ email sehingga tidak dapat mengonfirmasi email
- Meskipun memiliki validasi otomatis, seperti pada password, aplikasi belum tentu benar-benar aman sehingga masih perlu penambahan fitur untuk mendukung keamanan form dari serangan.
- Memiliki tampilan _default_ yang terbatas yang mungkin tidak sesuai dengan yang kita mau pada aplikasi kita sehingga mungkin masih perlu banyak penyesuaian.

## Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?
Autentikasi merupakan proses untuk memverifikasi identitas pengguna, sedangkan otorisasi adalah proses untuk menentukan apa yang boleh diakses atau dilakukan pengguna setelah diautentikasi. Autentikasi penting untuk menjaga keamanan aplikasi dan akses terhadap suatu informasi. Tanpa adanya autentikasi, semua orang dapat mengakses informasi atau data yang seharusnya hanya dapat diakses oleh pengguna yang sah. Sedangkan, otentikasi penting untuk membatasi pengguna sehingga hanya dapat bertindak atau mengakses informasi yang sewajarnya.

## Apa itu _cookies_ dalam konteks aplikasi web, dan bagaimana Django menggunakan _cookies_ untuk mengelola data sesi pengguna?
_Cookies_ adalah sekumpulan kecil data yang disimpan di sisi klien ketika pengguna mengunjungi sebuah situs web. _Cookies_ digunakan dalam konteks aplikasi web untuk menyimpan informasi tertentu yang dapat diakses dan dikelola oleh server web, serta digunakan untuk mengautentikasi pengguna, melacak sesi, atau menyimpan preferensi pengguna. Data dalam _cookie_ terdiri dari sebuah pasangan nama dan _value_ yang dikirim ke header dari HTTP GET atau POST request klien.

Django menggunakan _cookie_ untuk menyimpan _session ID_ yang akan dikirimkan ke server pada setiap _request_. Kemudian, _server_ akan mengembalikan respons bersamaan dengan satu atau lebih _cookies_ ke browser. Browser akan menyimpan _cookies_ dari _server_ dan akan terus mengirim _cookies_ ke server setiap kali terjadi _request_ hingga _cookies expire_.

## Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?
Penggunaan _cookies_ dalam pengembangan web dapat aman selama diimplementasikan dengan tepat. Selain itu di Django sendiri sudah ada _built in protection_ terhadap beberapa ancaman yang dapat terjadi pada aplikasi web, seperti CSRF(Cross Site Request Forgery) dan XSS(Cross Site Scripting). Namun, masih banyak ancaman lain pada aplikasi web yang bisa saja terjadi sehingga risiko potensial itu tetap ada dan harus diwaspadai, seperti _cookie/session poisoning_ yang digunakan oleh penyerang dengan tujuan untuk memodifikasi data sesi atau _cookies_ untuk mendapatkan akses secara tidak sah dan masih banyak lagi.

## _Step-by-step_ dalam mengimplementasikan _checklist_ Tugas 4
- Buka berkas `views.py` yang ada di subdirektori `main` dan _import_ `UserCreationForm` yang merupakan _built in_ dalam Django yang memudahkan pembuatan formulir pendaftaran pengguna. Kemudian, buat fungsi bernama `register` yang menerima parameter `request` dan isi dengan kode yang membuat `UserCreationForm` baru, memvalidasi input dari _form_, membuat dan menyimpan data dari _form_, menampilkan pesan ke pengguna, dan melakukan _redirect_ setelah data _form_ berhasil disimpan. Selanjutnya, buat berkas `register.html` di folder `main/templates` yang berguna sebagai templates dari fungsi `register` pada views. Setelah itu, buka `urls.py` yang ada pada folder `main` dan _import_ fungsi yang sudah dibuat tadi, kemudian tambahkan _path_ url ke dalam `urlpatterns` untuk mengakses fungsi yang sudah di-_import_.
- Buka berkas `views.py` yang ada di subdirektori `main` dan _import_ `authenticate` dan `login` yang berguna untuk melakukan autentikasi dan login jika autentikasi berhasil. Kemudian, buat fungsi bernama `login_user` yang menerima parameter `request` dan isi dengan kode untuk mengautentikasi pengguna berdasarkan username dan password yang diterima dari _request_ yang dikirim oleh pengguna saat login. Selanjutnya, buat berkas `login.html` di folder `main/templates` yang berguna sebagai templates dari fungsi `login_user` pada views. Setelah itu, buka `urls.py` yang ada pada folder `main` dan _import_ fungsi yang sudah dibuat tadi, kemudian tambahkan _path_ url ke dalam `urlpatterns` untuk mengakses fungsi yang sudah di-_import_.
- Buka berkas `views.py` yang ada di subdirektori `main` dan _import_ `logout` yang berguna untuk melakukan logout atau keluar dari sesi. Kemudian, buat fungsi bernama `logout_user` yang menerima parameter `request` dan isi dengan kode untuk melakukan logout dengan menghapus sesi pengguna yang saat ini masuk dan mengarahkan pengguna ke halaman login. Selanjutnya, buka berkas `main.html` yang ada pada folder `main/templates` dan tambahkan kode untuk membuat tombol logout di bawah _hyperlink tag_ untuk _Add New Item_. Setelah itu, buka `urls.py` yang ada pada folder `main` dan _import_ fungsi yang sudah dibuat tadi, kemudian tambahkan _path_ url ke dalam `urlpatterns` untuk mengakses fungsi yang sudah di-_import_.
- Untuk membuat dua akun pengguna, buka halaman login dari browser dan klik Register Now yang akan mengirim _request_ dan mengarahkan ke halaman register. Kemudian, pada halaman register, isi field username dan password sesuai ketentuan yang berlaku dan klik button _daftar_. Setelah itu, akan terjadi _redirect_ ke halaman login dan sekarang pengguna sudah terdaftar dan dapat melakukan login untuk menambah item.
- Untuk menghubungkan `Item` dengan `User`, buka `models.py` yang ada pada subdirektori `main` dan tambahkan import `User`. Kemudian, pada model `Item`, tambahkan kode `user = models.ForeignKey(User, on_delete=models.CASCADE)` yang berfungsi untuk menghubungkan satu item dengan satu user melalui sebuah _relationship_ di mana sebuah item pasti terasosiasikan dengan seorang user. Selanjutnya, buka `views.py` yang ada pada subdirektori `main` dan tambahkan kode yang mencegah Django agar tidak langsung menyimpan objek yang telah dibuat dari _form_ langsung ke database sehingga memungkinkan kita untuk memodifikasinya terlebih dahulu. Setelah itu, ubah fungsi `show_main` dengan menambahkan kode yang akan menyaring seluruh objek dengan hanya mengambil `Item` yang dimana field `user `terisi dengan objek `User` yang sama dengan pengguna yang sedang login. Terakhir, lakukan migrasi model untuk menyimpan perubahan yang terjadi pada model.
- Untuk menerapkan _cookies_ seperti last login, buka `views.py` yang ada pada subdirektori `main` dan tambahkan import `datetime`. Kemudian, pada fungsi `login_user`, ubah kode pada blok kode `if user is not None` yang akan melakukan login terlebih dahulu, membuat response, dan membuat _cookie `last_login` dan menambahkannya ke dalam response. Selanjutnya, pada fungsi `show_main`, tambahkan potongan kode `'last_login': request.COOKIES['last_login']` ke dalam variabel context yang berfungsi untuk menambahkan informasi cookie last_login pada response yang akan ditampilkan di halaman web. Setelah itu, ubah kode pada `logout_user` yang akan melakukan logout, membuat response, dan menghapus _cookie_ last_login. Terakhir, buka berkas `main.html` dan tambahkan potongan kode `<h5>Sesi terakhir login: {{ last_login }}</h5>` di antara tabel dan tombol logout untuk menampilkan data last login.

# Tugas 5
## Jelaskan manfaat dari setiap element selector dan kapan waktu yang tepat untuk menggunakannya.
- _Element selector_ memungkinkan kita mengubah properti untuk semua elemen yang memiliki tag HTML yang sama. _Element selector_ cocok digunakan ketika kita ingin memberikan gaya umum kepada semua elemen dengan tipe tertentu. Misalnya, kita mau memberikan warna merah pada elemen yang memiliki tag `<p>` yang bisa kita implementasikan sebagai berikut
    ```p {
        color: red
    }```

- ID _selector_ menggunakan ID pada tag sebagai selector-nya. ID dapat ditambahkan pada halaman template HTML. ID bersifat unik sehingga cocok digunakan untuk elemen yang unik dalam dokumen dan sebaiknya hanya satu elemen per halaman yang memiliki ID sama.

- Class _selector_ memungkinkan kita untuk mengelompokkan elemen dengan karakteristik yang sama. Class selector cocok digunakan apabila kita ingin memberikan _style_ tertentu kepada sekelompok elemen yang serupa, tetapi tidak semua elemen dalam dokumen.

## Jelaskan HTML5 Tag yang kamu ketahui.
HTML5 adalah versi terbaru dari bahasa _markup_ yang digunakan untuk membuat halaman web
Berikut adalah beberapa HTML5 Tag:
- `<html>` : Menandai awal dan akhir dokumen html
- `<head>` : Menyediakan informasi tentang dokumen, seperti judul dan penghubung ke berkas-berkas eksternal.
- `<body>` : Menandai konten utama halaman web
- `<h1>`, `<h2>`, `<h3>`, `<h4>`, `<h5>`, `<h6>`: Menandai judul atau _heading_ dengan tingkat kepentingan yang berbeda.
- `<p>` : Menandai paragraf teks.
- `<a>` : Membuat _link_ ke halaman atau sumber eksternal.
- `<table>` : Membuat tabel data
- `<tr>`: Menandai baris dalam tabel.
- `<td>` : Menandai kolom dalam tabel.
- `<form>`: Membuat formulir untuk mengumpulkan input dari pengguna.
- `<style>` : Internal CSS dalam dokumen HTML
- `<meta>` : Mmberikan informasi meta seperti karakter encoding atau deskripsi dokumen.
- `<link>` : Menghubungkan dokumen dengan berkas eksternal, seperti Bootstrap CSS.
- `<script>` : Menghubungkan dokumen dengan kode JavaScript.

## Jelaskan perbedaan antara margin dan padding.
Margin dan padding adalah properti CSS yang digunakan untuk mengatur ruang di sekitar dan di dalam elemen HTML

### Margin
- Merupakan ruang di luar elemen HTML, di antara elemen tersebut dan elemen-elemen lain di sekitarnya.
- Digunakan untuk mengatur jarak antara elemen HTML dengan elemen-elemen lain di sekitarnya

### Padding
- Merupakan ruang di dalam elemen HTML, di antara konten elemen dan batas (border) elemen tersebut
- Digunakan untuk mengatur jarak antara konten elemen dengan batas elemen (border).


## Jelaskan perbedaan antara framework CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?
### Tailwind
- Membangun tampilan dengan menggabungkan kelas-kelas utilitas yang telah didefinisikan sebelumnya.
- Memiliki file CSS yang lebih kecil sedikit dibandingkan Bootstrap dan hanya akan memuat kelas-kelas utilitas yang ada
- Memiliki memberikan fleksibilitas dan adaptabilitas tinggi terhadap proyek
- Memiliki pembelajaran yang lebih curam karena memerlukan pemahaman terhadap kelas-kelas utilitas yang tersedia dan bagaimana menggabungkannya untuk mencapai tampilan yang diinginkan.

### Bootstrap
- Menggunakan gaya dan komponen yang telah didefinisikan, yang memiliki tampilan yang sudah jadi dan dapat digunakan secara langsung.
- Memiliki file CSS yang lebih besar dibandingkan dengan Tailwind CSS karena termasuk banyak komponen yang telah didefinisikan.
- Menghasilkan tampilan yang lebih konsisten di seluruh proyek karena menggunakan komponen yang telah didefinisikan.
- Memiliki pembelajaran yang lebih cepat untuk pemula karena dapat mulai dengan komponen yang telah didefinisikan.

Bootstrap cocok digunakan apabila kita ingin membangun halaman web dengan cepat karena Bootstrap memiliki banyak komponen siap pakai dan tidak memerlukan waktu banyak untuk memahami komponen-komponen yang ada. Selain itu, Bootstrap juga cocok digunakan apabila kita ingin tampilan yang lebih konsisten di seluruh proyek. Sedangkan, Tailwind cocok digunakan apabila kita ingin kustomisasi yang tidak terbatas karena Tailwind memberikan fleksibilitas dan adaptabilitas yang tinggi. Selain itu, Tailwind cocok digunakan apabila kita ingin menghindari _overhead_ CSS yang tidak terpakai karena Taliwind menghasilkan file CSS yang lebih kecil dibandingkan Bootstrap.

## _Step-by-step_ dalam mengimplementasikan _checklist_ Tugas 5
- Buka file `base.html` yang ada di dalam folder `templates` dan menambahkan Bootstrap CSS dengan membuat tag `<link>` untuk menambahkan _link_ Bootstrap. Kemudian, tambahkan juga JavaScript ke dalam dokumen dengan membuat tag `<script>` untuk menambahkan _source_ JavaScript. Sekarang, kita sudah dapat mengkustomisasi halaman aplikasi web kita.
- Di dalam halaman login dan register, saya menggunakan _class selector_ untuk mengkustomisasi elemen-elemen yang hanya ada di class login.
- Di dalam halaman inventori, saya menambahkan navbar untuk menampilkan nama _user_ dan tombol _logout_. Kemudian, saya menggunakan _element selector_ untuk mengkustomisasi elemen berdasarkan tag-nya.