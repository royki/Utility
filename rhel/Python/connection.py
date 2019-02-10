import mysql.connector as mariadb

mariadb_connection = mariadb.connect(user='root', password='root', host='host', port='3306', database='db')
cursor = mariadb_connection.cursor()

cursor.execute("select * from amp_app_scopes")

for id in cursor:
    print("ID: {}").format(id)

