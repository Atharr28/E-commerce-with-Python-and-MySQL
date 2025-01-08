import time
from pembeli import mode_pembeli
from penjual import mode_penjual

# Fungsi yang pertama kali muncul ketika program dijalankan (Jantung dari aplikasi)
def menu_utama():
    print("\n==== Selama Datang Di BuyAndGo ===")
    print("\n1. Pembeli\n2. Penjual\n3. Matikan Program")

while True:
    menu_utama()
    jwbu = input("\nSilahkan Pilih : ")
    if jwbu.lower() in ["Pembeli", "1"]:
        mode_pembeli()
    elif jwbu.lower() in ["Penjual","2"]: 
        print("Masukan password untuk ke mode penjual")
        password = input("Password: ")
        if password.lower() == "admin123":
            mode_penjual()
        else:
            print("Password salah! akses di tolak")    
    elif jwbu.lower() in ["keluar","3"]:
        print("Keluar Dari Program....")
        for i in range (3,0,-1):
            print(i, end="\n")
            time.sleep(1)
        print("Terima Kasih sudah menggunakan BuyAndGo")
        break
    elif jwbu.isdigit() and int (jwbu) not in [1,2,3]:
        print("Harap masukan angka yang sudah disediakan [1, 2, 3]")
    else:
        print("!!! Harap masukan angka !!!")