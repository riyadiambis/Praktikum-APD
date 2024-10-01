#Cabang penjualan Amerika menjual:
#Rendang (4.99$),Nasi Padang(6.99$) Nasi Bakepor Samarinda (6.29$), Kacang Tanah Rebus (2.49$), 

print()
samadengan = "="
bintang = "*"
batas1 = samadengan*70
batas2 = bintang*70
import sys
print("Halo member toko X, silahkan Login menggunakan kartu member anda!!")
print()
print(batas1)
print()
salah = 0
while salah < 3:
    usn = input(str("Masukkan Username : "))
    pas = input(str("Masukkan Password : "))
    if usn == "riyadi" and pas == "074":
        print()
        print(batas2)
        print("ANDA TELAH BERHASIL LOGIN")
        print(batas2)
        break
    else:
        print("login gagal")
        print()
        salah += 1
        if salah == 3:
            print(batas2)
            print("KESEMPATAN LOGIN TELAH HABIS!!")
            print(batas2)
            sys.exit()
print()
print(batas1)

print(f"""
oke {usn}, Hari ini kami memberikan diskon 74% khusus untuk member kami !!
Diskon berlaku untuk Rendang, Nasi Padang, Bakepor Samarinda dan Kacang Tanah rebus
Silahkan tentukan pilihan Anda!!""")

print()
print(batas1)
print()

while True:
    nama = input("Masukkan nama produk : ")
    harga = float(input(f"Harga satuan dari produk {nama} ($) : "))
    jumlah = int(input("Total "+nama+" yang ingin di beli : " ))

    #Besaran diskon bergantung pada NIM (Rahmat Riyadi NIM 74), maka diskon sebesar 74%
    diskon = 74
    persen_diskon = diskon / 100

    total_harga = jumlah * harga
    harga_diskon = total_harga * persen_diskon
    Harga_Bayar = total_harga - harga_diskon
    total_harga = round(total_harga, 2)
    Harga_Bayar = round(Harga_Bayar, 2)

    #Output/Keluaran
    print(f"""
    Pelanggan yang terhormat anda telah membeli {nama} dengan harga satuan {harga}$ 
    total yang harus anda bayarkan sebelum diskon untuk {jumlah} {nama} ialah {total_harga}$ 
    Tetapi jangan khawatir, anda mendapatkan diskon sebesar {diskon}% Sehingga harga yang
    harus anda bayarkan untuk {jumlah} produk {nama} adalah sebesar {Harga_Bayar}$""")
    print()
    lanjut = input("Apakah masih ada yang ingin anda beli? [ya/tidak]:  ")
    print()
    print(batas1)
    print()
    if lanjut == "tidak" or lanjut == "Tidak":
        print("Terima Kasih karena telah memilih Toko X")
        break

print(batas1)
print()