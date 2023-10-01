import PySimpleGUI as sg
import sys
import os
from requests.exceptions import ConnectionError
import Backend


#all of the characture creation screens
sys.path.insert(1, os.path.dirname(__file__)+'\Character Creation')
import CharacterSettings as CC
import CharacterSheet as CS

#Champaign Creator menu
sys.path.insert(1, os.path.dirname(__file__)+'\Champaign Creation')
import ChampaignCreator as ChC
import CampaignScreen as CampS

rq = Backend.requester()


sg.theme('DarkAmber') #dark theme
# colors
C = sg.theme_button_color()
B = sg.theme_background_color()
#layouts
top = [
    [sg.Button('My Characters', key='Characters', pad=(2,0),button_color = (C[1],B),border_width=0),      
    sg.Button('My Campaigns', key='Campaigns', pad=(2,0),button_color = (C[0],B),border_width=0)]
]
topColumn = sg.Column(top,justification="c")

CharacterList = [
    [sg.Listbox(values = [],key="List",background_color=B,s=(45,20),enable_events=True)],
    [sg.Button("Make a new character",key='newC',s=(40,1),button_color = (C[1],B),border_width=0)],
    [sg.Text('')]
]

CharacterColumn = sg.Column(CharacterList,justification="center")

startlayout = [
    [sg.Text('Gameplay',s=(50,1),justification="c")],
    [topColumn],
    [CharacterColumn]
]

#Create the main window
mainWindow = sg.Window('D&DHub', startlayout)

#Variables 
state = 0
tempCharacter = {}

subraceList = []
currentRace = ''
event = ''
values = {}

#pre load values into layout
event, values = mainWindow.read(timeout=0.01)
mainWindow['List'].update(values = rq.findAllFileNames(state))

while True:
    if state == 0 or state == 1:
        if mainWindow._Hidden:
            mainWindow.un_hide()
            event, values = mainWindow.read(timeout=0.01)
            mainWindow['List'].update(values = rq.findAllFileNames(state))
        event, values = mainWindow.read()
        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            break

        if event == "Characters" and state != 0:
            state = 0
            mainWindow["Characters"].update(button_color = (C[1],B))
            mainWindow["Campaigns"].update(button_color = (C[0],B))
            mainWindow['newC'].update(text = 'Make a new character')
            event, values = mainWindow.read(timeout=0.01)
            mainWindow['List'].update(values = rq.findAllFileNames(state))
        

        if event == "Campaigns" and state != 1:
            state = 1
            mainWindow["Campaigns"].update(button_color = (C[1],B))
            mainWindow["Characters"].update(button_color = (C[0],B))
            mainWindow['newC'].update(text = 'Make a new campaign')
            event, values = mainWindow.read(timeout=0.01)
            mainWindow['List'].update(values = rq.findAllFileNames(state))
        if event == 'List' and state == 1:
            state = 11
            mainWindow.hide()
        
        if event == "newC" and state == 0:
            state = 2
            mainWindow.hide()
        if event == "newC" and state == 1:
            state = 10
            mainWindow.hide()
    

    if state == 2:#General character creator
        stepOne = CC.loadStepOne()
        state, tempCharacter = stepOne.WindowActive()
    if state == 3:#sheet
        StepFive = CS.loadStepFive()
        StepFive.WindowActive(tempCharacter)
    
    #Campaign
    if state == 10:
        StepTen = ChC.loadStepTen()
        state = StepTen.WindowActive()
    if state == 11:
        StepEleven = CampS.loadStepEleven(values['List'][0])
        state = StepEleven.WindowActive()


mainWindow.close()
