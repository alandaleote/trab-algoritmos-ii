import mysql.connector

# conecção com banco de dados
conn = mysql.connector.connect(host='localhost', database='english_school', user='root', password='')


module = ['Iniciante', 'Basico', 'Intermediario', 'Avancado']
weekday = ['Domingo', 'Segunda-feira', 'Terca-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sabado']
country = ['Brasil', 'Canada', 'France', 'Germany', 'England', 'Argentina', 'Spain', 'Italy', 'Netherlands', 'US' ]


# testando a conexão com Banco de Dados
if conn.is_connected():
    info = conn.get_server_info()
   
    cursor = conn.cursor()

    query = " "
    query += "values ('Alanda Leote', '{}', '{}', '{}'), ".format(country[1], module[3], weekday[6])
    query += "values ('Aline Necchi', '{}', '{}', '{}'), ".format(country[0], module[2], weekday[0])
    query += "values ('Bernardo Araujo', '{}', '{}', '{}'), ".format(country[1], module[3], weekday[6])
    query += "values ('Vanessa Thompson', '{}', '{}', '{}'), ".format(country[2], module[2], weekday[4])
    query += "values ('Bianca Whitaker', '{}', '{}', '{}'), ".format(country[3], module[3], weekday[1])
    query += "values ('Margarete Goodwin', '{}', '{}', '{}'), ".format(country[2], module[3], weekday[1])
    query += "values ('Derick Mclaughlin', '{}', '{}', '{}'), ".format(country[0], module[2], weekday[4])
    query += "values ('Carina Richardson', '{}', '{}', '{}'), ".format(country[1], module[1], weekday[3])
    query += "values ('Oswaldo Hays', '{}', '{}', '{}'), ".format(country[1], module[0], weekday[2])
    query += "values ('Johan Snow', '{}', '{}', '{}'), ".format(country[4], module[2], weekday[0])
    query += "values ('Noel Green', '{}', '{}', '{}'), ".format(country[4], module[0], weekday[2])
    query += "values ('Selena Benton', '{}', '{}', '{}'), ".format(country[5], module[2], weekday[0])
    query += "values ('David Phillips', '{}', '{}', '{}'), ".format(country[8], module[2], weekday[0])
    query += "values ('Jack Brooks', '{}', '{}', '{}'); ".format(country[7], module[2], weekday[4])
    cursor.execute(query)

    query = "INSERT INTO teachers(name, country, module, weekday)"
    query += " values ('Sophia Goodwin', '{}', '{}', '{}'),".format(country[4], module[0], weekday[2])
    query += " values ('Alfred Lambert', '{}', '{}', '{}'),".format(country[4], module[1], weekday[3])
    query += " values ('Derick Riggs', '{}', '{}', '{}'),".format(country[9], module[2], weekday[0])
    query += " values ('Derick Riggs', '{}', '{}', '{}'),".format(country[9], module[2], weekday[4])
    query += " values ('Trevor Norman', '{}', '{}', '{}'),".format(country[1], module[3], weekday[6])
    query += " values ('Meaghan Bender', '{}', '{}', '{}');".format(country[1], module[3], weekday[1])
    cursor.execute(query)

    query = "INSERT INTO classes(module, weekday, teachername)"
    query += " values ('{}', '{}', 'Sophia Goodwin'),".format(module[0], weekday[2])
    query += " values ('{}', '{}', 'Alfred Lambert'),".format(module[1], weekday[3])
    query += " values ('{}', '{}', 'Derick Riggs'),".format(module[2], weekday[0])
    query += " values ('{}', '{}', 'Derick Riggs'),".format(module[2], weekday[4])
    query += " values ('{}', '{}', 'Trevor Norman'),".format(module[3], weekday[6])
    query += " values ('{}', '{}', 'Meaghan Bender');".format(module[3], weekday[1])
    cursor.execute(query)

    conn.commit()
    cursor.close()
    conn.close()
else:
    print("Não foi possível conectar ao banco")








