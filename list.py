import mysql.connector

conn = mysql.connector.connect(host='localhost', database='english_school', user='root', password='')
if conn.is_connected():
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    result = cursor.fetchall()

    for produto in result:
        print("Nome: ", students[0], "- ", students[1], "-", students[2])
        print("---------------------------------------------------")
    cursor.close()
    conn.close()
else:
    print("Não foi possível conectar ao banco")