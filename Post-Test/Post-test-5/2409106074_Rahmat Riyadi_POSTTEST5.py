import os
os.system('cls')

kesempatan_login = 3
daftar_anime = ["Re:Zero Season 3",
                "Dan Da Dan",
                "Blue LOck Season 2",
                "Blue Lock Season 2 ",
                "Bleach: Thousand-Year Blood War Part 3",
                "Ranma 1/2",
                "Dragon Ball Daima",
                "Tomb Raider: The Legend of Lara Croft",
                "Arcane Season 2",
                "Fate/strange Fake",
                "Beastars Season 3"
                ]
batas1 = "="*45
batas2 = "+"*45
Login_Admin = True
Login_User = True
Pengguna_Baru = []
Hasil_Donasi = []

os.system('cls')
print(batas1)
print(batas2)
print(batas1)
print()
print("SELAMAT DATANG DI ANIMELIST SEASON 2024".center(45))
print()
print(batas1)
print(batas2)
print(batas1)
print()
input("\nTekan Enter untuk memulai LOGIN!!!")
print()
print(batas1)


while kesempatan_login >0:
    os.system('cls')
    print(batas1)
    print()
    print("ANDA INGIN LOGIN SEBAGAI".center(45),"\n")
    print(batas1)
    print("""
    1. Pengguna Biasa
    2. Sebagai Admin 
    3. Daftar Sebagai Pengguna Baru""")
    print()
    menu = input("Pilihan Anda (1/2/3)\t : ")
    os.system('cls')

    if menu == "1":
        print(batas1)
        print("LOGIN SEBAGAI PENGGUNA BIASA".center(45))
        print(batas1)
        usn = input("\nUsername : ")
        pas = input("\nPassword : ")
        if usn in Pengguna_Baru and pas in Pengguna_Baru:
            print()
            print(batas2)
            print("SELAMAT ANDA BERHASIL LOGIN".center(45))
            print(batas2)
            input("\nEnter untuk melanjutkan ...")
            Login_User = True
            Login_Admin = False
            break
        else:
            print()
            kesempatan_login -=1
            if kesempatan_login == 0:
                print()
                print(batas2)
                print("KESEMPATAN LOGIN TELAH HABIS!!!") 
                print(batas2)
                input("\nKetuk Enter untuk meankhiri sesi ...")
                Login_User = False
                Login_Admin = False
                break
            else:
                print(f"""
    Login Gagal, anda masih memiliki {kesempatan_login} 
    kesempatan untuk mencoba'""")
                input("\nKetuk Enter untuk login ulang ...")

    elif menu == "2":
        print(batas1)
        print("LOGIN SEBAGAI ADMIN".center(45))
        print(batas1)
        usn = input("\nUsername : ")
        pas = input("\nPassword : ")
        if usn == "wibu" and pas == "anime":
            print()
            print(batas2)
            print("SELAMAT SEPUH BERHASIL LOGIN".center(45))
            print(batas2)
            input("\nEnter untuk melanjutkan ...") 
            Login_Admin = True
            Login_User = False   
            break
        else:
            print()
            kesempatan_login -=1
            if kesempatan_login == 0:
                print()
                print(batas2)
                print("KESEMPATAN LOGIN TELAH HABIS!!!".center(45)) 
                print(batas2)
                input("\nKetuk Enter untuk mengakhiri sesi ...")
                Login_User = False
                Login_Admin = False
                break
            else:
                print(f"""
    Login Gagal, kesempatan anda tinggal {kesempatan_login} silahkan 
    ulangi kembali atau silahkan login sebagai 'Pengguna Biasa'""")
                input("\nEnter untuk login ulang ...")  

    elif menu == "3":
        print(batas1)
        print("DAFTAR SEBAGAI PENGGUNA BARU".center(45))
        print(batas1)
        Newusn = input("\nUsername : ")
        Newpas = input("\nPassword : ")
        Pengguna_Baru.append(Newusn)
        Pengguna_Baru.append(Newpas)
        print(f"Pengguna dengan username {Newusn} telah terdaftar")
        input("\nTekan Enter untuk melakukan Login pada Menu ...")

    else:
        print("Pilihan tersebut tidak ada, silahkan pilih pilihan yang tepat!")
        input("\nKetuk Enter untuk kembali ke Menu!!")
        

