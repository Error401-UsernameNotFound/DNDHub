import requests
import PySimpleGUI as sg

class requester:
    def __init__(self) -> None:
        self.source = "http://dnd5e.wikidot.com"
        self.mainPage = requests.get(self.source)
        pass
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
        infoDict:dict[str:str] = {}
        currentSubrace = race.capitalize()
        infoDict[currentSubrace] = ''
        allSubraces = [race.capitalize()]
        for i in text:
            if i == '        <div class="main-content">':
                areaOfIntrest = True
            if i == '            <!-- wikidot_bottom_300x250 -->':
                areaOfIntrest = False
            if areaOfIntrest:
                rawInformation.append(i)
        
        for i in rawInformation:
            i:str
            if i.find('</span></h2>') != -1:
                a = i.find('<span>')+6
                sub = i[a:i.find('</span>')]
                allSubraces.append(sub)
                currentSubrace = sub
                infoDict[currentSubrace] = ''

            if i.find('<strong>') != -1: #bullet point
                t1 = i[i.find('<strong>')+8:i.find('</strong>')-1]
                t2 = i[i.find('</strong>')+10:i.find('</li>')]

                t1 = self.removeEffects(t1)
                t2 = self.removeEffects(t2)
                infoDict[currentSubrace] += t1 + ':\n' + t2 + '\n\n\n'
            
                
        return infoDict, allSubraces

    def swapWindow(self,window:sg.Window,newLayout) -> sg.Window:
        newWindow = sg.Window('D&D Helper',newLayout)
        window.close()
        window = newWindow
        return window
    
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
