nama = str(input("\nMasukkan nama anda : "))
BeratMg = int(input("Masukkan berat badan anda dalam satuan Miligram (1 kg = 10^6 mg): "))
TinggiKm = float(input("Masukkan tinggi badan anda dalam satuan Kilometer (172 cm = 0.00172 km) : "))
print("\n")

Berat = BeratMg / 10**6
Tinggi = TinggiKm * 10**3
BMI = Berat / Tinggi**2
BMI = round(BMI, 2)

if BMI < 18.5:
    print(f"""
halo {nama}, dari hasil perhitungan didapatkan nilai BMI Anda adalah {BMI}, angka tersebut termasuk kategori 'Kurang' (Underweight)
Kami menyarankan agar Anda lebih banyak mengonsumsi makanan bergizi, makanlah makanan yang tinggi kalori, dan tingkatkan frekuensi makan Anda
""")
elif BMI < 24.9:
    print(f"Bagus {nama}! nilai BMI Anda adalah {BMI} Berat badan tersebut Ideal, tetap pertahankan dan semangat! ")

elif BMI < 29.9:
    print(f"""
Nilai BMI anda adalah {BMI} Harap WASPADA {nama}, berat badan tersebut masuk kategori 'Berlebih' (Overweight)
Lakukan pola hidup sehat dan kurangi frekuensi dan volume konsumsi makanan anda, serta pilihlah makanan rendah kalori!
""")
else:
    print(f"GAWAT!!! {nama} Anda terindikasi mengalami OBESITAS dengan nilai BMI sebesar {BMI}, segera lakukan perubahan dan berkonsultasi dengan dokter bila perlu")

print("\n")