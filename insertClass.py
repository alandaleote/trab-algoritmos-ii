import mysql.connector
from FormClasses import FormClasses

def insertClass():
    conn = mysql.connector.connect(host='localhost', database='english_school', user='root', password='')
    if conn.is_connected():
        form = FormClasses()
        newclass = form.show()

        if newclass:
            query = "INSERT INTO classes (module, weekday, teachername) VALUES ('{}', '{}', '{}')".format(newclass.module, newclass.weekday, newclass.teachername)
            cursor = conn.cursor()
            cursor.execute( query )
            conn.commit()
            cursor.close()
            conn.close()
    else: 
        print( "Não foi possível conectar ao banco")
