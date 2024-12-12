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