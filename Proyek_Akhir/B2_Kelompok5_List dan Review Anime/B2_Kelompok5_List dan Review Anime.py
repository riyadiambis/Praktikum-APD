import os
import json
from datetime import datetime
import quizs_file2
from colorama import init, Fore, Back, Style

# Initialize Colorama
init(autoreset=True)  # This will reset the color after each print


''' DEKLARASI VARIABEL '''
kesempatan_login = 3
batas1 = "=" * 70
batas2 = "=" * 70
batas_kanan = ">"*70
batas_kiri = "<"*70
batas_garis= "-"*70
Admin = False 
User  = False
Exit = False
usn_komen = None

file_diskusi = "diskusi_File_Eksternal.json"
file_pengguna = "user_File_Eksternal.json"
file_anime= 'data_anime_File_Eksternal.json'

genre_dict = {
    "1": "Action",
    "2": "Adventure",
    "3": "Comedy",
    "4": "Drama",
    "5": "Fantasy",
    "6": "Horror",
    "7": "Mystery",
    "8": "Music",
    "9": "Psychological",
    "10": "Romance",
    "11": "School",
    "12": "Sci-Fi",
    "13": "Shounen",
    "14": "Slice of Life",
    "15": "Sports",
    "16": "Supernatural"
}

# Daftar Top 20 Anime (judul, tahun)
top_20_anime = [ 
    ["Attack on Titan", 2013],
    ["Death Note", 2006],
    ["Fullmetal Alchemist: Brotherhood", 2009],
    ["Naruto", 2002],
    ["One Piece", 1999],
    ["My Hero Academia", 2016],
    ["Demon Slayer: Kimetsu no Yaiba", 2019],
    ["Steins;Gate", 2011],
    ["Sword Art Online", 2012],
    ["Hunter x Hunter", 2011],
    ["Your Name", 2016],
    ["Neon Genesis Evangelion", 1995],
    ["Code Geass", 2006],
    ["Cowboy Bebop", 1998],
    ["Spirited Away", 2001],
    ["Mob Psycho 100", 2016],
    ["Tokyo Ghoul", 2014],
    ["The Promised Neverland", 2019],
    ["Vinland Saga", 2019],
    ["Re:Zero - Starting Life in Another World", 2016],
]

''' FUNGSI DAFTAR DAN LOGIN '''
# Menyimpan data pengguna baru ke Database
def daftar():
    os.system("cls || clear")
    print("Membuat Akun")
    usn = input("Masukkan Username: ")
    pas = input("Masukkan Password: ")
    try:
        with open(file_pengguna, "r") as file:
            users = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        users = {}
    users[usn] = pas
    with open(file_pengguna, "w") as file:
        json.dump(users, file, indent=4)
    print("Pendaftaran Berhasil\n")

# Mengecek data pengguna di database
def user_login():
    while True:
        global kesempatan_login, usn_komen
        os.system("cls || clear")
        print(Fore.LIGHTBLUE_EX + batas1, "\n")
        print(Fore.LIGHTYELLOW_EX + "Silahkan Login terlebih dahulu!\n".center(70))
        print(Fore.LIGHTBLUE_EX + batas1, "\n")
        print(Fore.LIGHTWHITE_EX + batas_garis)
        usn = input(Fore.LIGHTYELLOW_EX + "Username: ")
        pas = input(Fore.LIGHTYELLOW_EX + "Password: ")
        print(Fore.LIGHTWHITE_EX + batas_garis)
        try:
            with open(file_pengguna, "r") as file:
                users = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            users = {}
        if usn == "admin" and pas == "admin":
            print()
            print(batas2)
            print(Fore.LIGHTYELLOW_EX + "SELAMAT SEPUH BERHASIL LOGIN".center(70))
            print(batas2, "\n")
            return "ADMIN"
            input("Tekan Enter untuk melanjutkan...")
        elif usn in users and users[usn] == pas:
            print()
            print(batas2)
            print(Fore.LIGHTYELLOW_EX + "ANDA BERHASIL LOGIN".center(70))
            print(batas2,"\n")
            usn_komen = usn
            return "USER"
            input("Tekan Enter untuk melanjutkan...")
        else:
            print(Fore.LIGHTYELLOW_EX + "Login Gagal Silahkan Login Ulang")
            input(Fore.LIGHTYELLOW_EX + "Tekan enter untuk melakukan login...")
            return user_login()

