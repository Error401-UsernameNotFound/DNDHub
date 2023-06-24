import json
class dataHelper:
    def __init__(self) -> None:
        pass
    
    def saveRace(self,data:dict):
        try: Rfile = open('Races/'+data['Name']+'.race','x',encoding='utf-8')
        except: Rfile = open('Races/'+data['Name']+'.race','w',encoding='utf-8')
        json.dump(data,Rfile,indent=4)
        Rfile.close()
        
    def loadRace(self,name:str) -> dict:
        Rfile = open('Races/'+name+'.race','r',encoding='utf-8')
        data = json.load(Rfile)
        Rfile.close()
        return data

    def saveClass(self,data:dict):
        try: Rfile = open('Classes/'+data['Name']+'.clas','x',encoding='utf-8')
        except: Rfile = open('Classes/'+data['Name']+'.clas','w',encoding='utf-8')
        json.dump(data,Rfile,indent=4)
        Rfile.close()

    def loadClass(self,clas):
        Rfile = open('Classes/'+clas+'.clas','r',encoding='utf-8')
        data = json.load(Rfile)
        Rfile.close()
        return data

    def loadOverideClass(self,clas):
        Rfile = open('Classes Overide/'+clas+'.clas','r',encoding='utf-8')
        Rtxt = Rfile.readlines()
        data = {}
        data['Name'] = Rtxt[0].removeprefix('Name: ').removesuffix('\n')
        lstart = 0
        c = 4
        for i in Rtxt[4:len(Rtxt)-1]:
            if i == 'Layout:\n': lstart = c
            c += 1

        data['Info'] = ''.join(Rtxt[3:lstart])
        data['Layout'] = Rtxt[lstart+1:len(Rtxt)]
        try:
            self.saveClass(data)
        except Exception as e:
            print(e)
        return data
    def saveSubclass(self,data:dict):
        pass
    def loadSubclass(self):
        pass