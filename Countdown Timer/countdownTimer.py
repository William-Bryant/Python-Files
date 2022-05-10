import time
import os



def count(t):
    x = 0
    y = 0
    file = "Beep.wav"
    while t > 0:
        if t >59:
            x = t // 60
            y = t % 60
        else:
            x = 0
            y = t
        print('{:02d}:{:02d}'.format(x,y))
        time.sleep(1)
        t -= 1
    os.system("afplay Beep.wav&")
    print("Timer is up!")   
        
t = input('Enter the time in seconds: ')

count(int(t))
