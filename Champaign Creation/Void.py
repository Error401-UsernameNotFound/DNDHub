#semi endless grid of tiles that you can move ig
import PySimpleGUI as sg
import DataHelper

dh = DataHelper.dataHelper()
sg.theme('DarkAmber') #dark theme
# colors
C = sg.theme_button_color()
B = sg.theme_background_color()

class Void():
    def __init__(self) -> None:
        display = [
            [sg.Graph(
                canvas_size=(600, 600),
                graph_bottom_left=(0, 0),
                graph_top_right=(600, 600),
                key="Map",
                enable_events=True,
                background_color= C[0],
                
            )],
           [sg.Text('Graph size:'),sg.Text('(600,600)',key='GSize'), sg.Text('|  # of rows'),sg.Text('10',key='NumbX'), sg.Text('|  # of coloums'),sg.Text('10',key='NumbY')],
           [sg.Input(s=(17,None),key='Size',pad=(10,None)),sg.Text('  '),sg.Input(s=(10,None),key='Rows'),sg.Text('   '),sg.Input(s=(10,None),key='coloums')],
           [sg.Button("Back",key='Back',s=(10,1),button_color = (C[1],B),border_width=0),sg.Button("Submit Changes",key='Submit',s=(15,1),button_color = (C[1],B),border_width=0)],
        ]
        self.window = sg.Window('D&DHub',display,finalize=True)
    def WindowActive(self):
        while True:
            event, values = self.window.read()
            if event == "Submit":
                pass
            if event == "Back" or event == sg.WIN_CLOSED:
                break

