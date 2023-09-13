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
