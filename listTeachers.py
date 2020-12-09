import mysql.connector

def listTeachers():
    conn = mysql.connector.connect(host='localhost', database='english_school', user='root', password='')
    if conn.is_connected():
        cursor = conn.cursor()

        cursor.execute("SELECT t.name, t.country, t.module, t.weekday FROM teachers t order by t.name")
        result = cursor.fetchall()

        for data in result:
            print("Nome: {:<20} País: {:<20} Turma: {} - {:<15} ".format(data[0], data[1], data[2], data[3]))

        cursor.close()
        conn.close()
    else:
        print("Não foi possível conectar ao banco")