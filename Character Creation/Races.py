import PySimpleGUI as sg
import Backend
from requests.exceptions import ConnectionError

rq = Backend.requester()

sg.theme('DarkAmber') #dark theme
# colors
C = sg.theme_button_color()
B = sg.theme_background_color()



class loadStepTwo:
    def __init__(self) -> None:
        self.races = rq.getRaces()

        self.raceMenu = [
            [sg.Text('Choose a Race',s=(15,1),font=(sg.DEFAULT_FONT[0],20)),sg.Text('Subrace',s=(7,1),pad=(0,0)),sg.DropDown(['Subrace'],'Subrace',enable_events=True,readonly=True,key='subrace',s=(55,1),pad=(0,0),text_color=C[1],button_background_color=B,background_color=B)]
        ]
        self.raceMenu.append([sg.Listbox(self.races,no_scrollbar=True,s=(20,20),key="Race",enable_events=True),sg.Multiline("",no_scrollbar=True,s=(80,20),key='info',)])
        self.raceMenu.append([sg.Button("Back",key='Back',s=(15,1),button_color = (C[1],B),border_width=0),sg.Button("Submit",key="Submit Race",s=(15,1),pad=(0,0),button_color = (C[1],B),border_width=0)])
        self.window = sg.Window('D&DHub',self.raceMenu)
    def WindowActive(self,tempCharacter:dict):
        Forward = True
        currentRace = ''
        while True:
            event, values = self.window.read()
            if event == "Race":
                try:
                    subraceList = rq.getRaceInformation(values["Race"][0])
                except ConnectionError:
                    #no wifi
                    subraceList = rq.getSavedRaceInformation(values["Race"][0])
                self.window["subrace"].update(values=subraceList,value=subraceList[0])
                self.window["info"].update(rq.getRaceFile(subraceList[0]))
                currentRace = subraceList[0]

            if event == "subrace":
                self.window["info"].update(rq.getRaceFile(values['subrace']))
                currentRace = values['subrace']
            
            if event == "Submit Race":
                tempCharacter['race'] = currentRace
                if values["info"].find('Increase one ability score by 2, and increase a different one by 1, or increase three different scores by 1.') != -1:
                    tempCharacter['CustomAsi'] = True
                else:
                    tempCharacter['CustomAsi'] = False
                if currentRace != '':
                    break
            
            if event == 'Back':
                Forward = False
                break
        self.window.close()
        if Forward:
            return (4,tempCharacter)
        else: return (2,tempCharacter)
