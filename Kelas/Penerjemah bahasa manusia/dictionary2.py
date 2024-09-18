numbers = input("Masukkan Angka :  ")

numbers_mapping = {
    "1": "Satu",
    "2": "Dua",
    "3": "Tiga",
    "4": "Empat",
    "5": "Lima",
    "6": "Enam",
    "7": "Tujuh",
    "8": "Delapan",
    "9": "Sembilan"
}

output = ""

for n in numbers:
    terbilang = numbers_mapping.get(n, "Invalid")
    
    output = output + terbilang + " "
    
print(output)