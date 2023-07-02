import PySimpleGUI as sg
import Backend

rq = Backend.requester()

sg.theme('DarkAmber') #dark theme
# colors
C = sg.theme_button_color()
B = sg.theme_background_color()

p = [8,9,10,11,12,13,14,15]

class loadStepFour:
    def __init__(self,tempCharacter:dict) -> None:
        self.PointBuyScreen = [
            [sg.Text('Ability Scores',s=(60,1),pad=(0,4),font=(sg.DEFAULT_FONT[0],20))],
            [sg.Text('POINTS REMAINING',s=(90,1),pad=(0,4),font=('Helvetica',15),justification = 'c')],
            [sg.Text('27/27',s=(90,1),pad=(0,4),font=('Helvetica',15),key = 'points',justification = 'c')],
            [sg.Text('STRENGTH',s=(16,1),pad=(0,4),font=('Helvetica',15)),sg.Text('DEXTERITY',s=(16,1),pad=(0,4),font=('Helvetica',15)),sg.Text('CONSTITUTION',s=(16,1),pad=(0,4),font=('Helvetica',15)),sg.Text('INTELLIGENCE',s=(16,1),pad=(0,4),font=('Helvetica',15)),sg.Text('WISDOM',s=(16,1),pad=(0,4),font=('Helvetica',15)),sg.Text('CHARISMA',s=(16,1),pad=(0,4),font=('Helvetica',15))],
            [sg.DropDown(p,s=(21,10),readonly=True,default_value=8,pad=(7,0),enable_events=True,key='str'),sg.DropDown(p,s=(21,10),readonly=True,default_value=8,pad=(7,0),enable_events=True,key='dex'),sg.DropDown(p,s=(21,10),readonly=True,default_value=8,pad=(7,0),enable_events=True,key='con'),sg.DropDown(p,s=(21,10),readonly=True,default_value=8,pad=(7,0),enable_events=True,key='int'),sg.DropDown(p,s=(21,10),readonly=True,default_value=8,pad=(7,0),enable_events=True,key='wis'),sg.DropDown(p,s=(21,10),readonly=True,default_value=8,pad=(7,0),enable_events=True,key='cha')],
            [sg.Text('Score Calculations',s=(90,1),pad=(0,4),font=('Helvetica',15))],
            [rq.makeScoreColoum('Strength',''),rq.makeScoreColoum('Dexterity','0'),rq.makeScoreColoum('Constitution','1'),rq.makeScoreColoum('Intellegence','2'),rq.makeScoreColoum('Wisdom','3'),rq.makeScoreColoum('Charisma','4')],
            [sg.Button("Back",key='Back',s=(10,1),button_color = (C[1],B),border_width=0),sg.Button("Submit",key="Submit pointbuy",s=(10,1),button_color = (C[1],B),border_width=0)]
        ]
        self.window = sg.Window('D&DHub',self.PointBuyScreen)
        self.data = rq.getRacialBonus(tempCharacter['race'])
        event, values = self.window.read(timeout=0)
        for i in self.data.keys():
            i:str
            if i != 'custom' and self.data[i] != 0:
                t = 'ts' + rq.StrAddition(i)
                m = 'mod' + rq.StrAddition(i)
                rb = 'rb' + rq.StrAddition(i)
                self.window[rb].update('+'+str(self.data[i]))
                self.window[t].update(8+self.data[i])
                self.window[m].update((int(8+self.data[i]/2)-5))
    def WindowActive(self,tempCharacter:dict):
        Forward = True
        while True:
            event, values = self.window.read()
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
                self.window[t].update(values[mod]+int(self.window[rb].DisplayText)+values[cus])
                self.window[t].update(values[mod]+int(self.window[rb].DisplayText)+values[cus])
                self.window[m].update((int((values[mod]+int(self.window[rb].DisplayText)+values[cus])/2)-5))
                self.window['points'].update(str(r)+'/27')
            
            if event == 'Submit pointbuy':
                if int(rq.firstInt(self.window['points'].DisplayText)) >= 0:
                    valid = False
                    total = 0
                    for k in values.keys():
                        if k[0:3] == 'cus':
                            total += values[k]
                    if total <= self.data['custom']:
                        print('move')
                        tempCharacter['str'] = int(self.window['ts'].DisplayText)
                        tempCharacter['dex'] = int(self.window['ts0'].DisplayText)
                        tempCharacter['con'] = int(self.window['ts1'].DisplayText)
                        tempCharacter['int'] = int(self.window['ts2'].DisplayText)
                        tempCharacter['wis'] = int(self.window['ts3'].DisplayText)
                        tempCharacter['cha'] = int(self.window['ts4'].DisplayText)
                        pass #move to the next thing
                    else:
                        print('to many custom points')
                else:
                    print('to many points used')
            if event == "Back":
                Forward = False
                break
        self.window.close()
        if Forward:
            return (6,tempCharacter)
        else: return (4,tempCharacter)