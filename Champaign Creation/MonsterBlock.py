import PySimpleGUI as sg
import DataHelper
import Backend

rq = Backend.requester()
dh = DataHelper.dataHelper()
sg.theme('DarkAmber') #dark theme
# colors
C = sg.theme_button_color()
B = sg.theme_background_color()

class Block:
    def __init__(self,MonsterData:dict) -> None:
        self.InternalData = MonsterData
        self.Name = MonsterData['Name']
        #sences
        ExtraModifiers = []
        if self.InternalData['SaveThrows'] != []:
            ExtraModifiers.append([sg.Text("Saving Throws: " + self.GetSave())])
        if self.InternalData['Skills'] != []:
            ExtraModifiers.append([sg.Text("Skills: " + self.GetSkills())])
        if self.InternalData['Skills'] != []:
            ExtraModifiers.append([sg.Text("Condition Immunities: " + self.GetCondition())])
        if self.InternalData['DamageRes'] != []:
            ExtraModifiers.append(self.GetDamageRes())

        Display = [
            [sg.Text(self.Name,font=(None,20))],
            [sg.Text(self.InternalData['Size']+' '+ self.InternalData['Type']+', '+self.InternalData['Alignment'])],
            [sg.Text("______________________________________________")],
            [self.SB('Str',self.InternalData['Stats'][0]),self.SB('Dex',self.InternalData['Stats'][1]),self.SB('Con',self.InternalData['Stats'][2]),self.SB('Int',self.InternalData['Stats'][3]),self.SB('Wis',self.InternalData['Stats'][4]),self.SB('Cha',self.InternalData['Stats'][5])],
            [sg.Text("______________________________________________")],
            ExtraModifiers,
            [sg.Text("Senses: " + self.Sence(),s=(40,None))], #sences
            [sg.Text("Languages: "+ self.GetLang())], #languages
            [sg.Text("Challange: "+self.InternalData['CR'])],
            [sg.Text("Proficency Bonus: "+str(rq.calculateProf(int(self.InternalData['CR']))))],
            [sg.Text("______________________________________________")],
            self.getFeatures(),
            [sg.Text("______________________________________________")],
            [sg.Text('Actions',font=(None,20))],
            self.getActions(),
            [sg.Text("______________________________________________")],
            [sg.Text('Bonus Actions',font=(None,20))],
            self.getBonusActions(),
            [sg.Text("______________________________________________")],
            [sg.Text('Reactions',font=(None,20))],
            self.getReactions(),
        ]
        self.w = sg.Window('D&DHub',Display)
    def WindowActive(self):
        e, v = self.w.read(timeout=0)
    
    def getFeatures(self):
        res = []
        for f in self.InternalData['Features']:
            res.append([sg.Text(f['name']+': '+ f['desc'],s=(40,None),)])
        return res
    def getActions(self):
        res = []
        for f in self.InternalData['Actions']:
            res.append([sg.Text(f['name']+': '+ f['desc'],s=(40,None),)])
        return res
    def getBonusActions(self):
        res = []
        for f in self.InternalData['BonusActions']:
            res.append([sg.Text(f['name']+': '+ f['desc'],s=(40,None),)])
        return res
    def getReactions(self):
        res = []
        for f in self.InternalData['Reactions']:
            res.append([sg.Text(f['name']+': '+ f['desc'],s=(40,None),)])
        return res
    def GetDamageRes(self):
        vuln = ''
        res = ''
        imm = ''
        for dam in self.InternalData['DamageRes']:
            if dam['type'] == 'v':
                vuln += dam['name'] + ', '
            elif dam['type'] == 'r':
                res += dam['name']+ ', '
            elif dam['type'] == 'i':
                imm += dam['name'] + ', '
        ret = []
        if vuln != '':
            ret.append([sg.Text('Damage Vulnerabilities: '+ vuln)])
        if res != '':
            ret.append([sg.Text('Damage Resistances: '+ res)])
        if imm != '':
            ret.append([sg.Text('Damage Immunities: '+ imm)])
        return ret

    def GetLang(self):
        ls = ''
        for L in self.InternalData['Languages']:
            ls += L['name']+', '
        return ls
    def GetSave(self):
        ls = ''
        for L in self.InternalData['SaveThrows']:
            ls += L['name']+', '
        return ls
    def GetCondition(self):
        ls = ''
        for L in self.InternalData['Conditions']:
            ls += L['name']+', '
        return ls
    def GetSkills(self):
        ls = ''
        for L in self.InternalData['Skills']:
            ls += L['name']+', '
        return ls
    def Sence(self):
        res = ''
        if self.InternalData['BlindSight'] != '0':
            res += 'BlindSight ' + self.InternalData['BlindSight'] +" ft., "
        if self.InternalData['Darkvision'] != '0':
            res += 'Darkvision ' + self.InternalData['Darkvision'] +" ft., "
        if self.InternalData['Tremorsense'] != '0':
            res += 'Tremorsense ' + self.InternalData['Tremorsense'] +" ft., "
        if self.InternalData['Truesight'] != '0':
            res += 'Truesight ' + self.InternalData['Truesight'] +" ft., "
        return res
        
        pass
    def SB(self,string,Score):
        mod = int(int(Score)/2 - 5)
        layout = [
            [sg.Text(string,justification='Center',s=(4,1))],
            [sg.Text(Score + ' (' + str(mod) + ')',justification='Center',s=(4,1))],
        ]
        return sg.Column(layout)