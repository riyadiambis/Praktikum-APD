# '''Cara Mendeklarasikan deff'''

# def aku_fungsi():
#     print("Hello World")

# aku_fungsi()


# '''variabel di dalamnya disebut argumen'''
# def tambah(a,b):
#     hasil=a+b
#     print(hasil)

# tambah(10,2)

# '''Fungsi mengembalikan nilai'''
# def tambah(a,b):
#     hasil=a+b
#     print(hasil)

# tambah = tambah(2,4) + tambah(4,10)
# '''tambahan = 6+4'''
# '''Return disini fungsinya mengembalikan nilai, pokoknya apapun yang direturn itulah yang akan digunakan'''


# def pilihan():
#     opsi= input("Masukkan pilihan: ")
#     match opsi:
#         case "1":
#             print(1)
#             return
#         case "2":
#             print(2)
#             return
#     print(3)

# pilihan(2)

# '''return kosong disatu sisi fungsinya seperti break, pokoknya stop sampai return'''
# '''Fungsinya adalah untuk menghentikan, bisa digunakan di while true yang ada nilai'''

# '''tanda bintang * akan menempung data sisanya dengan syarat tanda itu diakhir'''

# def cetak(nama, nim, *matkul):
#     print(nama, nim, matkul)

# cetak("Riyadi", 41, "kalkulus", "fisdas")


# def cetak(nama, nim, **matkul):
#     print(nama, nim, matkul)

# cetak("Riyadi", 41, kalkulus=90, fisdas=70)

# '''ketika ada variabel yang isinya banyak angka yang dipisahkan dengan koma (bukan titik)
# maka jadinya akan menjadi tuple'''

# var = 1,2,3
# var1, var2, var3 = var
# print(var)
# print(var1)
# print(var2)
# print(var3)

# import os
# os.system('cls')

# '''penting untuk mendefinisikan nilai sebelum dipanggil'''


Nama = "Informatika"
Mata_Kuliah = "Algoritma dan Pemrograman Dasar"
# membuat variabel lokal
def info():
    Nama = "Teknik Elektro"
    Mata_Kuliah = "Pengantar Teknik ELektro"
# mengakses variabel lokal
    print("Prodi:", Nama)
    print("Mata Kuliah:", Mata_Kuliah)
# mengakses variabel global
print("Prodi:", Nama)
print("Mata Kuliah:", Mata_Kuliah)
# memanggil fungsi info
info()
'''Intinya adalah variabel di luar dapat diakses di dalam sedangkan yang ada di dalam harus dipanggil menggunakan def'''
'''untuk menyimpan data gunakan variabel global'''


