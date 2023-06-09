import PySimpleGUI as sg
import subprocess
import argparse
from autoclicker import AutoClicker
#WINDOW CREATION 
sg.theme('DarkAmber')
#sg.Window(title="AUTO CLICKER", layout=[[]], margins=(250,350)).read()

# Parse command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('--click_type', type=str, default='left', help='Specify the click type')
parser.add_argument('--click_interval', type=float, default=0.1, help='Specify the click interval (in seconds)')
parser.add_argument('--key', type=str, default="r", help='Specify the key')
parser.add_argument('--time_speed', type=float, default=1, help='Specify the time speed')
args = parser.parse_args()

layout = [
    [sg.Text('Auto Clicker', font=('Helvetica', 25), justification='center')],
    [sg.HorizontalSeparator()],
    [sg.Text('Click Type', font=('Helvetica', 14)), 
     sg.Radio('Left', 'click_type', default=True, key='click_left'), 
     sg.Radio('Right', 'click_type', key='click_right')],
    [sg.Text('Click Interval (Seconds)', font=('Helvetica', 14)), 
     sg.Input(default_text=0.1, key='click_interval', size=(10, 1))],
    [sg.Text('Key', font=('Helvetica', 14)),
     sg.Input(default_text='R', key='Key', size=(10, 1))], 
    [sg.Text('Time Speed', font=('Helvetica', 14)), 
     sg.Slider(range=(1, 10), default_value=1, orientation='h', size=(20, 15), key='time_speed')],
    [sg.HorizontalSeparator()],
    [sg.Button('Start/Stop', size=(15, 2), button_color=('white', '#4CAF50'), border_width=0, key='start_stop'), 
     sg.Button('Help', size=(10, 2), button_color=('white', '#3498DB'), border_width=0, key='help'),
     sg.Button('Quit', size=(10, 2), button_color=('white', '#E74C3C'), border_width=0, key='quit')],
    [sg.HorizontalSeparator()],
    [sg.Text('Current Position:', font=('Helvetica', 14)), 
     sg.Text('Unknown', font=('Helvetica', 14), size=(20, 1), key='current_position')],
    [sg.Text('X:', font=('Helvetica', 14)), sg.Input(default_text='0', key='x', size=(5, 1)),
     sg.Text('Y:', font=('Helvetica', 14)), sg.Input(default_text='0', key='y', size=(5, 1)),
     sg.Button('Set Position', button_color=('white', '#8E44AD'), border_width=0, key='set_position')],
]

# Create the window
window = sg.Window('Auto Clicker', layout, size=(500, 400), element_justification='c')

#instance 
#autoclicker = AutoClicker(click_type, float(click_interval), key, int(time_speed))
# Loop to handle user input
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'quit':
        break
    elif event == 'start_stop':
        click_type = 'left' if values['click_left'] else 'right'
        subprocess.Popen(['python', 'autoclicker.py', 
                          '--click_type', click_type, 
                          '--click_interval', values['click_interval'],
                          '--key', values['Key'],
                          '--time_speed', str(values['time_speed'])])
    elif event == 'help':
        sg.popup('Help message goes here', title='Help')
    elif event == 'set_position':
        window['current_position'].update('X: {}, Y: {}'.format(values['x'], values['y']))


window.close()