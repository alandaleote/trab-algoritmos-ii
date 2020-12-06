import PySimpleGUI as gui
from Student import Student


class FormStudent:
    def __init__(self):
        conteudo = [
            [gui.Text("Nome: ") , gui.Input()],
            [gui.Text("Pa�s: ") , gui.Input(key = 'txtCountry')],
            [gui.Text("M�dulo: "), gui.Input(key = 'txtModule')],
            [gui.Button("Salvar ")]
        ]
        self.tela = gui.Window("Formul�rio de Estudantes").layout(conteudo)

    def show(self):
        self.button, self.valores = self.tela.Read()
        name = self.valores[0]
        if len(name) != 0:
            stud = Student()
            stud.name = name.upper()
            country= self.valores['txtCountry']
            module = self.valores['txtModule']
            stud.country = country.upper()
            stud.module = module.upper()
            
            return stud
        else:
            return None