import PySimpleGUI as sg

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


creationMenu = [
    [sg.Text('Name'), sg.Input(default_text="Character")],
    [sg.Text('Character Preferences',s=(30,1),font=(sg.DEFAULT_FONT[0],20))],
    [sg.Checkbox("Custom Homebrew",key="CH",pad=(0,0))],
    [sg.Checkbox("'Offical' Homebrew",key="OH",pad=(0,0))],
    [sg.Checkbox("Critical Role Content",key="CR",pad=(0,0))],
    [sg.Text('Optional Features',pad=(4,4),font=(sg.DEFAULT_FONT[0],15))],
    [sg.Checkbox("Optional Class Features",key="OF")],
    [sg.Checkbox("Customize Your Origin",key="CO")],
    [sg.Text('Hit Point Type',pad=(4,4),font=(sg.DEFAULT_FONT[0],15))],
    [sg.DropDown(["Fixed","Manual"],s=(15,2),readonly=True,text_color=C[1],button_background_color=B,background_color=B,)]
]





# Create the main window
mainWindow = sg.Window('D&D Helper', startlayout)

#Variables 
state = 0


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
        creationWindow = sg.Window('D&D Helper',creationMenu)
        mainWindow.close()
        mainWindow = creationWindow #skuffed but it works

        


mainWindow.close()
