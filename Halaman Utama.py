import time
from pembeli import mode_pembeli
from penjual import mode_penjual

# Fungsi yang pertama kali muncul ketika program dijalankan (Jantung dari aplikasi)
def menu_utama():
    print("==== Selama Datang Di BuyAndGo ===")
    print("\n1. Pembeli\n2. Penjual\n3. Matikan Program")

while True:
    menu_utama()
    jwbu = input("\nSilahkan Pilih : ")
    if jwbu == '1':
        mode_pembeli()
    elif jwbu =='2':
        mode_penjual()
    elif jwbu =='3':
        print("Keluar Dari Program....")
        for i in range (3,0,-1):
            print(i, end="\n")
            time.sleep(1)
        print("Terima Kasih sudah menggunakan BuyAndGo")
        break
    else:
        print("!!! Harap masukan angka !!!")