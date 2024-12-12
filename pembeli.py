from services import db

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


def membeli_barang():
    print(f"Daftar barang yang tersedia")

    barang_list = db.get_all_items()

    for item in barang_list:
        print(f"Kode Barang : {item[1]} | Nama Barang : {item[2]:<10} | Harga Barang : {item[3]} | Stok Barang : {item[4]}")
    
    total = 0
    while True:
        nama_barang = input("Masukan nama barang : ")
        item = db.find_item(nama_barang)
        jumlah_stok = int(input("Masukan Jumlah Stok : "))