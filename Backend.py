import requests
import PySimpleGUI as sg
import DataHelper as dh
from requests.exceptions import ConnectionError
import os

simpleWeapons = ['Club','Dagger','Greatclub','Handaxe','Javelin','Light hammer','Mace','Quarterstaff','Sickle','Spear','Crossbow, light','Dart','Shortbow','Sling']
MeleeMartialWeapons = ['Battleaxe','Flail','Glaive','Greataxe','Greatsword','Halberd','Lance','Longsword','Maul','Morningstar','Pike','Rapier','Scimitar','Trident','War pick','Warhammer','Whip']
rangedMartialWeapon = ['Blowgun','Crossbow, hand','Crossbow, heavy','Longbow']
artisanTools = ["Alchemist's supplies","Brewer's supplies","Calligrapher's supplies","Carpenter's tools","Cartographer's tools","Cobbler's tools","Cook's utensils","Glassblower's tools","Jeweler's tools","Leatherworker's tools","Mason's tools","Painter's supplies","Potter's tools","Smith's tools","Tinker's tools","Weaver's tools","Woodcarver's tools"]
Asi = ['Strength','Dexterity','Constitution','Intellegence','Wisdom','Charisma']

class requester:
    def __init__(self) -> None:
        self.source = "http://dnd5e.wikidot.com"
        self.dh = dh.dataHelper()
        self.infoDict = {}
        self.allSubraces = []
        self.RacialBonus = [0,0,0,0,0,0]
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
                
            if i.find('</span></h2>') != -1 and i.find('Traits') == -1 and i.find('Racial Features') == -1: #new subrace
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
                while c < len(sInfo) and sInfo[c].find('Ability Score Increase') == -1 :
                    c += 1
                if c == len(sInfo):
                    #no asi
                    RaceInfo['Description'] = '\n'.join(sInfo[0:1])
                    RaceInfo['ASI'] = 'Ability Score Increase. One ability score of your choice increases by 2.'
                    RaceInfo['Features'] = '\n'.join(sInfo[3:len(sInfo)])
                else:
                    RaceInfo['Description'] = '\n'.join(sInfo[0:c])
                    RaceInfo['ASI'] = '\n'.join(sInfo[c:c+2]) 
                    RaceInfo['Features'] = '\n'.join(sInfo[c+2:len(sInfo)])
                self.dh.saveRace(RaceInfo)
                return self.getRaceFile(name)

    def swapWindow(self,window:sg.Window,newLayout:list) -> sg.Window:
        newWindow = sg.Window('D&DHub',newLayout)
        window.close()
        window = newWindow
        return window
    
    def getClassinformation(self,clas:str):
        web = requests.get(self.source+'/'+clas)
        with open('wididot.txt','w',encoding='utf-8') as w: w.write(web.text)
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

        layout = self.ClassParcer(rawInformation,clas)
        self.dh.saveClass({'Name':clas,'Info':info,'Layout':layout})
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
    
    def ClassParcer(self,text:list[str],clas:str)->list:
        layout = []
        TableList:list[list] = []
        row = []
        count = 0
        firstTable = True
        tableStart = False
        #generate the table
        while firstTable:
            line = text[count]
            if line == '<th>Level</th>':
                tableStart = True
            elif line == '</table>':
                tableStart = False
                firstTable = False
            if tableStart:
                if line[0:4] == '<th>' or line[0:4] == '<td>':
                    row.append(self.removeEffects(line))
                if line[0:5] == '</tr>':
                    TableList.append(row)
                    row = []
            count += 1
        #start on the layout
        TableList.pop(0)
        keywords:dict[str:int] = {}
        for i in TableList:
            i:list[str]
            features = i[2].split(', ')
            lv = int(i[0].replace('st','').replace('nd','').replace('rd','').replace('th',''))
            for a in features:
                if list(keywords.keys()).count(a) == 0: #manual add in for now
                    keywords[a] = lv

        processLayout = True
        currentLV = 0
        maxCount = len(text)
        buffer = [] #delayed apending
        #dont reset count
        while processLayout:
            if count < maxCount:
                line = text[count]
            else: processLayout = False
            line = line.replace('&amp;','&').replace('&quot;',"'")
            if line.find('Ability Score Improvement') != -1:
                count += 2 #skip
                line = text[count]
            if line.find('Class Features') != -1:
                layout.append("sg.Text(\"%s\",s=(45,1),pad=(0,4),font=('Helvetica',20))" % (clas))
                count += 3 #skip to hp
                line = text[count]
            if line[0:3] == '<h5': #sub catagories
                t = self.removeEffects(line)
                layout.append("sg.Text(\"%s\",s=(45,1),pad=(0,4),font=('Helvetica',15))" % (t))
            elif line[0:3] == '<p>' or line[0:8] == '<strong>':
                t = self.removeEffects(line)
                if len(t) < 130:
                    layout.append("sg.Text(\"%s\",pad=(0,0),font=('Helvetica',10))" % (t))
                else:
                    layout.append("sg.Multiline(\"%s\",s=(80,%s),pad=(0,0),font=('Helvetica',10),disabled=True,background_color='2c2825',no_scrollbar=True,border_width=0)" % (t,str(int(len(t)/95)+1)))
            elif line[0:4] == '<li>':#indent
                t = self.removeEffects(line)
                if len(t) < 130:
                    layout.append("sg.Text(\"%s\",pad=(0,0),font=('Helvetica',10))" % ('\t- '+t))
                else:
                    layout.append("sg.Multiline(\"%s\",s=(80,%s),pad=(60,0),font=('Helvetica',10),disabled=True,background_color='2c2825',no_scrollbar=True,border_width=0)" % ('- '+t,str(int(len(t)/95)+1)))
            
                if line.find('two simple weapons') != -1:
                    buffer.append("sg.DropDown(%s,s=(25,10),readonly=True,default_value='')" % (str(simpleWeapons)))
                    buffer.append("sg.DropDown(%s,s=(25,10),readonly=True,default_value='')" % (str(simpleWeapons)))
                elif line.find('(a) studded leather armor or (b) scale mail armor') != -1:
                    buffer.append("sg.DropDown(['Studded leather','Scale mail'],s=(25,10),readonly=True,default_value='Studded leather')")
            elif line[0:3] == '<h3': #catagories
                #check for diffrent lv
                t = self.removeEffects(line)
                l = self.firstKey(keywords,t)
                if l > currentLV:
                    currentLV = l
                    layout.append("sg.Text(\"%s\",s=(45,1),pad=(0,4),font=('Helvetica',15))" % ('Level '+str(l)))
                    layout.append("sg.Text(\"%s\",s=(45,1),pad=(0,4),font=('Helvetica',15))" % (t))
                elif l == currentLV:
                    layout.append("sg.Text(\"%s\",s=(45,1),pad=(0,4),font=('Helvetica',15))" % (t))
            elif line == '<table class="wiki-content-table">': #subclass label
                #new loop
                ua = False
                sub = True
                subclasses = []
                while sub:
                    line = text[count]
                    if line == '</table>':
                        sub = False
                    if line.find('Unearthed Arcana') != -1:
                        ua = True
                    elif line[0:6] == '<td><a':
                        t = self.removeEffects(line)
                        if ua:
                            subclasses.append(t+'-ua')
                        else:
                            subclasses.append(t)
                    count += 1
                layout.append("sg.DropDown(%s,s=(25,10),readonly=True,default_value='')" % (str(subclasses)))
            elif line == '</ul>':
                layout += buffer
                buffer = []
            if line.find('one type of artisan’s tools of your choice') != -1:
                layout.append("sg.DropDown(%s,s=(25,10),readonly=True,default_value='')" % (str(artisanTools)))
            if line.find('Choose two from') != -1:
                z = line.find('Choose two from')
                t = line[z+15:line.find('<',z+15)]
                ts = t.split(',')
                ts[len(ts)-1] = ts[len(ts)-1].replace('and ','')
                layout.append("sg.DropDown(%s,s=(25,10),readonly=True,default_value='')" % (str(ts)))
                layout.append("sg.DropDown(%s,s=(25,10),readonly=True,default_value='')" % (str(ts)))
            count += 1
        #fix layout for saving
        for L in layout:
            L:str
            L = L.replace('\n','/n').replace("'","***")
        return layout
    
    def firstKey(self,dic:dict,key) -> int:
        for i in dic.keys():
            if i.find(key) != -1:
                return dic[i]
        return -1

    def loadLayout(self,clas,level):
        d = self.dh.loadClass(clas)
        dout:list = d['Layout']
        layout = []
        c = 'class t:\n def __init__(self) -> None:\n  pass\n def rL(self):\n  return layout' #injected class wrapper
        code = 'import PySimpleGUI as sg\nlayout =[\n'+'\n,'.join(dout)+']\n\n'+c
        with open('temp.py','w',encoding='utf-8') as f: f.write(code) 
        import temp
        tcode = temp.t()
        l:list = tcode.rL() #this works
        #wipe temp.py 
        os.remove('temp.py')
        #correct some formating
        textcolor = ''
        for i in l:
            if type(i) == sg.Text:
                textcolor = i.TextColor
            if type(i) == sg.Multiline:
                i.DefaultText = i.DefaultText.replace('/n','\n').replace("***","'")
                i.BackgroundColor = '#2c2825'
            if type(i) == sg.DropDown:
                i.BackgroundColor = '#2c2825'
                i.button_background_color = '#2c2825'
                i.TextColor = textcolor
            
            layout.append([i])
        return layout
    
    def makeScoreColoum(self,ScoreType:str,keymod:str):
        L = [
            [sg.Text(ScoreType,s=(20,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10))],
            [sg.Text('Total Score',s=(15,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10)),sg.Text('8',key='ts'+keymod,s=(5,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10),justification='r')],
            [sg.Text('Modifier',s=(15,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10)),sg.Text('-1',key='mod'+keymod,s=(5,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10),justification='r')],
            [sg.Text('Base Score',s=(15,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10)),sg.Text('8',s=(5,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10),justification='r')],
            [sg.Text('Racial Bonus',s=(15,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10)),sg.Text('+0',key='rb'+keymod,s=(5,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10),justification='r')],
            [sg.Text('Ability Improvements',s=(15,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10)),sg.Text('+0',key='ai'+keymod,s=(5,1),pad=(0,0),font=(sg.DEFAULT_FONT[0],10),justification='r')],

        ]
        return sg.Column(L)
    
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
        
    def getRacialBonus(self,race:str) -> dict:
        Datapack = {'str':0,'dex':0,'con':0,'int':0,'wis':0,'cha':0,'custom':0}
        Race = self.dh.loadRace(race)
        Asi:str = Race['ASI']
        #Check for custom asi.
        if Asi.find('increase one score by 2 and increase a different score by 1, or increase three different scores by 1.') != -1:
            Datapack['custom'] = 3 
        elif Asi.find('Two different ability scores of your choice increase by 1') != -1:
            Datapack['custom'] = 2 
        if Asi.find('one other ability score of your choice increases by 1') != -1:
            Datapack['custom'] = 1
        aSplit = Asi.split(' and ')
        for a in aSplit:
           if a.find('Strength') != -1:
               Datapack['str'] = int(self.firstInt(a))
           if a.find('Constitution') != -1:
               Datapack['con'] = int(self.firstInt(a))
           if a.find('Dexterity') != -1:
               Datapack['dex'] = int(self.firstInt(a))
           if a.find('Intelligence') != -1:
               Datapack['int'] = int(self.firstInt(a))
           if a.find('Wisdom') != -1:
               Datapack['wis'] = int(self.firstInt(a))
           if a.find('Charisma') != -1:
               Datapack['cha'] = int(self.firstInt(a))
        print(Datapack)
        return Datapack
