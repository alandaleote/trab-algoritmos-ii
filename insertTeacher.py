import mysql.connector
from FormTeacher import FormTeacher

def insertTeacher():
    conn = mysql.connector.connect(host='localhost', database='english_school', user='root', password='')
    if conn.is_connected():
        form = FormTeacher()
        teacher = form.show()

        if teacher:
            query = "INSERT INTO teachers (name, country, module, weekday) VALUES ('{}', '{}', '{}', '{}')".format(teacher.name, teacher.country, teacher.module, teacher.weekday)
            cursor = conn.cursor()
            cursor.execute( query ) 
            conn.commit()
            cursor.close()
            conn.close()
    else: 
        print( "Não foi possível conectar ao banco") 