import PySimpleGUI as gui
from Classes import Classes


class FormClasses:
    def __init__(self):
        conteudo = [
            [gui.Text("Módulo: ", size=(12, 0)) , gui.Input()],
            [gui.Text("Dia da semana: ",size=(12, 0)) , gui.Input(key = 'txtWeekDay')],
            [gui.Text("Professor: ", size=(12, 0)), gui.Input(key = 'txtTeacher')],
            [gui.Button("Salvar ")]
        ]
        self.tela = gui.Window("Inserir turma").layout(conteudo)

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