''' FUNGSI TAMPILAN '''
def load_data(file_anime):
    try:
        with open(file_anime, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading data: {e}")
        return []

# Fungsi untuk menyimpan data ke file JSON
def simpan_data(file_anime, data):
    try:
        with open(file_anime, 'w') as file:
            json.dump(data, file, indent=4)
    except IOError as e:
        print(f"Error saving data: {e}")

# Fungsi untuk menghapus duplikasi data
def hapus_duplikat(anime_list):
    judul_unik = set()
    anime_unik = []
    for anime in anime_list:
        if anime['title'] not in judul_unik:
            judul_unik.add(anime['title'])
            anime_unik.append(anime)
    return anime_unik

# Fungsi untuk mencari anime berdasarkan judul
def cari_dengan_judul(anime_list, title):
    anime_unik_list = hapus_duplikat(anime_list)
    results = []
    for anime in anime_unik_list:
        if title.lower() in anime["title"].lower():
            results.append(anime)
    return results

# Fungsi untuk mencetak judul anime berdasarkan tahun
def tampil_urut_tahun(year):
    try:
        with open('data_anime_File_Eksternal.json', 'r') as file:
            anime_data = json.load(file)
        print(f"Daftar judul anime yang dirilis pada tahun {year}:")
        anime_unik_list = hapus_duplikat(anime_data)
        Tahun = False
        for anime in anime_unik_list:
            if anime["year"] == year:
                print(f"- {anime['title']}")
                Tahun = True
        if not Tahun:
            print("Tidak ada anime yang ditemukan pada tahun tersebut.")
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading anime data: {e}")

# Fungsi untuk mencetak judul anime berdasarkan genre dan jumlah episodenya
def cetak_berdasarkan_gendre(anime_list, genre):
    print(f"Daftar judul anime berdasarkan genre yang dipilih (Contoh: {genre}):")
    anime_unik_list = hapus_duplikat(anime_list)
    for anime in anime_unik_list:
        if genre in anime["genres"]:
            print(f"- {anime['title']}: {anime['episodes']} episodes")

# Fungsi untuk mesin pencari
def mesin_pencari_judul():
    anime_data = load_data("data_anime_File_Eksternal.json")
    anime_data = hapus_duplikat(anime_data)
    cari_judul = input("Masukkan judul anime yang ingin dicari: ").strip().lower()
    hasil_pencarian = []
    for anime in anime_data:
        if cari_judul in anime["title"].lower():
            hasil_pencarian.append(anime)
    if hasil_pencarian:
        for anime in hasil_pencarian:
            print(f"Title: {anime['title']}")
            print(f"Year: {anime['year']}")
            print(f"Genres: {', '.join(anime['genres'])}")
            print(f"Episodes: {anime['episodes']}")
            print()
    else:
        print("Anime tidak ditemukan.")

# Fungsi untuk menampilkan anime berdasarkan abjad
def tampil_urut_abjad():
    try:
        with open('data_anime_File_Eksternal.json', 'r') as file:
            data = json.load(file)
        data = hapus_duplikat(data)
        hasil = {}
        for anime in data:
            judul = anime['title']
            karakter_awal = judul[0].upper()  
            if karakter_awal not in hasil:
                hasil[karakter_awal] = []
            hasil[karakter_awal].append(judul)
        for key in hasil.keys():
            hasil[key] = sorted(hasil[key])
        for key in sorted(hasil.keys()):
            print(key)
            for judul in hasil[key]:
                print(f"- {judul}")
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading anime data: {e}")

# Fungsi menampilkan pilihan Genre
def daftar_pilihan_gendre():
    print("1) Action")
    print("2) Adventure")
    print("3) Comedy")
    print("4) Drama")
    print("5) Fantasy")
    print("6) Horror")
    print("7) Mystery")
    print("8) Music")
    print("9) Psychological")
    print("10) Romance")
    print("11) School")
    print("12) Sci-Fi")
    print("13) Shounen")
    print("14) Slice Of Life")
    print("15) Sports")
    print("16) Supernatural")

# Fungsi menampilkan top 20 anime
def tampilkan_top_20_anime():
    print("Top 20 Anime:")
    for i in range(len(top_20_anime)):
        judul = top_20_anime[i][0]
        tahun = top_20_anime[i][1]
        print(f"{i + 1}. {judul} ({tahun})")

''' FUNGSI CRUD System'''
# Fungsi untuk mengedit anime di dalam json
def update_anime(data):
    anime_data = load_data("data_anime_File_Eksternal.json")
    cari_judul = input("Masukkan judul anime yang ingin diperbarui: ")
    hasil_pencarian = cari_dengan_judul(anime_data, cari_judul)
    if hasil_pencarian:
        print("\nHasil pencarian:")
        for index, anime in enumerate(hasil_pencarian, start=1): 
            print(f"{index}. Title: {anime['title']}")
            print(f"   Year: {anime['year']}")
            print(f"   Genres: {', '.join(anime['genres'])}")
            print(f"   Episodes: {anime['episodes']}")
            print()
        try:
            pilihan = int(input("Pilih nomor anime yang ingin diperbarui: ")) - 1   
            if 0 <= pilihan < len(hasil_pencarian):
                anime_to_update = hasil_pencarian[pilihan]  
                new_title = input("Masukkan judul anime baru: ").strip()  
                new_year = int(input("Masukkan tahun rilis baru: "))
                new_genres = input("Masukkan genre baru (pisahkan dengan koma): ").split(", ")
                new_episodes = int(input("Masukkan jumlah episode baru: "))
                pembaruan = False 
                for anime in anime_data:
                    if anime["title"].strip().lower() == anime_to_update["title"].strip().lower():
                        anime["title"] = new_title
                        anime["year"] = new_year
                        anime["genres"] = new_genres
                        anime["episodes"] = new_episodes
                        pembaruan = True  
                        print("Anime berhasil diperbarui.")
                        break 
                if pembaruan:
                    simpan_data("data_anime_File_Eksternal.json", anime_data)  
                else:
                    print("Anime tidak ditemukan untuk diperbarui.") 
            else:
                print("Pilihan tidak ada, silahkan pilih nomor lain.")
        except ValueError:
            print("Pilihan harus berupa angka!")
    else:
        print("Anime tidak ditemukan.")
    return data

# Fungsi untuk menambahkan anime ke 
def create_anime(data, title, year, genres, episodes):
    new_anime = {
        "title": title,
        "year": year,
        "genres": genres,
        "episodes": episodes
    }
    data.append(new_anime)
    return hapus_duplikat(data)

# Fungsi untuk menghapus judul anime dari data
def hapus_anime(data):
    anime_data = load_data("data_anime_File_Eksternal.json")
    cari_judul = input("Masukkan judul anime yang ingin dihapus: ")
    hasil_pencarian = cari_dengan_judul(anime_data, cari_judul)  
    if hasil_pencarian:
        print("\nHasil pencarian:")
        for index, anime in enumerate(hasil_pencarian):
            print(f"{index + 1}. Title: {anime['title']}")
            print(f"   Year: {anime['year']}")
            print(f"   Genres: {', '.join(anime['genres'])}")
            print(f"   Episodes: {anime['episodes']}")
            print() 
        pilihan = input("Pilih nomor anime yang ingin dihapus: ")     
        try:
            pilihan = int(pilihan) - 1
            if 0 <= pilihan < len(hasil_pencarian):
                konfirmasi = input("Apakah Anda yakin ingin menghapus anime ini? (y/n): ").lower()
                if konfirmasi == 'y':
                    anime_to_delete = hasil_pencarian[pilihan]
                    data = [anime for anime in data if anime["title"].strip().lower() != anime_to_delete["title"].strip().lower()]
                    print("Anime berhasil dihapus.")
                else:
                    print("Penghapusan dibatalkan.")
            else:
                print("Pilihan tidak valid.")
        except ValueError:
            print("Input harus berupa angka.")
    else:
        print("Anime tidak ditemukan.")
    return data

# Fungsi Untuk mengedit TOP 20 anime
def edit_top_20_anime():
    tampilkan_top_20_anime()  
    try:
        pilihan = int(input("Masukkan nomor anime yang ingin diedit (1-20): ")) - 1
        if 0 <= pilihan < len(top_20_anime):
            print(f"Editing: {top_20_anime[pilihan][0]} ({top_20_anime[pilihan][1]})")
            judul_baru = input("Masukkan judul baru (tekan Enter untuk tidak mengubah): ")
            tahun_baru = input("Masukkan tahun rilis baru (tekan Enter untuk tidak mengubah): ")
            if judul_baru:
                top_20_anime[pilihan][0] = judul_baru
            if tahun_baru:
                top_20_anime[pilihan][1] = int(tahun_baru)
            print("Daftar anime berhasil diperbarui.")
        else:
            print("Pilihan tidak valid.")
    except ValueError:
        print("Input harus berupa angka.")

''' FUNGSI UNTUK FITUR DISKUSI'''
#Fungsi untuk memuat diskusi dari file json
def muat_diskusi(nama_file):
    try:
        with open(nama_file, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"comments": []}

#Fungsi untuk menyimpan diskusi ke file json
def simpan_diskusi(data, nama_file):
    try:
        with open(nama_file, "w") as file:
            json.dump(data, file, indent=4)
    except IOError:
        print(f"Gagal menyimpan diskusi ke file '{nama_file}'")

#Funsi untuk menampilkan diskusi
def tampilkan_diskusi(data, usn_login):
    if not data["comments"]:
        print("Belum ada diskusi.")
    else:
        os.system("cls || clear")
        print(batas_kanan)
        print("DISKUSI".center(70))
        print(batas_kiri)
        print("\n")
        print(batas_garis)
        for komentar in data["comments"]:
            if komentar['username'] == usn_login:
                print(f"\033[92m{komentar['username']}\033[0m")
            else:
                print(komentar['username'])
            print(komentar['comment'])
            print(f"({komentar['date']})\n")  
            print(batas_garis)

#Fungsi untuk menambahkan pesan user ke dalam diskusi
def tambah_diskusi(data_diskusi, nama_pengguna, pesan):
    waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    diskusi_baru = {
        "username": nama_pengguna,
        "comment": pesan,
        "date": waktu
    }
    data_diskusi["comments"].append(diskusi_baru)
    if len(data_diskusi["comments"]) > 30:
        data_diskusi["comments"].pop(0)
    return data_diskusi

#Fungsi untuk mengedit pesan yang sebelumnya ditulis user
def edit_diskusi(file_diskusi, usn_login):
    os.system("cls || clear")
    print(batas_kanan)
    print("Mengedit Pesan Saya".center(70))
    print(batas_kiri, "\n")
    data_diskusi = muat_diskusi(file_diskusi) 
    diskusi_user = [] 
    for d in data_diskusi["comments"]:
        if d['username'] == usn_login:
            diskusi_user.append(d)
    if not diskusi_user:
        print("Anda tidak memiliki diskusi yang dapat diedit.")
        input("Tekan Enter untuk kembali ke menu sebelumnya...")
        return
    print("Diskusi Anda:")
    for index, d in enumerate(diskusi_user, start=1): 
        print(f"{index}. {d['comment']}")
    diskusi_nomor = int(input("Masukkan nomor diskusi yang ingin diedit: "))
    if 1 <= diskusi_nomor <= len(diskusi_user):  
        diskusi_baru = input("Tulis diskusi baru: ")
        diskusi_user[diskusi_nomor - 1]['comment'] = diskusi_baru 
        simpan_diskusi(data_diskusi, file_diskusi)
        print("Diskusi berhasil diedit!")
    else:
        print("Nomor diskusi tidak valid.")
    input("Tekan Enter untuk kembali ke menu sebelumnya...") 

#Fungsi untuk menghapus pesan yang sebelumnya ditulis user
def hapus_diskusi(file_diskusi, usn_login):
    os.system("cls || clear")
    print(batas_kanan)
    print("Menghapus Pesan Saya".center(70))
    print(batas_kiri, "\n")
    data_diskusi = muat_diskusi(file_diskusi) 
    diskusi_user = [d for d in data_diskusi["comments"] if d['username'] == usn_login]
    if not diskusi_user:
        print("Anda tidak memiliki diskusi yang dapat dihapus.")
        input("Tekan Enter untuk kembali ke menu sebelumnya...")
        return
    print("Diskusi Anda:")
    for index, d in enumerate(diskusi_user, start=1):
        print(f"{index}. {d['comment']}")
    diskusi_nomor = int(input("Masukkan nomor diskusi yang ingin dihapus: "))
    if 1 <= diskusi_nomor <= len(diskusi_user):
        komentar_yang_hilang = diskusi_user[diskusi_nomor - 1]
        data_diskusi["comments"].remove(komentar_yang_hilang) 
        simpan_diskusi(data_diskusi, file_diskusi)
        print("Diskusi berhasil dihapus!")
    else:
        print("Nomor diskusi tidak valid.")
    input("Tekan Enter untuk kembali ke menu sebelumnya...") 


''' INI ADALAH PROGRAM UTAMA'''
os.system("cls || clear")
print(Fore.LIGHTGREEN_EX + batas1)
print(Fore.LIGHTGREEN_EX + batas2)
print(Fore.LIGHTGREEN_EX + "||",Fore.LIGHTBLUE_EX + "SELAMAT DATANG DI PROGRAM".center(64), Fore.LIGHTGREEN_EX + "||")
print(Fore.LIGHTGREEN_EX + "||", Fore.LIGHTBLUE_EX + "PROTOTIPE LIST DAN REVIEW ANIME".center(64), Fore.LIGHTGREEN_EX + "||")
print(Fore.LIGHTGREEN_EX + batas2)
print(Fore.LIGHTGREEN_EX + batas1, "\n\n")
input(Fore.LIGHTRED_EX + "Tekan ENTER untuk MEMULAI.....")

# MENU LOGIN DAN DAFTAR
while True:
    os.system("cls || clear")
    print(Fore.LIGHTRED_EX + batas1)
    print(Fore.LIGHTRED_EX +"||", Fore.LIGHTMAGENTA_EX + "MENU DAFTAR DAN LOGIN".center(64), Fore.LIGHTRED_EX + "||")
    print(Fore.LIGHTRED_EX + batas1, "\n")
    print(Fore.LIGHTYELLOW_EX + """
    [1] Login 
    [2] Daftar 
    [3] Exit\n\n""")
    dafLog = str(input(Fore.LIGHTRED_EX + "Masukkan pilihan Anda: ")) 
    if dafLog == "1": 
        result = user_login() 
        if result == "ADMIN": 
            Admin = True 
        elif result == "USER": 
            User = True 
        else: 
            Exit = True 
    elif dafLog == "2": 
        daftar() 
        print("Tekan Enter untuk kembali ke MENU LOGIN...") 
    elif dafLog == "3": 
        break 
    else: 
        print("Pilihan tidak ada") 
        input(Fore.LIGHTRED_EX  + "Tekan Enter untuk login ulang...")

    while Admin: 
        # Menu ADMIN 
        os.system("cls || clear") 
        print(Fore.LIGHTBLUE_EX + batas1) 
        print(Fore.LIGHTBLUE_EX + "||", Fore.LIGHTYELLOW_EX  + "PILIHAN MENU UTAMA ADMIN".center(64), Fore.LIGHTBLUE_EX + "||") 
        print(Fore.LIGHTBLUE_EX + batas1, "\n") 
        print(Fore.LIGHTYELLOW_EX  + """ 
        [1] Menu Tampilan dan Fitur User 
        [2] Menu Perubahan Program 
        [0] LogOut""") 
        Utama_Admin = str(input(Fore.LIGHTYELLOW_EX  + "Pilih Menu Admin Sekunder: ")) 
        if Utama_Admin == "1": 
            while True: 
                os.system("cls || clear") 
                print(batas1) 
                print("PILIHAN MENU TAMPILAN DAN FITUR USER".center(70)) 
                print(batas1, "\n") 
                print(""" 
        a) List Anime Berdasarkan Abjad 
        b) List Anime Berdasarkan Tahun Rilis 
        c) Searching Judul Anime 
        d) Mencari Judul Berdasarkan Genre 
        e) Menampilkan TOP 20 Anime Terpopuler 
        f) Uji Kuiz Pengetahuan Wibu 
        0) Kembali ke Menu Utama Admin""") 
                Menu_dan_User = str(input("Pilih Apa yang Ingin Anda Lihat: ").lower()) 
                if Menu_dan_User == "a": 
                    os.system("cls || clear") 
                    print(batas1) 
                    print("Menampilkan Anime Berdasarkan Abjad".center(70)) 
                    print(batas1, "\n") 
                    tampil_urut_abjad() 
                    input("Tekan Enter untuk kembali ke menu sebelumnya...") 
                elif Menu_dan_User == "b": 
                    os.system("cls || clear") 
                    print(batas1) 
                    print("Menampilkan Anime Berdasarkan Tahun Rilis".center(70)) 
                    print(batas1, "\n") 
                    cari_tahun = int(input("Masukkan tahun anime yang ingin dicari: ")) 
                    tampil_urut_tahun(cari_tahun) 
                    input("Tekan Enter untuk kembali ke menu sebelumnya...") 
                elif Menu_dan_User == "c": 
                    os.system("cls || clear") 
                    print(batas1) 
                    print("Mencari Judul Anime".center(70)) 
                    print("Anda tidak harus mengetikkan judul secara lengkap") 
                    print("Mengetikkan beberapa huruf saja juga diperbolehkan\n") 
                    print(batas1,"\n") 
                    mesin_pencari_judul() 
                    print(batas1, "\n") 
                    input("Tekan Enter untuk kembali ke menu sebelumnya...") 
                elif Menu_dan_User == "d": 
                    os.system("cls || clear") 
                    print(batas1) 
                    print("Mencari Judul Berdasarkan Genre".center(70)) 
                    print(batas1, "\n") 
                    print(batas_garis) 
                    daftar_pilihan_gendre() 
                    print(batas_garis) 
                    print("0) Kembali ke Menu Sebelumnya") 
                    print(batas_garis) 
                    pilih_genre = str(input("Masukkan pilihan genre: ")) 
                    if pilih_genre in genre_dict and pilih_genre != "0": 
                        genre = genre_dict[pilih_genre] 
                        file_anime="data_anime_File_Eksternal.json" 
                        anime_data=load_data(file_anime) 
                        cetak_berdasarkan_gendre(anime_data, genre) 
                        input("Tekan Enter untuk kembali...") 
                    elif pilih_genre == "0": 
                        input("Tekan Enter untuk kembali...") 
                    else: 
                        print("Pilihan tidak ada dalam daftar...") 
                        input("Tekan Enter untuk kembali...") 
                elif Menu_dan_User == "e": 
                    os.system("cls || clear") 
                    print(batas1) 
                    print("Menampilkan TOP 20 Anime Terpopuler".center(70)) 
                    print(batas1, "\n") 
                    tampilkan_top_20_anime() 
                    input("Tekan Enter untuk kembali ke menu sebelumnya...") 
                elif Menu_dan_User == "f": 
                    os.system("cls || clear") 
                    print(batas1) 
                    print("UJI KUIS PENGETAHUAN WIBU".center(70)) 
                    print(batas1, "\n") 
                    quizs_file2.soal() 
                    input("Tekan Enter untuk kembali ke menu sebelumnya...") 
                elif Menu_dan_User == "0": 
                    break 
                else: 
                    print("Pilihan yang anda masukkan tidak ada") 
                    input("Tekan Enter untuk kembali ke menu sebelumnya...") 

        elif Utama_Admin == "2": 
            while True: 
                os.system("cls || clear") 
                print(batas1) 
                print("MENU CRUD PROGRAM".center(70)) 
                print(batas1, "\n") 
                print(""" 
        a) Tambahkan Anime Baru 
        b) Mengedit Judul Anime 
        c) Mengedit TOP 20 Anime 
        d) Menghapus List Anime 
        0) Kembali ke Menu Utama Admin""") 
                Perubahan_Program = str(input("Pilih mana yang ingin diubah: ").lower()) 
                if Perubahan_Program == "a": 
                    os.system("cls || clear") 
                    print(batas1) 
                    print("Tambahkan Anime Baru".center(70)) 
                    print(batas1, "\n") 
                    file_anime = 'data_anime_File_Eksternal.json' 
                    anime_data = load_data(file_anime) 
                    new_title = input("Masukkan judul anime baru: ") 
                    new_year = int(input("Masukkan tahun rilis: ")) 
                    new_genres = input("Masukkan genre (pisahkan dengan koma): ").split(", ") 
                    new_episodes = int(input("Masukkan jumlah episode: ")) 
                    anime_data = create_anime(anime_data, new_title, new_year, new_genres, new_episodes) 
                    simpan_data(file_anime, anime_data) 
                    print("Anime baru telah ditambahkan ke dalam database.") 
                    input("Tekan Enter untuk kembali ke menu sebelumnya...") 
                elif Perubahan_Program == "b": 
                    os.system("cls || clear") 
                    print(batas1) 
                    print("Mengedit Judul Anime".center(70)) 
                    print(batas1, "\n") 
                    print("!) Sebelum melakukan pengeditan anime, anda harus mencari judulnya dahulu") 
                    print("!) Anda dapat menuliskan penggalan judul saja tanpa harus lengkap") 
                    print("!) Jika judul anime tidak ditemukan, anda tidak dapat melakukan pengeditan") 
                    print(batas_kanan) 
                    anime_data = load_data(file_anime) 
                    anime_data = update_anime(anime_data) 
                    input("Tekan Enter untuk kembali ke menu sebelumnya...") 
                elif Perubahan_Program == "c": 
                    os.system("cls || clear") 
                    print(batas1) 
                    print("Mengedit TOP 20 Anime".center(70)) 
                    print(batas1) 
                    edit_top_20_anime() 
                    input("Tekan Enter untuk kembali ke menu sebelumnya...") 
                elif Perubahan_Program == "d": 
                    os.system("cls || clear") 
                    print(batas1) 
                    print("Menghapus List Anime".center(70)) 
                    print(batas1, "\n") 
                    data_anime = load_data("data_anime_File_Eksternal.json") 
                    data_anime = hapus_anime(data_anime) 
                    simpan_data("data_anime_File_Eksternal.json", data_anime)  # Simpan kembali data setelah penghapusan 
                    input("Tekan Enter untuk kembali ke menu sebelumnya...") 
                elif Perubahan_Program == "0": 
                    break 
                else: 
                    print("Perhatikan opsi dan input sesuai perintah") 
                    input("Tekan Enter untuk kembali ke menu sebelumnya...") 

        elif Utama_Admin == "0": 
            os.system("cls || clear") 
            pilih_out = input("Apakah anda yakin ingin LogOut (y|n): ").lower() 
            if pilih_out in ["y", "ya"]: 
                Admin = False 
                Exit = True 
            elif pilih_out in ["n", "tidak"]: 
                print("Oke anda tidak jadi keluar") 
                input("Tekan Enter untuk kembali ke menu sebelumnya...") 
            else: 
                print("Pilihan tidak ada, silahkan ulangi!") 
                input("Tekan Enter untuk kembali ke menu sebelumnya...") 

        else: 
            print("Pilihan yang anda masukkan tidak ada, silahkan ulangi!") 
            input("Tekan Enter untuk kembali...") 

    while User: 
        os.system("cls || clear") 
        print(Fore.LIGHTBLUE_EX + batas1) 
        print(Fore.LIGHTYELLOW_EX + "PILIHAN MENU UTAMA USER".center(70)) 
        print(Fore.LIGHTBLUE_EX + batas1, "\n") 
        print(Fore.LIGHTYELLOW_EX + """ 
        [1] Mencari Anime (Search)
        [2] Mengurutkan Judul Anime
        [3] Menampilkan Top 20 Anime 
        [4] Cek Pengetahuan Anime (QUIZ) 
        [5] Forum Diskusi Anime
        [0] LogOut\n""") 
        print(Fore.LIGHTYELLOW_EX + batas1, "\n") 
        pilihan_user = str(input(Fore.LIGHTYELLOW_EX + "Masukkan Pilihan Anda: ")) 
        if pilihan_user == "1": 
            while True: 
                os.system("cls") 
                print(batas1) 
                print("MESIN PENCARI ANIME".center(70)) 
                print(batas1, "\n") 
                print("!) Anda tidak harus mengetikkan judul secara lengkap") 
                print("!) Mengetikkan beberapa huruf saja juga diperbolehkan\n") 
                print(batas1, "\n") 
                mesin_pencari_judul() 
                print(batas_kanan) 
                pilih_cari = input("Apakah anda masih ingin mencari judul anime? (y|n): ").lower()
                if pilih_cari == "y":
                    continue
                elif pilih_cari == "n":
                    input("Tekan Enter untuk kembali ke menu sebelumnya...")
                    break
                else:
                    print("Pilihan tidak ada, memaksa untuk kembali ke menu awal")
                    break

        elif pilihan_user == "2": 
            while True: 
                os.system("cls || clear") 
                print(batas_kanan) 
                print("Pilihan Untuk Menampilkan Anime".center(70)) 
                print(batas_kiri, "\n") 
                print("a) Tampilkan Anime Berdasarkan Abjad") 
                print("b) Tampilkan Anime Berdsarkan Gendre") 
                print("c) Tampilkan Anime Berdasarkan Tahun Rilis")
                print("0) Kembali ke Menu Sebelumnya") 
                pilih_tampil = str(input("Masukkan pilihan anda: ").lower()) 
                if pilih_tampil == "a": 
                    os.system("cls || clear") 
                    print(batas_kanan) 
                    print("Anime Berdasarkan Urutan Abjad") 
                    print(batas_kiri, "\n") 
                    tampil_urut_abjad() 
                    input("Tekan Enter untuk kembali...") 
                elif pilih_tampil == "b": 
                    while True:
                        os.system("cls || clear") 
                        print(batas_kanan) 
                        print("Pilih Genre Anime Untuk Mencari".center(70)) 
                        print(batas_kiri, "\n") 
                        print(batas_garis) 
                        daftar_pilihan_gendre() 
                        print(batas_garis) 
                        print("0) Kembali ke Menu Sebelumnya") 
                        print(batas_garis) 
                        pilih_genre = str(input("Masukkan pilihan genre: ")) 
                        if pilih_genre in genre_dict and pilih_genre != "0": 
                            genre = genre_dict[pilih_genre] 
                            file_anime="data_anime_File_Eksternal.json" 
                            anime_data=load_data(file_anime) 
                            cetak_berdasarkan_gendre(anime_data, genre) 
                            input("Tekan Enter untuk kembali...") 
                        elif pilih_genre == "0": 
                            input("Tekan Enter untuk kembali...") 
                            break
                        else: 
                            print("Pilihan tidak ada dalam daftar...") 
                            input("Tekan Enter untuk kembali...") 
                elif pilih_tampil == "c":
                    os.system("cls || clear") 
                    print(batas_kanan) 
                    print("Anime Berdasarkan Tahun Rilis") 
                    print(batas_kiri, "\n") 
                    cari_tahun = int(input("Masukkan tahun anime yang ingin dicari: ")) 
                    tampil_urut_tahun(cari_tahun) 
                    input("Tekan Enter untuk kembali...") 
                elif pilih_tampil == "0": 
                    break 
                else: 
                    print("Pilihan tidak ada, silahkan ulangi!") 
                    input("Tekan Enter untuk kembali...") 

        elif pilihan_user == "3": 
            os.system("cls || clear") 
            print(batas1) 
            print("Top 20 Anime".center(70)) 
            print(batas1, "\n") 
            tampilkan_top_20_anime() 
            input("Tekan Enter untuk kembali ke menu sebelumnya...") 

        elif pilihan_user == "4": 
            os.system("cls || clear") 
            print(batas1) 
            print("Cek Pengetahuan Anime (QUIZ)".center(70)) 
            print(batas1, "\n") 
            quizs_file2.soal() 
            input("Tekan Enter untuk kembali ke menu sebelumnya...") 

        elif pilihan_user == "5": 
            while True: 
                os.system("cls || clear") 
                print(batas1) 
                print("FITUR DISKUSI ANIME".center(70)) 
                print(batas1, "\n") 
                print("a) Lihat Diskusi") 
                print("b) Buat Pesan Baru")
                print("c) Mengedit Pesan Saya")
                print("d) Menghapus Pesan Saya")
                print("0) Kembali ke menu sebelumnya") 
                pilih_diskusi = str(input("Masukkan pilihan menu : ").lower()) 
                print()
                if pilih_diskusi == "a": 
                    data_diskusi = muat_diskusi(file_diskusi) 
                    tampilkan_diskusi(data_diskusi, usn_komen)  # Menampilkan diskusi dengan parameter username
                    input("Tekan Enter untuk kembali ke menu sebelumnya...") 

                elif pilih_diskusi == "b": 
                    os.system("cls || clear")
                    print(batas_kanan)
                    print("Menuliskan Pesan Diskusi".center(70))
                    print(batas_kiri, "\n")
                    data_diskusi = muat_diskusi(file_diskusi) 
                    nama_pengguna = usn_komen 
                    pesan_input = input("Tulis Pesan Anda : ")  # Mengubah komentar menjadi pesan
                    data_diskusi = tambah_diskusi(data_diskusi, nama_pengguna, pesan_input)  # Mengubah fungsi dari komentar ke diskusi
                    simpan_diskusi(data_diskusi, file_diskusi) 
                    print("\n|Pesan berhasil ditambahkan|")  # Mengubah pesan berhasil
                    input("Tekan Enter untuk kembali ke menu sebelumnya...") 

                elif pilih_diskusi == "c": 
                    try:
                        edit_diskusi(file_diskusi, usn_komen)  # Mengubah fungsi dari edit_pesan menjadi edit_diskusi
                    except Exception:
                        print("Terjadi kesalahan saat mengedit pesan. Pastikan Anda memasukkan nomor diskusi yang valid dan Anda memiliki hak untuk mengeditnya.")

                elif pilih_diskusi == "d": 
                    try:
                        hapus_diskusi(file_diskusi, usn_komen)  # Mengubah fungsi dari hapus_pesan menjadi hapus_diskusi
                    except Exception:
                        print("Terjadi kesalahan saat menghapus pesan. Pastikan Anda memasukkan nomor diskusi yang valid dan Anda memiliki hak untuk menghapusnya.") 

                elif pilih_diskusi == "0": 
                    input("Tekan Enter untuk kembali ke menu sebelumnya...") 
                    break 
                
                else: 
                    print("Pilihan tidak ada, silahkan ulangi!") 
                    input("Tekan Enter untuk kembali ke menu sebelumnya...") 

        elif pilihan_user == "0": 
            os.system("cls || clear") 
            print(batas1)
            print("Konfirmasi Keluar".center(70))
            print(batas1,"\n")
            pilih_out = str(input("Apakah anda yakin ingin LogOut? (y|n): ")) 
            if pilih_out in ["y", "ya"]: 
                User = False 
                Exit = True 
            elif pilih_out in ["n", "tidak"]: 
                print("Oke anda tidak jadi keluar") 
                input("Tekan Enter untuk kembali ke menu sebelumnya...") 
            else: 
                print("Pilihan tidak ada, silahkan ulangi!") 
                input("Tekan Enter untuk kembali ke menu sebelumnya...") 

        else: 
            print("Pilihan yang anda masukkan tidak ada, silahkan ulangi!") 
            input("Tekan Enter untuk kembali...") 

    while Exit: 
        os.system("cls || clear") 
        print(batas2) 
        print("ANDA TELAH KELUAR DARI PROGRAM".center(70)) 
        print(batas2, "\n") 
        input("Tekan Enter untuk kembali ke Menu Login") 
        break 

os.system("cls || clear") 
print(batas2)
print("Terima Kasih".center(70)) 
print(batas2, "\n\n\n")