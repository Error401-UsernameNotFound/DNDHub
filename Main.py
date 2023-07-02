import PySimpleGUI as sg
import sys
import os
from requests.exceptions import ConnectionError
import Backend


#all of the characture creation screens
sys.path.insert(1, os.path.dirname(__file__)+'\Character Creation')
import CharacterColumn as cc
import Races as R
import ClassesMenu as CM
import PointBuyScreen as PBS


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


p = [8,9,10,11,12,13,14,15]
PointBuyScreen = [
    [sg.Text('Ability Scores',s=(60,1),pad=(0,4),font=(sg.DEFAULT_FONT[0],20))],
    [sg.Text('POINTS REMAINING',s=(90,1),pad=(0,4),font=('Helvetica',15),justification = 'c')],
    [sg.Text('27/27',s=(90,1),pad=(0,4),font=('Helvetica',15),key = 'points',justification = 'c')],
    [sg.Text('STRENGTH',s=(16,1),pad=(0,4),font=('Helvetica',15)),sg.Text('DEXTERITY',s=(16,1),pad=(0,4),font=('Helvetica',15)),sg.Text('CONSTITUTION',s=(16,1),pad=(0,4),font=('Helvetica',15)),sg.Text('INTELLIGENCE',s=(16,1),pad=(0,4),font=('Helvetica',15)),sg.Text('WISDOM',s=(16,1),pad=(0,4),font=('Helvetica',15)),sg.Text('CHARISMA',s=(16,1),pad=(0,4),font=('Helvetica',15))],
    [sg.DropDown(p,s=(21,10),readonly=True,default_value=8,pad=(7,0),enable_events=True,key='str'),sg.DropDown(p,s=(21,10),readonly=True,default_value=8,pad=(7,0),enable_events=True,key='dex'),sg.DropDown(p,s=(21,10),readonly=True,default_value=8,pad=(7,0),enable_events=True,key='con'),sg.DropDown(p,s=(21,10),readonly=True,default_value=8,pad=(7,0),enable_events=True,key='int'),sg.DropDown(p,s=(21,10),readonly=True,default_value=8,pad=(7,0),enable_events=True,key='wis'),sg.DropDown(p,s=(21,10),readonly=True,default_value=8,pad=(7,0),enable_events=True,key='cha')],
    [sg.Text('Score Calculations',s=(90,1),pad=(0,4),font=('Helvetica',15))],
    [rq.makeScoreColoum('Strength',''),rq.makeScoreColoum('Dexterity','0'),rq.makeScoreColoum('Constitution','1'),rq.makeScoreColoum('Intellegence','2'),rq.makeScoreColoum('Wisdom','3'),rq.makeScoreColoum('Charisma','4')],
    [sg.Button("Submit",key="Submit pointbuy",s=(20,1),button_color = (C[1],B),border_width=0)]
]


savingThrowCol = sg.Column([
    [sg.Frame('Saving Throws',[
        [sg.Text('+0',s=(3,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10),key='strSave'),sg.Text('Strength',s=(10,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10))],
        [sg.Text('+0',s=(3,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10),key='dexSave'),sg.Text('Dexterity',s=(10,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10))],
        [sg.Text('+0',s=(3,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10),key='conSave'),sg.Text('Constitution',s=(10,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10))],
        [sg.Text('+0',s=(3,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10),key='intSave'),sg.Text('Inteligence',s=(10,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10))],
        [sg.Text('+0',s=(3,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10),key='wisSave'),sg.Text('Wisdom',s=(10,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10))],
        [sg.Text('+0',s=(3,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10),key='chaSave'),sg.Text('Charisma',s=(10,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10))],
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
    ],title_location='n',pad=(15,0))]
    ])
