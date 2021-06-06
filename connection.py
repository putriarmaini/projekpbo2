import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector\
                      .connect(host='localhost',
                               database='tokobuku',
                               user='root',
                               password='')
    if connection.is_connected():
        db_info = connection.get_server_info()
        print("Berhasil Terhubung ", db_info)
except Error as db:
    print("Tidak terhubung ke database ", db)
finally:
    if connection.is_connected():
        connection.close()
        print("Koneksi ditutup")