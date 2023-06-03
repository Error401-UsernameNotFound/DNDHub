import requests
import PySimpleGUI as sg
import DataHelper as dh

class requester:
    def __init__(self) -> None:
        self.source = "http://dnd5e.wikidot.com"
        self.mainPage = requests.get(self.source)
        self.dh = dh.dataHelper()
        self.infoDict = {}
        self.allSubraces = []
    def getRaces(self) -> list:
        txt = self.mainPage.text.split('\n')
        #isolate the race coloum
        rawRaces = []
        races = []
        areaOfIntrest = False
        for i in txt:
            if i == '<p><span style="font-size:140%;"><a href="/lineage">All Lineages</a></span></p>':
                areaOfIntrest = True
            if i == '<h3 id="toc2"><span>Common Backgrounds</span></h3>':
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
    def getRaceInformation(self,race:str):
        web = requests.get(self.source+'/lineage:'+race)
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
            
            if i.find('/p') != -1: #clean line marker
                t1 = i[i.find('<strong>')+8:i.find('</strong>')-1]
                t1 = self.removeEffects(t1)
                self.infoDict[currentSubrace] += t1 + '\n'

            elif i.find('<strong>') != -1: #bullet point
                t1 = i[i.find('<strong>')+8:i.find('</strong>')-1]
                t2 = i[i.find('</strong>')+10:i.find('</li>')]

                t1 = self.removeEffects(t1)
                t2 = self.removeEffects(t2)
                self.infoDict[currentSubrace] += t1 + ':\n' + t2 + '\n\n'
        
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
    
    def getClassinformation(self,clas): #inProgress
        web = requests.get(self.source+'/lineage:'+clas)
        text = web.text.split('\n')


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
        return cleantext
