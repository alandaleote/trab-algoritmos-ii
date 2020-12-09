import PySimpleGUI as gui
from Student import Student


class FormStudent:
    def __init__(self):
        conteudo = [
            [gui.Text("Nome: ", size=(12, 0)) , gui.Input(key = 'txtName')],
            [gui.Text("País: ", size=(12, 0)) , gui.Input(key = 'txtCountry')],
            [gui.Text("Módulo: ", size=(12, 0)), gui.Input(key = 'txtModule')],
            [gui.Text("Dia da semana: ", size=(12, 0)), gui.Input(key = 'txtWeekday')],
            [gui.Button("Salvar ")]
        ]
        self.tela = gui.Window("Formulário de Estudantes").layout(conteudo)

    def show(self):
        self.button, self.valores = self.tela.Read()
        name = self.valores[key = 'txtName']
        if len(name) > 3:
            stud = Student()
            stud.setName(name.upper())
            country= self.valores['txtCountry']
            module = self.valores['txtModule']
            weekday = self.valores['txtWeekday']
            stud.setCountry(country.upper())
            stud.setModule(module.upper())
            stud.setWeekday(weekday.upper())
            
            return stud
        else:
            return None
