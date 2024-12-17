from services import db
from services.db import take_item

#Menu utama ketika user milih mode pembeli
def mode_pembeli():
    print("Berhasil Masuk Mode Pembeli")
    while True:
        print("\n1.Membeli Barang\n2.Keluar")
        pilihan = input("\nPilih Menu (atau ketik (keluar) untuk keluar dari mode pembeli) : ")
        if pilihan.lower() == '1':
            membeli_barang()
        elif pilihan.lower() == '2':
            break
        else:
            print("Sepertinya yang anda pilih di luar menu :) harap masukan yang sudah disediakan menu")

#Command untuk mme
def membeli_barang():
    print(f"Daftar barang yang tersedia")

    barang_list = db.get_all_items()

    for item in barang_list:
        print(f"Kode Barang : {item[1]} | Nama Barang : {item[2]:<10} | Harga Barang : {item[3]} | Stok Barang : {item[4]}")

        
    while True:
        nama_barang = input("Masukan nama barang : ").lower()
        
        try:
            jumlah_beli = int(input("Masukan Jumlah jumlah beli : "))
            db.take_item(nama_barang,jumlah_beli)
            return
        except ValueError :
            print("Wajib memasukan angka !!! ")
        
