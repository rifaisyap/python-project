# Latar Belakang
Program ini dibuat dengan menggunakan bahasa python yang diperuntukkan sebagai aplikasi kasir sederhana yang datanya terdiri dari nama item, harga item, dan jumlah item dengan fitur-fiturnya adalah sebagai berikut: <br />
<ol>
  <li>Membuat ID transaksi</li>
  <li>Menambahkan data barang yang dibeli beserta jumlah dan total harganya</li>
  <li>Mengubah data barang yang dibeli beserta jumlah dan total harganya</li>
  <li>Menghapus data dari salah satu barang yang sudah diinput</li>
   <li>Menghapus seluruh data yang sudah diinput</li>
  <li>Mengecek data</li>
   <li>Menghitung total diskon</li>
  <li>Menghitung total transaksi</li>
   <li>Menampilkan seluruh informasi transaksi</li>
</ol><br />

# Requirement
<ul>
    <li>Alur Program/Flowchart</li>
    <li>Fungsi</li>
</ul><br />

# Flowchart
![flowchart](Self Service Cashier-Tokopaedi.jpg)

# Penjelasan Code
a. init()\
Fungsi inisialisasi untuk class Transaction

b. add_item\
Fungsi untuk menambahkan item baru\
item_name (str, key) = nama dari item yang dibeli\
item_price (int) = harga dari item yang dibeli\
total_item (int) = total quantity dari item yang dibeli

c. update_item_name\
Fungsi untuk mengubah nama item yang sudah diinput\
existing_item_name = nama dari item sebelum dilakukan perubahan, key dari dictionary\
update_item_name = nama baru untuk item yang dibeli, menjadi key baru dari dictionary

d. update_item_price\
Fungsi untuk mengubah harga dari item yang sudah diinput\
existing_item_name = nama dari item yang ingin dirubah data harganya, key dari dictionary\
update_item_price = harga baru dari item yang ingin dibeli

e. update_total_item\
Fungsi untuk mengubah total quantity dari item yang sudah diinput\
existing_item_name = nama dari item yang ingin dirubah data jumlah quantity nya, key dari dictionary\
update_total_item = total quantity baru dari item yang ingin dibeli

f. delete_item\
Fungsi untuk menghapus dataa spesifik item beserta harga dan jumlahnya\
existing_item_name = nama item yang ingin dihapus

g. reset_transaction\
Fungsi untuk menghapus semua data transaksi dalam dictionary

h. show_order\
Fungsi untuk menunjukkan semua data transaksi dalam dictionary

i. total_transaction\
Fungsi untuk menghitung total transaksi dan total diskon yang didapatkan pembeli

# Hasil Test Case
## Test Case 1
## Test Case 2
## Test Case 3
## Test Case 4
## Test Case 5
## Test Case 6
## Test Case 7
## Test Case 8
## Test Case 9


# Conclusion & Future Work
## Conclusion
Module cashier dapat digunakan untuk aplikasi self-service Super Cashier.
## Future Work
a. Dapat mengembangkan fungsi untuk penambahan diskon bagi customer yang memiliki member ID\
b. Penggunaan database dalam menyimpan data sehingga integritas data lebih baik


