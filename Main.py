import PySimpleGUI as sg
import Backend 

rq = Backend.requester()

sg.theme('DarkAmber')   #dark theme
# colors
C = sg.theme_button_color()
B =  sg.theme_background_color()

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

#creation screen one
creationMenu = [
    [sg.Text('Name'), sg.Input(default_text="Character",key="Name")],
    [sg.Text('Character Preferences',s=(30,1),font=(sg.DEFAULT_FONT[0],20))],
    [sg.Checkbox("Custom Homebrew",key="CH",pad=(0,0))],
    [sg.Checkbox("'Offical' Homebrew",key="OH",pad=(0,0))],
    [sg.Checkbox("Unearthed Arcana",key="OH",pad=(0,0))],
    [sg.Checkbox("Strixhaven",key="OH",pad=(0,0))],
    [sg.Checkbox("Setting Specific*",key="OH",pad=(0,0))],
    [sg.Checkbox("Critical Role Content",key="CR",pad=(0,0))],
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

# Create the main window
mainWindow = sg.Window('D&D Helper', startlayout)

#Variables 
state = 0
tempCharacter = {}
infoDict = {}
subraceList = []
#stuff to be done frame 1

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
            [sg.Text('Choose a Race',s=(30,1),font=(sg.DEFAULT_FONT[0],20)),sg.Text('Subrace',s=(8,1),pad=(0,0)),sg.DropDown(['Subrace'],'Subrace',enable_events=True,readonly=True,key='subrace',s=(15,1),pad=(0,0),text_color=C[1],button_background_color=B,background_color=B)]
        ]
        raceMenu.append([sg.Listbox(races,no_scrollbar=True,s=(20,20),key="Race",enable_events=True),sg.Multiline("",no_scrollbar=True,s=(70,20),key='info')])
        mainWindow = rq.swapWindow(mainWindow,raceMenu)
    

    #race Menu
    if event == "Race":
        infoDict, subraceList = rq.getRaceInformation(values["Race"][0])
        mainWindow["subrace"].update(values=subraceList,value=subraceList[0])
        mainWindow["info"].update(infoDict[subraceList[0]])

    if event == "subrace":
        mainWindow["info"].update(infoDict[values['subrace']])
        


mainWindow.close()