skillsCol = sg.Column([
    [sg.Frame('Skills',[
        [sg.Text('+0',s=(3,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10),key='Acrobatics'),sg.Text('Acrobatics',s=(13,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10))],
        [sg.Text('+0',s=(3,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10),key='Animal Handling'),sg.Text('Animal Handling',s=(13,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10))],
        [sg.Text('+0',s=(3,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10),key='Arcana'),sg.Text('Arcana',s=(13,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10))],
        [sg.Text('+0',s=(3,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10),key='Athletics'),sg.Text('Athletics',s=(13,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10))],
        [sg.Text('+0',s=(3,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10),key='Deception'),sg.Text('Deception',s=(13,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10))],
        [sg.Text('+0',s=(3,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10),key='History'),sg.Text('History',s=(13,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10))],
        [sg.Text('+0',s=(3,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10),key='Insight'),sg.Text('Insight',s=(13,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10))],
        [sg.Text('+0',s=(3,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10),key='Intimidation'),sg.Text('Intimidation',s=(13,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10))],
        [sg.Text('+0',s=(3,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10),key='Investigation'),sg.Text('Investigation',s=(13,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10))],
        [sg.Text('+0',s=(3,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10),key='Medicine'),sg.Text('Medicine',s=(13,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10))],
        [sg.Text('+0',s=(3,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10),key='Nature'),sg.Text('Nature',s=(13,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10))],
        [sg.Text('+0',s=(3,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10),key='Performance'),sg.Text('Performance',s=(13,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10))],
        [sg.Text('+0',s=(3,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10),key='Persuasion'),sg.Text('Persuasion',s=(13,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10))],
        [sg.Text('+0',s=(3,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10),key='Religion'),sg.Text('Religion',s=(13,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10))],
        [sg.Text('+0',s=(3,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10),key='Sleight of Hand'),sg.Text('Sleight of Hand',s=(13,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10))],
        [sg.Text('+0',s=(3,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10),key='Stealth'),sg.Text('Stealth',s=(13,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10))],
        [sg.Text('+0',s=(3,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10),key='Survival'),sg.Text('Survival',s=(13,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10))]
    ],title_location='n')],
    ])
