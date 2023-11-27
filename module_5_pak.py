# pip install mysql-connector

import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
)

exec = db.cursor()

def cek_koneksi():
    if db.is_connected():
        print("Berhasil terhubung ke database")
    else :
        print("Error guoblok")

def buat_database():
    nama=input("Masukan nama database :")
    exec.execute("CREATE DATABASE IF NOT EXISTS "+nama)
    print("Database berhasil terbuat!")

def hapus_database():
    nama=input("Masukan nama database :")
    if (input("Apakakh kamu benar benar ingin menghapus "+nama +" (y/n)") == "y") :
        exec.execute("DROP DATABASE "+nama)
        print("Database berhasil Terhapus!")
    else :
        print("Oke gajadi")

def bikin_tabel(): 
    nama_db=input("Masukan nama database :")
    db = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = nama_db
    )
    exec = db.cursor()
    nama_tabel=input("Masukan Nama tabel :")
    query="CREATE TABLE " + nama_tabel +" (" 

    jumlah_kolom=int(input("Masukan jumlah kolom :"))
    for i in range(0,jumlah_kolom):
        nama_kolom=input("Masukan nama dari kolom ke-" + str(i)+" : ")
        if i == 0:
            query=query+nama_kolom+" INT AUTO_INCREMENT PRIMARY KEY,"
        else:
            jenis = int(input("Masukan Jenis Data\n1. INT\n2. VARCHAR\n3. TEXT\n4. DATE\n :"))
            if jenis == 1:
                panjang = (input("Masukan panjang data :"))
                query=query+nama_kolom+" INT("+ panjang +"),"
            elif jenis == 2:
                panjang = (input("Masukan panjang data :"))
                query=query+nama_kolom+" VARCHAR("+ panjang +"),"
            elif jenis == 3:
                panjang = (input("Masukan panjang data :"))
                query=query+nama_kolom+" TEXT("+ panjang +"),"
            elif jenis == 4: 
                query=query+nama_kolom+" DATE,"
    
    exec.execute(query[:-1]+")")

def hapus_tabel():
    nama_db=input("Masukan nama database :")
    db = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = nama_db
    )
    exec = db.cursor()
    nama_tabel = input("Masukkan nama table yang ingin dihapus: ")
    if (input(f"Apakah kamu benar benar ingin menghapus {nama_tabel} (y/n)") == "y") :
        exec.execute(f"DROP TABLE {nama_tabel}")
        print("Database berhasil Terhapus!")
    else :
        print("Oke gajadi")

def input_data():
    nama_db=input("Masukan nama database :")
    db = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = nama_db
    )
    exec = db.cursor(buffered=True)
    nama_tabel=input("Masukan Nama tabel :")
    baca = "SELECT * FROM "+nama_tabel
    exec.execute(baca)
    baca = "INSERT INTO "+nama_tabel+" ("
    for x in (exec.column_names) :
        baca=baca+x+","
    baca=baca[:-1]+") VALUES ("
    banyak_data=int(input("Masukan banyak data : "))
    data=[]
    for y in range (len(exec.column_names)): 
        baca=baca+"%s,"   
    for x in range(banyak_data):
        data_collom=[]
        for x in (exec.column_names):
            a = input(f'Masukan data untuk kolom {x} :')
            data_collom.append(a)
        data.append(data_collom)
    baca=baca[:-1]+")"
    print(data)
    for val in data:
        print(baca,val)
        exec.execute(baca,tuple(val))
        db.commit()
        print("data berhasil ditambahkan.")


def baca_data():
    nama_db=input("Masukan nama database :")
    db = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = nama_db
    )
    exec = db.cursor(buffered=True)
    nama_tabel=input("Masukan Nama tabel :")
    baca = "SELECT * FROM "+nama_tabel
    exec.execute(baca)

    hasil = exec.fetchall()
    print(hasil)
    for data in hasil:
        print(data)

def hapus_data():
    nama_db=input("Masukan nama database :")
    db = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = nama_db
    )
    exec = db.cursor(buffered=True)
    nama_tabel=input("Masukan Nama tabel :")
    baca = "SELECT * FROM "+nama_tabel
    exec.execute(baca)
    baca = "DELETE FROM "+nama_tabel+" WHERE "+exec.column_names[0]+"=%s"
    id = int(input('Masukkan id Data : '))
    val = (id, )
    exec.execute(baca, val)

    db.commit()
    print(f"{id} data dihapus")
    
def update_data():
    nama_db = input("Masukkan database yang ingin di ubah: ")
    db = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = nama_db
    )
    exec = db.cursor(buffered=True)
    nama_table = input("Masukkan nama tabel: ")
    
    data_ubah = input("Masukkan kolom yang ingin diubah: ")
    jadi_apa = input("Masukkan perubahan data: ")
    bagian_siapa = input("Masukkan baris yang ingin diubah: ")
    yang_mana = input("Masukkan data bagiannya: ")
    
    uppy = f"UPDATE {nama_table} SET {data_ubah} = %s WHERE {bagian_siapa} = %s"
    exec.execute(uppy, (jadi_apa, yang_mana))
    db.commit()
    print(f"data dari database {nama_db} tabel {nama_table} sudah di update")
    

while True:
    print("\nMENU:\n1. Cek Koneksi Database\n2. Buat database\n3. Hapus Database\n4. Buat Tabel\n5. Hapus Table\n6. Input Tabel\n7. Hapus Data\n8. Baca Data\n9. Update Data")
    menu_input=int(input("Menu :"))
    if menu_input == 1:
        cek_koneksi()
    elif menu_input == 2:
        buat_database()
    elif menu_input == 3:
        hapus_database()
    elif menu_input == 4:
        bikin_tabel()
    elif menu_input == 5:
        hapus_tabel()
    elif menu_input == 6:
        input_data()
    elif menu_input == 7:
        hapus_data()
    elif menu_input == 8:
        baca_data()
    elif menu_input == 9:
        update_data()
    else :
        print("Dadah")
        break