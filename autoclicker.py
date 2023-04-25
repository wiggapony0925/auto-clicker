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

#auto clicker

class AutoClicker:
      def __init__(self, click_type: str, click_interval: float, key: Optional[str], time_speed: int):
        self.click_type = click_type
        self.click_interval = click_interval
        self.key = key
        self.time_speed = time_speed
        self.stop_event = threading.Event()
        self.mouse = Controller()
        self.keyboard = KeyboardController()
