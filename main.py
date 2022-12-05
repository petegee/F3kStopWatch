from picographics import PicoGraphics, DISPLAY_PICO_DISPLAY_2
from pimoroni import Button
import time

class flight_time:
    def __init__(self, start, stop, valid=True):
        self.start = start
        self.stop = stop      
        self.valid = valid

display = PicoGraphics(display=DISPLAY_PICO_DISPLAY_2, rotate=90)
WHITE = display.create_pen(255, 255, 255)
BLACK = display.create_pen(0, 0, 0)
RED = display.create_pen(255, 0, 0)
GREEN = display.create_pen(0, 255, 0)
button_a = Button(12)
button_b = Button(13)
button_x = Button(14)
button_y = Button(15)

max_rows = 10
button_b_down = False
skip = 0
total_completed_times=0

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
    global skip, total_completed_times
    display.set_pen(BLACK)   
    display.rectangle(0, 64, 320, 293) 
    display.update() 
    index = 0
    for i in range(skip, total_completed_times):
        if index == max_rows:
            break
        index = index + 1
        display.set_pen(WHITE)
        display.text(f'{i+1}.', 20, 25*index+42, 200, 3)   
        if times[i].valid is True:
            display.set_pen(GREEN)
        else:
            display.set_pen(RED)
            display.line(76, 25*index+52, 188, 25*index+52)

        display.text(getFlightTimeAsString(times[i]), 80, 25*index+42, 200, 3)

    display.update()   


def toggleStrikeOutLastTime():
    global total_completed_times, times
    if timing == True:
        return
    if total_completed_times < 1:
        return
    times[total_completed_times-1].valid = not times[total_completed_times-1].valid
    renderTimes()
    time.sleep(0.2)

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
    global timing, total_completed_times
    if timing == False:
        return
    else:
        timing = False
        renderCurrentTimeBox(RED)
        times[len(times)-1].stop = time.ticks_ms()   
        total_completed_times = total_completed_times + 1
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
    overflowed_times_count = 0
    if total_completed_times - max_rows > 0:
        overflowed_times_count =  total_completed_times - max_rows

    if button_a.is_pressed:
        toggleStrikeOutLastTime()
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
        if overflowed_times_count > 0 and skip > 0:
            skip = skip - 1
            renderTimes()
        time.sleep(0.1)
        continue
    if button_y.is_pressed:
        if overflowed_times_count > 0 and skip < overflowed_times_count:
            skip = skip + 1
            renderTimes()
        time.sleep(0.1)
        continue
    
    button_b_down = False
    