import mysql.connector
import PySimpleGUI as gui
def listTeachers():
    conn = mysql.connector.connect(host='localhost', database='english_school', user='root', password='')
    if conn.is_connected():
        cursor = conn.cursor()

        cursor.execute("SELECT t.name, t.country, t.module, t.weekday FROM teachers t order by t.name")
        result = cursor.fetchall()
        listHeader = ["     Nome      ", "    Pais   ","     Turma    ", "    Dia da Semana   "]
        listWidth = [20, 20, 20, 20]
        for row in result:
            layout =[
                [gui.Table(values= result, col_widths=listWidth, headings=listHeader, justification="left")],
                [gui.Button('Exit')]]
                
        window = gui.Window('Lista de Professores', layout)
        while True:  # Event Loop
            event, values = window.read()
            if event in (gui.WIN_CLOSED, 'Exit'):
                break
            window.close()

        cursor.close()
        conn.close()
    else:
        print("Não foi possível conectar ao banco")