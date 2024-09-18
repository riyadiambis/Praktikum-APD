def start_game():
    import random
    from libs import welcome_message
    loli_position = random.randint(1, 4)
    
    welcome_message("WELCOME TO LOLI GAME")
    nama_user = input("\nmasukkan nama kamu;  ")
    
    while nama_user == "":
        nama_user = input("Cepat selamatkan Loli imut ini!! \nIsi dulu nama Oni-chan")
        
        
    bentuk_goa = "|_|"
    goa_kosong = [bentuk_goa] * 4
    
    goa = goa_kosong.copy()
    goa_kosong = '  '.join(goa_kosong)
    
    goa[loli_position - 1] = "|>-<|"
    goa = '  '.join(goa)
        
    