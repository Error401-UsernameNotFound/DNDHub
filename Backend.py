import requests
import PySimpleGUI as sg
import DataHelper as dh
from requests.exceptions import ConnectionError
import os

C = sg.theme_button_color()
B =  sg.theme_background_color()

class requester:
    def __init__(self) -> None:
        self.source = "http://dnd5e.wikidot.com"
        self.dh = dh.dataHelper()
        self.infoDict = {}
        self.allSubraces = []
    def getRaces(self) -> list:
        races = []
        rawRaces = []
        try:
            txt = requests.get(self.source+'/lineage').text.split('\n')
            #isolate the race coloum
            areaOfIntrest = False
            for i in txt:
                if i == '            <!-- wikidot_top_728x90 -->':
                    areaOfIntrest = True
                if i == '            <!-- wikidot_bottom_300x250 -->':
                    areaOfIntrest = False
                if areaOfIntrest:
                    rawRaces.append(i)
            
            #isolate exact race
            for i in rawRaces:
                i:str
                if i.find('/lineage:') != -1:
                    a = i.find(':') + 1
                    R = i[a:i.find('"',a)]
                    races.append(R.capitalize())
            races.sort()
            return races
        except ConnectionError as e:
            #no wifi
            rawRaces = os.listdir(os.path.curdir+'/Races')
            MainRaces = []
            for i in rawRaces:
                if i.find('- ') == -1:
                    MainRaces.append(i.removesuffix('.race'))
            return MainRaces
    
    def getSavedRaceInformation(self,race:str):
        rawRaces = os.listdir(os.path.curdir+'/Races')
        MainRaces = [race]
        for i in rawRaces:
            if i.find(race) != -1 and i != race+'.race':
                MainRaces.append(i.removesuffix('.race'))
        return MainRaces

    def getRaceInformation(self,race:str):
        web = requests.get(self.source+'/lineage:'+race)
        #with open('wididot.txt','w',encoding='utf-8') as w: w.write(web.text)
        text = web.text.split('\n')
        areaOfIntrest = False
        rawInformation = []
        self.infoDict:dict[str:str] = {}
        currentSubrace = race.capitalize()
        self.infoDict[currentSubrace] = ''
        self.allSubraces = [race.capitalize()]
        for i in text:
            if i == '        <div class="main-content">':
                areaOfIntrest = True
            if i == '            <!-- wikidot_bottom_300x250 -->':
                areaOfIntrest = False
            if areaOfIntrest:
                rawInformation.append(i)
        
        for i in rawInformation:
            i:str
            if i.find('&quot;'):
                i = ''.join(i.split('&quot;'))

            if i.find('<h1 id=') != -1: #new subrace maybe
                a  = i.find('<span>')+6
                sufix = i[a:i.find('</span>')]
                if i.find('<h1 id="toc0">') == -1:
                    #not the first one lol
                    currentSubrace += '- ' + sufix
                    currentSubrace = currentSubrace.replace(':','') #avoiding errors :(
                    currentSubrace = currentSubrace.replace('/',' or ')
                    self.allSubraces.append(currentSubrace)
                    self.infoDict[currentSubrace] = ''
                
            if i.find('</span></h2>') != -1: #new subrace
                a = i.find('<span>')+6
                sub = i[a:i.find('</span>')]
                if sub.find(race,0,len(race)) == -1: sub = race + '- ' + sub
                if self.allSubraces.count(sub) == 1: sub += '-ua'
                sub = sub.replace('/',' or ')
                self.allSubraces.append(sub)
                currentSubrace = sub
                self.infoDict[currentSubrace] = ''

            #table logic from the other thing
            if i[0:4] == '</tr':
                t1 = '\n--------------------------------------------------------------------------------------------------------------\n'
                self.infoDict[currentSubrace] += t1
            elif i == '</table>' or i== '<table class="wiki-content-table">':
                t1 = '\n\n'
                self.infoDict[currentSubrace] += t1
            elif i[0:4] == '<th>':#title
                t1 = self.removeEffects(i[4:i.find('</')]) + '\t\t'
                self.infoDict[currentSubrace] += t1
            elif i[0:12] =='<th colspan=': #new table.. kinda
                t1 = '\n\n\n'+ self.removeEffects(i)+'\n'
                self.infoDict[currentSubrace] += t1
            elif i[0:4] == '<td>': #element
                t1 = self.removeEffects(i[4:i.find('</')]) + '\t\t'
                self.infoDict[currentSubrace] += t1
            if i.find('i="toc') != -1:
                t1 = '\n\n\n'+self.removeEffects(i[i.find('<span>')+6:i.find('</span>')]) + '\n\n\n'
                self.infoDict[currentSubrace] += t1
            #clean stuff?
            if i.find('/p') != -1: #clean line marker
                t1 = i[i.find('<strong>')+8:i.find('</strong>')-1]
                t1 = self.removeEffects(t1)
                self.infoDict[currentSubrace] += t1
            elif i.find('<strong>') != -1 or i[0:4] =='<li>': #bullet point
                t1 = self.removeEffects(i)
                self.infoDict[currentSubrace] += t1 +'\n'
            elif i == '<ul>':
                self.infoDict[currentSubrace] += '\n'


        #check for blank subraces
        for i in self.allSubraces.copy():
            if len(self.infoDict[i]) < 10:
                self.allSubraces.remove(i)
        return self.allSubraces
    
    def getRaceFile(self,name:str) -> str:
        #check pre build races. this is only 1 subrace
        info = ''
        RaceInfo = {}
        try: #file made 
            RaceInfo = self.dh.loadRace(name)
            info += ''.join(RaceInfo['Description']) + '\n\nFeatures:\n'
            info += RaceInfo['ASI'] + ''.join(RaceInfo['Features'])
            return info
        except: #make file :)
            if self.allSubraces != []:
                #has something
                RaceInfo['Name'] = name
                sInfo:list[str] = self.infoDict[name].split('\n')
                #everything to the asi is dict
                c = 0
                while c < len(sInfo) and sInfo[c] != 'Ability Score Increase:' :
                    c += 1
                if c == len(sInfo): c = 1 #no asi?
                RaceInfo['Description'] = '\n'.join(sInfo[0:c])
                RaceInfo['ASI'] = '\n'.join(sInfo[c:c+2])
                RaceInfo['Features'] = '\n'.join(sInfo[c+2:len(sInfo)])
                self.dh.saveRace(RaceInfo)
                return self.getRaceFile(name)

    def swapWindow(self,window:sg.Window,newLayout) -> sg.Window:
        newWindow = sg.Window('D&D Helper',newLayout)
        window.close()
        window = newWindow
        return window
    
    def getClassinformation(self,clas:str):
        web = requests.get(self.source+'/'+clas)
        text = web.text.split('\n')
        areaOfIntrest = False
        rawInformation = []
        sectionDict = {}
        section = 'Description'
        sectionDict[section] = ''
        info = ''
        for i in text:
            if i == '            <!-- wikidot_top_728x90 -->':
                areaOfIntrest = True
            if i == '            <!-- wikidot_bottom_300x250 -->':
                areaOfIntrest = False
            if areaOfIntrest:
                rawInformation.append(i)
        
        for i in rawInformation:
            #table things :)
            i:str
            if i.find('&amp;'):
                i = i.replace('&amp;','&')
            if i[0:4] == '</tr':
                info += '\n----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n'
            if i == '</table>' or i== '<table class="wiki-content-table">':
                info += '\n\n'
            if i[0:4] == '<th>':#elements
                info += self.removeEffects(i[4:i.find('</')]) + '\t'
            if i[0:12] =='<th colspan=': #new table.. kinda
                info += '\n\n\n'+ self.removeEffects(i)+'\n'
            if i[0:4] == '<td>': #title
                info += self.removeEffects(i[4:i.find('</')]) + ' \t'
            if i.find('i="toc') != -1:
                info += '\n\n\n'+self.removeEffects(i[i.find('<span>')+6:i.find('</span>')]) + '\n\n\n'
            if i.find('<p>') != -1:
                info += self.removeEffects(i[3:len(i)]) + '\n\n'
            elif i[0:8] =='<strong>' or i[0:4] =='<li>':
                info += self.removeEffects(i) + '\n'
            self.dh.saveClass({'Name':clas,'Info':info})
        return info

    
        
    def checkForClassFile(self,clas:str) -> str:
        try:
            t = self.dh.loadClass(clas)
            return t["Info"]
        except:
            return self.getClassinformation(clas)



    def removeEffects(self,dirtytext:str) ->str:
        c = 0
        a = 0
        cleantext = dirtytext
        for i in dirtytext:
            if i == '<':
                a = dirtytext.find('>',c)
                if a == -1: a = len(dirtytext)-1
                r = dirtytext[c:a+1]
                if r.find('sup') != -1:
                    r = dirtytext[c:dirtytext.find('<',a)]

                if a != len(dirtytext) - 1:
                    cleantext = ''.join(cleantext.split(r))
                else:
                    cleantext = cleantext.removesuffix(r)
            c += 1
        cleantext = cleantext.removeprefix("&nbsp;")
        return cleantext

    def firstInt(self,string:str) -> str:
        s = ''
        for i in string:
            if i.isnumeric():
                s += i
            elif s != '':
                return s
        return s