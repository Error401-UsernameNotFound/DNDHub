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

#univercal things
simpleWeapons = ['Club','Dagger','Greatclub','Handaxe','Javelin','Light hammer','Mace','Quarterstaff','Sickle','Spear']
artisanTools = ["Alchemist's supplies","Brewer's supplies","Calligrapher's supplies","Carpenter's tools","Cartographer's tools","Cobbler's tools","Cook's utensils","Glassblower's tools","Jeweler's tools","Leatherworker's tools","Mason's tools","Painter's supplies","Potter's tools","Smith's tools","Tinker's tools","Weaver's tools","Woodcarver's tools"]
ArtificerSpecialist = ['Alchemist','Armorer','Artillerist','Battle Smith','Forge Adept','Mastermaker','Maverick','Archivist-ua','Armorer-ua']
Asi = ['Strength','Dexterity','Constitution','intellegence','Wisdom','Charisma']
#hardcoded Classes
ArtificerLayout = [
    [sg.Text('Artificer',s=(45,1),pad=(0,4),font=(sg.DEFAULT_FONT[0],20))],
    [sg.Text('Hit Points',s=(45,1),pad=(0,4),font=(sg.DEFAULT_FONT[0],15))],
    [sg.Text('Hit Dice: 1d8 per Artificer level',pad=(0,0),font=(sg.DEFAULT_FONT[0],10))],
    [sg.Text('Hit Points at 1st Level: 8 + your Constitution modifier',pad=(0,0),font=(sg.DEFAULT_FONT[0],10))],
    [sg.Text('Hit Points at Higher Levels: 1d8 (or 5) + your Constitution modifier per Artificer level after 1st',pad=(0,0),font=(sg.DEFAULT_FONT[0],10))],
    [sg.Text('Proficiencies',s=(45,1),pad=(0,4),font=(sg.DEFAULT_FONT[0],15))],
    [sg.Text('Armor: Light armor, medium armor, shields',pad=(0,0),font=(sg.DEFAULT_FONT[0],10))],
    [sg.Text('Weapons: Simple weapons',pad=(0,0),font=(sg.DEFAULT_FONT[0],10))],
    [sg.Text('Tools: Thieves’ tools, tinker’s tools, one type of artisan’s tools of your choice',pad=(0,0),font=(sg.DEFAULT_FONT[0],10))],
    [sg.DropDown(artisanTools,s=(25,10),readonly=True,text_color=C[1],button_background_color=B,background_color=B,default_value=artisanTools[0])],
    [sg.Text('Saving Throws: Constitution, Intelligence',pad=(0,0),font=(sg.DEFAULT_FONT[0],10))],
    [sg.Text('Skills: Choose two from Arcana, History, Investigation, Medicine, Nature, Perception, Sleight of Hand',pad=(0,0),font=(sg.DEFAULT_FONT[0],10))],
    [sg.DropDown(['Arcana', 'History', 'Investigation', 'Medicine', 'Nature', 'Perception', 'Sleight of Hand'],s=(25,10),readonly=True,text_color=C[1],button_background_color=B,background_color=B,default_value='Arcana')],
    [sg.Text('Equipment',s=(45,1),pad=(0,4),font=(sg.DEFAULT_FONT[0],15))],
    [sg.Text('You start with the following equipment, in addition to the equipment granted by your background:',pad=(0,0),font=(sg.DEFAULT_FONT[0],10))],
    [sg.Text('\tany two simple weapons',pad=(0,0),font=(sg.DEFAULT_FONT[0],10))],
    [sg.Text('\ta light crossbow and 20 bolts',pad=(0,0),font=(sg.DEFAULT_FONT[0],10))],
    [sg.Text('\t(a) studded leather armor or (b) scale mail',pad=(0,0),font=(sg.DEFAULT_FONT[0],10))],
    [sg.Text('\tthieves’ tools and a dungeoneer’s pack',pad=(0,0),font=(sg.DEFAULT_FONT[0],10))],
    [sg.DropDown(simpleWeapons,s=(25,10),readonly=True,text_color=C[1],button_background_color=B,background_color=B,default_value=simpleWeapons[0])],
    [sg.DropDown(simpleWeapons,s=(25,10),readonly=True,text_color=C[1],button_background_color=B,background_color=B,default_value=simpleWeapons[0])],
    [sg.DropDown(['Studded leather','Scale mail'],s=(25,10),readonly=True,text_color=C[1],button_background_color=B,background_color=B,default_value='Studded leather')],
    #end of level 0,
    [sg.Text('Level 1',s=(45,1),pad=(0,4),font=(sg.DEFAULT_FONT[0],15))],
    [sg.Multiline("You've learned how to invest a spark of magic into mundane objects.To use this ability, you must have thieves' tools or artisan's tools in hand.You then touch a Tiny nonmagical object as an action and give it one of the following magical properties of your choice:",s=(70,5),pad=(0,0),font=(sg.DEFAULT_FONT[0],10),disabled=True,background_color='#2c2825',no_scrollbar=True,border_width=0)],
    [sg.Text('\t- The object sheds bright light in a 5-foot radius and dim light for an additional 5 feet.',pad=(0,0),font=(sg.DEFAULT_FONT[0],10))],
    [sg.Multiline("- Whenever tapped by a creature, the object emits a recorded message that can be heard up to 10 feet away. You utter the message when you bestow this property on the object, and the recording can be no more than 6 seconds long.",s=(70,3),pad=(60,0),font=(sg.DEFAULT_FONT[0],10),disabled=True,background_color='#2c2825',no_scrollbar=True,border_width=0)],
    [sg.Multiline("- The object continuously emits your choice of an odor or a nonverbal sound (wind, waves, chirping, or the like). The chosen phenomenon is perceivable up to 10 feet away.",s=(70,3),pad=(60,0),font=(sg.DEFAULT_FONT[0],10),disabled=True,background_color='#2c2825',no_scrollbar=True,border_width=0)],
    [sg.Multiline("- A static visual effect appears on one of the object's surfaces. This effect can be a picture, up to 25 words of text, lines and shapes, or a mixture of these elements, as you like.",s=(70,3),pad=(60,0),font=(sg.DEFAULT_FONT[0],10),disabled=True,background_color='#2c2825',no_scrollbar=True,border_width=0)],
    [sg.Text('The chosen property lasts indefinitely. As an action, you can touch the object and end the property early.\n',pad=(0,1),font=(sg.DEFAULT_FONT[0],10))],
    [sg.Multiline("You can bestow magic on multiple objects, touching one object each time you use this feature, though a single object can only bear one property at a time. The maximum number of objects you can affect with this feature at one time is equal to your Intelligence modifier (minimum of one object). If you try to exceed your maximum, the oldest property immediately ends, and then the new property applies.",s=(70,5),pad=(0,0),font=(sg.DEFAULT_FONT[0],10),disabled=True,background_color='#2c2825',no_scrollbar=True,border_width=0)],
    [sg.Text('Spellcasting',s=(45,1),pad=(0,4),font=(sg.DEFAULT_FONT[0],15))],
    [sg.Multiline("You've studied the workings of magic and how to cast spells, channeling the magic through objects. To observers, you don't appear to be casting spells in a conventional way; you appear to produce wonders from mundane items and outlandish inventions.",s=(70,3),pad=(0,0),font=(sg.DEFAULT_FONT[0],10),disabled=True,background_color='#2c2825',no_scrollbar=True,border_width=0)],
    [sg.Text('Tools Required',s=(45,1),pad=(0,4),font=(sg.DEFAULT_FONT[0],15))],
    [sg.Multiline("You produce your artificer spell effects through your tools. You must have a spellcasting focus - specifically thieves' tools or some kind of artisan's tool - in hand when you cast any spell with this Spellcasting feature (meaning the spell has an 'M' component when you cast it). You must be proficient with the tool to use it in this way. See the equipment chapter in the Player's Handbook for descriptions of these tools. After you gain the Infuse Item feature at 2nd level, you can also use any item bearing one of your infusions as a spellcasting focus.",s=(70,7),pad=(0,0),font=(sg.DEFAULT_FONT[0],10),disabled=True,background_color='#2c2825',no_scrollbar=True,border_width=0)],
    #end of level 1,
    [sg.Text('Level 2',s=(45,1),pad=(0,4),font=(sg.DEFAULT_FONT[0],15))],
    [sg.Text('Infuse Item',s=(45,1),pad=(0,4),font=(sg.DEFAULT_FONT[0],15))],
    [sg.Multiline("At 2nd level, you've gained the ability to imbue mundane items with certain magical infusions, turning those objects into magic items.",s=(70,2),pad=(0,0),font=(sg.DEFAULT_FONT[0],10),disabled=True,background_color='#2c2825',no_scrollbar=True,border_width=0)],
    [sg.Text('Infusions Known',s=(45,1),pad=(0,4),font=(sg.DEFAULT_FONT[0],14))],
    [sg.Multiline("When you gain this feature, pick four artificer infusions to learn. You learn additional infusions of your choice when you reach certain levels in this class, as shown in the Infusions Known column of the Artificer table.\nWhenever you gain a level in this class, you can replace one of the artificer infusions you learned with a new one.",s=(70,5),pad=(0,0),font=(sg.DEFAULT_FONT[0],10),disabled=True,background_color='#2c2825',no_scrollbar=True,border_width=0)],
    [sg.Text('Infusing an Item',s=(45,1),pad=(0,4),font=(sg.DEFAULT_FONT[0],14))],
    [sg.Multiline("Whenever you finish a long rest, you can touch a nonmagical object and imbue it with one of your artificer infusions, turning it into a magic item. An infusion works on only certain kinds of objects, as specified in the infusion's description. If the item requires attunement, you can attune yourself to it the instant you infuse the item. If you decide to attune to the item later, you must do so using the normal process for attunement (see the attunement rules in the Dungeon Master's Guide).\nYour infusion remains in an item indefinitely, but when you die, the infusion vanishes after a number of days equal to your Intelligence modifier (minimum of 1 day). The infusion also vanishes if you replace your knowledge of the infusion.\nYou can infuse more than one nonmagical object at the end of a long rest; the maximum number of objects appears in the Infused Items column of the Artificer table. You must touch each of the objects, and each of your infusions can be in only one object at a time. Moreover, no object can bear more than one of your infusions at a time. If you try to exceed your maximum number of infusions, the oldest infusion ends, and then the new infusion applies.\nIf an infusion ends on an item that contains other things, like a bag of holding, its contents harmlessly appear in and around its space.",s=(70,17),pad=(0,0),font=(sg.DEFAULT_FONT[0],10),disabled=True,background_color='#2c2825',no_scrollbar=True,border_width=0)],
    #end of level 2,
    [sg.Text('Level 3',s=(45,1),pad=(0,4),font=(sg.DEFAULT_FONT[0],15))],
    [sg.Text('Artificer Specialist',s=(45,1),pad=(0,4),font=(sg.DEFAULT_FONT[0],15))],
    [sg.Multiline("At 3rd level, you choose the type of specialist you are. Your choice grants you features at 5th level and again at 9th and 15th level.",s=(70,2),pad=(0,0),font=(sg.DEFAULT_FONT[0],10),disabled=True,background_color='#2c2825',no_scrollbar=True,border_width=0)],
    [sg.DropDown(ArtificerSpecialist,s=(25,10),readonly=True,text_color=C[1],button_background_color=B,background_color=B,default_value='')],
    [sg.Text('The Right Tool for the Job',s=(45,1),pad=(0,4),font=(sg.DEFAULT_FONT[0],15))],
    [sg.Multiline("At 3rd level, you've learned how to produce exactly the tool you need: with thieves' tools or artisan's tools in hand, you can magically create one set of artisan's tools in an unoccupied space within 5 feet of you. This creation requires 1 hour of uninterrupted work, which can coincide with a short or long rest. Though the product of magic, the tools are nonmagical, and they vanish when you use this feature again.",s=(70,5),pad=(0,0),font=(sg.DEFAULT_FONT[0],10),disabled=True,background_color='#2c2825',no_scrollbar=True,border_width=0)],
    #end of level 3,
    [sg.Text('Level 4',s=(45,1),pad=(0,4),font=(sg.DEFAULT_FONT[0],15))],
    [sg.Text('Ability Score Improvement',s=(45,1),pad=(0,4),font=(sg.DEFAULT_FONT[0],15))],
    [sg.DropDown(Asi,s=(25,10),readonly=True,text_color=C[1],button_background_color=B,background_color=B,default_value=Asi[0])],
    [sg.DropDown(Asi,s=(25,10),readonly=True,text_color=C[1],button_background_color=B,background_color=B,default_value=Asi[0])],

]
#***************Debug***********
dWindow = sg.Window('Debug',[[sg.Column(ArtificerLayout,scrollable=True,s=(700,500))]])


# Create the main window
mainWindow = sg.Window('D&DHub', startlayout)

#Variables 
state = 0
tempCharacter = {}

subraceList = []
currentRace = ''

while True:
    event, values = dWindow.read()
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
    
mainWindow.close()
