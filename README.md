# F3K Stop Watch Project
This repo contains the code and instructions to build your own F3K stopwatch.

![](/pic.jpg)

## What is it?
Its a home-made stopwatch using a raspberry pi pico micro-controller and pimoroni2 OLED display to use for timing a pilot competing in an F3K discus-launched glider contest.


## Components Required
 - Raspberry Pi pico https://shop.pimoroni.com/products/raspberry-pi-pico?variant=32402092294227
 - pimoroni pimoroni2 320x240 OLED display https://shop.pimoroni.com/products/pico-display-pack-2-0?variant=39374122582099
 - A 3D printer to print the case
 - 4x momentary buttons
 - A 18500 Li-Ion battery
 - Some sort of charger or way to charge the battery
 - An on/off switch

## Getting Started
1. Assemble the screen onto the board. 
2. Download the pimoroni custom ROM here: https://github.com/pimoroni/pimoroni-pico/releases/download/v1.19.6/pimoroni-pico-v1.19.6-micropython.uf2 or get the latest version (1.19.6 is what ive developed against).
3. Press the boot select "BOOT SEL" button on the back of the board and plug into your computer via the USB
4. It should mount a 'drive' on the pi pico, copy the pimoroni-pico-v1.19.6-micropython.uf2 file you downloaded above into that drive. The pi pico should reset.
5. Use your favourite IDE to upload my main.py script to the root of the device. I use vscode and the Pico-Go add-on to communicate with the pi pico once its out of boot select mode. https://code.visualstudio.com/ & http://pico-go.net/

