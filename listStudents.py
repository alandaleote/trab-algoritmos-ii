import mysql.connector

def listStudents():
    conn = mysql.connector.connect(host='localhost', database='english_school', user='root', password='')
    if conn.is_connected():
        cursor = conn.cursor()

        cursor.execute("SELECT s.name, s.country, s.module, s.weekday FROM students s order by s.module")
        result = cursor.fetchall()

        for data in result:
            
            print("Nome: {:<20} País: {:<20} Módulo: {} - {:<15} ".format(data[0], data[1], data[2], data[3]))

        cursor.close()
        conn.close()
    else:
        print("Não foi possível conectar ao banco")