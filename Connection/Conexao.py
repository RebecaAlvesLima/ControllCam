import mysql.connector

con = mysql.connector.connect(host='db4free.net', database="contrllcam", user="gustavorleme", password="livia301021")

if con.is_connected():
    db_info = con.get_server_info()
    print("conectado ao servidor ", db_info)
    cursor = con.cursor()
    cursor.execute("select database();")
    linha = cursor.fetchone()
    print("conectado ao banco de dados ", linha)

if con.is_connected():
    cursor.close()
    con.close()
    print("conexão com mysql encerrada")