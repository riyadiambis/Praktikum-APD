# list1 = ["a",
#          2,
#          True,
#          [1,2,3]]

# print(list1[-1][2])



# tas = ["buku", 32, True, 3.14, ["IF", 24]]
# print(tas)

# for i in tas:
#     print(i)

# for i in range(len(tas)):
#     print(tas[i])


# matkul = ["kalkulus", "Fisika Dasar", "PTI"]

# print(matkul)

# matkul.append("Logika Informatika")
# print(matkul)

# matkul.insert(1, "Tes")
# print(matkul)

# matkul[1] = "Fisika Kuantum"
# print(matkul)

# del matkul[1]
# print(matkul)

# buang = matkul.pop(1)
# print(f"ini adalah buang : {buang}")

# prodi = ["Informatika", "Sistem Informasi", "Teknik Arsitektur", "Teknik Lingkungan", "Teknik Pertambangan", "Teknik Elektro", "Teknik Industri", "Teknik SIpil", "TeknikGeologi", "Teknik Kimia"]
# print(prodi[::2])
# print(prodi[0:10:2])

# Manga = ["Maru-maru", "Nekomi", "hirura"]
# Anime = ["Re:Zero", "Boruto"]

# jepang = Manga + Anime
# print(Manga)
# print(Anime)
# print(jepang)



# barang = [["sepatu", "tas", "baju"],
#           ["pulpen", "pensil", "laptop"]]
# # 
# for i in barang:
#     for j in i:
#         print(j)

# nama = ("aldi", "daffa", "arishi")

# print(nama)



# barang1 = ["sepatu", "tas", "baju"],
# barang2 =  ["pulpen", "pensil", "laptop"]

# mahasiswa = (69, "Informatika", "2209106044", "Aldy septian ")#lalu kita unpacking
# absen, prodi, nim, nama = mahasiswa
# print(absen)
#mahas print(prodi)
# print(nim)
# print(nama)
# '''namanya unpacking'''


mahasiswa = (69, "Informatika", "2209106044", "Aldy septian ")#lalu kita unpacking
mahasiswa = list(mahasiswa)
mahasiswa[2] = "2409106074"
mahasiswa = tuple(mahasiswa)
print(mahasiswa)

