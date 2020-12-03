# encoding: utf-8
import mysql.connector
from FormProduto import FormProduto
from Produto import Produto

conn = mysql.connector.connect(host='localhost', database='english_school', user='root', password='')
if conn.is_connected():
    form = FormProduto()
    produto = form.show()

    if produto != None:
        query = "INSERT INTO students (name, module) VALUES ( "
        query += " '" + students.name + "' , " +  students.module+ " ) "

        cursor = conn.cursor()
        cursor.execute( query )
        conn.commit()
        cursor.close()
        conn.close()
else: 
    print( "Não foi possível conectar ao banco") 