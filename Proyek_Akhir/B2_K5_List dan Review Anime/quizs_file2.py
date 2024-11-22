import os
from colorama import init, Fore, Back, Style
batas1 = "=" * 100
batas4 = "-" * 100
batas2 = "_" * 100

# Variabel untuk skor total dan jumlah soal benar
score = 0
correct_answers = 0

# Fungsi untuk konfirmasi sebelum melanjutkan ke stage berikutnya

# Fungsi untuk menentukan rank berdasarkan skor
def evaluate_rank(score, correct_answers):
    if score > 23000 and correct_answers >= 21:
        return "Wibu Elite", "Kamu adalah seorang wibu sejati yang telah mencapai level tertinggi! Pengaruhmu di dunia anime sangat besar dan kamu adalah inspirasi bagi banyak orang."
    elif score >= 15000 and correct_answers >= 18:
        return "SenBu", "Kamu adalah seorang seniman anime yang berbakat! Karya-karyamu sangat inspiratif dan menunjukkan bakatmu yang luar biasa."
    elif score >= 10000 and correct_answers >= 15:
        return "Weeaboo", "Kamu sangat mengagumi budaya Jepang? Kamu adalah seorang weeaboo sejati!"
    elif score >= 7000 and correct_answers >= 12:
        return "Nikijon", "Hidupmu sudah tidak bisa lepas dari anime? Kamu adalah seorang nikijon sejati!"
    elif score >= 3500 and correct_answers >= 10:
        return "Otamega", "Kamu adalah ahli sejati dalam fandommu! Pengetahuanmu yang mendalam tentang karakter dan cerita sangat menginspirasi."
    elif score >= 2000 and correct_answers >= 5:
        return "Otaku", "Kamu adalah seorang otaku sejati! Pengetahuanmu tentang anime sangat luas."
    elif score >= 500:
        return "Newbie", "Baru mulai tertarik dengan dunia anime? Selamat datang!"
    else:
        return "Bukan Wibu", "Sayang sekali anda belum cukup untuk di sebut WIBU, tetap tingkatkan motivasi anda dalam menjelajahi dunia anime ya!!!"

def konfirmasi_lanjut():
    global score, correct_answers
    while True:
        konfirmasi = input("Apakah Anda ingin melanjutkan ke stage berikutnya? (y/n): ").lower()
        if konfirmasi == 'y':
            return True
        elif konfirmasi == 'n':
            global score, correct_answers
            os.system('cls')
            result = evaluate_rank(score, correct_answers)
            rank = result[0] 
            pesan = result[1] 
            print(batas2)
            print("+", f"Rank {rank}".center(96), "+")
            print(batas2, "\n")
            print(f"Anda mendapatkan nominasi sebagai | {rank} |")
            print(f"Total Skor : {score}\n")
            print(pesan)
            input("Silahkan Tekan Enter...")
            return False
        else:
            print("Input tidak valid. Silakan masukkan 'y' atau 'n'.")
