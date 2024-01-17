#semi endless grid of tiles that you can move ig
import PySimpleGUI as sg
import DataHelper

dh = DataHelper.dataHelper()
sg.theme('DarkAmber') #dark theme
# colors
C = sg.theme_button_color()
B = sg.theme_background_color()

class Void():
    def __init__(self,CampaignData:dict) -> None:
        self.NumbRows = 10
        self.NumbCols = 10
        self.gridBackground = C[0]
        self.Linecolor = 'white'
        display = [
            [sg.Graph(
                canvas_size=(600, 600),
                graph_bottom_left=(0, 0),
                graph_top_right=(600, 600),
                key="Map",
                enable_events=True,
                background_color= C[0],
                
            )],
           [sg.Text('Graph size:'),sg.Text('600,600',key='GSize'), sg.Text('|  # of rows'),sg.Text('10',key='NumbX'), sg.Text('|  # of coloums'),sg.Text('10',key='NumbY'),sg.Text('| Background Color (hex)'),sg.Text('| Line Color')],
           [sg.Input(s=(17,None),key='Size',pad=(10,None),do_not_clear=False),sg.Text('  '),sg.Input(s=(10,None),key='Rows',do_not_clear=False),sg.Text('   '),sg.Input(s=(10,None),key='Coloums',do_not_clear=False),sg.Text('   '),sg.Input(s=(10,None),key='Bgcolor',do_not_clear=False),sg.Text('   '),sg.Input(s=(10,None),key='Linecolor',do_not_clear=False)],
           [sg.Button("Back",key='Back',s=(10,1),button_color = (C[1],B),border_width=0),sg.Button("Submit Changes",key='Submit',s=(15,1),button_color = (C[1],B),border_width=0)],
        ]
        self.window = sg.Window('D&DHub',display,grab_anywhere=True,finalize=True)
        self.lines = self.CalculateGrid()
    def WindowActive(self):
        while True:
            event, values = self.window.read()
            if event == "Submit":
                try: 
                    t = (int(values['Size'].split(',')[0]),int(values['Size'].split(',')[1])) if values['Size'] != '' else self.window['Map'].TopRight
                    r = int(values['Rows']) if values['Rows'] != '' else self.NumbRows
                    c = int(values['Coloums']) if values['Coloums'] != '' else self.NumbCols
                    bg = values['Bgcolor'] if values['Bgcolor'] != '' else self.gridBackground
                    lc = values['Linecolor'] if values['Linecolor'] != '' else self.Linecolor
                except:
                    sg.popup(['Invalid format'])
                    continue
                #reframe
                self.window['Map'].set_size(t)
                self.window['Map'].change_coordinates((0,0),t)
                self.window['Map'].BackgroundColor = bg
                self.Linecolor = lc
                self.gridBackground = bg
                self.NumbRows = r
                self.NumbCols = c
                #update the text
                self.window['GSize'].Update(str(t[0])+','+str(t[1]))
                self.window['NumbX'].Update(str(r))
                self.window['NumbY'].Update(str(c))
                #recalculate the grid
                self.lines = self.CalculateGrid()
            if event == "Back" or event == sg.WIN_CLOSED:
                break
    def CalculateGrid(self):
        numberofRowLines = self.NumbRows+1
        numberofColoumLines = self.NumbCols+1
        Grid = self.window['Map']
        Grid:sg.Graph
        Grid.erase()
        MaxX,MaxY = Grid.TopRight
        MaxX:int 
        MaxY:int
        for drawRowLineNumb in range(0,numberofRowLines):
            p1 = (0,(drawRowLineNumb/self.NumbRows)*MaxY)
            p2 = (MaxX,(drawRowLineNumb/self.NumbRows)*MaxY)
            Grid.DrawLine(p1,p2,self.Linecolor,2)#left to right
        for drawColLineNumb in range(0,numberofColoumLines):
            p1 = ((drawColLineNumb/self.NumbCols)*MaxX,0)
            p2 = ((drawColLineNumb/self.NumbCols)*MaxX,MaxY)
            Grid.DrawLine(p1,p2,self.Linecolor,2)#down to up
        

