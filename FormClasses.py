import PySimpleGUI as gui
from Classes import Classes

class FormClasses:
    def __init__(self):
        conteudo = [
            [gui.Text("Módulo: ") , gui.Input()],
            [gui.Text("WeekDay: ") , gui.Input(key = 'txtWeekDay')],
            [gui.Text("Teacher: "), gui.Input(key = 'txtTeacher')],
            [gui.Button("Salvar ")]
        ]
        self.tela = gui.Window("Formulário de Módulos").layout(conteudo)

    def show(self):
        self.button, self.valores = self.tela.Read()
        module = self.valores[0]
        if len(module) != 0:
            clas = Classes()
            clas.module = module.upper()
            weekday= self.valores['txtWeekDay']
            teachername = self.valores['txtTeacher']
            clas.weekday = weekday.upper()
            clas.teachername = teachername.upper()
            
            return clas
        else:
            return None