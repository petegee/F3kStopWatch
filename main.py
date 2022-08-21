from picographics import PicoGraphics, DISPLAY_PICO_DISPLAY_2
from pimoroni import Button
import time

class flight_time:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop      

display = PicoGraphics(display=DISPLAY_PICO_DISPLAY_2, rotate=90)
WHITE = display.create_pen(255, 255, 255)
BLACK = display.create_pen(0, 0, 0)
RED = display.create_pen(255, 0, 0)
GREEN = display.create_pen(0, 255, 0)
button_a = Button(12)
button_b = Button(13)
button_x = Button(14)
button_y = Button(15)

button_b_down = False


def getFlightTimeAsString(flightTime):
    totalTimeAsMilliseconds = (flightTime.stop - flightTime.start)
    s, ms = divmod(totalTimeAsMilliseconds, 1000)
    m, sec = divmod(s, 60)
    return f'{m:02d}:{sec:02d}.{ms:0>3d}'[:-1]

def clear(): 
    display.set_pen(BLACK)
    display.clear()
    display.update()   

def renderCurrentTime():
    global timing
    if timing:
        current_flight_time = flight_time(times[len(times)-1].start, time.ticks_ms())
        renderTimeInMainBox(current_flight_time)
    else:
        renderTimeInMainBox(flight_time(0,0))

def renderCurrentTimeBox(colour):
    # Draw current time box
    display.set_pen(colour)    
    display.rectangle(8, 10, 220, 50)
    display.set_pen(BLACK)   
    display.rectangle(10, 12, 216, 46) 
    display.update()   

previousTime = flight_time(0,0)
def renderTimeInMainBox(ftime):
    global previousTime
    display.set_pen(BLACK)  
    display.text(getFlightTimeAsString(previousTime), 33, 18, 5, 5) 
    previousTime = ftime
    display.set_pen(WHITE)  
    display.text(getFlightTimeAsString(ftime), 33, 18, 5, 5) 
    display.update()   

def renderTimes():
    index = 0
    for ftime in times:
        index = index + 1
        display.set_pen(WHITE)
        display.text(f'{index}.', 20, 25*index+42, 200, 3)   
        display.set_pen(GREEN)
        display.text(getFlightTimeAsString(ftime), 80, 25*index+42, 200, 3)

    display.update()   

def reset():
    global timing
    if timing == True:
        return
    else:
        times.clear()
        timing = False
        clear()
        renderCurrentTimeBox(RED)
        renderCurrentTime()

def startStopTimer():
    global timing
    if timing == True:
        stopTimer()
    else:
        startTimer()

def startTimer():
    global timing
    if timing == True:
        return
    else:
        timing = True
        renderCurrentTimeBox(GREEN)
        times.append(flight_time(time.ticks_ms(), time.ticks_ms()))
        
def stopTimer():
    global timing
    if timing == False:
        return
    else:
        timing = False
        renderCurrentTimeBox(RED)
        times[len(times)-1].stop = time.ticks_ms()   
        renderTimes()
        
def splash():
    display.set_pen(GREEN)
    display.text("F3K Stopwatch", 28, 25, 200, 3)
    display.update() 
    time.sleep(2)
    clear()

display.set_font("bitmap8")
display.set_backlight(1.0)
times = []
timing = False

splash()
renderCurrentTimeBox(RED)

while True:
    renderCurrentTime()
    if button_a.is_pressed:
        reset()
        time.sleep(0.1)
        continue
    if button_b.is_pressed:
        if(button_b_down): 
            continue
        button_b_down = True
        startStopTimer()
        time.sleep(0.1)
        continue
    if button_x.is_pressed:
        continue
    if button_y.is_pressed:
        continue
    
    button_b_down = False
    