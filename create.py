import mysql.connector

# conecção com banco de dados
conn = mysql.connector.connect(host='localhost', database='english_school', user='root', password='')

# testando a conexão com Banco de Dados
if conn.is_connected():
    info = conn.get_server_info()
    print("Conectado ao MySQL", info)
    print("------------------")
    print("Tabelas existentes")

    cursor = conn.cursor()
    cursor.execute("SHOW TABLES")
    for linha in cursor:
        print(linha)
    print("----------------------")
    # criando tabela
    query = "CREATE TABLE IF NOT EXISTS students("
    query += " id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,"
    query += " name VARCHAR(100) NOT NULL UNIQUE,"
    query += " country VARCHAR(50) NOT NULL,"
    query += " module VARCHAR(50) NOT NULL,"
    query += " weekday VARCHAR(50) NOT NULL );"
    cursor.execute(query)

    query = "CREATE TABLE IF NOT EXISTS teachers("
    query += " id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,"
    query += " name VARCHAR(100) NOT NULL UNIQUE,"
    query += " country VARCHAR(50) NOT NULL,"
    query += " module VARCHAR(50) NOT NULL,"
    query += " weekday VARCHAR(50) NOT NULL );"
    cursor.execute(query)

    query = "CREATE TABLE IF NOT EXISTS classes("
    query += " module VARCHAR(50) NOT NULL,"
    query += " weekday VARCHAR(50) NOT NULL,"
    query += " teachername VARCHAR(50),"
    query += " PRIMARY KEY (module, weekday) );"
    cursor.execute(query)

    print("Tabelas existentes")
    cursor.execute("SHOW TABLES")
    for linha in cursor:
        print(linha)
    cursor.close()
    conn.close()
else:
    print("Não foi possível conectar ao banco")