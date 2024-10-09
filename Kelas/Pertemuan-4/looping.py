# ulang = 10
# for i in range(ulang):
#     print("Perulangan ke-" + str(i + 1))
#     print(f"perulangan ke-{ulang} kali")

# for i in range(1, 11, 3):
#     print(f"Perulangan ke {i}")

# simpan = [12, "udin petot", 14.5, True, 'A']
# for i in simpan:
#     print(i)

# simpan = "Udin Petot"
# for i in simpan:
#     print(i)

# for i in range(1, 4):
#     for j in range(1, 4):
#         print(f"{i} x {j} = {i * j}")
#     print()

# for i in range(1, 6, 2):
#     for j in range (1, 6, 2):
#         print(f"{i} x {j} = {i * j}")
#     print()


# for i in range(10, -1, -1):
#     print(f"anak ayam turun {i}") namanya inkremen

# ulang = 'ya'
# hitung = 1
# while ulang == "ya":
#     print(f"Perulangan ke {hitung}")
#     ulang = input("Apakah anda masih ingin mengulang?")
#     hitung += 1
# print("Perulangan selesai")


# hitung = 1
# while True:
#     print(f"Perulangan ke {hitung}")
    
#     hitung += 1
# print("Perulangan selesai")

# x=0
# while x < 5:
#     print(x)
#     x=+1

# hitung = 1
# while True:
#     ulang = input("apakah anda masih ingin mengulang?")
#     if ulang == "tidak":
#         print("perulangan berenti")
#         break
#     hitung += 1

# print(f"total perulangan : {hitung}")


# for i in range(10):
#     if i % 2 == 0:
#         continue
#     if i == 5:
#         break
#     print(i) hasilnya 1,3


usn = "admin"
pw = "admin123"
salah = 0

while salah < 3:
    username = input("Masukkan username: ")
    password = input ("Masukkan password: ")
    if usn == username and pw == password:
        print("Login berhasil")
        break
    else:
        print("Login gagal")
        salah += 1

