import random

trying = 0
secret_number = random.randint(1, 9)
limit = 3

name_user = input("Masukkan namau kamu dulu donk :  ")
print(f"Oke {name_user}, kamu harus memasukkan angka *1 sampai 9* ingat kamu hanya punya {limit} kesempatan.")

while trying < limit:
    guess_number = input("\n oke, silahkan masukkan angka (1-9)! =  ")
    guess_number = int(guess_number)
    if guess_number == secret_number:
        print(f"Selamat bro {name_user}, jawabanmu Benar loh")
        break
        
    trying = trying + 1
    
if trying == limit:
    print(f"Maaf bro {name_user}, kesempatan kamu telah habis... Jawabannya adalah {secret_number}")
elif guess_number == secret_number:
    print(f"selamat sekali lagi {name_user}, kamu berhasil menebak dengan benar! Jawabannya adalah {secret_number}")