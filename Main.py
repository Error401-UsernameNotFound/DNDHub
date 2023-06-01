import PySimpleGUI as sg

sg.theme('DarkAmber')   #dark
# ["My Characters","My Campaigns"]
C = sg.theme_button_color()
B =  sg.theme_background_color()


top = [
    [sg.Button('My Characters', key='Characters', pad=(0,0),button_color = (C[1],B),border_width=0),      
    sg.Button('My Campaigns', key='Campaigns', pad=(0,0),button_color = (C[0],B),border_width=0)]
]
#center the buttons
topColumn = sg.Column(top,justification="C")

CharacterList = [[sg.Text('')]]
CharacterColumn = sg.Column(CharacterList,size=(50,300))

layout = [
            [sg.Text('Gameplay',s=(50,1),justification="c")],
            [topColumn],
            [CharacterColumn],
            [sg.Button('Ok'), sg.Button('Cancel')] 
        ]


# Create the Window
window = sg.Window('D&D Helper', layout)

#keep track of current state
state = 0

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    if event == "Characters" and state != 0:
        state = 0
        window["Characters"].update(button_color = (C[1],B))
        window["Campaigns"].update(button_color = (C[0],B))
    if event == "Campaigns" and state != 1:
        state = 1
        window["Campaigns"].update(button_color = (C[1],B))
        window["Characters"].update(button_color = (C[0],B))


window.close()
