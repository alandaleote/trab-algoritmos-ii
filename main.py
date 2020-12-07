import PySimpleGUI as gui
from insertClass import insertClass



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
            pass
        elif escolha == '3':
            pass
        elif escolha == '4':
            pass
        else:
            input('Opção inválida! [Enter]')
       






menu = '''

1 - Inserir Turma                  
2 - Inserir Professor              
3 - Inserir Aluno                  
4 - Listar Alunos                  

Insira a sua escolha:
 '''

form = FormMenu()
newclass = form.show()
    
    
    
