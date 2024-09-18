import random
import sys
from libs import welcome_message

ya_position = "y"
no_position = "n"

welcome_message("welcome to -MENCARI LOLI GAME-")

nama_user = input("\nmasukkan nama kamu Oni-chan: ")

while nama_user == "":
    nama_user = input("Cepat selamatkan Loli Imut ini!! \nIsi dulu nama Oni-chan : ")



while True:
    bentuk_karung = "|_|"
    karung_kosong = [bentuk_karung] * 4

    karung = karung_kosong.copy()
    karung_kosong = '  '.join(karung_kosong)
    
    loli_position = random.randint(1, 4)

    karung[loli_position - 1] = "|>-<|"
    karung = '  '.join(karung)

    print(f'''\nHalo {nama_user}! Coba kamu perhatikan keempat karung di bawah ini!
        
    {karung_kosong}
    ''')

    pilihan_user = input("Menurut kamu di karung nomor berapa berapa seorang Loli Imut berada? [1 / 2 / 3 / 4]:  ")
        

    while pilihan_user == "":
        pilihan_user = input("Ayo Oni-chan cepat isi pilihan mu, Loli Imut sedang menunggumu untuk di selamatkan! Pilihan : ")
        
    pilihan_user = int(pilihan_user)

    pilihan_konfirmasi = input(f"\nApakah kamu yakin dengan pilihan kamu {pilihan_user} ini Onii-chan? [y | n]:  ")

    while pilihan_konfirmasi == "":
        pilihan_konfirmasi = input("\nAyo cepat Oni-chan, bukan saatnya untuk bimbang! Ketik [y/n] : ")

    if pilihan_konfirmasi == ya_position:
        
        if pilihan_user == loli_position:
            print(f"\nSELAMAT KAMU MENANG! \n{nama_user} kun kamu dapat membawa Loli Imut ini pulang, pilihan kamu TEPAT di karung nomor {loli_position} \n\n{karung}")
        
        else:
            print(f"\nSAYANG SEKALI KAMU KALAH! \nLoli imut tidak ada di situ, kamu memilih karung nomor {pilihan_user} sedangkan pilihan yang tepat adalah karung nomor {loli_position} \n\n{karung}")
            
            
    elif pilihan_konfirmasi == no_position:
        print(f"\nHARUS YAKIN DONK! \n{nama_user} kun, kamu harus menemukan Loli Imut ini dan membawanya pulang...")
        sys.exit()
        
    else:
        print(f"YAMETE YO!!! \n{nama_user} kun, ketikkan dengan benar!!")
        sys.exit()
    
    play_again = input(f"\n\napakah {nama_user} Onii-chan ingin bermain lagi? [y/n] :   ")  
    if play_again == "n":
        break
      
    while play_again == "":
        input(f"\n{nama_user} Oni-chan kamu harus memilih terlebih dahulu loh, silahkan pilih [y/n] :   ")
    
    
    
print(f"\nOke {nama_user} Onichannn Telah Mengakhiri GAME \nsayang sekali kamu tidak melanjutkan game ini")


