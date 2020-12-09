import PySimpleGUI as gui

from delete import deleteStudent
from insertClass import insertClass
from insertStudent import insertStudent
from insertTeacher import insertTeacher
from listClasses import listClasses
from listStudents import listStudents
from listTeachers import listTeachers

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
            insertStudent()
        elif escolha == '4':
            listStudents()
        elif escolha == '5':
            listTeachers()
        elif escolha == '6':
            listClasses()
        elif escolha == '7':
            deleteStudent()
        else:
            input('Opcao Invalida! [Enter]')
menu = '''
1 - Inserir Turma                  
2 - Inserir Professor              
3 - Inserir Aluno                  
4 - Listar Alunos
5 - Listar Professor
6 - Listar Classes
7 - Deletar Estudantes                 

Insira a sua escolha:
 '''

form = FormMenu()
newclass = form.show()
    
    
    
