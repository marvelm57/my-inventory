# Tugas 1

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

# Tugas 2
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