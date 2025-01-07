from services import db


#Menu utama ketika user memilih mode penjual
def mode_penjual():
    print("Berhasil Masuk Mode Penjual")
    while True:
        print("\nMenu Penjual \n1. Menambahkan Barang\n2. Edit Barang\n3. Hapus Barang\n4. Keluar")
        pilihan = input("\nPilih Menu (ketik 'keluar' untuk keluar dari mode pembeli) : ")
        if pilihan.lower() == '1':
            menambahkan_barang()
        elif pilihan.lower() == '2':
            edit_barang()
        elif pilihan.lower() == '3':
            hapus_barang()
        elif pilihan.lower() == '4':
            break
        else:
            print("Sepertinya yang anda pilih di luar menu :) harap masukan yang sudah disediakan menu")


# Fungsi ini untuk menambahkan barang (menambahkan_barang)
def menambahkan_barang():
    kode_barang = input('kode Barang :')
    nama_barang = input('Nama Barang :')
    harga_barang = input('Harga Barang : ')
    stok_barang = input('Stok Barang : ')

    save = db.insert_item(kode_barang, nama_barang, harga_barang, stok_barang)
    print(save)


# Fungsi untuk mengedit barang (edit)
def edit_barang():
    print(f"Dafter barang yang tersedia")
    
    barang_list = db.get_all_items()

    for item in barang_list:
        print(f"Kode Barang : {item[1]} | Nama Barang : {item[2]:<10} | Harga Barang : {item[3]} | Stok Barang : {item[4]}")

    while True:
        kode_barang = input("\nMasukan kode barang yang akan diubah : ")
        item = db.find_item (kode_barang)  # Mengambil item berdasarkan kode_barang

        if item:
            print("\nBarang yang tersedia saat ini:")
            print(f"Nama barang : {item[2]}")
            print(f"Harga barang : {item[3]}")
            print(f"Stok barang : {item[4]}")

            # Memasukkan inputan baru, atau biarkan tetap sesuai dengan nilai item yang ada
            nama_barang = input('Nama Barang (jika tidak ingin diubah tekan ENTER)') or item[2]
            harga_barang = input('Harga Barang (Jika tidak ingin diubah tekan ENTER)') or item[3]
            stok_barang = input('Stok Barang (Jika tidak ingin diubah tekan ENTER)') or item[4]

        # Update data barang
        db.update_item(kode_barang, nama_barang,harga_barang,stok_barang )
        break

def hapus_barang():
    print(f"List barang yang tersedia")

    barang = db.get_all_items()

    for item in barang:
        print(f"\nKode Barang : {item[1]} | Nama Barang : {item[2]:<10} | Harga Barang : {item[3]} | Stok Barang : {item[4]}")

        while True:
            kode_barang = input("\nMasukan kode barang yang ingin di hapus (atau ketik keluar): ")
            item = db.find_item(kode_barang)

            if kode_barang == "keluar" or kode_barang == "KELUAR":
                break

            if item:
                db.delete_item(kode_barang)
                print(f"barang dengan kode {kode_barang} berhasil di hapus ")
                break
            else:
                print(f"Barang dengan kode {kode_barang} tidak ditemukan")