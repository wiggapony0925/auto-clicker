import time
import threading
from typing import Optional
from pynput.mouse import Button, Controller
from pynput.keyboard import Key, Controller as KeyboardController


#pass user arguemnts 
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--click_type', type=str, default='left', help='Specify the click type')
parser.add_argument('--click_interval', type=float, default=0.1, help='Specify the click interval (in seconds)')
parser.add_argument('--key', type=str, default="r", help='Specify the key')
parser.add_argument('--time_speed', type=float, default=1, help='Specify the time speed')
args = parser.parse_args()

#auto clicker

class AutoClicker:
    def __init__(self, click_type: str, click_interval: float, key: Optional[str], time_speed: float):
        self.click_type = click_type
        self.click_interval = click_interval
        self.key = key
        self.time_speed = time_speed
        self.stop_event = threading.Event()
        self.mouse = Controller()
        self.keyboard = KeyboardController()

    def start_clicking(self):
        def click():
            while not self.stop_event.is_set():
                if self.click_type == 'left':
                    self.mouse.click(Button.left)
                elif self.click_type == 'right':
                    self.mouse.click(Button.right)
                if self.key:
                    self.keyboard.press(self.key)
                    time.sleep(0.01 * self.time_speed)
                    self.keyboard.release(self.key)
                time.sleep(self.click_interval * self.time_speed)

        threading.Thread(target=click, daemon=True).start()

    def stop_clicking(self):
        self.stop_event.set()
