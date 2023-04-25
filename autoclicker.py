import time
import threading
from typing import Optional
from pynput.mouse import Button, Controller
from pynput.keyboard import Key, Controller as KeyboardController


#pass user arguemnts 
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--click_type', type=str, default='left', help='Specify the click type')
parser.add_argument('--click_interval', type=float, default=1.0, help='Specify the click interval (in seconds)')
parser.add_argument('--key', type=str, default="r", help='Specify the key')
parser.add_argument('--time_speed', type=int, default=1, help='Specify the time speed')
args = parser.parse_args()

#some
delay = 0.1 
button = Button.left 
start_stop_key = KeyCode(char='r') #ipnut for gui 


class user_settings: 
    def __init__(self, buttons):
        self.buttons = buttons
