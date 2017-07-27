# EG4-01 Self Timer

import time
import random

print('''Welcome to Self Timer

Everybody stand up
Stay standing until you think the time has ended.
Then sit down.
Anyone still standing when the time ends loses.
The last person to sit down before the time ended will win.''')

stand_time = random.randint(5, 20) 

print('Stay standing for', stand_time, 'seconds.') 

time.sleep(stand_time) 

print('****TIME UP****') 

