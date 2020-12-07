import PySimpleGUI as gui
# Add your new theme colors and settings
gui.LOOK_AND_FEEL_TABLE['EnglishSchool'] = {'BACKGROUND': '#EAE7E2',
                                        'TEXT': '#2C3C5B',
                                        'INPUT': '#FFFDFD',
                                        'TEXT_INPUT': '#473C8B',
                                        'SCROLL': '#473C8B',
                                        'BUTTON': ('#2C3C5B', '#51BFA4'),
                                        'PROGRESS': ('#2C3C5B', '#D0D0D0'),
                                        'BORDER': 5, 'SLIDER_DEPTH': 5, 'PROGRESS_DEPTH': 5,
                                        }
# Switch to use your newly created theme
gui.theme('EnglishSchool')
# Call a popup to show what the theme looks like
gui.popup_get_text(' English School')


gui.LOOK_AND_FEEL_TABLE['English'] = {'BACKGROUND': '#FFC0CB',
                                        'TEXT': '#FF1493',
                                        'INPUT': '#FFFDFD',
                                        'TEXT_INPUT': '#473C8B',
                                        'SCROLL': '#473C8B',
                                        'BUTTON': ('#FF1493', '#DB7093'),
                                        'PROGRESS': ('#D0D0D0', '#DB7093'),
                                        'BORDER': 5, 'SLIDER_DEPTH': 5, 'PROGRESS_DEPTH': 5,
                                        }
# Switch to use your newly created theme
gui.theme('English')
# Call a popup to show what the theme looks like
gui.popup_get_text(' English School') 