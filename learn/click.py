from pynput.mouse import Button, Controller
import time
from datetime import datetime
mouse = Controller()
hours = 8
minutes = 10

duration = (hours * 60 + minutes) * 60 # convert into seconds

timestamp = time.time()
dt_object = datetime.fromtimestamp(timestamp)
formatted_time = dt_object.strftime('%Y-%m-%d %H:%M:%S')

sleep_time = 5*60
print(f'Start at: {formatted_time}')
print(f'Schedule clicking for {hours} h {minutes} min')
print(f'Click every {sleep_time} seconds')
while time.time()-timestamp < duration:
    mouse.click(Button.left, 1)
    time.sleep(0.5)
    mouse.click(Button.left, 1)
    time.sleep(sleep_time)

print('END CLICKING')
timestamp = time.time()
dt_object = datetime.fromtimestamp(timstamp)
formatted_time = dt_object.strftime('%Y-%m-%d %H:%M:%S')
print('Stops at:', formatted_time)
