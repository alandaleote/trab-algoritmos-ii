import PySimpleGUI as gui
from Teacher import Teacher


class FormTeacher:
    def __init__(self):
        conteudo = [
            [gui.Text("Nome: ") , gui.Input()],
            [gui.Text("Pa�s: ") , gui.Input(key = 'txtCountry')],
            [gui.Text("Turmas: "), gui.Input(key = 'txtClasses')],
            [gui.Button("Salvar ")]
        ]
        self.tela = gui.Window("Formul�rio de Professores").layout(conteudo)

    def show(self):
        self.button, self.valores = self.tela.Read()
        name = self.valores[0]
        if len(name) != 0:
            teach = Teacher()
            teach.name = name.upper()
            country= self.valores['txtCountry']
            classes = self.valores['txtClasses']
            teach.country = country.upper()
            teach.classes = classes.upper()
            
            return teach
        else:
            return None