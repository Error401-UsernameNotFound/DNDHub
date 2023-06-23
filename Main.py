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

SkillProfs = ['Acrobatics','Animal Handling','Arcana','Deception','History','Insight','Intimidation','Investigation','Medicine','Nature','Perception','Performance','Persuasion','Religion','Sleight of Hand','Stealth','Survival']
Languages = ['Common','Dwarvish','Elvish','Giant','Gnomish','Goblin','Halfling','Orc','Abyssal','Celestial','Draconic','Deep Speech','Infernal','Primordial','Sylvan','Undercommon']

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
    [sg.DropDown(SkillProfs,s=(15,2),readonly=True,key="prof1",default_value="Acrobatics")],
    [sg.DropDown(SkillProfs,s=(15,2),readonly=True,key="prof2",default_value="Acrobatics")],
    [sg.Text('Pick two Lanuages',pad=(4,4),font=(sg.DEFAULT_FONT[0],15))],
    [sg.DropDown(Languages,s=(15,2),readonly=True,key="lang1",default_value="Common")],
    [sg.DropDown(Languages,s=(15,2),readonly=True,key="lang2",default_value="Common")],
    [sg.Button("Submit",key="Submit Preferences",s=(60,1),button_color = (C[1],B),border_width=0)]
]


classes = ['Artificer','Barbarian','Bard','Blood-Hunter','Cleric','Druid','Fighter','Monk','Paladin','Ranger','Rogue','Sorcerer','Warlock','Wizard']
classesMenu = [
    [sg.Text('Choose a Class',s=(45,1),font=(sg.DEFAULT_FONT[0],20)),sg.DropDown(classes,enable_events=True,readonly=True,key='classes',s=(15,1),pad=(0,0),text_color=C[1],button_background_color=B,background_color=B),sg.Text('level',s=(8,1),pad=(0,0)),sg.DropDown(['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20',],'1',enable_events=True,readonly=True,key='level',s=(15,1),pad=(0,0),button_arrow_color=C[0])],
    [sg.Multiline('',no_scrollbar=True,s=(150,30),key='info')],
    [sg.Button("Submit",key="Submit Class",s=(130,1),button_color = (C[1],B),border_width=0)]
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





#***************Debug***********
#dWindow = sg.Window('Debug',[[sg.Column(PointBuyScreen,s=(1080,400))]])
#***************Debug***********

#Create the main window
mainWindow = sg.Window('D&DHub', startlayout)

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
        if values["info"].find('Increase one ability score by 2, and increase a different one by 1, or increase three different scores by 1.') != -1:
            tempCharacter['CustomAsi'] = True
        else:
            tempCharacter['CustomAsi'] = False
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
            classColumn = sg.Column(classLayout,scrollable=True,s=(700,600))
            t = [[classColumn],[sg.Button("Submit",key="Confirm Class",s=(19,1),pad=(0,0),button_color = (C[1],B),border_width=0)]]
            mainWindow = rq.swapWindow(mainWindow,t)
            
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
