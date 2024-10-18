# '''Membuat Fungsi'''

# def hello_world():
#     print("hello world")
#     print("Mantap Jiwa CUY")
#     print("gila banget")

# hello_world()
# hello_world()


# def fungsi():
#     '''seharunya ini muncul ya jika memang bisa'''
#     print("ini adalah fungsi loh")

# fungsi()


# def salam():
#     print("Selamat pagi")
    
# def kali():
#     x=6*4
#     print(x)

# salam()
# salam()
# salam()
# kali()
# kali()
# kali()


# '''Fungsi dengan Parameter'''

# def luas_persegi_panjang(panjang, lebar):
#     luas = panjang * lebar
#     print("luas persegi panjang", luas)

# '''Nah ini nanti yang akan aku tanyakan'''
# luas_persegi_panjang(2,3)
# print(f"ini adalah luas  persegi panjang loh{luas_persegi_panjang(10,5)}")


# def luas_persegi(sisi):
#     luas = sisi * sisi
#     return luas
# print("luas persegi", luas_persegi(8))
# print("luas persegi", luas_persegi(100))

# def tambah(angka1, angka2):
#     hasil =  angka1 + angka2
#     return hasil

# hasil_tambah = tambah(5,3)
# print(hasil_tambah)  

# def faktorial(n):
#     if n ==0:
#         return 1
#     else:
#         return n*faktorial(n-1)
    
# hasil_faktorial = faktorial(3)
# print(hasil_faktorial)


# def luas(sisi):
#     hasil = sisi*sisi
#     print(hasil)
#     # return hasil
# (luas(3))
# # def volume(sisi):
# #     volume = luas(sisi)*sisi
# #     print("volume persegi ini adalah", volume)
# '''Nah disini dapat kita simpulkan kalau nama variabel dari deff bisa sama dengan variabel lain'''
# # volume(3)



# def luas_segitiga(alas,tinggi):
#     luas = 1/2 * alas * tinggi
#     return (int(luas))

# # # print(luas_segitiga(10,5))
# # alas = int(input("masukkan nilai: "))
# # tinggi = int(input("masukkan nilai: "))
# print(luas_segitiga(10,5))
# print(luas_segitiga(20,10))

# def luas_persegi(sisi):
#     luas = sisi * sisi
#     return luas

# def volume_persegi(sisi):
#     volume = luas_persegi(sisi) * sisi
#     print ("Volume Persegi = ", volume)

# volume_persegi(5)



# print("Hello World")

# def hello_world(argumen):
#     print(argumen)

# hello_world("print")

# Nama = "Informatika"
# Mata_kuliah = "Algoritma Pemprograman Dasar"

# def info():
#     Nama = "Teknik elektro"
#     Mata_Kuliah = "Pengantar Teknik elektro"
#     print("Prodi:", Nama)
#     print("Mata kuliah:", Mata_Kuliah)

# # mengakses variabel global
# print("Prodi:", Nama)
# print("Mata Kuliah:", Mata_kuliah)
# # memanggil fungsi info
# info()

buku =["Anime","Bakwan"]

def show_data():
    if len(buku) <= 0:
        print ("Belum Ada data")    
    else:
        print("ID", "Nama Buku")
        for indeks in range(len(buku)):
            print (indeks+1, ".", buku[indeks])

print(len(buku))
show_data()


def insert_data():
    buku_baru = input("judul baru: ")
    buku.append(buku_baru)

def edit_data():
    show_data()
    indeks = int(input("Input ID buku: "))
    if (indeks>=len(buku) or indeks<0):
        print("ID salah")
    else:
        judul_baru = input("Judul baru: ")
        buku[indeks] = judul_baru
    
insert_data()
edit_data()


