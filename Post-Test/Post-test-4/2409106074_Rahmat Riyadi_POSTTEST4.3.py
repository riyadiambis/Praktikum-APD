print("""
Halo Sobat Sehat, mari kita menghitung BMI
Silahkan Login terlebih dahulu!""")

samadengan = "="
strip = "-"
batas1 = samadengan*105
batas2 = strip*105
import sys
salah = 0
print()
print(batas1)
print()
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
            print()
            print(batas1)
            sys.exit()
print()
print(batas1)
print()
print("Oke sobat sehat, sekarang mari kita mulai menghitung perbandingan antara berat badan dan tinggi badan anda\n")
print()
while True:
    BeratMg = int(input("Masukkan berat badan anda dalam satuan Miligram (1 kg = 10^6 mg): "))
    TinggiKm = float(input("Masukkan tinggi badan anda dalam satuan Kilometer (172 cm = 0.00172 km) : "))
    print()

    Berat = BeratMg / 10**6
    Tinggi = TinggiKm * 10**3
    BMI = Berat / Tinggi**2
    BMI = round(BMI, 2)

    if BMI < 18.5:
        print(f"""
    Dari hasil perhitungan didapatkan nilai BMI Anda adalah {BMI}, angka tersebut termasuk kategori 'Kurang' (Underweight)
    Kami menyarankan agar Anda lebih banyak mengonsumsi makanan bergizi, makanlah makanan yang tinggi kalori, dan tingkatkan frekuensi makan Anda
    """)
    elif BMI < 24.9:
        print(f"Bagus! nilai BMI Anda adalah {BMI} Berat badan tersebut Ideal, tetap pertahankan dan semangat! ")

    elif BMI < 29.9:
        print(f"""
    Nilai BMI anda adalah {BMI} Harap WASPADA, berat badan tersebut masuk kategori 'Berlebih' (Overweight)
    Lakukan pola hidup sehat dan kurangi frekuensi dan volume konsumsi makanan anda, serta pilihlah makanan rendah kalori!
    """)
    else:
        print(f"""
    GAWAT!!! Anda terindikasi mengalami OBESITAS dengan nilai BMI sebesar {BMI}, 
    segera lakukan perubahan dan berkonsultasi dengan dokter bila perlu!!""")
    print()
    print(batas2)
    print()
    ulang = input("Oke apakah sobat sehat masih ingin mnelakukan perhitungan BMI? [Ya/Tidak] :  ")
    print()
    print(batas1)
    print()

    if ulang == "Tidak" or ulang == "tidak" or ulang == "TIDAK":
        break

print("Tetetap jaga kesehatan ya sobat sehat!!")
print()