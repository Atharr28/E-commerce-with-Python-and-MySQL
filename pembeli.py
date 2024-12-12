def mode_pembeli():
    print("Berhasil Masuk Mode Pembeli")
    while True:
        print("\n1.Membeli Barang\n2.Keluar")
        pilihan = input("\nPilih Menu (atau ketik (keluar) untuk keluar dari mode pembeli) : ")
        if pilihan.lower() == '1':
            ()
        elif pilihan.lower() == '2':
            break
        else:
            print("Sepertinya yang anda pilih di luar menu :) harap masukan yang sudah disediakan menu")


def membeli_barang():
    while True: 
        user_milih = input("\nMasukkan nama produk yang ingin dibeli atau keluar dengan mengetik (keluar) : ").lower()
        if user_milih == "keluar":
            break
        if user_milih in produk:
            jumlah = int(input(f"Berapa Banyak Pilihan yang ingin dibeli : "))
            if jumlah <= produk[user_milih]["stok"]:
                produk[user_milih]["stok"] -= jumlah
                total += jumlah * produk[user_milih]["harga"]
                print(f"{jumlah} {user_milih} Di tambahkan ke kerangjang. Total : Rp.{total}")
            else:
                print("Maaf,stok tidak mencukupi")
        else:
            print("Mohon maaf produk tidak tersedia saat ini")

    print(f"Total belanja anda {total}")
    print("Terima kasih sudah berbelanja 😀")