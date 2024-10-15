import os
os.system('cls')

kesempatan_login = 3
daftar_anime = {
    "Fantasy": ["Re:Zero Season 3", "Dan Da Dan"],
    "Sports": ["Blue Lock Season 2", "Beastars Season 3"],
    "Action": ["Bleach: Thousand-Year Blood War Part 3", "Dragon Ball Daima"],
    "Adventure": ["Tomb Raider: The Legend of Lara Croft", "Arcane Season 2"],
    "Fate": ["Fate/strange Fake"],
    "Comedy": ["Ranma 1/2"]
}

batas1 = "="*55
batas2 = "+"*55
Login_Admin = True
Login_User = True
Pengguna_Baru = {
    "usn" : " ",
    "pas" : " "

}
tampilan = {
    "1" : "SPRING",
    "2" : "2024"
}

semua_anime = []

os.system('cls')
print(batas1)
print(batas2)
print(batas1)
print()
print(f"SELAMAT DATANG DI ANIMELIST {tampilan["1"]} {tampilan["2"]}".center(55))
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
    print("ANDA INGIN LOGIN SEBAGAI".center(55),"\n")
    print(batas1)
    print("""
    1. Pengguna Biasa
    2. Sebagai Admin 
    3. Daftar Sebagai Pengguna Baru""")
    print()
    menu = input("Pilihan Anda (1/2/3)\t : ")

    if menu == "1":
        print(batas1)
        print("LOGIN SEBAGAI PENGGUNA BIASA".center(55))
        print(batas1)
        usn = input("\nUsername : ")
        pas = input("\nPassword : ")
        if Pengguna_Baru["usn"] == usn and Pengguna_Baru["pas"] == pas:
            print()
            print(batas2)
            print("SELAMAT ANDA BERHASIL LOGIN".center(55))
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
        print("LOGIN SEBAGAI ADMIN".center(55))
        print(batas1)
        usn = input("\nUsername : ")
        pas = input("\nPassword : ")
        if usn == "wibu" and pas == "anime":
            print()
            print(batas2)
            print("SELAMAT SEPUH BERHASIL LOGIN".center(55))
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
                print("KESEMPATAN LOGIN TELAH HABIS!!!".center(55)) 
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
        print("DAFTAR SEBAGAI PENGGUNA BARU".center(55))
        print(batas1)
        Newusn = input("\nUsername : ")
        Newpas = input("\nPassword : ")
        Pengguna_Baru["usn"] = Newusn
        Pengguna_Baru["pas"] = Newpas
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
            print("PILIH MENU YANG ANDA INGINKAN".center(55))
            print(batas1)
            print("""
    [1] Lihat Daftar Anime
    [2] Daftar Anime Berdasarkan Gendre
    [3] Keluar sistem
            """)
            pilihan_user= input("\nSilahkan masukkan menu yang anda pilih : ")

            if pilihan_user == "1":
                os.system('cls')
                print(batas1)
                print(f"BERIKUT DAFTAR ANIME MUSIM {tampilan['1']} INI!!!".center(55))
                print(batas1)
                print()
                urut = 1
                for genre in daftar_anime:
                    animes = daftar_anime[genre]
                    for anime in animes:
                        print(f"{urut}. {anime}")
                        urut += 1
                input("\nEnter untuk kembali ke Menu ...")

            elif pilihan_user == "2":
                os.system('cls')
                print(batas1)
                print("LIHAT ANIME BERDASARKAN GENRE".center(55))
                print(batas1)
                gendre_list = list(daftar_anime.keys())
                for i, gendre in enumerate(gendre_list):
                    print(f"{i + 1}. {gendre}")

                noGen = int(input("Masukkan nomor gendre : ")) - 1
                if 0 <= noGen < len(gendre_list):
                    pilihan = gendre_list[noGen]
                    print(f"\nAnime dalam gendre {pilihan} diantaranya:")
                    for i, anime in enumerate (daftar_anime[pilihan]):
                        print(f"{i+1}. {anime}")
                    input("\nEnter untuk kembali ke Menu ...")
                
                else:
                    print("Gendre tersebut tidak ada dalam daftar")
                    input("\nEnter untuk kembali ke Menu ...")


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
            print("PILIH MENU YANG ADMIN INGINKAN".center(55))
            print(batas1)
            print()
            print(""" 
    [1] Lihat Daftar Anime
    [2] Daftar Anime Berdasarkan Gendre
    [3] Tambah Judul Anime
    [4] Edit Daftar Anime
    [5] Edit Tampilan Musiman
    [6] Hapus Judul Anime 
    [7] Keluar Program""")
            pilihan_admin = input("\nOke masukkan pilihanmu : ")

            if pilihan_admin == "1":
                os.system('cls')
                print(batas1)
                print(f"BERIKUT DAFTAR ANIME MUSIM {tampilan['1']} INI!!!".center(55))
                print(batas1)
                print()
                urut = 1
                for genre in daftar_anime:
                    animes = daftar_anime[genre]
                    for anime in animes:
                        print(f"{urut}. {anime}")
                        urut += 1
                input("\nEnter untuk kembali ke Menu ...")

            elif pilihan_admin == "2":
                os.system('cls')
                print(batas1)
                print("LIHAT ANIME BERDASARKAN GENRE".center(55))
                print(batas1)
                gendre_list = list(daftar_anime.keys())
                for i, gendre in enumerate(gendre_list):
                    print(f"{i + 1}. {gendre}")

                noGen = int(input("Masukkan nomor gendre : ")) - 1
                if 0 <= noGen < len(gendre_list):
                    pilihan = gendre_list[noGen]
                    print(f"\nAnime dalam gendre {pilihan} diantaranya:")
                    for i, anime in enumerate (daftar_anime[pilihan]):
                        print(f"{i+1}. {anime}")
                    input("\nEnter untuk kembali ke Menu ...")

            elif pilihan_admin == "3":
                os.system('cls')
                print(batas1)
                print("MENAMBAHKAN JUDUL ANIME".center(55))
                print(batas1)
                print()
                list_gendre = list(daftar_anime.keys())
                for i, gendre in enumerate(list_gendre):
                    print(f"{i+1}. {gendre}")
                pilihan_hapus = int(input("\nAnime yang ingin ditambah bergendre (angka): ")) -1
                if 0 <= pilihan_hapus < len(list_gendre):
                    gen_pilih = list_gendre[pilihan_hapus]
                    New_judul = input("Masukkan judul anime baru : ")
                    daftar_anime[gen_pilih].append(New_judul)
                    print(f"\nAnime {New_judul} berhasil dimasukkan ke daftar!")
                else:
                    print("Masukkan angka yang valid")
                input("\nKembali ke Menu ...")

            elif pilihan_admin == "4":
                os.system('cls')
                print(batas1)
                print("MENGEDIT DAFTAR ANIME".center(55))
                print(batas1)
                print()
                gendre_list = list(daftar_anime.keys())
                for i, gendre in enumerate(gendre_list):
                    print(f"{i + 1}. {gendre}")
                pilihan_hapus = int(input("\nAnime yang ingin diedit (angka): ")) -1
                if 0 <= pilihan_hapus < len(gendre_list):
                    hapusgen = gendre_list[pilihan_hapus]
                    for i, anime in enumerate(daftar_anime[hapusgen]):
                        print(f"{i+1}. {anime}")
                    
                    edit_nom = int(input("\nMasukkan nomor yang ingin di edit : ")) -1
                    if 0 <= edit_nom < len(daftar_anime[hapusgen]):
                        judul_baru = str(input("Masukkan judul baru : "))
                        daftar_anime[hapusgen][edit_nom] = judul_baru
                        print("\nPerubahan berhasil")
                    else:
                        print("\nNomor tersebut tidak ada dalam daftar")
                else:
                    print("Gendre tersebut tidak ada")
                input("\nEnter untuk kembali ke Menu...")

            elif pilihan_admin == "5":
                os.system('cls')
                print(batas1)
                print("MENGEDIT TAMPILAN MUSIMAN".center(55))
                print(batas1)
                print()
                print("Anda ingin megupdate apa di tampilan?\n")
                print("1. Season saat ini (musim)")
                print("2. Tahun saat ini")
                print()
                pilihUp = input("Masukkan pilihan (1/2): ")
                if pilihUp == "1":
                    gantimusim = str(input("Masukan season saat ini : "))
                    tampilan.update({"1" : f"{gantimusim}"})
                    print("Musim/Season berhasil di update")
                elif pilihUp == "2":
                    gantitahun = int(input("Masukkan tahun saat ini: "))
                    tampilan.update({"2" : f"{gantitahun}"})
                    print("Tahun berhasil di update")
                else:
                    print("pilihan tidak ada")
                input("Tekan enter untuk kemali...")

            elif pilihan_admin == "6":
                os.system('cls')
                print(batas1)
                print("MENGHAPUS JUDUL ANIME DARI DAFTAR".center(55))
                print(batas1)
                print()
                print("Apa yang ingin anda hapus?")
                print("1) Hapus satu judul")
                print("2) Hapus semuanya")
                pilih_hapus = int(input("\nMasukkan pilihan anda : "))

                if pilih_hapus == 1:
                    gendre_list = list(daftar_anime.keys())
                    for i, gendre in enumerate(gendre_list):
                        print(f"{i + 1}. {gendre}")
                    pilihan_hapus = int(input("\nAnime yang ingin anda HAPUS (angka): ")) - 1
                    if 0 <= pilihan_hapus < len(gendre_list):
                        hapusgen = gendre_list[pilihan_hapus]
                        for i, anime in enumerate(daftar_anime[hapusgen]):
                            print(f"{i + 1}. {anime}")
                        hapus_satu = int(input("Masukkan judul yang ingin dihapus: ")) - 1
                        if 0 <= hapus_satu < len(daftar_anime[hapusgen]):
                            del daftar_anime[hapusgen][hapus_satu]
                            print("\nJudul tersebut berhasil dihapus")
                        else:
                            print("\nNomor tersebut tidak ada dalam daftar")
                elif pilih_hapus == "2":
                    daftar_anime.clear()
                    print("\nSEMUA GENDRE DAN JUDUL TELAH DIHAPUS!!")
                else:
                    print("\nSilahkan pilih dengan teliti")
                input("\nEnter untuk kembali ke Menu...")

            elif pilihan_admin == "7":
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
        print("PROGRAM SELESAI".center(55))
        print("TERIMA KASIH ATAS KUNJUNGANNYA".center(55))
        print(batas1)
        break

print("SELESAI")