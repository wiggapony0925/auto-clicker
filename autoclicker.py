import time 
import threading 
from typing import get_args
from pynput.mouse import Button, Controller 
from pynput.keyboard import Listener, KeyCode

#some
delay = 0.1 
button = Button.left 
start_stop_key = KeyCode(char='r') #ipnut for gui 



