import PySimpleGUI as sg
from requests.exceptions import ConnectionError
import Backend 

rq = Backend.requester()


sg.theme('DarkAmber')   #dark theme
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
    [sg.Listbox(values = [],key="",background_color=B,s=(45,20))],
    [sg.Button("Make a new character",key='newC',s=(40,1),button_color = (C[1],B),border_width=0)],
    [sg.Text('')]
]

CharacterColumn = sg.Column(CharacterList,justification="center")

startlayout = [
    [sg.Text('Gameplay',s=(50,1),justification="c")],
    [topColumn],
    [CharacterColumn]
]


creationMenu = [
    [sg.Text('Name'), sg.Input(default_text="Character",key="Name")],
    [sg.Text('Character Preferences',s=(30,1),font=(sg.DEFAULT_FONT[0],20))],
    [sg.Checkbox("Custom Homebrew",key="CH",pad=(0,0))],
    [sg.Text('Optional Features',pad=(4,4),font=(sg.DEFAULT_FONT[0],15))],
    [sg.Checkbox("Optional Class Features",key="OF")],
    [sg.Checkbox("Customize Your Origin",key="CO")],
    [sg.Text('Hit Point Type',pad=(4,4),font=(sg.DEFAULT_FONT[0],15))],
    [sg.DropDown(["Fixed","Manual"],s=(15,2),readonly=True,text_color=C[1],button_background_color=B,background_color=B,key="HPT",default_value="Fixed")],
    [sg.Text('Use Prerequisites',pad=(4,4),font=(sg.DEFAULT_FONT[0],15))],
    [sg.Checkbox("Feats",key="FP")],
    [sg.Checkbox("Multiclass Requirements",key="MR")],
    [sg.Text('Show Level-Scaled Spells',pad=(4,4),font=(sg.DEFAULT_FONT[0],15))],
    [sg.Checkbox("Display and highlight available spells to cast with higher level spell slots",key="HLSS")],
    [sg.Text('Ability Score/Modifier Display',pad=(4,4),font=(sg.DEFAULT_FONT[0],15))],
    [sg.DropDown(["Modifiers Top","Scores Top"],s=(15,2),readonly=True,text_color=C[1],button_background_color=B,background_color=B,key="ASD",default_value="Modifiers Top")],
    [sg.Button("Submit",key="Submit Preferences",s=(60,1),button_color = (C[1],B),border_width=0)]
]


classes = ['Artificer','Barbarian','Bard','Blood-Hunter','Cleric','Druid','Fighter','Monk','Paladin','Ranger','Rogue','Sorcerer','Warlock','Wizard']
classesMenu = [
    [sg.Text('Choose a Class',s=(45,1),font=(sg.DEFAULT_FONT[0],20)),sg.DropDown(classes,enable_events=True,readonly=True,key='classes',s=(15,1),pad=(0,0),text_color=C[1],button_background_color=B,background_color=B),sg.Text('level',s=(8,1),pad=(0,0)),sg.DropDown(['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20',],'1',enable_events=True,readonly=True,key='level',s=(15,1),pad=(0,0),text_color=C[1],button_background_color=B,background_color=B,button_arrow_color=C[0])],
    [sg.Multiline('',no_scrollbar=True,s=(150,30),key='info')],
    [sg.Button("Submit",key="Submit Class",s=(130,1),button_color = (C[1],B),border_width=0)]
]

# Create the main window
mainWindow = sg.Window('D&D Helper', startlayout)

#Variables 
state = 0
tempCharacter = {}

subraceList = []
currentRace = ''

while True:
    event, values = mainWindow.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    if event == "Characters" and state != 0:
        state = 0
        mainWindow["Characters"].update(button_color = (C[1],B))
        mainWindow["Campaigns"].update(button_color = (C[0],B))
    if event == "Campaigns" and state != 1:
        state = 1
        mainWindow["Campaigns"].update(button_color = (C[1],B))
        mainWindow["Characters"].update(button_color = (C[0],B))
    if event == "newC":
        mainWindow = rq.swapWindow(mainWindow,creationMenu)
    
    #creationMenu
    if event == "Submit Preferences":
        #remember everything
        values:dict
        tempCharacter = values.copy()
        #move on to page 2
        races = rq.getRaces()

        raceMenu = [
            [sg.Text('Choose a Race',s=(15,1),font=(sg.DEFAULT_FONT[0],20)),sg.Text('Subrace',s=(7,1),pad=(0,0)),sg.DropDown(['Subrace'],'Subrace',enable_events=True,readonly=True,key='subrace',s=(55,1),pad=(0,0),text_color=C[1],button_background_color=B,background_color=B)]
        ]
        raceMenu.append([sg.Listbox(races,no_scrollbar=True,s=(20,20),key="Race",enable_events=True),sg.Multiline("",no_scrollbar=True,s=(80,20),key='info',)])
        raceMenu.append([sg.Button("Submit",key="Submit Race",s=(19,1),pad=(0,0),button_color = (C[1],B),border_width=0)])
        mainWindow = rq.swapWindow(mainWindow,raceMenu)
    

    #race Menu
    if event == "Race":
        try:
            subraceList = rq.getRaceInformation(values["Race"][0])
        except ConnectionError:
            #no wifi
            subraceList = rq.getSavedRaceInformation(values["Race"][0])
        mainWindow["subrace"].update(values=subraceList,value=subraceList[0])
        mainWindow["info"].update(rq.getRaceFile(subraceList[0]))
        currentRace = subraceList[0]

    elif event == "subrace":
        mainWindow["info"].update(rq.getRaceFile(values['subrace']))
        currentRace = values['subrace']
    
    elif event == "Submit Race":
        tempCharacter['race'] = currentRace
        if currentRace != '':
            mainWindow = rq.swapWindow(mainWindow,classesMenu)

    #classes window
    if event == 'classes':
        mainWindow["info"].update(rq.checkForClassFile(values['classes']))
    if event == 'Submit Class':
        tempCharacter['level'] = int(values['level'])
        tempCharacter['class'] = values['classes']
        if values['classes'] != '':
            classLayout = rq.loadLayout(values['classes'],values['level'])
            classColumn = sg.Column(classLayout,scrollable=True,s=(1050,500))
            t = [[classColumn],[[sg.Button("Submit",key="Confirm Class",s=(19,1),pad=(0,0),button_color = (C[1],B),border_width=0),sg.Button("Reload Class",key="Reload",s=(19,1),pad=(0,0),button_color = (C[1],B),border_width=0)]]]
            mainWindow = rq.swapWindow(mainWindow,t)
    
    if event == 'Reload':
        mainWindow.close()
        classLayout = rq.loadLayout(tempCharacter['class'])
        tc = sg.Column(classLayout,scrollable=True,s=(1050,500))
        tt = [[tc],[[sg.Button("Submit",key="Confirm Class",s=(19,1),pad=(0,0),button_color = (C[1],B),border_width=0),sg.Button("Reload Class",key="Reload",s=(19,1),pad=(0,0),button_color = (C[1],B),border_width=0)]]]
        mainWindow = sg.Window('Dev',tt)

mainWindow.close()
