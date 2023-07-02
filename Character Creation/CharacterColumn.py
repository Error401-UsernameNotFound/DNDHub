import PySimpleGUI as sg
import Backend

rq = Backend.requester()

sg.theme('DarkAmber') #dark theme
# colors
C = sg.theme_button_color()
B = sg.theme_background_color()

SkillProfs = ['Acrobatics','Animal Handling','Arcana','Deception','History','Insight','Intimidation','Investigation','Medicine','Nature','Perception','Performance','Persuasion','Religion','Sleight of Hand','Stealth','Survival']
Languages = ['Common','Dwarvish','Elvish','Giant','Gnomish','Goblin','Halfling','Orc','Abyssal','Celestial','Draconic','Deep Speech','Infernal','Primordial','Sylvan','Undercommon']



class loadStepOne:
    def __init__(self) -> None:
        #layout
        creationMenu = [
            [sg.Text('Name'), sg.Input(default_text="Character",key="Name")],
            [sg.Text('Character Preferences',s=(30,1),font=(sg.DEFAULT_FONT[0],20))],
            [sg.Checkbox("Custom Homebrew",key="CH",pad=(0,0))],
            [sg.Text('Optional Features',pad=(4,4),font=(sg.DEFAULT_FONT[0],15))],
            [sg.Checkbox("Optional Class Features",key="OF")],
            [sg.Checkbox("Customize Your Origin",key="CO")],
            [sg.Text('Hit Point Type',pad=(4,4),font=(sg.DEFAULT_FONT[0],15))],
            [sg.DropDown(["Fixed","Manual"],s=(15,2),readonly=True,key="HPT",default_value="Fixed")],
            [sg.Text('Use Prerequisites',pad=(4,4),font=(sg.DEFAULT_FONT[0],15))],
            [sg.Checkbox("Feats",key="FP")],
            [sg.Checkbox("Multiclass Requirements",key="MR")],
            [sg.Text('Show Level-Scaled Spells',pad=(4,4),font=(sg.DEFAULT_FONT[0],15))],
            [sg.Checkbox("Display and highlight available spells to cast with higher level spell slots",key="HLSS")],
            [sg.Text('Ability Score/Modifier Display',pad=(4,4),font=(sg.DEFAULT_FONT[0],15))],
            [sg.DropDown(["Modifiers Top","Scores Top"],s=(15,2),readonly=True,key="ASD",default_value="Modifiers Top")],
            [sg.Text('Pick two Skill Proficiencies',pad=(4,4),font=(sg.DEFAULT_FONT[0],15))],
            [sg.DropDown(SkillProfs,s=(15,12),readonly=True,key="prof1",default_value="Acrobatics")],
            [sg.DropDown(SkillProfs,s=(15,12),readonly=True,key="prof2",default_value="Acrobatics")],
            [sg.Text('Pick two Lanuages',pad=(4,4),font=(sg.DEFAULT_FONT[0],15))],
            [sg.DropDown(Languages,s=(15,12),readonly=True,key="lang1",default_value="Common")],
            [sg.DropDown(Languages,s=(15,12),readonly=True,key="lang2",default_value="Common")],
            [sg.Button("Back",key='Back',s=(30,1),button_color = (C[1],B),border_width=0),sg.Button("Submit",key="Submit Preferences",s=(30,1),button_color = (C[1],B),border_width=0)]
        ]
        self.window = sg.Window('D&DHub',creationMenu)
    def WindowActive(self):
        forward = True
        tempCharacter = {}
        while True:
            event, values = self.window.read()
            if event == "Submit Preferences":
                #remember everything
                values:dict
                tempCharacter = values.copy()
                break
            if event == 'Back':
                forward = False
                break
        self.window.close()
        if forward:
            return (3,tempCharacter)
        else:
            return (0, {})
        