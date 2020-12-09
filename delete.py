import mysql.connector

def deleteStudent():
    conn = mysql.connector.connect(host='localhost', database='english_school', user='root', password='')
    if conn.is_connected():
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM students")
        result = cursor.fetchall()

        for students in result:
            texto = str(students[0]) + ": " + students[1] + "-" + str(students[2])
            print(texto)
        id = input("Digite o nome do estudante que deseja excluir: ")
        cursor.execute("DELETE FROM students WHERE name = '{}'".format(id.upper()))
        conn.commit()

        cursor.execute("SELECT * FROM students")
        result = cursor.fetchall()
        for students in result:
            texto = str(students[0]) + ": " + students[1] + "-" + str(students[2])
            print(texto)
        cursor.close()
        conn.close()
    else:
        print("Não foi possível conectar ao banco")