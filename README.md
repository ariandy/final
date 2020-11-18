# Attrition Problem

Attrition adalah sebuah siklus yang normal pada sebuah perusahaan dimana pegawai memilih untuk berhenti dari sebuah perusahaan, entah karena pensiun, mengundurkan diri, masalah kesehatan, mendapatkan kesempatan untuk mendapatkan karir yang lebih baik di tempat lain, merasa tidak sesuai dengan kultur perusahaan dan alasan serupa lainnya.  
Attrition adalah kasus yang sifatnya merupakan keinginan pribadi dari pegawai untuk mengundurkan diri, bukan dorongan dari perusahaan. Itu sebabnya, attrition sering dikaitkan kasus turnover (pemberhentian). Namun turnover itu sifatnya adalah keluarnya pegawai karena faktor-faktor yang datang dari perusahaan (misal, pengurangan pegawai, pemecatan sepihak, dll).

# Facts

Mengutip dari https://toggl.com/blog/cost-of-hiring-an-employee :

- Merekrut dan mempertahankan karyawan adalah hal yang kompleks dan membutuhkan dana, waktu dan skill Human Resource yang baik.  
- Pemilik Perusahaan Skala Kecil menghabiskan 40% waktu kerjanya untuk melakukan taks yang tidak berhubungan dengan perputaran uang, contohnya adalah perekrutan.
- Perusahaan menggelontorkan 15% s/d 20% dari gaji karyawan untuk merekrut kandidat baru.  
- Banyak perusahan yang kehilangan rata-rata antara 1% sampai 2.5% dari total revenue-nya untuk melakukan penyelarasan skill sehingga bisa bekerja dengan ritme kerja di perusahaan tersebut.  
- Di sekitar 500 korporasi di US, proses perekrutan karyawan bisa memakan dana sebesar 7645USD.  
- Diperlukan paling tidak rata-rata 52 hari untuk mengisi suatu posisi.  

# The common problem with Attrition

Tidak jarang dengan keluarnya seorang pegawai, perusahaan mendapatkan imbas negatif seperti:

- Workforce dan produktifitas yang berkurang drastis.
- Workload yang bertambah pada pekerja lain.
- Kehilangan pegawai potensial artinya akan ada bottleneck pada hal-hal yang berkaitan dengan transfer knowledge. Ini sebabnya, agar tidak ada bottleneck pada transfer knowledge, perusahaan terkadang harus mengeluarkan dana yang tidak kecil untuk keperluan training.

# Scenario & Goals

Kita adalah seorang Data Scientist yang bekerja pada perusahaan multinasional. HRD dari perusahaan tersebut telah mengumpulkan data dari pegawainya dan menugaskan kita **untuk membuat sebuah model yang mana bisa memprediksi pegawai yang mana yang sekiranya yang memungkinkan untuk keluar dari perusahaan tersebut**.

# Dataset

... soon (Bisa dilihat di Notebook #1)

# Workflows

![Workflows](https://raw.githubusercontent.com/ariandy/final/master/workflows.png)

# Model Selection

![Model Selection](https://raw.githubusercontent.com/ariandy/final/master/model_selection.png)

- `*` cv=5, Medium Grid
- `**` cv = 8. Heavy Grid , Post-Pruning
- `***` cv = 8, Tiny Grid, Post-Pruning

Semua pengerjaan dilakukan di Lenovo T450, prosesor i5 vPro Gen 4th. (tahun rilis 2015).

Tiny, Medium dan Heavy adalah skala yang bersifat subjektif, yang saya buat berdasarkan durasi yang diperlukan (waktu komputasi) di laptop saya.
Misal, bisa saja sebuah grid memakan waktu yang sedang-sedang saja pada laptop saya (Medium), namun ternyata bisa lebih cepat di laptop lain (yang spec-nya lebih mumpuni tentunya), atau bahkan lebih lambat daripada laptop saya. Sehingga ini tidak bisa menjadi patokan objektif.

# Notes

Link pada laman Home ditulis secara hardcode. Ubah portnya semisal bertabrakan dengan port yang sudah dipakai.

# Next Improvement for this project

### Analysis aspects
- Melakukan EDA lebih dalam lagi (contohnya bivariate analysis dengan feature lainnya selain target) untuk mencari temuan-temuan lainnya.

### Modeling aspects
- Mencoba menggunakan algoritma lain
- Melakukan tuning yang lebih complex
- Mencoba dengan metrics F1-Score

### Programming aspects
- Membuat estimator SkippablePCA agar GridSearchCV bisa memilih untuk melakukan skip atau tidak pada PCA
- Mengubah flow pengerjaan agar bisa membuat pipeline end-to-end (dari data benar-benar raw, sampai dengan menjadi model).
- Masih berhubungan dengan point ke dua, mengkonversi beberapa fungsi yang berguna untuk data cleaning menjadi FunctionTransformer agar bisa digunakan dalam pembuatan end-to-end pipeline.
- Membuat logging (dan export ke text file) disaat melakukan fit. Berguna untuk train beberapa model sekaligus dalam waktu yang lama.

### Front-End aspects

- Memperbaiki tampilan dashboard
- Melakukan render pada Seaborn/Pyplot plot dan langsung di-embed ke dashboard (tanpa harus menyimpan gambarnya, meletakkannya di direktori `static` dan memanggilanya secara hardcode) 
- Melakukan modularitas pada laman Home agar tidak perlu melakukan hardcode link untuk berpindah antar laman (dari halaman depan)

### Back-End aspects

- Membuat unit test untuk beberapa fungsi yang riskan (contohnya, fungsi yang ada berhubungan dengan app.py yang harus diperiksa lewat Jupyter Notebook untuk mengetahui resultnya benar atau tidak) agar mempermudah saya dalam melakukan scaling pada fungsi tertentu.

### Quality Assurance aspects

- Membuat Testcafe Script untuk melakukan Automated Test pada laman `predict`

### Documentation aspects

- Maintain dokumentasi github, comments pada code ataupun Jupyter notebook agar proyek tetap reproducable disaat saya ingin melanjutkannya di lain hari, meningkatkan readability pada code dan mempermudah saya untuk mentracking error apabila harus melakukan scale pada fungsi tertentu.
