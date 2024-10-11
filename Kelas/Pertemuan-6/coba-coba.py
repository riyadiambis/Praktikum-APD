# daftar_buku = {
# "Buku1" : "Harry Potter",
# "Buku2" : "Percy Jackson",
# "Buku3" : "Twillight"
# }
# print(daftar_buku["Buku1"])
# print(daftar_buku["Buku2"])
# print(daftar_buku["Buku3"])

# daftar_buku = {}

# daftar_buku["Buku1"] = "Harry Potter"
# daftar_buku["Buku2"] = "Percy Jackson"
# daftar_buku["Buku3"] = "Twillight"

# print(daftar_buku)

# musik = {
#     "judul" : "All we Know",
#     "judul" : "Something Just Like This"
# }

# print(musik['judul'])

# Biodata = {
#     'Nama' : "Rahmat Riyadi",
#     "NIM" : "212121212",
#     "KRS" : ["Programan Dasar", "Struktur Data", "Basis Data"],
#     "Mahasiswa_Aktif" : True,
#     "Social Media" : {
#         "Instagram" : "@riyadi_ofisharu",
#         "Discord" : "Riyadichan"
#     }
# }

# nah_ini = ", ".join(Biodata["KRS"])
# print(nah_ini)

# print(Biodata["Mahasiswa_Aktif"])

# games = dict(Tonikawa = "romance", Pokemon = "Adventure", Genshin = "FPS")
# print(games)

# print(f"nama saya adalah {Biodata["Nama"]}")
# print(f"nama saya adalah {Biodata.get('Nama')}")
# print(f"Instagram saya : {Biodata["Social Media"]["Instagram"]}")
# print(f"Instagram saya {Biodata.get('Instagram')}")
# Instagram = Biodata['Social Media'].get("Instagram")
# print(Instagram)


Nilai = {
"Matematika" : 99,
"Bahasa Indonesia" : 75,
"Bahasa Inggris" : 65,
"Kimia" : 93,
"Fisika" : 100
}

# Item = Nilai.items()
# print(Item)

# for kunci,nilai in Nilai.items():
#     print(f"Kunci: {kunci}, Nilai: {nilai}")

# for x in Nilai:
#     print(x)
# print()
# for x, (i, j) in enumerate(Nilai.items()):
#     print(f"[{x}]Nilai {i} anda adalah {j}")

# for kunci, nilai in Nilai.items():
#     print(f"{kunci} nilainya {nilai}")


# Film = {
# "Tonikaku Kawaii" : "Romace",
# "Kiyttoni" : "game",
# "Pororo" : "anak-anak"
# }

# # print(Film)
# # Film["Kimi No Nawa"] = "Movie"
# # Film.update({"Indonesia" : "Negara"})

# # print(Film)

# Film["Pororo"] = "remaja"
# print(Film)

# for kunci, isi in Film.items():
#     print(f"Ini kuncinya : {kunci}, dan ini jawabannya {isi}")



# Film = {
# "Tonikaku Kawaii" : "Romace",
# "Kiyttoni" : "game",
# "Pororo" : "anak-anak"
# }

# del Film["Pororo"]
# print(Film)

# print(Film.get("Pororo"))

# Data = {
#     "Nama" : "Rahmat Riyadi",
#     "Umur" : 19,
#     "Jurusan IT" : True
# }

# print(Data)
# sampah = Data.pop("Nama")
# print(Data)

# print(Data.get("Nama"))
# print(sampah)

# print("jumlah data", len(Data))

# Data.clear()
# print(Data)



# Buku = {
# "No Longer Human" : "Osamu Dazai",
# "Harry Potter" : "J.K. Rowlings",
# "Hamlet" : "William Shakespeare"
# }

# pinjam = Buku.copy()

# print("Dictionary telah disalin :", pinjam)

Musik = {
    "The Chainsmoker" : ["All we Know", "The Paris"],
    "Alan Walker" : ["Alone", "Lily"],
    "Neffex" : ["Best of Me", "Memories"]
}
for i, j in Musik.items():
    print(f"Musik milik {i} adalah : ")
for song in j:
    print(song)
print("")






