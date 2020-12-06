# encoding: utf-8
import mysql.connector
from FormStudents import FormStudent
from Student import Student

conn = mysql.connector.connect(host='localhost', database='english_school', user='root', password='')
if conn.is_connected():
    form = FormStudent()
    student = form.show()

    if student:
        query = "INSERT INTO students (name, country, module) VALUES ( "
        query += " '" + student.name + "', '"  + student.country + "', '" +  student.module+ " ')"
        cursor = conn.cursor()
        cursor.execute( query ) 
        conn.commit()
        cursor.close()
        conn.close()
else: 
    print( "Não foi possível conectar ao banco") 