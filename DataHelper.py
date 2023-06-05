
class dataHelper:
    def __init__(self) -> None:
        pass
    
    def saveRace(self,data:dict):
        try: Rfile = open('Races/'+data['Name']+'.race','x',encoding='utf-8')
        except: Rfile = open('Races/'+data['Name']+'.race','w',encoding='utf-8')
        t:list[str] = [
            'Name: ' + data['Name'],
            'ASI: ' + data['ASI'],
            'Description:\n' + data['Description'], #could be multiple lines
            'Features:\n' + data['Features'] #could be multiple lines
        ]
        Rfile.writelines('\n'.join(t))
        Rfile.close()
        
    def loadRace(self,name:str) -> dict:
        Rfile = open('Races/'+name+'.race','r',encoding='utf-8')
        Rtxt = Rfile.readlines()
        data = {}
        data['Name'] = Rtxt[0].removeprefix('Name: ')
        data['ASI'] = Rtxt[1].removeprefix('ASI: ') + Rtxt[2]
        Fstart = 0
        c = 4
        for i in Rtxt[4:len(Rtxt)-1]:
            if i == 'Features:\n': Fstart = c
            c += 1

        data['Description'] = Rtxt[4:Fstart]
        data['Features'] = Rtxt[Fstart+1:len(Rtxt)-1]
        return data

    def saveClass(self,data:dict):
        try: Rfile = open('Races/'+data['Name']+'.race','x',encoding='utf-8')
        except: Rfile = open('Races/'+data['Name']+'.race','w',encoding='utf-8')
        t:list[str] = [
            'Name: ' + data['Name'],
            'Info: ' + data['Info'], #could be multiple lines
            'Layout:\n' + data['Layout'] #could be multiple lines
        ]
        Rfile.writelines('\n'.join(t))
        Rfile.close()
        pass
    def loadClass(self):
        pass

    def saveSubclass(self,data:dict):
        pass
    def loadSubclass(self):
        pass