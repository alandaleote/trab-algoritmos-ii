import mysql.connector

def listClasses():
    conn = mysql.connector.connect(host='localhost', database='english_school', user='root', password='')
    if conn.is_connected():
        cursor = conn.cursor()

        cursor.execute("SELECT c.module, c.weekday, c.teachername FROM classes c order by c.weekday")
        result = cursor.fetchall()

        for data in result:
            print("Módulo: {} - {:<15} Professor {:<20}".format(data[0], data[1], data[2]))

        cursor.close()
        conn.close()
    else:
        print("Não foi possível conectar ao banco")