ActionBlock = sg.Column([
     [sg.Frame('Actions',[
        [sg.Multiline("=== ACTIONS ===\n\nStandard Actions\nAttack, Cast a Spell, Dash, Disengage, Dodge, Help, Hide, Ready, Search, Use an Object, Opportunity Attack, Grapple, Shove, Improvise, Two-Weapon Fighting, Interact with an Object\n\n=== BONUS ACTIONS ===",s=(40,10),key='Actions',pad=(10,0),font=('Helvetica',7),disabled=True,background_color='#2c2825',no_scrollbar=True,border_width=1), sg.Multiline("=== SPECIAL ===",s=(40,10),key='SPECIAL',pad=(10,0),font=('Helvetica',7),disabled=True,background_color='#2c2825',no_scrollbar=True,border_width=1)]
    ],title_location='nw',font=(sg.DEFAULT_FONT[0],15))],
    [sg.Frame('Weapon Attacks & Cantrips',[
        [sg.Table([['','','','']],['    Name    ','Hit','Damage/Type','    Notes    '],s=(None,8),key='AttackTable',pad=(0,None))]
    ],title_location='nw',font=(sg.DEFAULT_FONT[0],15))],
])
InictiveBlock = sg.Column([
    [sg.Frame('Hit Points',[
        [sg.Text('Max HP',s=(10,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10),justification='c'),sg.Text('Current HP',s=(15,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10),justification='c'),sg.Text('Temp HP',s=(10,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10),justification='c')],
        [sg.Text('100',s=(5,1),pad=(15,0),font=(sg.DEFAULT_FONT[0],15),justification='c',key='Max HP'),sg.Text('100',s=(9,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],15),justification='c',key='CurrentHP'),sg.Text('',s=(3,1)),sg.Text('100',s=(3,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],15),justification='c',key='TempHP')],
    ],title_location='s')],
    [sg.Frame('Initiative',[ 
        [sg.Text('+4',s=(10,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],15),justification='c',key='Initiative')]
    ],title_location='s',pad=(20,0)),sg.Frame('Armor Class',[
        [sg.Text('10',s=(10,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],15),justification='c',key='Armor Class')]
    ],title_location='s',pad=(13,0))],

    [sg.Frame('Defences',[
        [sg.Multiline("Resistences:\nImmunities:",s=(35,3),pad=(10,0),font=('Helvetica',10),disabled=True,background_color='#2c2825',no_scrollbar=True,border_width=0)]
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
ProfBlock = sg.Column([
        [sg.Frame('Proficiencies & Languages',[
            [sg.Text('=== Armor ===',s=(30,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10),justification='c')],
            [sg.Multiline("",s=(35,3),pad=(10,0),font=('Helvetica',10),disabled=True,key='Armor',background_color='#2c2825',no_scrollbar=True,border_width=0)],
            [sg.Text('=== Weapons ===',s=(30,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10),justification='c')],
            [sg.Multiline("",s=(35,3),pad=(10,0),font=('Helvetica',10),disabled=True,key='Weapons',background_color='#2c2825',no_scrollbar=True,border_width=0)],
            [sg.Text('=== Tools ===',s=(30,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10),justification='c')],
            [sg.Multiline("",s=(35,3),pad=(10,0),font=('Helvetica',10),disabled=True,key='Tools',background_color='#2c2825',no_scrollbar=True,border_width=0)],
            [sg.Text('=== Languages ===',s=(30,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10),justification='c')],
            [sg.Multiline("",s=(35,3),pad=(10,0),font=('Helvetica',10),disabled=True,key='Languages',background_color='#2c2825',no_scrollbar=True,border_width=0)]
        ],title_location='n')],
        [sg.Frame('Feats',[
            [sg.Multiline("",s=(35,10),font=('Helvetica',10),disabled=True,key='Feats',background_color='#2c2825',no_scrollbar=True,border_width=1)],
        ],title_location='n')],
        [sg.Text('',s=(10,1),pad=(0,7),font=(sg.DEFAULT_FONT[0],10))],
    ])
FeaturesBlock = sg.Column([
    [
        sg.Frame('Features and Traits',[
            [
                sg.Column([[sg.Text('=== Class Features ===',s=(45,1),pad=(10,0),font=(sg.DEFAULT_FONT[0],10),justification='c')],[sg.Multiline("",s=(50,30),pad=(10,0),font=('Helvetica',10),disabled=True,key='Class Features',background_color='#2c2825',no_scrollbar=True,border_width=1)]]),
                sg.Column([[sg.Text('=== Racial Features ===',s=(45,1),pad=(10,0),font=(sg.DEFAULT_FONT[0],10),justification='c')],[sg.Multiline("",s=(50,30),pad=(10,0),font=('Helvetica',10),disabled=True,key='Race Features',background_color='#2c2825',no_scrollbar=True,border_width=1)]])
            ],
        ],title_location='n')
    ],
])
EquipmentBlock = sg.Column([
    [sg.Frame('Equipment',[
        [
            sg.Column([[sg.Text('CP',s=(3,1),pad=(10,0),font=(sg.DEFAULT_FONT[0],10))],[sg.Text('SP',s=(3,1),pad=(10,0),font=(sg.DEFAULT_FONT[0],10))],[sg.Text('EP',s=(3,1),pad=(10,0),font=(sg.DEFAULT_FONT[0],10))],[sg.Text('GP',s=(3,1),pad=(10,0),font=(sg.DEFAULT_FONT[0],10))],[sg.Text('PP',s=(3,1),pad=(10,0),font=(sg.DEFAULT_FONT[0],10))]]),
            sg.Column([[]])
        ],
    ],title_location='n')],
])
CharacterSheet = [
    [sg.Text('Character Name',s=(35,1),pad=(0,4),font=(sg.DEFAULT_FONT[0],20)), sg.Text('Class and level',s=(20,1),pad=(0,4),font=(sg.DEFAULT_FONT[0],10)), sg.Text('Race',s=(30,1),pad=(0,4),font=(sg.DEFAULT_FONT[0],10)), sg.Text('Background',s=(15,1),pad=(0,4),font=(sg.DEFAULT_FONT[0],10))],
    [rq.makeModifierColoum('Strength',''),rq.makeModifierColoum('Dexterity','0'),rq.makeModifierColoum('Constitution','1'),rq.makeModifierColoum('Intellegence','2'),rq.makeModifierColoum('Wisdom','3'),rq.makeModifierColoum('Charisma','4')],
    [skillsCol,savingThrowCol,ActionBlock,InictiveBlock],
    [ProfBlock,FeaturesBlock],
]


#***************Debug***********
dWindow = sg.Window('Debug',[[sg.Column(CharacterSheet,s=(1120,600),scrollable=True,vertical_scroll_only=True)]])
#***************Debug***********

#Create the main window
mainWindow = sg.Window('D&DHub', startlayout)

#Variables 
state = 0
tempCharacter = {}

subraceList = []
currentRace = ''
event = ''
values = {}
while True:
    if state == 0 or state == 1:
        if mainWindow._Hidden:
            mainWindow.un_hide()
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
            state = 2
            mainWindow.hide()
    if state == 2:#General characture creator
        stepOne = cc.loadStepOne()
        state, tempCharacter = stepOne.WindowActive()
    if state == 3:#Race selection
        StepTwo = R.loadStepTwo()
        state, tempCharacter = StepTwo.WindowActive(tempCharacter)
    if state == 4:#class selection
        StepThree = CM.loadStepThree()
        state, tempCharacter = StepThree.WindowActive(tempCharacter)
    if state == 5:#pointBuy
        StepFour = PBS.loadStepFour(tempCharacter)
        state, tempCharacter = StepThree.WindowActive(tempCharacter)
        
            
    #Custom Class wimdow
    if event == 'Confirm Class':
        #go to asi screen 'Locathah'
        mainWindow = rq.swapWindow(mainWindow,PointBuyScreen)
        data = rq.getRacialBonus(currentRace)
        event, values = mainWindow.read(timeout=0)
        for i in data.keys():
            i:str
            if i != 'custom' and data[i] != 0:
                t = 'ts' + rq.StrAddition(i)
                m = 'mod' + rq.StrAddition(i)
                rb = 'rb' + rq.StrAddition(i)
                mainWindow[rb].update('+'+str(data[i]))
                mainWindow[t].update(8+data[i])
                mainWindow[m].update((int(8+data[i]/2)-5))
    
    #9 1p, 10 1p, 11 1p, 12 1p, 13 1p, 14 2p, 15 2p, 12 1p,
    #elements str (null), dex 0, con 1, int 2, wis 3, cha 4
    #Asi screen
    if event == 'str' or event == 'dex' or event == 'con' or event == 'int' or event == 'wis' or event == 'cha' or event[0:3] == 'cus':
        totalCost = 0
        mod = ''
        if event[0:3] == 'cus':
            mod = rq.StrSubtractor(event)
        else:
            mod = event
        for v in values.values():
            if v > 6:
                totalCost += rq.calculateCost(v)
        r = 27 - totalCost
        t = 'ts' + rq.StrAddition(mod)
        m = 'mod' + rq.StrAddition(mod)
        rb = 'rb' + rq.StrAddition(mod)
        cus = 'cus' + rq.StrAddition(mod)
        mainWindow[t].update(values[mod]+int(mainWindow[rb].DisplayText)+values[cus])
        mainWindow[t].update(values[mod]+int(mainWindow[rb].DisplayText)+values[cus])
        mainWindow[m].update((int((values[mod]+int(mainWindow[rb].DisplayText)+values[cus])/2)-5))
        mainWindow['points'].update(str(r)+'/27')
    
    if event == 'Submit pointbuy':
        if int(rq.firstInt(mainWindow['points'].DisplayText)) >= 0:
            valid = False
            total = 0
            for k in values.keys():
                if k[0:3] == 'cus':
                   total += values[k]
            if total <= data['custom']:
                print('move')
                tempCharacter['str'] = int(mainWindow['ts'].DisplayText)
                tempCharacter['dex'] = int(mainWindow['ts0'].DisplayText)
                tempCharacter['con'] = int(mainWindow['ts1'].DisplayText)
                tempCharacter['int'] = int(mainWindow['ts2'].DisplayText)
                tempCharacter['wis'] = int(mainWindow['ts3'].DisplayText)
                tempCharacter['cha'] = int(mainWindow['ts4'].DisplayText)
                pass #move to the next thing
            else:
                print('to many custom points')
        else:
            print('to many points used')

mainWindow.close()
