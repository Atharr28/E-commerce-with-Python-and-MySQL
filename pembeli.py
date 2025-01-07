from services import db
from services.db import take_item

#Menu utama ketika user milih mode pembeli
def mode_pembeli():
    print("Berhasil Masuk Mode Pembeli")
    while True:
        print("\n1.Membeli Barang\n2.Keluar")
        pilihan = input("\nPilih Menu atau ketik (keluar) untuk keluar dari mode pembeli : ")
        if pilihan.lower() == '1':
            membeli_barang()
        elif pilihan.lower() == '2':
            break
        else:
            print("Harap memasukan angka [1, 2] !!!")


#Command untuk mme
def membeli_barang():
    print(f"Daftar barang yang tersedia")

    barang_list = db.get_all_items()

    for item in barang_list:
        print(f"Kode Barang : {item[1]} | Nama Barang : {item[2]:<10} | Harga Barang : {item[3]} | Stok Barang : {item[4]}")

    while True:
        nama_barang = input("Masukan nama barang (atau ketik keluar):  ").lower()
        if nama_barang == "keluar" or nama_barang == "KELUAR" :
            return
        try:
            jumlah_beli = int(input("Masukan Jumlah jumlah beli : "))
            if jumlah_beli <= 0:
                print("Angka tidak boleh kurang dari 0")
                continue
            total_harga = db.take_item(nama_barang,jumlah_beli)

            if total_harga:
                if pembayaran(total_harga):
                    print("Terima kasih sudah berbelanja")
                else:
                    print("Pembayaran gagal. Silahkan coba lagi.")
            else:
                print("barang tidak ditemukan atau stok tidak me")
        except ValueError :
            print("Wajib memasukan angka !!! ")
            break

def pembayaran(total_harga):
    while True:
        try:
            # Meminta input dari pembeli
            uang_dibayar = float(input(f"Total harga adalah Rp {round(total_harga,2)}. Masukkan jumlah uang yang dibayar: Rp "))
            
            if uang_dibayar >= total_harga:
                kembalian = round(uang_dibayar - total_harga)
                print(f"Pembayaran berhasil! Kembalian Anda: Rp {kembalian}")
                return True
            else:
                print(f"Uang yang Anda bayarkan kurang. Kurang Rp {round(total_harga - uang_dibayar,2)}.")
                return False
        except ValueError:
            print("Masukkan jumlah uang yang valid!")