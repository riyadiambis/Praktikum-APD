#Cabang penjualan Amerika menjual:
#Rendang (4.99$),Nasi Padang(6.99$) Nasi Bakepor Samarinda (6.29$), Kacang Tanah Rebus (2.49$), 

nama = input("Masukkan nama produk : ")
harga = float(input(f"Harga satuan dari produk {nama} ($) : "))
jumlah = int(input("Total "+nama+" yang ingin di beli : " ))

#Besaran diskon bergantung pada NIM (Rahmat Riyadi NIM 74), maka diskon sebesar 74%
diskon = int(input("Besar diskon yang doiberikan (%) : "))
persen_diskon = diskon / 100

total_harga = jumlah * harga
harga_diskon = total_harga * persen_diskon
Harga_Bayar = total_harga - harga_diskon
Harga_Bayar = round(Harga_Bayar, 2)
sisa_bagdis = diskon % 3


#Output/Keluaran
print(f"""
    Pelanggan yang terhormat anda telah membeli {nama} dengan harga satuan {harga}$ 
    total yang harus anda bayarkan sebelum diskon untuk {jumlah} {nama} ialah {total_harga}$ 
    Tetapi jangan khawatir, anda mendapatkan diskon sebesar {diskon}% Sehingga harga yang harus 
    anda bayarkan untuk {jumlah} produk {nama} adalah sebesar {Harga_Bayar}$
      """)

print(f"nilai modulus setelah di bagi 3 adalah = {sisa_bagdis}")
print("program berakhir")

