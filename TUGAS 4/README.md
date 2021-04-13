# SISTEMPAKAR
Dian Markuci - 1184095 - D4TI3C 

# Pendahuluan
Logika fuzzy merupakan metodologi sistem kontrol untuk memecahan permasalahan. Untuk studi kasus ini yaitu penerapan logika fuzzy untuk mesin cuci.
Proses mencuci pada mesin cuci konvensional apabila dilihat dari waktu masing-masing proses pencuciannya diatur oleh pengguna mesin cuci. Walaupun fleksibel, namun hal tersebut tentu menjadi kesulitan tersendiri dalam menentukan ketepatan waktu. Sebagian besar orang tidak memperhatikan  jenis kotoran dan jumlah kotoran pada kain, kemudian jenis dan kualitas kain. dan hal tersebut juga membutuhkan waktu mencuci yang tidak sama. Apabila mengatur waktunya tidak sesuai maka hasil pencucian menjadi tidak maksimal. Sebaliknya, apabila mengatur waktu mencuci yang terlalu lama, maka akan ada pemborosan waktu dan energi.

# Tujuan
Tujuan penerapan logika fuzzy disini yaitu untuk mengotomatisasi sistem kendali waktu pencucian dengan data tingkat kekotoran dan jenis kotoran Pakaian untuk menghasilkan rata-rata lama waktu pencucian pada mesin cuci berdasarkan tipe kain dan jenis kotoran pakaian.

# Python

Sebelum menjalankan kodenya pastikan sudah :

    pip install numpy
    
    pip install -U scikit-fuzzy
    
Terdapat 2 variabel input type_of_dirtiness dan degree_of_dirtiness yang merepresentasi nilai dalam persentase kisaran 1-100 dengan tipe data sebagai floating-point.
untuk variable output di antaranya wash_time dan amount_of_powder. Waktu mencuci akan dihasilkan sesuai dengan tingkat dan jenis kotornya. Simulasi ini akan menghasilkan hasil yang sederhana yaitu washing_time. Pertama untuk memasukkan parameter maka jalankan main.py

# Aturan
# Rule Application
    rule1 = ctrl.Rule(degree_dirt['High'] | type_dirt['Fat'], wash_time['VeryLong'])
    rule2 = ctrl.Rule(degree_dirt['Medium'] | type_dirt['Fat'], wash_time['long'])
    rule3 = ctrl.Rule(degree_dirt['Low'] | type_dirt['Fat'], wash_time['long'])
    rule4 = ctrl.Rule(degree_dirt['High'] | type_dirt['Medium'], wash_time['long'])
    rule5 = ctrl.Rule(degree_dirt['Medium'] | type_dirt['Medium'], wash_time['medium'])
    rule6 = ctrl.Rule(degree_dirt['Low'] | type_dirt['Medium'], wash_time['medium'])
    rule7 = ctrl.Rule(degree_dirt['High'] | type_dirt['NonFat'], wash_time['medium'])
    rule8 = ctrl.Rule(degree_dirt['Medium'] | type_dirt['NonFat'], wash_time['short'])
    rule9 = ctrl.Rule(degree_dirt['Low'] | type_dirt['NonFat'], wash_time['very_short'])
    
Input (Antesednet) dan Output(Consequents) 

# Input
Antesednet:

a. type_of_dirtiness:

Universe (kisaran nilai yang tajam): jenis kekotoran dalam persentase kisaran 1 hingga 100
Fuzzy set (Rentang nilai fuzzy): NonFat, Medium, Fat

b. degree_of_dirtiness:

Universe (Rentang nilai tajam): tingkat kekotoran dalam persentase kisaran 1 hingga 100
Fuzzy set (Rentang nilai fuzzy): Low, Medium, Fat

# Output
Consequents:
wash_time:
Universe : Menurut program type_of_dirtiness dan degree_of_dirtiness maka akan menentukan atau menghasilkan berapa lama waktu yang dibutuhkan untuk mencuci satu pakaian dan output dihasilkan berupa format menit kisaran (1 hingga 60))
fuzzy set (Rentang nilai fuzzy): Sangat Pendek(VeryShort),Pendek(Short), Sedang(Medium,), Panjang(Long), Sangat Panjang (VeryLong)   

# Visualisasi Matplotlib
![fuzzy](https://user-images.githubusercontent.com/50128205/114517923-038cf280-9c69-11eb-94f5-9445c4b5d02e.JPG)

Input type_of_dirtiness dan degree_of_dirtiness masing-masing 34 dan 56, Waktu proses pencucian yang dihasilkan sekitar 29.69653079440644 menit atau bisa dibulatkan 30 menit.
    


