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
