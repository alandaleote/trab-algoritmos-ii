import PySimpleGUI as gui

from delete import deleteStudent
from insertClass import insertClass
from insertStudent import insertStudente
from insertTeacher import insertTeacher
from listStudents import listEstudents

gui.theme('Dark Brown')

class FormMenu:
    def __init__(self):
        conteudo = [
            [gui.Text(menu)],
            [gui.Input()],
            [gui.Button("Abrir")]
        ]
        self.tela = gui.Window("English School").layout(conteudo)
    def show(self):
        self.button, self.valores = self.tela.Read()
        escolha = self.valores[0]
        if escolha == '1':
            insertClass()
        elif escolha == '2':
            insertTeacher()
        elif escolha == '3':
            insertStudente()
        elif escolha == '4':
            listEstudents()
        elif escolha == '5':
            deleteStudent()
        else:
            input('OpÃ§Ã£o invÃ¡lida! [Enter]')
menu = '''

1 - Inserir Turma                  
2 - Inserir Professor              
3 - Inserir Aluno                  
4 - Listar Alunos
5 - Deletar Estudantes                 

Insira a sua escolha:
 '''

form = FormMenu()
newclass = form.show()
    
    
    
