# Latar Belakang
Program ini dibuat dengan menggunakan bahasa python yang diperuntukkan sebagai aplikasi kasir sederhana yang datanya terdiri dari nama item, harga item, dan jumlah item dengan fitur-fiturnya adalah sebagai berikut: <br />
<ol>
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
![Flowchart](https://github.com/rifaisyap/python-project/assets/134842689/e28acc36-daa2-43d6-b622-a4c0d5b13983)


# Penjelasan Code
## a. init()
Fungsi inisialisasi untuk class Transaction\
![image](https://github.com/rifaisyap/python-project/assets/134842689/39c36ee8-d630-4faf-8365-ac5816748f96)

## b. add_item
Fungsi untuk menambahkan item baru\
Parameter yang dibutuhkan pada fungsi ini adalah:
<ul>
<li>item_name (str, key) = nama dari item yang dibeli
<li>item_price (int) = harga dari item yang dibeli
<li>total_item (int) = total quantity dari item yang dibeli
</ul><br />

![image](https://github.com/rifaisyap/python-project/assets/134842689/f66ebf40-c0d4-4879-92ef-ac48913e405b)

Cara kerja fungsi ini adalah setelah data nama item, harga item, dan total quantity item diinput, data harga item dan total quantity item akan divalidasi terlebih dahulu untuk memastikan bahwa data yang dimasukkan adalah angka. Jika validasinya gagal, maka akan mengeluarkan error berupa : ```Price and total item must be numerical```. Jika validasinya berhasil, maka data akan tersimpan dan akan mengeluarkan kalimat berupa ```Item that will be bought is Sayur with price 3000 and total item : 5 ``` 

## c. update_item_name
Fungsi untuk mengubah nama item yang sudah diinput\
Parameter yang dibutuhkan pada fungsi ini adalah:
<ul>
<li>existing_item_name = nama dari item sebelum dilakukan perubahan, key dari dictionary
<li>update_item_name = nama baru untuk item yang dibeli, menjadi key baru dari dictionary
</ul><br />

![image](https://github.com/rifaisyap/python-project/assets/134842689/8da7d5c0-0475-426b-ad1d-546d12a99e91)

Cara kerja fungsi ini adalah pertama-tama mencari data item yang akan diganti dengan menggunakan parameter existing_item_name, jika item ditemukan maka nama item tersebut akan diganti menjadi update_item_name dan mengeluarkan kalimat berupa ```Item is successfully updated to Tahu```. Akan tetapi, jika nama item tidak ditemukan, maka akan mengeluarkan error berupa : ```item not found```.

## d. update_item_price
Fungsi untuk mengubah harga dari item yang sudah diinput\
Parameter yang dibutuhkan pada fungsi ini adalah:
<ul>
<li>existing_item_name = nama dari item yang ingin dirubah data harganya, key dari dictionary
<li>update_item_price = harga baru dari item yang ingin dibeli
</ul><br />

![image](https://github.com/rifaisyap/python-project/assets/134842689/7d2ec1c0-cb52-4e4d-8e38-ad164e6dd447)

Cara kerja fungsi ini adalah pertama-tama mencari data item yang akan diganti dengan menggunakan parameter existing_item_name, jika item ditemukan, maka harga item tersebut akan diganti menjadi update_item_price dan mengeluarkan kalimat berupa ```Tahu price is successfully updated to 7000```. Akan tetapi, jika nama item tidak ditemukan, maka akan mengeluarkan error berupa : ```item not found```.

## e. update_total_item
Fungsi untuk mengubah total quantity dari item yang sudah diinput\
Parameter yang dibutuhkan pada fungsi ini adalah:
<ul>
<li>existing_item_name = nama dari item yang ingin dirubah data jumlah quantity nya, key dari dictionary
<li>update_total_item = total quantity baru dari item yang ingin dibeli
</ul><br />

![image](https://github.com/rifaisyap/python-project/assets/134842689/2e947cf8-c8be-4f4d-9c14-4c54a3b323a0)

Cara kerja fungsi ini adalah pertama-tama mencari data item yang akan diganti dengan menggunakan parameter existing_item_name, jika item ditemukan, maka total item tersebut akan diganti menjadi update_total_item dan mengeluarkan kalimat berupa ```Total Santan is successfully updated to 8```. Akan tetapi, jika nama item tidak ditemukan, maka akan mengeluarkan error berupa : ```item not found```.

## f. delete_item
Fungsi untuk menghapus dataa spesifik item beserta harga dan jumlahnya\
Parameter yang dibutuhkan pada fungsi ini adalah:
<ul>
<li>existing_item_name = nama item yang ingin dihapus
</ul><br />

![image](https://github.com/rifaisyap/python-project/assets/134842689/d6ed6912-c523-4319-8b58-e4a2dd6472cb)

Cara kerja fungsi ini adalah pertama-tama mencari data item yang akan dihapus dengan menggunakan parameter existing_item_name, jika item ditemukan, maka item tersebut akan dihapus dan akan muncul kalimat ```Item successfully deleted```. Akan tetapi, jika nama item tidak ditemukan, maka akan mengeluarkan error berupa : ```item not found```.

## g. reset_transaction
Fungsi untuk menghapus semua data transaksi dalam dictionary

![image](https://github.com/rifaisyap/python-project/assets/134842689/7282dd73-9641-4667-bf6d-bbad7111621e)

## h. show_order
Fungsi untuk menunjukkan semua data transaksi dalam dictionary

![image](https://github.com/rifaisyap/python-project/assets/134842689/0eb70e4f-17e0-4058-9b5d-18ccfb602173)

## i. total_transaction
Fungsi untuk menghitung total transaksi dan total diskon yang didapatkan pembeli

![image](https://github.com/rifaisyap/python-project/assets/134842689/113407f3-d3ba-42b2-8494-90f85123c6bd)

Cara kerja dari fungsi ini adalah untuk menghitung total transaksi dari harga item dan dikalikan dengan total item. Jika total transaksi lebih dari 200.000, maka customer akan mendapatkan diskon sebesar 5%, sedangkan jika total transaksi lebih dari 300.00, maka customer akan mendapatkan diskon sebesar 8%, dan jika total transaksi lebih dari 500.000, maka customer akan mendapatkan diskon sebesar 0%.
Namun, jika total pesanan kurang dari 200.000, maka akan muncul kalimat ```Total belanja anda adalah 130000```.

# Hasil Test Case
![image](https://github.com/rifaisyap/python-project/assets/134842689/97c67df4-9ca0-44c5-b70f-446336a842ce)

## Test Case 1
![image](https://github.com/rifaisyap/python-project/assets/134842689/f67ae827-d27a-4295-88e5-1cf578b73110)

## Test Case 2
![image](https://github.com/rifaisyap/python-project/assets/134842689/66aaf7b8-22a1-4877-9c34-839757915e21)

## Test Case 3
![image](https://github.com/rifaisyap/python-project/assets/134842689/f0dc40a4-46d0-4fa0-b186-a191b6d86ea8)

## Test Case 4
![image](https://github.com/rifaisyap/python-project/assets/134842689/4ac3eade-12a5-412e-807c-2dfd08db4aaf)

## Test Case 5
![image](https://github.com/rifaisyap/python-project/assets/134842689/78cf4007-5982-473c-8e97-17c462ade4ff)

## Test Case 6
![image](https://github.com/rifaisyap/python-project/assets/134842689/b4314cbd-74b3-4d84-a240-ab405847cdea)

## Test Case 7
![image](https://github.com/rifaisyap/python-project/assets/134842689/d497bee8-b903-422c-a0e7-49e0da77f863)

## Test Case 8
![image](https://github.com/rifaisyap/python-project/assets/134842689/c238551b-1e5d-48e7-935e-9602e227f3db)


# Conclusion & Future Work
## Conclusion
Module cashier dapat digunakan untuk aplikasi self-service Super Cashier.
## Future Work
a. Dapat mengembangkan fungsi untuk penambahan diskon bagi customer yang memiliki member ID\
b. Penggunaan database dalam menyimpan data sehingga integritas data lebih baik


