import PySimpleGUI as gui
from Teacher import Teacher


class FormTeacher:
    def __init__(self):
        conteudo = [
            [gui.Text("Nome: ") , gui.Input()],
            [gui.Text("País: ") , gui.Input(key = 'txtCountry')],
            [gui.Text("Módulo: "), gui.Input(key = 'txtModule')],
            [gui.Text("Dia da semana: "), gui.Input(key = 'txtWeekday')],
            [gui.Button("Salvar ")]
        ]
        self.tela = gui.Window("Formulário de Professores").layout(conteudo)

    def show(self):
        self.button, self.valores = self.tela.Read()
        name = self.valores[0]
        if len(name) != 0:
            teach = Teacher()
            teach.name = name.upper()
            country= self.valores['txtCountry']
            module = self.valores['txtModule']
            weekday = self.valores['txtWeekday']
            teach.country = country.upper()
            teach.module = module.upper()
            teach.weekday = weekday.upper()
            
            return teach
        else:
            return None