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


#Command Untuk Mengedit Barang
def find_item(kode_barang):
    cursor = db.cursor()
    query = "SELECT * FROM tabel_barang WHERE kode_barang = %s"
    cursor.execute(query, (kode_barang,))
    return cursor.fetchone()

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

def take_item():
    cursor = db.cursor()
    