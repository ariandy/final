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
Source : https://www.kaggle.com/colearninglounge/employee-attrition  
Informasi mengenai dateset inipun dapat dilihat pada laman tersebut.

# Workflows
![Workflows](https://raw.githubusercontent.com/ariandy/final/master/workflows.png)

# Pre-Processing & Feature Engineering
- Menghapus beberapa features dengan standard deviasi bernilai 0
- Menghapus beberapa features yang tidak memberikan advantage apapun dalam melakukan EDA dan juga dalam permodelan
- Mengaplikasikan One-Hot Encoding ke features yang bersifat nominal
- Memasukkan PCA ke dalam Pipeline. Mencegah terjadinya Curse of Dimensionality 

# Model Selection
![Model Selection](https://raw.githubusercontent.com/ariandy/final/master/model_selection.png)

- `*` cv=5, Medium Grid
- `**` cv = 8. Heavy Grid , Post-Pruning
- `***` cv = 8, Tiny Grid, Post-Pruning

Semua pengerjaan dilakukan di Lenovo T450, prosesor i5 vPro Gen 4th. (tahun rilis 2015).

Tiny, Medium dan Heavy adalah skala yang bersifat subjektif, yang saya buat berdasarkan durasi yang diperlukan (waktu komputasi) di laptop saya.
Misal, bisa saja sebuah grid memakan waktu yang sedang-sedang saja pada laptop saya (Medium), namun ternyata bisa lebih cepat di laptop lain (yang spec-nya lebih mumpuni tentunya), atau bahkan lebih lambat daripada laptop saya. Sehingga ini tidak bisa menjadi patokan objektif.

# Modeling
**Catatan**: Karena dari diagram di atas menunjukkan bahwa DecisionTreeClassification yang terpilih daripada model lainnya, maka dibagian ini dan selanjutnya hanya akan mengulas tentang step tentang DecisionTreeClassification saja.  

Pada classifier problem, kita akan memilih salah satu metrik penilaian yang akan dijadikan acuan. Ini dikarenakan False Positive dan False Negative akan selalu trade-off satu sama lain. Jadinya, umumnya kita akan dihadapkan dengan 2 pilihan berikut:
- Kasus False Negative lebih beresiko daripada kasus False Positive
- Kasus False Positive lebih beresiko daripada kasus False Negative  
Di kasus ini, False Positive dan False Negative bisa diterjemahkan seperti ini:
- FP : Pegawai yang tidak keluar, terprediksi keluar.
- FN : Pegawai yang keluar, terprediksi tidak keluar.

Untuk kasus Attrition, saya menganggap kasus **False Negative adalah yang beresiko**.

Alasannya adalah, apabila ada pegawai keluar namun terprediksi tidak keluar, perusahaan beresiko kehilangan pegawai potensialnya. Dengan decision seperti ini, maka saya putuskan untuk memilih **Recall** sebagai metric yang diutamakan.

Dengan parameter  default, kita mendapatkan model yang overfit, dimana Train Recallnya dengan score 1.000000, sementara Test Recallnya dengan score 0.285714. 	

# Hyperparameter Tuning
Saat menggunakan Hyperparameter Tuning, saya menggunakan parameter grid (dengan Pipelining format) berikut:
```
params_for_DecisionTreeClassifier = {
    'pca__n_components': [10,15,20],
    'algorithm__random_state': [11111992],
    'algorithm__class_weight': [{0: 1, 1: 4.75}],
    'algorithm__splitter' : ['best', 'random'],
    'algorithm__max_features' : list(range(1,X_train.shape[1])),
    'algorithm__class_weight': [{0: 1, 1: 4.75}],
    'algorithm__max_depth' : np.linspace(4, 15, 10),
    'algorithm__min_samples_split' : [200,300,400],
    'algorithm__min_samples_leaf' : [100,150,200],
}
```
Sehingga mendapatkan parameter berikut,
```
<class 'sklearn.tree._classes.DecisionTreeClassifier'>
Pipeline(steps=[('pca', PCA(n_components=10)),
                ('algorithm',
                 DecisionTreeClassifier(class_weight={0: 1, 1: 4.75},
                                        max_depth=4.0, max_features=1,
                                        min_samples_leaf=100,
                                        min_samples_split=200,
                                        random_state=11111992,
                                        splitter='random'))])
```

Adapaun Classification Report yang diperoleh adalah seperti berikut.

```
<class 'sklearn.tree._classes.DecisionTreeClassifier'>
              precision    recall  f1-score   support

           0       0.89      0.23      0.37       639
           1       0.19      0.86      0.31       132

    accuracy                           0.34       771
   macro avg       0.54      0.54      0.34       771
weighted avg       0.77      0.34      0.36       771

              precision    recall  f1-score   support

           0       0.97      0.28      0.43       214
           1       0.21      0.95      0.35        44

    accuracy                           0.39       258
   macro avg       0.59      0.62      0.39       258
weighted avg       0.84      0.39      0.42       258
```
# Flask
- Ke direktori `flask`, lalu jalankan `python app.py`
- Pada browser, masuk ke localhost:9292
- Model dapat digunakan pada localhost:9292/prediction

# Notes
Link pada laman Home ditulis secara hardcode. Ubah portnya semisal bertabrakan dengan port yang sudah dipakai.

# Secondary Improvement for this project

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
