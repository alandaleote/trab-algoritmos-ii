import mysql.connector
import PySimpleGUI as gui

def listClasses():
    conn = mysql.connector.connect(host='localhost', database='english_school', user='root', password='')
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("SELECT c.module, c.weekday, c.teachername FROM classes c order by c.weekday")
        result = cursor.fetchall()
        listHeader = ["     Modulo      ", "    Dia da semana   ","     Professor    "]
        listWidth = [20,20,20]
        for data in result:
            layout =[
                [gui.Table(values= result, key='-LIST-', col_widths= listWidth,headings=listHeader,justification="left")],
                [gui.Button('Exit')]]
        window = gui.Window('Lista de Turmas ', layout)
        while True:  # Event Loop
            event, values = window.read()
            if event in (gui.WIN_CLOSED, 'Exit'):
                break
            window.close()
        cursor.close()
        conn.close()
    else:
        print("Não foi possível conectar ao banco")