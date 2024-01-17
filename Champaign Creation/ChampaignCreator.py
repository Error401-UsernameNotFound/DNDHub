import PySimpleGUI as sg
import DataHelper

dh = DataHelper.dataHelper()
sg.theme('DarkAmber') #dark theme
# colors
C = sg.theme_button_color()
B = sg.theme_background_color()

class loadStepTen:
    def __init__(self) -> None:
        CreationScreen = [
            [sg.Text('Champaign Title',justification='center',s=(45,1))],
            [sg.Input('',k='title',s=(50,1))],
            [sg.Text('Description',justification='center',s=(45,1))],
            [sg.Multiline("",no_scrollbar=True,s=(50,10),k='description')],
            [sg.Button("Back",key='Back',s=(20,1),button_color = (C[1],B),border_width=0),sg.Button("Submit",key="Submit",s=(20,1),button_color = (C[1],B),border_width=0)]
        ]
        self.window = sg.Window('D&DHub',CreationScreen)
    def WindowActive(self):
        while True:
            event, values = self.window.read()
            if event == "Submit":
                #save the Champaign
                Champaign = {
                    'Title': values['title'],
                    'Description': values['description']
                }
                dh.saveChampaign(Champaign)
                break

            if event == "Back":
                break
        self.window.close()
        return 1