# daftar_buku = {
# "Buku1" : "Harry Potter",
# "Buku2" : "Percy Jackson",
# "Buku3" : "Twillight"
# }
# print(daftar_buku["Buku1"])
# print(daftar_buku["Buku2"])
# print(daftar_buku["Buku3"])

# daftar_buku = {}
# daftar_buku["novel 1"] = "senyum pertama di pagi hari Airin"
# daftar_buku[1] ="Matahari"
# print(daftar_buku)

# daftar_buku = dict(Buku1 = "Harry Potter", Buku2 = "Percy Jackson" )

# print(daftar_buku.get("Buku2")) 

# Nilai = {
# "Matematika" : 80,
# "B. Indonesia" : 90,
# "B. Inggris" : 81,
# "Kimia" : 78,
# "Fisika" : 80
# }

# for i in Nilai:
#     print(i)
# print("")

# print(Nilai.items())

# for i, j in Nilai.items():
#     print(f"Nilai dari {i} itu valuenya adalah {j}")

# Nilai = {
# "Matematika" : 80,
# "B. Indonesia" : 90,
# "B. Inggris" : 81,
# "Kimia" : 78,
# "Fisika" : 80
# }

# Nilai["Struktur Data"] = 99

# Nilai.update({"struktur data" : "99"})


# Nilai = {
# "Matematika" : 80,
# "B. Indonesia" : 90,
# "B. Inggris" : 81,
# "Kimia" : 78,
# "Fisika" : 80
# }

# print(Nilai)
# hapus = Nilai.pop("Matematika")
# print()
# print(Nilai)
# print()
# print(hapus)

# del Nilai["Fisika"]
# print(Nilai)

# Nilai.clear()
# print(Nilai)





# Nilai = {
# "Matematika" : 80,
# "B. Indonesia" : 90,
# "B. Inggris" : 81,
# "Kimia" : 78,
# "Fisika" : 80
# }

# print(f"jumlah nilai di atas adalah {len(Nilai)}")
# for i in range(len(Nilai)):
#     print(i)

# import os

# nilai = {
# "Matematika" : 80,
# "B. Indonesia" : 90,
# "B. Inggris" : 81,
# "Kimia" : 78,
# "Fisika" : 80
# }
# # print(nilai)
# # daftar_nilai = nilai.copy()
# # print(daftar_nilai)

# key = "motor", "mobil", "sepeda"
# value = 2
# daftar_kendaraan = dict.fromkeys(key, value)

# print(daftar_kendaraan)



# Musik = {
# "The Chainsmoker" : ["All we Know", "The Paris"],
# "Alan Walker" : ["Alone", "Lily"],
# "Neffex" : ["Best of Me", "Memories"]
# }

# #Mengakses key dan value dalam dictionary
# print(Musik.items())

# for i, j in Musik.items():
#     print(f"Musik milik {i} adalah : ")
#     for song in j:
#         print(song)
#     print("")


mahasiswa = {
101 : {"Nama" : "Aldy", "Umur" : 19},
111 : {"Nama" : "Abdul", "Umur" : 18, "Hobi" : ["membaca", "ngoding", "nulis makalah"]}
}
# for key, value in mahasiswa.items():
#     print("ID Mahasiswa : ", key)
#     for key_a, value_a in value.items():
#         print (key_a, " : ", value_a)
#     print("")

#bertahap ya pokoknya perhatikan key dan tipe datanya
print(mahasiswa[111]["Hobi"][-1])
    


nilai = {
    "Matematika": 90,
    "Fisika": 80,
    "Biologi": 80,
    "Kimia": 70,
    "Algoritma": 85
}

for i in nilai.value():
    print(i)
