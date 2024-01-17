import PySimpleGUI as sg
import DataHelper

dh = DataHelper.dataHelper()
sg.theme('DarkAmber') #dark theme
# colors
C = sg.theme_button_color()
B = sg.theme_background_color()

#other windows
import MonsterManager as MM
import Void as V
class loadStepEleven:
    def __init__(self,Title:str) -> None:
        self.CampaignData = dh.loadChampaign(Title)
        Mainmenu = [
           [sg.Text('Champaign Title',k='Title',justification='center',s=(20,1))],
           [sg.Button("Monsters",key='Monsters',s=(10,1),button_color = (C[1],B),border_width=0)],
           [sg.Button("Players",key='Players',s=(10,1),button_color = (C[1],B),border_width=0)],
           [sg.Button("Void",key='Void',s=(10,1),button_color = (C[1],B),border_width=0)],
           [sg.Button("Back",key='Back',s=(10,1),button_color = (C[1],B),border_width=0)],
        ]
        self.window = sg.Window('D&DHub',Mainmenu)
        e, v = self.window.read(timeout=0)
        self.window['Title'].update(Title)
    def WindowActive(self):
        while True:
            event, values = self.window.read()
            if event == "Monsters":
                MonsterScreen = MM.MonsterManger(self.CampaignData)
                MonsterScreen.WindowActive()
            if event == "Players":
                pass
            if event == "Void":
                VoidScreen = V.Void(self.CampaignData)
                VoidScreen.WindowActive()
            if event == "Back":
                break
        self.window.close()
        return 1