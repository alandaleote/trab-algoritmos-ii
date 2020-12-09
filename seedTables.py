import mysql.connector

# conecção com banco de dados
conn = mysql.connector.connect(host='localhost', database='english_school', user='root', password='')


module = ('Iniciante', 'Basico', 'Intermediario', 'Avancado')
weekday = ('Segunda-feira', 'Terca-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sabado', 'Domingo')
country = ('Brasil', 'Canada', 'France', 'Germany', 'England', 'Argentina', 'Spain', 'Italy', 'Netherlands', 'US' )


# testando a conexão com Banco de Dados
if conn.is_connected():
    info = conn.get_server_info()
   
    cursor = conn.cursor()

    query = "INSERT INTO STUDENTS (name, country, module, weekday) "
    query += "values ('Alanda Leote', 'Canada', 'Avancado', 'Sabado'), "
    query += "values ('Aline Necchi', 'Brasil', 'Intermediario', 'Domingo'), "
    query += "values ('Bernardo Araujo', 'Canada', 'Avancado', 'Sabado'), "
    query += "values ('Vanessa Thompson', 'France', 'Intermediario', 'Quinta-feira'), "
    query += "values ('Bianca Whitaker', 'Germany', 'Avancado', 'Segunda-feira'), "
    query += "values ('Margarete Goodwin', 'France', 'Avancado', 'Segunda-feira'), "
    query += "values ('Derick Mclaughlin', 'Brasil', 'Intermediario', 'Quinta-feira'), "
    query += "values ('Carina Richardson', 'Spain', 'Basico', 'Quarta-feira'), "
    query += "values ('Oswaldo Hays', 'Germany', 'Iniciante', 'Terca-feira'), "
    query += "values ('Johan Snow', 'England', 'Intermediario', 'Domingo'), "
    query += "values ('Noel Green', 'England', 'Iniciante', 'Terca-feira'), "
    query += "values ('Selena Benton', 'Argentina', 'Intermediario', 'Domingo'), "
    query += "values ('David Phillips', 'Netherlands', 'Intermediario', 'Domingo'), "
    query += "values ('Jack Brooks', 'Italy', 'Intermediario', 'Quinta-feira'); "
    cursor.execute(query)

    query = "INSERT INTO TEACHERS (name, country, module, weekday)"
    query += " values ('Sophia Goodwin', 'England', 'Iniciante', 'Terca-feira'),"
    query += " values ('Alfred Lambert', 'England', 'Basico', 'Quarta-feira'),"
    query += " values ('Derick Riggs', 'US', 'Intermediario', 'Domingo'),"
    query += " values ('Derick Riggs', 'US', 'Intermediario', 'Quinta-feira'),"
    query += " values ('Trevor Norman', 'Canada', 'Avancado', 'Sabado'),"
    query += " values ('Meaghan Bender', 'Canada', 'Avancado', 'Segunda-feira');"
    cursor.execute(query)

    query = "INSERT INTO CLASSES (module, weekday, teachername)"
    query += " values ('Iniciante', 'Terca-feira', 'Sophia Goodwin'),"
    query += " values ('Basico', 'Quarta-feira', 'Alfred Lambert'),"
    query += " values ('Intermediario', 'Domingo', 'Derick Riggs'),"
    query += " values ('Intermediario', 'Quinta-feira', 'Derick Riggs'),"
    query += " values ('Avancado', 'Sabado', 'Trevor Norman'),"
    query += " values ('Avancado', 'Segunda-feira', 'Meaghan Bender');"
    cursor.execute(query)

    cursor.close()
    conn.close()
else:
    print("Não foi possível conectar ao banco")








