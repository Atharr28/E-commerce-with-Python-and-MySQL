from services.db import get_available_item, take_item, start_transaction, commit_transaction, rollback_transaction

# Menu utama ketika user memilih mode pembeli
def mode_pembeli():
    print("\nSelamat datang di mode pembeli")
    while True:
        print("\n1. Membeli Barang\n2. Keluar")
        pilihan = input("\nPilih Menu atau ketik (keluar) untuk keluar dari mode pembeli: ")
        if pilihan == '1':
            membeli_barang()
        elif pilihan == '2' or pilihan.lower() == 'keluar':
            print("Keluar dari mode pembeli. Terima kasih!")
            break
        else:
            print("Harap memasukan angka [1, 2] !!!")


# Command untuk membeli barang
def membeli_barang():
    try:
        print("\n" + "=" * 80)
        print("Daftar barang yang tersedia")
        print("=" * 80)

        # Ambil daftar barang dari database
        barang_list = get_available_item()
        for item in barang_list:
            print(f"Nama Barang: {item[2]:<10} | Harga Barang: {item[3]} | Stok Barang: {item[4]}")

        print("-" * 80)

        nama_barang = input("\nMasukkan nama barang (atau ketik keluar): ").lower()
        if nama_barang == "keluar":
            return

        jumlah_beli = int(input("Masukkan jumlah beli: "))
        if jumlah_beli <= 0:
            print("Angka tidak boleh kurang dari 0")
            return

        # Mulai transaksi
        start_transaction()
        total_harga = take_item(nama_barang, jumlah_beli)
        if total_harga:
            if pembayaran(total_harga):
                commit_transaction()  # Commit hanya jika pembayaran berhasil
                print("Terima kasih sudah berbelanja.")
            else:
                rollback_transaction()  # Rollback jika pembayaran gagal
                print("Pembayaran gagal. Transaksi dibatalkan.")
        else:
            rollback_transaction()  # Rollback jika barang tidak ditemukan
            print("Barang tidak ditemukan atau stok tidak mencukupi.")
    except ValueError:
        print("Masukkan angka yang valid!")
    except Exception as e:
        rollback_transaction()
        print(f"Terjadi error: {e}")


def pembayaran(total_harga):
    try:
        while True:
            # Meminta input dari pembeli
            nama = input("Masukkan nama lengkap: ")
            alamat = input("Masukkan alamat: ")
            notelp = input("Masukkan nomor telepon: ")
            uang_dibayar = int(input(f"Total harga adalah Rp {total_harga}. Masukkan jumlah uang yang dibayar: Rp "))

            if uang_dibayar >= total_harga:
                kembalian = uang_dibayar - total_harga
                print(f"Pembayaran berhasil! Kembalian Anda: Rp {kembalian}")
                print("Barang ini atas nama:", nama)
                print("Dengan alamat:", alamat)
                print("Nomor telepon:", notelp)
                return True
            else:
                print(f"Uang yang Anda bayarkan kurang. Kurang Rp {total_harga - uang_dibayar}.")
                return False
    except ValueError:
        print("Masukkan jumlah uang yang valid!")
        return False
