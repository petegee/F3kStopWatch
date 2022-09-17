# F3K Stop Watch Project
This repo contains the code and instructions to build your own F3K stopwatch.

![](/watch.jpg)

## What is it?
Its a home-made stopwatch using a raspberry pi pico micro-controller and pimoroni2 OLED display to use for timing a pilot competing in an F3K discus-launched glider contest.

### F3 what?
https://f3ksa.blogspot.com/p/what-is-f3k.html


## Components Required
 - Raspberry Pi pico https://shop.pimoroni.com/products/raspberry-pi-pico?variant=32402092294227
 - pimoroni pimoroni2 320x240 OLED display https://shop.pimoroni.com/products/pico-display-pack-2-0?variant=39374122582099
 - A 3D printer to print the case
 - 2x momentary buttons
 - A 14500 Li-Ion battery
 - A USB lipo/l-ion charger board
 - A 5V step-up volt regulator
 - An small LCD volt meter to show battery voltage
 - An on/off switch

## Getting Started
1. Assemble the screen onto the board. 
2. Download the pimoroni custom ROM here: https://github.com/pimoroni/pimoroni-pico/releases/download/v1.19.6/pimoroni-pico-v1.19.6-micropython.uf2 or get the latest version (1.19.6 is what ive developed against).
3. Press the boot select "BOOT SEL" button on the back of the board and plug into your computer via the USB
4. It should mount a 'drive' on the pi pico, copy the pimoroni-pico-v1.19.6-micropython.uf2 file you downloaded above into that drive. The pi pico should reset.
5. Use your favourite IDE to upload my main.py script to the root of the device. I use vscode and the Pico-Go add-on to communicate with the pi pico once its out of boot select mode. https://code.visualstudio.com/ & http://pico-go.net/
6. Print the case and back from the supplied STLs or modify the case using the provided F360 files.
7. Assemble something like per the internals.jpg picture.

![](/internals.jpg)

View the F360 model here:
https://a360.co/3djS4cy


## Thoughts So Far
I have completed my first watch and the assembly was a bit tighter than i had hoped, so i had to file a few spots on the momentaries to get the board to fit in its home. 

The run time on mine with a fully charged 800mAh 14500 Li-Ion battery was over 7 hours. So more than enough for a whole weekend of 10min rounds of f3k.

Daylight readability of the screen is OK, just not amazing. Under the direct high summer sun, a bit of body sheilding light may help.

I still want to progress the software to be F3K task based and give more task-specific timings and suggestions. But this will do for now...