import PySimpleGUI as sg
import DataHelper
import Backend

dh = DataHelper.dataHelper()
rq = Backend.requester()
sg.theme('DarkAmber') #dark theme
# colors
C = sg.theme_button_color()
B = sg.theme_background_color()

import MonsterBlock as mb

class Monster:
    def __init__(self,MonData:dict) -> None:
        self.InternalData = MonData
        self.Name = MonData['Name']
    def disp(self):
        ac = 0
        if self.InternalData['Armor'] == "natural armor":
            ac = 10 + self.InternalData['NatArmor'] + rq.calculateMod(self.InternalData['Stats'][1])
        else:
            ac = rq.calculateAC(self.InternalData['Armor'].title(),self.InternalData['Stats'][1])

        return [self.InternalData['Name'],self.InternalData['CR'],self.InternalData['Type'],self.InternalData['Size'],str(ac),self.InternalData['HP'],self.InternalData['Speed'],self.InternalData['Alignment'],]

class MonsterManger:
    def __init__(self,CampaignData:dict) -> None:
        self.CampaignData = CampaignData
        self.Display = self.CalculateDisplay()
        Screen = [
            [sg.Column([[sg.Text('Monster List',justification='center',s=(60,1))]],justification='center')],
            [sg.Table(self.Display,['  Creature Name  ', '  CR  ', '    Type    ', '  Size  ', ' AC ', ' Hp ', 'Speed', '    Alignment    '],vertical_scroll_only=True,k='Table',alternating_row_color=None,size=(None,30),select_mode=sg.TABLE_SELECT_MODE_BROWSE)],
            [sg.Button("Back",key='Back',s=(10,1),button_color = (C[1],B),border_width=0),sg.Button("Import .Monster File",key='Import',s=(20,1),button_color = (C[1],B),enable_events=True,border_width=0),sg.Button("Open Slected Monster",key='Open',s=(20,1),button_color = (C[1],B),enable_events=True,border_width=0),sg.Button("Remove Slected Monster",key='Remove',s=(20,1),button_color = (C[1],B),enable_events=True,border_width=0)],
        ]
        self.window = sg.Window('D&DHub',Screen)
    
    def CalculateDisplay(self):
        Raw = self.CampaignData.get('Monsters')
        self.Display = []
        if Raw != None:
            for mon in Raw:
                m = Monster(Raw[mon])
                self.Display.append(m.disp())
        else:
            self.CampaignData['Monsters'] = {}
        return self.Display
    
    def WindowActive(self):
        while True:
            event, values = self.window.read() #file_types= (("Monster Files",".monster"),)
            if event == "Import":
                fileLocation = sg.popup_get_file("Import Monster",file_types=(("Monster Files",".monster"),),)
                MonsterData =  dh.loadMonster(fileLocation)
                FormatedData = {
                    'Name': MonsterData['name'],                #disp
                    'CR': MonsterData['cr'],                    #disp
                    'Type': MonsterData['type'],                #disp
                    'Size': MonsterData['size'],                #disp
                    'Armor': MonsterData['armorName'],          #disp as ac
                    'Shield': MonsterData['shieldBonus'],       #disp as ac
                    'NatArmor': MonsterData['natArmorBonus'],   #disp as ac
                    'HP': MonsterData['hpText'].split(' ')[0],  #disp
                    'Speed': MonsterData['speed'],              #disp
                    'Alignment':MonsterData['alignment'],       #disp
                    #stats
                    'Stats': [MonsterData['strPoints'],MonsterData['dexPoints'],MonsterData['conPoints'],MonsterData['intPoints'],MonsterData['wisPoints'],MonsterData['chaPoints']],
                    #senses
                    'BlindSight': MonsterData['blindsight'],
                    'Darkvision': MonsterData['darkvision'],
                    'Tremorsense': MonsterData['tremorsense'],
                    'Truesight': MonsterData['truesight'],
                    'Telepathy': MonsterData['telepathy'],
                    'BurrowSpeed': MonsterData['burrowSpeed'],
                    'ClimbSpeed': MonsterData['climbSpeed'],
                    'FlySpeed': MonsterData['flySpeed'],
                    #proficiencies / resistences
                    'SaveThrows': MonsterData['sthrows'],
                    'Skills': MonsterData['skills'],
                    'DamageRes': MonsterData['damagetypes'],
                    'Conditions': MonsterData['conditions'],
                    'Languages': MonsterData['languages'],
                    #Features
                    'Features': MonsterData['abilities'],
                    'Actions': MonsterData['actions'],
                    'BonusActions': MonsterData['bonusActions'],
                    'Reactions': MonsterData['reactions'],
                }
                self.CampaignData['Monsters'][FormatedData['Name']] = FormatedData
                dh.saveChampaign(self.CampaignData)
                self.window['Table'].update(self.CalculateDisplay())
            if event == "Remove" and values['Table'] != []:
                self.CampaignData['Monsters'].pop(self.Display[values['Table'][0]][0])
                dh.saveChampaign(self.CampaignData)
                self.window['Table'].update(self.CalculateDisplay())
            if event == "Back" or event == sg.WIN_CLOSED:
                break
            if event == 'Open' and values['Table'] != []:
                block = mb.Block(self.CampaignData['Monsters'][self.Display[values['Table'][0]][0]])
                block.WindowActive()
                
        self.window.close()
        return 1