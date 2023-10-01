import PySimpleGUI as sg
import Backend

rq = Backend.requester()

sg.theme('DarkAmber') #dark theme
# colors
C = sg.theme_button_color()
B = sg.theme_background_color()

class loadStepFive:
    def __init__(self) -> None:
        self.savingThrowCol = sg.Column([
            [sg.Frame('Saving Throws',[
                [sg.Text('prof',s=(3,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10))],
                [sg.Checkbox('',change_submits=True,key='strProf'),sg.Text('+0',s=(3,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10),key='strSave'),sg.Text('Strength',s=(10,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10))],
                [sg.Checkbox('',change_submits=True,key='dexProf'),sg.Text('+0',s=(3,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10),key='dexSave'),sg.Text('Dexterity',s=(10,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10))],
                [sg.Checkbox('',change_submits=True,key='conProf'),sg.Text('+0',s=(3,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10),key='conSave'),sg.Text('Constitution',s=(10,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10))],
                [sg.Checkbox('',change_submits=True,key='intProf'),sg.Text('+0',s=(3,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10),key='intSave'),sg.Text('Inteligence',s=(10,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10))],
                [sg.Checkbox('',change_submits=True,key='wisProf'),sg.Text('+0',s=(3,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10),key='wisSave'),sg.Text('Wisdom',s=(10,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10))],
                [sg.Checkbox('',change_submits=True,key='chaProf'),sg.Text('+0',s=(3,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10),key='chaSave'),sg.Text('Charisma',s=(10,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10))],
                [sg.Text('',s=(3,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10))],
                [sg.Text('',s=(3,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10))],
                [sg.Text('',s=(3,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10))],
                [sg.Text('',s=(3,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10))],
                [sg.Text('',s=(3,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10))],
                [sg.Text('',s=(3,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10))],
                [sg.Text('',s=(3,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10))],
                [sg.Text('',s=(3,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10))],
                [sg.Text('',s=(3,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10))],
                [sg.Text('',s=(3,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10))],
                [sg.Text('',s=(3,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10))],
            ],title_location='n',pad=(0,0))]
            ])
        self.skillsCol = sg.Column([
            [sg.Frame('Skills',[
                [sg.Checkbox('',change_submits=True,key='acroProf'),sg.Text('+0',s=(3,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10),key='Acrobatics'),sg.Text('Acrobatics',s=(13,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10))],
                [sg.Checkbox('',change_submits=True,key='animlProf'),sg.Text('+0',s=(3,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10),key='Animal Handling'),sg.Text('Animal Handling',s=(13,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10))],
                [sg.Checkbox('',change_submits=True,key='arcanProf'),sg.Text('+0',s=(3,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10),key='Arcana'),sg.Text('Arcana',s=(13,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10))],
                [sg.Checkbox('',change_submits=True,key='athleProf'),sg.Text('+0',s=(3,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10),key='Athletics'),sg.Text('Athletics',s=(13,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10))],
                [sg.Checkbox('',change_submits=True,key='decepProf'),sg.Text('+0',s=(3,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10),key='Deception'),sg.Text('Deception',s=(13,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10))],
                [sg.Checkbox('',change_submits=True,key='histoProf'),sg.Text('+0',s=(3,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10),key='History'),sg.Text('History',s=(13,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10))],
                [sg.Checkbox('',change_submits=True,key='insigProf'),sg.Text('+0',s=(3,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10),key='Insight'),sg.Text('Insight',s=(13,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10))],
                [sg.Checkbox('',change_submits=True,key='intimProf'),sg.Text('+0',s=(3,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10),key='Intimidation'),sg.Text('Intimidation',s=(13,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10))],
                [sg.Checkbox('',change_submits=True,key='invesProf'),sg.Text('+0',s=(3,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10),key='Investigation'),sg.Text('Investigation',s=(13,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10))],
                [sg.Checkbox('',change_submits=True,key='medicProf'),sg.Text('+0',s=(3,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10),key='Medicine'),sg.Text('Medicine',s=(13,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10))],
                [sg.Checkbox('',change_submits=True,key='naturProf'),sg.Text('+0',s=(3,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10),key='Nature'),sg.Text('Nature',s=(13,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10))],
                [sg.Checkbox('',change_submits=True,key='perfoProf'),sg.Text('+0',s=(3,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10),key='Performance'),sg.Text('Performance',s=(13,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10))],
                [sg.Checkbox('',change_submits=True,key='persuProf'),sg.Text('+0',s=(3,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10),key='Persuasion'),sg.Text('Persuasion',s=(13,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10))],
                [sg.Checkbox('',change_submits=True,key='religProf'),sg.Text('+0',s=(3,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10),key='Religion'),sg.Text('Religion',s=(13,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10))],
                [sg.Checkbox('',change_submits=True,key='slightProf'),sg.Text('+0',s=(3,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10),key='Sleight of Hand'),sg.Text('Sleight of Hand',s=(13,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10))],
                [sg.Checkbox('',change_submits=True,key='stealProf'),sg.Text('+0',s=(3,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10),key='Stealth'),sg.Text('Stealth',s=(13,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10))],
                [sg.Checkbox('',change_submits=True,key='surviProf'),sg.Text('+0',s=(3,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10),key='Survival'),sg.Text('Survival',s=(13,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10))]
            ],title_location='n',pad=(0,None))],
            ])
        self.ActionBlock = sg.Column([
            [sg.Frame('Actions',[
                [sg.Multiline("=== ACTIONS ===\n\nStandard Actions\nAttack, Cast a Spell, Dash, Disengage, Dodge, Help, Hide, Ready, Search, Use an Object, Opportunity Attack, Grapple, Shove, Improvise, Two-Weapon Fighting, Interact with an Object\n",s=(40,10),key='Actions',pad=(10,0),font=('Helvetica',7),disabled=False,background_color='#2c2825',no_scrollbar=True,border_width=1), sg.Multiline("=== BONUS ===",s=(40,10),key='BONUS',pad=(10,0),font=('Helvetica',7),disabled=False,background_color='#2c2825',no_scrollbar=True,border_width=1)]
            ],title_location='nw',font=(sg.DEFAULT_FONT[0],15))],
            [sg.Frame('Weapon Attacks & Cantrips',[
                [sg.Table([['','','','']],['    Name    ','Hit','Damage/Type','    Notes    '],s=(None,8),key='AttackTable',pad=(0,None))]
            ],title_location='nw',font=(sg.DEFAULT_FONT[0],15))],
        ])
        self.InictiveBlock = sg.Column([
            [sg.Frame('Hit Points',[
                [sg.Text('Max HP',s=(10,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10),justification='c'),sg.Text('Current HP',s=(15,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10),justification='c'),sg.Text('Temp HP',s=(10,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10),justification='c')],
                [sg.Text('100',s=(5,1),pad=(15,0),font=(sg.DEFAULT_FONT[0],15),justification='c',key='Max HP'),sg.Multiline('100',s=(9,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],15),justification='c',key='CurrentHP',disabled=False,background_color='#2c2825',no_scrollbar=True,border_width=0),sg.Text('',s=(3,1)),sg.Text('100',s=(3,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],15),justification='c',key='TempHP')],
            ],title_location='s')],
            [sg.Frame('Initiative',[ 
                [sg.Text('+4',s=(10,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],15),justification='c',key='Initiative')]
            ],title_location='s',pad=(20,0)),sg.Frame('Armor Class',[
                [sg.Text('10',s=(10,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],15),justification='c',key='Armor Class')]
            ],title_location='s',pad=(13,0))],

            [sg.Frame('Defences',[
                [sg.Multiline("Resistences:\nImmunities:",s=(35,3),pad=(10,0),font=('Helvetica',10),disabled=False,background_color='#2c2825',no_scrollbar=True,border_width=0)]
            ],title_location='s',element_justification='c',pad=(20,None))],

            [sg.Frame('Proficiency Bonus',[
                [sg.Text('+2',s=(3,1),pad=(15,0),font=(sg.DEFAULT_FONT[0],10),justification='c')]
            ],title_location='s',element_justification='c',pad=(25,None)),sg.Frame('Walking Speed',[
                [sg.Text('30',s=(10,1),pad=(15,0),font=(sg.DEFAULT_FONT[0],10),justification='c')]
            ],title_location='s',element_justification='c',pad=(0,None))],

            [sg.Frame('Senses',[
                [sg.Text('10',s=(5,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10),justification='c'),sg.Text('Passive Wisdom (Percception)',s=(25,1),font=(sg.DEFAULT_FONT[0],10))],
                [sg.Text('10',s=(5,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10),justification='c'),sg.Text('Passive Wisdom (Insight)',s=(25,1),font=(sg.DEFAULT_FONT[0],10))],
                [sg.Text('10',s=(5,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10),justification='c'),sg.Text('Passive Intellegence (Investigation)',s=(25,1),font=(sg.DEFAULT_FONT[0],10))],
            ],title_location='s',pad=(25,None))],
            [sg.Text('',s=(10,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10))],

        ])
        self.ProfBlock = sg.Column([
                [sg.Frame('Proficiencies & Languages',[
                    [sg.Text('=== Armor ===',s=(30,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10),justification='c')],
                    [sg.Multiline("",s=(30,3),pad=(10,0),font=('Helvetica',10),disabled=False,key='Armor',background_color='#2c2825',no_scrollbar=True,border_width=0)],
                    [sg.Text('=== Weapons ===',s=(30,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10),justification='c')],
                    [sg.Multiline("",s=(30,3),pad=(10,0),font=('Helvetica',10),disabled=False,key='Weapons',background_color='#2c2825',no_scrollbar=True,border_width=0)],
                    [sg.Text('=== Tools ===',s=(30,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10),justification='c')],
                    [sg.Multiline("",s=(30,3),pad=(10,0),font=('Helvetica',10),disabled=False,key='Tools',background_color='#2c2825',no_scrollbar=True,border_width=0)],
                    [sg.Text('=== Languages ===',s=(30,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10),justification='c')],
                    [sg.Multiline("",s=(30,3),pad=(10,0),font=('Helvetica',10),disabled=False,key='Languages',background_color='#2c2825',no_scrollbar=True,border_width=0)]
                ],title_location='n')],
                [sg.Frame('Feats',[
                    [sg.Multiline("",s=(32,10),pad = (10,0),font=('Helvetica',10),disabled=False,key='Feats',background_color='#2c2825',no_scrollbar=True,border_width=0)],
                ],title_location='n')],
                [sg.Text('',s=(10,1),pad=(0,7),font=(sg.DEFAULT_FONT[0],10))],
            ])
        self.FeaturesBlock = sg.Column([
            [
                sg.Frame('Features and Traits',[
                    [
                        sg.Column([[sg.Text('=== Class Features ===',s=(45,1),pad=(10,0),font=(sg.DEFAULT_FONT[0],10),justification='c')],[sg.Multiline("",s=(50,30),pad=(10,0),font=('Helvetica',10),disabled=False,key='Class Features',background_color='#2c2825',no_scrollbar=True,border_width=1)]]),
                        sg.Column([[sg.Text('=== Racial Features ===',s=(45,1),pad=(10,0),font=(sg.DEFAULT_FONT[0],10),justification='c')],[sg.Multiline("",s=(50,30),pad=(10,0),font=('Helvetica',10),disabled=False,key='Race Features',background_color='#2c2825',no_scrollbar=True,border_width=1)]])
                    ],
                ],title_location='n')
            ],
        ])
        self.EquipmentBlock = sg.Column([
            [sg.Frame('Equipment',[
                [
                    sg.Column([[sg.Text('CP',s=(3,1),pad=(10,0),font=(sg.DEFAULT_FONT[0],10))],[sg.Text('SP',s=(3,1),pad=(10,0),font=(sg.DEFAULT_FONT[0],10))],[sg.Text('EP',s=(3,1),pad=(10,0),font=(sg.DEFAULT_FONT[0],10))],[sg.Text('GP',s=(3,1),pad=(10,0),font=(sg.DEFAULT_FONT[0],10))],[sg.Text('PP',s=(3,1),pad=(10,0),font=(sg.DEFAULT_FONT[0],10))]]),
                    sg.Column([[]])
                ],
            ],title_location='n')],
        ])
        CharacterSheet = [
            [sg.Text('Character Name',s=(35,1),pad=(0,4),font=(sg.DEFAULT_FONT[0],20)), sg.Text('Class and level',click_submits=True,key='Classes',s=(20,1),pad=(0,4),font=(sg.DEFAULT_FONT[0],10)), sg.Text('Race',s=(30,1),pad=(0,4),font=(sg.DEFAULT_FONT[0],10)), sg.Text('Background',s=(15,1),pad=(0,4),font=(sg.DEFAULT_FONT[0],10))],
            [rq.makeModifierColoum('Strength',''),rq.makeModifierColoum('Dexterity','0'),rq.makeModifierColoum('Constitution','1'),rq.makeModifierColoum('Intellegence','2'),rq.makeModifierColoum('Wisdom','3'),rq.makeModifierColoum('Charisma','4')],
            [self.skillsCol,self.savingThrowCol,self.ActionBlock,self.InictiveBlock],
            [self.ProfBlock,self.FeaturesBlock],
            [sg.Button("Exit and Save",key='Exit',s=(10,1),button_color = (C[1],B),border_width=0)]
        ]
        self.tempCharacter = {}
        self.window = sg.Window('D&DHub',[[sg.Column(
            CharacterSheet,vertical_scroll_only=True,scrollable=True,s=(None,1000)
        )]],grab_anywhere=True)
    def WindowActive(self,tempCharacter:dict):
        self.tempCharacter = tempCharacter
        while True:
            event, values = self.window.read()
            if event == "Exit":
                break
        self.window.close()
    
    def recalculateDisplay(self,Values):
        TotalLv = rq.calculateTotalLevel('Temperary argument')
        HitDice:list[tuple(int,int)] = [(8,6)] #lv8 d6 *****************Temperary*************
        HpTotal = 0
        for hd in HitDice:
            HpTotal += hd[1] + (1-hd[0])*(hd[1]/2+1)
        stats = self.tempCharacter['Stats'] #S,D,Con,I,W,Cha
        if self.tempCharacter['ASD'] =="Modifiers Top":
            #Strength
            strScore:sg.Text = self.window["TotalScore"]
            strMod = rq.calculateMod(stats[0])
            strModText:sg.Text = self.window["mod"]
            strScore.update(str(stats[0]))
            strModText.update(str(strMod))
            self.window["strSave"].update(str(strMod + int(Values)))


        pass

    


