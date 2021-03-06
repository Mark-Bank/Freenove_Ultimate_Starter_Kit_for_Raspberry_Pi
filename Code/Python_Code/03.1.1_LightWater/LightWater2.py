#!/usr/bin/env python3
########################################################################
# Filename    : LightWater.py
# Description : Use LEDBar Graph(10 LED) 
# Author      : www.freenove.com
# modification: 2019/12/27
########################################################################
from gpiozero import LEDBoard

print('Program is starting ... ')

ledPins = ["J8:11", "J8:12", "J8:13", "J8:15", "J8:16", "J8:18", "J8:22", "J8:3", "J8:5", "J8:24"]
ledPins.reverse()

leds = LEDBoard(*ledPins, active_high=False)

while True:

    raw_score = float(input("Enter points received out of 100: "))
    leds.off()  # clear previous representation

    normalized_score = raw_score / 100.0  # map the score to a normalized range of 0.0 - 1.0
    possible_output_values = len(ledPins) + 1  # add 1 because no LEDs on is a value
    num_on = int(possible_output_values * normalized_score)  # remap the normalized score to the range offered by the
    #                                                          number of LEDs available
    num_on = min(len(ledPins), num_on)  # a perfect score would result in 1 more LED turned on than are available

    if num_on == 0:
        continue

    led_indexes_to_turn_on = [index for index in range(0, num_on)]

    leds.on(*led_indexes_to_turn_on)

    """
    0,1,2,3
    
    (len = 4)
    
    len * score
    
    value += 0.5
    int(value)
    
    
    score is already normalized... 1/(len + 1) = bucket breadth
    
    multiply score by (len + 1) (e.g. .66 * 5 -> 3.3 ... -> 3 on
                                      .18 * 5 -> 0.9 ... -> 0 on
                                      1.0 * 5 -> 5.0 ... -> 5?!?!?! min ( len, result )
    
    
    ___nil___  ____1____  ____2____  ____3____  ____4____
    [0.0-0.2)  [0.2-0.4)  [0.4-0.6)  [0.6-0.8)  [0.8-1.0]
    
    none, 1, 2, 3, 4 = len + 1 possible values
    
    
    """

    # for index in range(0, len(ledPins), 1):  # move led(on) from left to right
    #     leds.on(index)
    #     sleep(0.1)
    #     leds.off(index)
    # for index in range(len(ledPins) - 1, -1, -1):  # move led(on) from right to left
    #     leds.on(index)
    #     sleep(0.1)
    #     leds.off(index)
