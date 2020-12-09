import PySimpleGUI as gui

"""
    Allows you to "browse" through the Theme settings.  Click on one and you'll see a
    Popup window using the color scheme you chose.  It's a simple little program that also demonstrates
    how snappy a GUI can feel if you enable an element's events rather than waiting on a button click.
    In this program, as soon as a listbox entry is clicked, the read returns.
"""

gui.theme('Dark Brown')


layout = [[gui.Text('Theme Browser')],
          [gui.Text('Click a Theme color to see demo window')],
          [gui.Listbox(values=gui.theme_list(), size=(20, 12), key='-LIST-', enable_events=True)],
          [gui.Button('Exit')]]

window = gui.Window('Theme Browser', layout)

while True:  # Event Loop
    event, values = window.read()
    if event in (gui.WIN_CLOSED, 'Exit'):
        break
    gui.theme(values['-LIST-'][0])
    gui.popup_get_text('This is {}'.format(values['-LIST-'][0]))

window.close()