def soal():
    global score, correct_answers
    # Daftar soal dan jawaban
    print(Fore.LIGHTBLUE_EX + "STAGE 1")
    quizs1 = [
            ("Apa nama pedang utama yang digunakan oleh Kirito di anime Sword Art Online?",
            ["A. Elucidator", "B. Excalibur", "C. Red Queen", "D. Yamato"], "a", "b"),
            ("Di anime Naruto, siapa karakter utama yang menjadi rival Naruto?",
            ["A. Rock Lee", "B. Sasuke Uchiha", "C. Gaara", "D. Neji Hyuga"], "b", "c"),
            ("Siapa nama karakter utama di anime Attack on Titan?",
            ["A. Mikasa Ackerman", "B. Armin Arlert", "C. Eren Yeager", "D. Levi Ackerman"], "c", "d"),
            ("Apa nama kemampuan khusus Saitama di anime One Punch Man?",
            ["A. Tinju 100%", "B. Serangan Garis Maut", "C. Satu Pukulan KO", "D. Tinju Cahaya"], "c", "d"),
            ("Di anime My Hero Academia, siapa yang memiliki Quirk One For All?",
            ["A. Bakugo", "B. Todoroki", "C. All Might", "D. Deku"], "d", "c"),
            ("Siapa karakter utama yang memiliki Sharingan di anime Naruto?",
            ["A. Naruto Uzumaki", "B. Sasuke Uchiha", "C. Rock Lee", "D. Kakashi Hatake"], "b", "d"),
            ("Di anime Dragon Ball, siapa yang menjadi Super Saiyan pertama kali?",
            ["A. Vegeta", "B. Gohan", "C. Goku", "D. Trunks"], "c", "d"),
            ("Apa nama kota tempat tinggal Midoriya Izuku di anime My Hero Academia?",
            ["A. Shinjuku", "B. Musutafu", "C. Tokyo", "D. Osaka"], "b", "c"),
            ("Di anime One Piece, siapa nama kru pertama yang bergabung dengan Luffy?",
            ["A. Sanji", "B. Zoro", "C. Nami", "D. Usopp"], "b", "c"),
            ("Di anime Fairy Tail, apa nama guild yang menjadi pusat cerita?",
            ["A. Black Bulls", "B. Akatsuki", "C. Fairy Tail", "D. Phantom Lord"], "c", "d")
    ]
    # Looping untuk setiap soal
    for i, (quiz, opsi, JawabanBenar, JawabanHampir) in enumerate(quizs1):
        while True:
            os.system('cls')
            print(batas1)
            print("STAGE 1".center(100))
            print(batas1)
            print(f"SOAL {i+1}")
            print(quiz)
            print("\n".join(opsi))
            print(batas2)
            jawaban = input("Masukkan jawaban Anda: ").lower()
            
            if jawaban == JawabanBenar:
                print(batas2)
                print("Jawabannya tepat sekali!")
                score += 100
                correct_answers += 1
                break
            elif jawaban == JawabanHampir:
                print(batas2)
                print("Tepat, namun masih ada yang lebih tepat sih.")
                score += 80
                correct_answers += 1
                break
            elif jawaban in ["a", "b", "c", "d"]:
                print(batas2)
                print("Sayang sekali jawaban Anda salah.")
                score += 20
                break
            else:
                print(batas2)
                print("Perhatikan opsi yang diberikan.")
                input("Tekan Enter untuk mengulang.")
        
        print(f"\nJawaban yang benar adalah {JawabanBenar.upper()}\n")
        print(f"Skor Anda: {score}\n\n")
        input("Tekan Enter untul lanjut ke stage berikutnya...")
    #Konfirmasi sebelum lanjut stage 2
    os.system('cls')
    print(batas2)
    print("MASIH MAU LANJUT?".center(100))
    print(batas2, "\n")
    if not konfirmasi_lanjut():
        return

    #Stage 2
    print(Fore.LIGHTBLUE_EX + "STAGE 2")
    quizs2 = [
            ("Di anime Jujutsu Kaisen, siapa yang mewarisi teknik kutukan terkuat dari keluarga Gojo?",
            ["A. Suguru Geto", "B. Megumi Fushiguro", "C. Satoru Gojo", "D. Yuta Okkotsu"], "c", "d"),
            ("Pada Attack on Titan musim terakhir, siapa karakter yang pertama kali mengetahui rencana Eren untuk membebaskan Eldia?",
            ["A. Mikasa Ackerman", "B. Armin Arlert", "C. Zeke Yeager", "D. Jean Kirstein"], "b", "c"),
            ("Dalam Chainsaw Man, apa nama iblis yang bekerja sama dengan Denji?",
            ["A. Fox Devil", "B. Gun Devil", "C. Blood Devil", "D. Pochita"], "d", "c"),
            ("Siapakah karakter yang memegang kekuatan Reversi di anime Ousama Ranking?",
            ["A. Bojji", "B. Miranjo", "C. Desha", "D. Kage"], "d", "c"),
            ("Di Spy x Family, apa pekerjaan asli dari karakter Yor Forger?",
            ["A. Guru", "B. Pembunuh bayaran", "C. Polisi", "D. Dokter"], "b", "d")
    ]
    # Looping untuk stage 2
    for i, (quiz, opsi, JawabanBenar, JawabanHampir) in enumerate(quizs2):
        while True:
            os.system('cls')
            print(batas1)
            print("STAGE 2".center(100))
            print(batas1)
            print(f"SOAL {i+1}")
            print(quiz)
            print("\n".join(opsi))
            print(batas2)
            jawaban = input("Masukkan jawaban Anda: ").lower()
            
            if jawaban == JawabanBenar:
                print(batas2)
                print("Jawabannya tepat sekali!")
                score += 100
                correct_answers += 1
                break
            elif jawaban == JawabanHampir:
                print(batas2)
                print("Tepat, namun masih ada yang lebih tepat sih.")
                score += 80
                correct_answers += 1
                break
            elif jawaban in ["a", "b", "c", "d"]:
                print(batas2)
                print("Sayang sekali jawaban Anda salah.")
                score += 20
                break
            else:
                print(batas2)
                print("Perhatikan opsi yang diberikan.")
                input("Tekan Enter untuk mengulang.")
        
        print(f"\nJawaban yang benar adalah {JawabanBenar.upper()}\n")
        print(f"Skor Anda: {score}\n\n")
        input("Tekan Enter untul lanjut ke stage berikutnya...")
    #Konfirmasi sebelum lanjut stage 3
    os.system('cls')
    print(batas2)
    print("MASIH MAU LANJUT?".center(100))
    print(batas2, "\n")
    if not konfirmasi_lanjut():
        return


    # Stage 3
    print(Fore.LIGHTBLUE_EX + "STAGE 3")
    quizs3 = [
            ("Dalam anime Demon Slayer: Kimetsu no Yaiba – Entertainment District Arc, siapa yang menjadi Hashira pelindung dalam arc ini?",
            ["A. Tengen Uzui", "B. Kyojuro Rengoku", "C. Sanemi Shinazugawa", "D. Mitsuri Kanroji"], "a", "b"),
            ("Di Hell’s Paradise, siapa yang dikirim bersama Gabimaru untuk mendapatkan Elixir of Life?",
            ["A. Chobe Aza", "B. Yuzuriha", "C. Yamada Asaemon Sagiri", "D. Senta"], "c", "d"),
            ("Dalam Blue Lock, siapa yang menjadi mentor utama bagi Isagi dan timnya?",
            ["A. Ego Jinpachi", "B. Yoichi Isagi", "C. Rin Itoshi", "D. Meguru Bachira"], "a", "b"),
            ("Pada My Dress-Up Darling, siapa karakter yang mempengaruhi Wakana Gojo untuk melanjutkan hobi menjahitnya?",
            ["A. Inui Sajuna", "B. Kitagawa Marin", "C. Wakana Gojo sendiri", "D. Juju"], "b", "a"),
            ("Di Oshi no Ko, apa alasan utama Ai Hoshino berusaha merahasiakan statusnya sebagai ibu dari anak kembar?",
            ["A. Untuk melindungi karirnya", "B. Takut pada penggemar", "C. Karena tekanan keluarga", "D. Agar anak-anaknya tumbuh tanpa beban"], "a", "d")
    ]
    # Looping untuk stage 3
    for i, (quiz, opsi, JawabanBenar, JawabanHampir) in enumerate(quizs3):
        while True:
            os.system('cls')
            print(batas1)
            print("STAGE 3".center(100))
            print(batas1)
            print(f"SOAL {i+1}")
            print(quiz)
            print("\n".join(opsi))
            print(batas2)
            jawaban = input("Masukkan jawaban Anda: ").lower()
            
            if jawaban == JawabanBenar:
                print(batas2)
                print("Jawabannya tepat sekali!")
                score += 100
                correct_answers += 1
                break
            elif jawaban == JawabanHampir:
                print(batas2)
                print("Tepat, namun masih ada yang lebih tepat sih.")
                score += 80
                correct_answers += 1
                break
            elif jawaban in ["a", "b", "c", "d"]:
                print(batas2)
                print("Sayang sekali jawaban Anda salah.")
                score += 20
                break
            else:
                print(batas2)
                print("Perhatikan opsi yang diberikan.")
                input("Tekan Enter untuk mengulang.")
        
        print(f"\nJawaban yang benar adalah {JawabanBenar.upper()}\n")
        print(f"Skor Anda: {score}\n\n")
        input("Tekan Enter untul lanjut ke stage berikutnya...")
    # Konfirmasi sebelum melanjutkan ke stage 4
    os.system('cls')
    print(batas2)
    print("MASIH MAU LANJUT?".center(100))
    print(batas2, "\n")
    if not konfirmasi_lanjut():
        return

    # Stage 4
    print(Fore.LIGHTMAGENTA_EX   + "STAGE 4")
    quizs4 = [
            ("Siapakah yang menciptakan Death Note?",
            ["A. Ryuk", "B. Light Yagami", "C. Shinigami King (Raja Shinigami)", "D. Soichiro Yagami"], "c", "a"),
            ("Di anime 'Fullmetal Alchemist: Brotherhood', homunculus manakah yang TIDAK diciptakan oleh Father?",
            ["A. Envy", "B. Wrath", "C. Sloth", "D. Pride"], "b", "d"),
            ("Apa nama pedang Zoro di anime 'One Piece' yang diambil dari Ryuma?",
            ["A. Shusui", "B. Wado Ichimonji", "C. Sandai Kitetsu", "D. Yubashiri"], "a", "d"),
            ("Di anime 'Hunter x Hunter', siapa nama nenek Gon?",
            ["A. Mito Freecss", "B. Abelia Freecss", "C. Grandma Abe", "D. Kalluto Zoldyck"], "a", "c"),
            ("Di anime 'Attack on Titan', siapa yang mewarisi Titan Attack sebelum Eren Yeager?",
            ["A. Grisha Yeager", "B. Eren Kruger", "C. Frieda Reiss", "D. Uri Reiss"], "b", "a"),
    ]
    # Looping untuk stage 4
    for i, (quiz, opsi, JawabanBenar, JawabanHampir) in enumerate(quizs4):
        while True:
            os.system('cls')
            print(batas1)
            print("STAGE 4".center(100))
            print(batas1)
            print(f"SOAL {i+1}")
            print(quiz)
            print("\n".join(opsi))
            print(batas2)
            jawaban = input("Masukkan jawaban Anda: ").lower()
            
            if jawaban == JawabanBenar:
                print(batas2)
                print("Jawabannya tepat sekali!")
                score += 100
                correct_answers += 1
                break
            elif jawaban == JawabanHampir:
                print(batas2)
                print("Tepat, namun masih ada yang lebih tepat sih.")
                score += 80
                correct_answers += 1
                break
            elif jawaban in ["a", "b", "c", "d"]:
                print(batas2)
                print("Sayang sekali jawaban Anda salah.")
                score += 20
                break
            else:
                print(batas2)
                print("Perhatikan opsi yang diberikan.")
                input("Tekan Enter untuk mengulang.")
        
        print(f"\nJawaban yang benar adalah {JawabanBenar.upper()}\n")
        print(f"Skor Anda: {score}\n\n")
        input("Tekan Enter untul lanjut ke stage berikutnya...")

    # Konfirmasi sebelum melanjutkan ke stage 5
    os.system('cls')
    print(batas2)
    print("MASIH MAU LANJUT?".center(100))
    print(batas2, "\n")
    if not konfirmasi_lanjut():
        return

    # Stage 5
    print(Fore.LIGHTMAGENTA_EX + "STAGE 5")
    quizs5 = [
            ("Di anime 'Naruto', siapa nama guru Kakashi Hatake saat masih Genin?",
            ["A. Minato Namikaze", "B. Hiruzen Sarutobi", "C. Jiraiya", "D. Tsunade"], "a", "b"),
            ("Di anime 'Bleach', siapakah kapten Divisi 11 sebelum Kenpachi Zaraki?",
            ["A. Yachiru Unohana", "B. Kenpachi Kiganjō", "C. Ikkaku Madarame", "D. Yumichika Ayasegawa"], "b", "a"),
            ("Di anime 'Neon Genesis Evangelion', apa nama malaikat pertama yang menyerang Tokyo-3?",
            ["A. Sachiel", "B. Ramiel", "C. Zeruel", "D. Arael"], "a", "b"),
            ("Di anime 'Code Geass', apa nama geass yang dimiliki C.C.?",
            ["A. Geass of Obedience (Ketaatan)", "B. Geass of Immortality (Keabadian)", "C. Geass of Love (Cinta)", "D. Geass of Time (Waktu)"], "b", "a"),
            ("Di anime 'Cowboy Bebop', apa nama kapal luar angkasa milik Spike Spiegel dan Jet Black?"),
    ]
    # Looping untuk stage 5
    for i, (quiz, opsi, JawabanBenar, JawabanHampir) in enumerate(quizs5):
        while True:
            os.system('cls')
            print("STAGE 5")
            print(f"SOAL {i+1}")
            print(quiz)
            print("\n".join(opsi))
            
            jawaban = input("Masukkan jawaban Anda: ").lower()
            
            if jawaban == JawabanBenar:
                print("Jawabannya tepat sekali!")
                score += 2000
                break
            elif jawaban == JawabanHampir:
                print("Tepat, namun masih ada yang lebih tepat sih.")
                score += 1000
                break
            elif jawaban in ["a", "b", "c", "d"]:
                print("Sayang sekali jawaban Anda salah.")
                score += 200
                break
            else:
                print("Perhatikan opsi yang diberikan.")
                input("Tekan Enter untuk mengulang.")
        
        print(f"\nJawaban yang benar adalah {JawabanBenar.upper()}\n")
        print(f"Skor Anda: {score}\n\n")
        input("Tekan Enter untuk lanjut ke soal berikutnya...")


    # Langsung panggil fungsi evaluate_rank dengan score
    os.system('cls')
    result = evaluate_rank(score, correct_answers)
    rank = result[0] 
    pesan = result[1] 
    print(batas2)
    print("+", f"Rank {rank}".center(96), "+")
    print(batas2, "\n")
    print(f"Anda mendapatkan nominasi sebagai | {rank} |")
    print(f"Total Skor : {score}\n")
    print(pesan)

