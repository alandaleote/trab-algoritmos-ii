import mysql.connector

def listStudents():
    conn = mysql.connector.connect(host='localhost', database='english_school', user='root', password='')
    if conn.is_connected():
        cursor = conn.cursor()

        cursor.execute("SELECT s.name, s.country, s.module, s.weekday FROM students s order by s.module")
        result = cursor.fetchall()
        listHeader = ["     Nome      ", "    Pais   ","     Modulo    ", "    Dia da Semana   "]
        listWidth = [20, 20, 20, 20]
        for row in result:
            layout =[
                [gui.Table(values= result, col_widths=listWidth, headings=listHeader, justification="left")],
                [gui.Button('Exit')]]
                
        window = gui.Window('Lista de Alunos', layout)
        while True:  # Event Loop
            event, values = window.read()
            if event in (gui.WIN_CLOSED, 'Exit'):
                break
            window.close()

        cursor.close()
        conn.close()
    else:
        print("Não foi possível conectar ao banco")