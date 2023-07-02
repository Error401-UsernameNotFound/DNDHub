import PySimpleGUI as sg
import Backend

rq = Backend.requester()

sg.theme('DarkAmber') #dark theme
# colors
C = sg.theme_button_color()
B = sg.theme_background_color()

classes = ['Artificer','Barbarian','Bard','Blood-Hunter','Cleric','Druid','Fighter','Monk','Paladin','Ranger','Rogue','Sorcerer','Warlock','Wizard']


class loadStepThree:
    def __init__(self) -> None:
        self.classesMenu = [
            [sg.Text('Choose a Class',s=(45,1),font=(sg.DEFAULT_FONT[0],20)),sg.DropDown(classes,enable_events=True,readonly=True,key='classes',s=(15,1),pad=(0,0),text_color=C[1],button_background_color=B,background_color=B),sg.Text('level',s=(8,1),pad=(0,0)),sg.DropDown(['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20',],'1',enable_events=True,readonly=True,key='level',s=(15,1),pad=(0,0),button_arrow_color=C[0])],
            [sg.Multiline('',no_scrollbar=True,s=(150,30),key='info')],
            [sg.Button("Back",key='Back',s=(65,1),button_color = (C[1],B),border_width=0),sg.Button("Submit",key="Submit Class",s=(65,1),button_color = (C[1],B),border_width=0)]
        ]
        self.window = sg.Window('D&DHub',self.classesMenu)
    def WindowActive(self,tempCharacter:dict):
        Forward = True
        ClassToLoad = []
        while True:
            event, values = self.window.read()
            #classes window
            if event == 'classes':
                self.window["info"].update(rq.checkForClassFile(values['classes']))
            if event == 'Submit Class':
                tempCharacter['level'] = int(values['level'])
                tempCharacter['class'] = values['classes']
                if values['classes'] != '':
                    classLayout = rq.loadLayout(values['classes'],values['level'])
                    classColumn = sg.Column(classLayout,scrollable=True,vertical_scroll_only=True,s=(700,600))
                    ClassToLoad = [[classColumn],[sg.Button("Back",key='Back',s=(20,1),button_color = (C[1],B),border_width=0),sg.Button("Submit",key="Confirm Class",s=(20,1),pad=(0,0),button_color = (C[1],B),border_width=0)]]
                    self.window = rq.swapWindow(self.window,ClassToLoad)

            #Custom Class wimdow
            if event == 'Confirm Class':
                values:dict
                tempCharacter['ClassInfo'] = values.copy()
                break
            if event == "Back":
                Forward = False
                break
        self.window.close()
        if Forward:
            return (5,tempCharacter)
        else: return (3,tempCharacter)