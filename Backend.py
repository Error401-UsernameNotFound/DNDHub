import requests
import PySimpleGUI as sg
import DataHelper as dh
from requests.exceptions import ConnectionError
import os
import importlib

simpleWeapons = ['Club','Dagger','Greatclub','Handaxe','Javelin','Light hammer','Mace','Quarterstaff','Sickle','Spear','Crossbow, light','Dart','Shortbow','Sling']
MeleeMartialWeapons = ['Battleaxe','Flail','Glaive','Greataxe','Greatsword','Halberd','Lance','Longsword','Maul','Morningstar','Pike','Rapier','Scimitar','Trident','War pick','Warhammer','Whip']
rangedMartialWeapon = ['Blowgun','Crossbow, hand','Crossbow, heavy','Longbow']
artisanTools = ["Alchemist's supplies","Brewer's supplies","Calligrapher's supplies","Carpenter's tools","Cartographer's tools","Cobbler's tools","Cook's utensils","Glassblower's tools","Jeweler's tools","Leatherworker's tools","Mason's tools","Painter's supplies","Potter's tools","Smith's tools","Tinker's tools","Weaver's tools","Woodcarver's tools"]
Asi = ['Strength','Dexterity','Constitution','Intellegence','Wisdom','Charisma']

# colors
C = sg.theme_button_color()
B = sg.theme_background_color()

class requester:
    def __init__(self) -> None:
        self.source = "http://dnd5e.wikidot.com"
        self.dh = dh.dataHelper()
        self.infoDict = {}
        self.allSubraces = []
        self.RacialBonus = [0,0,0,0,0,0]

    def swapWindow(self,window:sg.Window,newLayout:list) -> sg.Window:
        newWindow = sg.Window('D&DHub',newLayout)
        window.close()
        window = newWindow
        return window
    
    def makeScoreColoum(self,ScoreType:str,keymod:str):
        L = [
            [sg.Text(ScoreType,s=(20,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10))],
            [sg.Text('Total Score',s=(15,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10)),sg.Text('8',key='ts'+keymod,s=(5,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10),justification='r')],
            [sg.Text('Modifier',s=(15,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10)),sg.Text('-1',key='mod'+keymod,s=(5,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10),justification='r')],
            [sg.Text('Base Score',s=(15,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10)),sg.Text('8',s=(5,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10),justification='r')],
            [sg.Text('Racial Bonus',s=(15,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10)),sg.Text('+0',key='rb'+keymod,s=(5,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10),justification='r')],
            [sg.Text('Ability Improvements',s=(15,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10)),sg.Text('+0',key='ai'+keymod,s=(5,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10),justification='r')],
            [sg.Text('Custom Bonus',s=(13,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10)),sg.DropDown([0,1,2],default_value=0,key='cus'+keymod,s=(6,3),pad=(0,0),font=(sg.DEFAULT_FONT[0],10),readonly=True,enable_events=True,)],

        ]
        return sg.Column(L,justification='c')
    
    def makeModifierColoum(self,ScoreType:str,keymod:str):
        L = [
            [sg.Button('↓',key='d'+keymod),sg.Text('-1',s=(7,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],20),key='mod'+keymod,justification='c'),sg.Button('↑',key='d'+keymod)],
            [sg.Text('8',s=(21,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10),key='TotalScore'+keymod,justification='c')],
        ]
        return sg.Frame(ScoreType,L,title_location='n',font=(sg.DEFAULT_FONT[0],15),element_justification='c')
    
    def calculateCost(self,Score):
        #distence from 8
        if Score <= 12:
            return Score-8
        if Score > 12:
            return 3+(Score-12)*2
    
    def StrAddition(slef,mod):
        if mod == 'str':
            return ''
        if mod == 'dex':
            return '0'
        if mod == 'con':
            return '1'
        if mod == 'int':
            return '2'
        if mod == 'wis':
            return '3'
        if mod == 'cha':
            return '4'

    def StrSubtractor (self,num:str):
        if num == 'cus':
            return 'str'
        if num == 'cus0':
            return 'dex'
        if num == 'cus1':
            return 'con'
        if num == 'cus2':
            return 'int'
        if num == 'cus3':
            return 'wis'
        if num == 'cus4':
            return 'cha'
    
    def findAllFileNames(self,state):
        if state == 0:
            target = 'Characters'
        elif state == 1:
            target = 'Champaigns'
        path = os.getcwd()+'\\'+target
        L = os.listdir(path)
        cleanList = []
        if len(L) > 0:
            for i in L:
                cleanList.append(i.split('.')[0])
        return cleanList
    
    def calculateAC(self,Armor,dexMod):
        dexMod = int(dexMod)
        if Armor == 'None':
            return 10 + dexMod
        if Armor == 'Mage Armor':
            return 13 + dexMod
        if Armor == 'Padded' or Armor == 'Leather':
            return 11 + dexMod
        if Armor == 'Studded Leather':
            return 12 + dexMod
        if Armor == 'Hide':
            return (12 + dexMod) if dexMod < 3 else 14 
        if Armor == 'Chain Shirt':
            return (13 + dexMod) if dexMod < 3 else 15 
        if Armor == 'Scale Mail' and Armor == 'Spiked Armor' and Armor == 'Breastplate':
            return (14 + dexMod) if dexMod < 3 else 16
        if Armor == 'Halfplate':
            return (15 + dexMod) if dexMod < 3 else 17  
        if Armor == 'Ring Mail':
            return 14
        if Armor == 'Chain Mail':
            return 16
        if Armor == 'Splint':
            return 17
        if Armor == 'Plate':
            return 18
        return 0
    def calculateProf(self,level):
        return int((level-1)/4)+2
    def calculateMod(self,stat):
        return int(int(stat)/2 - 5)
    def calculateTotalLevel(self,stat):
        return 1