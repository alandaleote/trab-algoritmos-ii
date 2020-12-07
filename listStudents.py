import mysql.connector

conn = mysql.connector.connect(host='localhost', database='english_school', user='root', password='')
if conn.is_connected():
    cursor = conn.cursor()

    cursor.execute("SELECT s.name, s.module, c.teachername, c.weekday FROM students s join classes c on (students.module = classes.module) order by s.module")
    result = cursor.fetchall()

    for data in result:
        print("Módulo: {1} - {3}, Professor: {2}, Aluno: {0}".format(data[0], data[1], data[2], data[3]))

    cursor.close()
    conn.close()
else:
    print("Não foi possível conectar ao banco")