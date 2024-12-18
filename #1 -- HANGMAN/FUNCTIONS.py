import time
from COLORS import *

PRINT_DELAY = 0

@staticmethod
def rgb_colored(text, rgb):
    r, g, b = rgb
    return f"\033[1m\033[38;2;{r};{g};{b}m{text}\033[0m"  # Bold and RGB color



def print_delay(items, delay=PRINT_DELAY):
    for item in items:
        print(item, end='', flush=True)  # `flush=True` forces the output to be written immediately
        time.sleep(delay)  # Wait for 'delay' seconds before printing the next item
    print()  # Move to the next line after all items are printed


def exit_button():
    text = rgb_colored(f"""
┏┳━━━━━━━━━━━━━━━━━━━━━┳┓
┃┃ PRESS ENTER TO EXIT ┃┃
┗┻━━━━━━━━━━━━━━━━━━━━━┻┛                                    
                """, GREEN)
    input(text)
    
    print()