import mysql.connector
from FormStudent import FormStudent

def insertStudente():
    conn = mysql.connector.connect(host='localhost', database='english_school', user='root', password='')
    if conn.is_connected():
        form = FormStudent()
        student = form.show()

        if student:
            query = "INSERT INTO students (name, country, module, weekday) VALUES ('{}', '{}', '{}', '{}')".format(student.name, student.country, student.module, student.weekday)
            cursor = conn.cursor()
            cursor.execute( query ) 
            conn.commit()
            cursor.close()
            conn.close()
    else: 
        print( "Não foi possível conectar ao banco") 