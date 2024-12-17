import mysql.connector

db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'supermarket'
)

#Command Untuk Menambahkan Barang 
def insert_item(kode_barang, nama_barang, harga_barang, stok_barang):
    cursor = db.cursor()
    cursor.execute("INSERT INTO tabel_barang (kode_barang, nama_barang, harga_barang, stok_barang) VALUES (%s,%s, %s, %s)",(kode_barang,nama_barang,harga_barang,stok_barang))
    db.commit()

    #Untuk bukti berhasil atau tidak dalam proses menambahkan barang
    if cursor.rowcount > 0:
        return("Data berhasil ditambahkan")
    else:
        return("Data gagal di tambahkan")


#Command Untuk Menemukan Barang
def find_item(kode_barang):
    cursor = db.cursor()
    query = "SELECT * FROM tabel_barang WHERE kode_barang = %s"
    cursor.execute(query, (kode_barang,))
    return cursor.fetchone()

#Command Untuk Mengedit Barang
def update_item(kode_barang, nama_barang, harga_barang, stok_barang):
    cursor = db.cursor()
    query = """
        UPDATE tabel_barang
        SET nama_barang = %s,
            harga_barang = %s,
            stok_barang = %s
        WHERE kode_barang = %s
    """
    cursor.execute(query, (nama_barang, harga_barang, stok_barang, kode_barang))
    db.commit()
    
    #untuk bukti berhasil atau tidak dalam proses mengedit barang
    if cursor.rowcount > 0:
        print(f"{cursor.rowcount} baris berhasil diperbarui.")
    else:
        print("Tidak ada data yang diperbarui.")

#Memanggil semua barang yang tersedia
def get_all_items():
    cursor = db.cursor()
    query = "SELECT * FROM tabel_barang"
    cursor.execute(query)
    return cursor.fetchall()

#Command Proses terjadinya pengurangan stok 
def take_item(nama_barang,jumlah_beli):
    cursor = db.cursor()
    query = "SELECT * FROM tabel_barang WHERE nama_barang  = %s"
    cursor.execute(query, (nama_barang,))

    result = cursor.fetchone()

    if result:
        current_stock = result[4]
        harga_barang = result[3]

        if current_stock >= jumlah_beli:
            
            #Command untuk mengurangi stok
            update = "UPDATE tabel_barang SET stok_barang = stok_barang - %s WHERE nama_barang = %s"
            cursor.execute(update, (jumlah_beli, nama_barang))
            db.commit()

            #Command untuk bukti berhasil atau tidaknya 
            total_harga = jumlah_beli * harga_barang
            print(f"Barang '{nama_barang}' berhasil Dibeli. Dengan harga Rp. {total_harga}. Stok tersisa: {current_stock - jumlah_beli}.")
            return True
        else:
            print(f"Stok tidak mencukupi. Stok saat ini hanya {current_stock}.")
    else:
        print(f"Barang dengan nama '{nama_barang}' tidak ditemukan.")


    cursor.close()