while True:
    if Login_User:
        while Login_User:
            os.system('cls')
            print(batas1)
            print("PILIH MENU YANG ANDA INGINKAN".center(45))
            print(batas1)
            print("""
    [1] Lihat Daftar Anime
    [2] Memberikan Donasi
    [3] Keluar sistem
            """)
            pilihan_user= input("\nSilahkan masukkan menu yang anda pilih : ")

            if pilihan_user == "1":
                os.system('cls')
                print(batas1)
                print(f"BERIKUT DAFTAR ANIME MUSIM INI!!!".center(45))
                print(batas1)
                print()
                for i in range(len(daftar_anime)):
                    print(f"{i + 1}. {daftar_anime[i]}")
                input("\nEnter untuk kembali ke Menu ...")

            elif pilihan_user == "2":
                os.system('cls')
                print(batas1)
                print("MEMBERIKAN DONASI".center(45))
                print(batas1)
                print("""\n
        1) Donasi coklat batang 1$
        2) Donasi cake coklat 5$""")
                donasi = input("\nIngin donasi yang mana : ")
                jumlah = int(input("\nMasukkan jumlah yang ingin anda donasikan : "))
                if donasi == "1":
                    kalkulator = jumlah*1
                elif donasi == "2":
                    kalkulator = jumlah*5
                else:
                    input("\nBerikan Donasi sesuai pilihan ya!!!")
                    break
                print(f"\nTotal donasi anda ialah : {kalkulator}")
                print("""
    Terima Kasih atas donasi yang Anda berikan untuk program
    ini, kami akan menggunakannya dengan baik""")
                input("Tekan Enter untuk kembali...")
                


            elif pilihan_user == "3":
                input("\nTekan tombol Enter ...")
                Login_User = False
                break

            else:
                print("Mohon Maaf Pilihan Tidak Tersedia")
                input("\nSilahkan tekan Enter ...")
        

    elif Login_Admin:
        while Login_Admin:
            os.system('cls')
            print(batas1)
            print("PILIH MENU YANG ADMIN INGINKAN".center(45))
            print(batas1)
            print()
            print(""" 
    [1] Lihat Daftar Anime
    [2] Tambah Judul Anime
    [3] Edit Daftar Anime
    [4] Hapus Judul Anime 
    [5] Keluar Program""")
            pilihan_admin = input("\nOke masukkan pilihanmu : ")

            if pilihan_admin == "1":
                os.system('cls')
                print(batas1)
                print(f"BERIKUT DAFTAR ANIME MUSIM INI!!!".center(45))
                print(batas1)
                print()
                for i in range(len(daftar_anime)):
                    print(f"{i + 1}. {daftar_anime[i]}")
                input("\nEnter untuk kembali ke Menu ...")

            elif pilihan_admin == "2":
                os.system('cls')
                print(batas1)
                print("MENAMBAHKAN JUDUL ANIME".center(45))
                print(batas1)
                print()
                NewJudul_Anime = input("Masukkan judul anime baru : ")
                daftar_anime.append(NewJudul_Anime)
                print(f"\nAnime {NewJudul_Anime} berhasil dimasukkan ke daftar!")
                input("\nKembali ke Menu ...")

            elif pilihan_admin == "3":
                os.system('cls')
                print(batas1)
                print("MENGEDIT DAFTAR ANIME".center(45))
                print(batas1)
                print()
                for i in range(len(daftar_anime)):
                    print(f"{i+1}. {daftar_anime[i]}")
                edit_nom = int(input("\nMasukkan nomor dari Daftar yang ingin diedit : ")) -1
                if 0 <= edit_nom < len(daftar_anime):
                    new_judul = input("Masukkan judul baru : ")
                    daftar_anime[edit_nom] = new_judul
                    print(f"\nAnime no {daftar_anime[edit_nom]} berhasil diubah menjadi {new_judul}")
                else:
                    print("\nNomor tersebut tidak ada dalam daftar")
                input("\nKembali ke Menu ...")


            elif pilihan_admin == "4":
                os.system('cls')
                print(batas1)
                print("MENGHAPUS JUDUL ANIME DARI DAFTAR".center(45))
                print(batas1)
                print()
                for i in range(len(daftar_anime)):
                    print(f"{i+1}. {daftar_anime[i]}")
                hapus_nom = int(input("\nMasukkan nomor dari daftar yang ingin dihapus : ")) - 1
                if 0 <= hapus_nom < len(daftar_anime):
                    hapus_judul = daftar_anime.pop(hapus_nom)
                    print(f"\n{hapus_judul} telah di hapus")   
                else:
                    print("\nNomor tersebut tidak ada dalam daftar")
                input("\nKembali ke Menu ...")

            elif pilihan_admin == "5":
                input("\nTekan Enter untuk keluar ...")
                Login_Admin = False
                break

            else:
                print("\nPilihan Menu Tidak Ada")
                input("\nKlik Enter untuk kembali ke Menu")

    else:           
        os.system('cls')
        print()
        print(batas1)
        print("PROGRAM SELESAI".center(45))
        print("TERIMA KASIH ATAS KUNJUNGANNYA".center(45))
        print(batas1)
        break

