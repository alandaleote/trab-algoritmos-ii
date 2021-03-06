import PySimpleGUI as gui
from Teacher import Teacher


class FormTeacher:
    def __init__(self):
        conteudo = [
            [gui.Text("Nome: ", size=(12, 0)) , gui.Input(key = 'txtName')],
            [gui.Text("País: ", size=(12, 0)) , gui.Input(key = 'txtCountry')],
            [gui.Text("Módulo: ", size=(12, 0)), gui.Input(key = 'txtModule')],
            [gui.Text("Dia da semana: ", size=(12, 0)), gui.Input(key = 'txtWeekday')],
            [gui.Button("Salvar ")]
        ]
        self.tela = gui.Window("Formulário de Professores").layout(conteudo)

    def show(self):
        self.button, self.valores = self.tela.Read()
        name = self.valores['txtName']
        if len(name) != 0:
            teach = Teacher()
            teach.setName(name.upper())
            country= self.valores['txtCountry']
            module = self.valores['txtModule']
            weekday = self.valores['txtWeekday']
            teach.setCountry(country.upper())
            teach.setModule(module.upper())
            teach.setWeekday(weekday.upper())
            
            return teach
        else:
            return None