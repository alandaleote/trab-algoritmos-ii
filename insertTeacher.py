import mysql.connector
from FormTeacher import FormTeacher
from Teacher import Teacher

conn = mysql.connector.connect(host='localhost', database='english_school', user='root', password='')
if conn.is_connected():
    form = FormTeacher()
    teacher = form.show()

    if teacher:
        query = "INSERT INTO teachers (name, country, classes) VALUES ( "
        query += " '" + teacher.name + "', '"  + teacher.country + "', '" +  teacher.classes + " ')"
        cursor = conn.cursor()
        cursor.execute( query ) 
        conn.commit()
        cursor.close()
        conn.close()
else: 
    print( "Não foi possível conectar ao banco") 