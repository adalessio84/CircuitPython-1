# My CircuitPython assignments
* [Helpful tool for making your github page!](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)

This tool gives your information and guidline for certain features like links and picture formating for github.
## LED Blink Fade

##### Objective 

The first assignment I did was and LED blink/fade
project, I used the CircuitPython metro board
to make an LED blink and then fade in and out

##### Pictures

<img src="media/led_fade.png" width="300px" /> 

* I got this from [Dr. Shields](https://github.com/DoctorShields)

```python
led = pulseio.PWMOut(board.D13, frequency=5000, duty_cycle=0)    # sets up pin.

while True:
    for i in range(100):
        # PWM LED up and down
        if i < 50:
```

* This is a portion of my code that is helpful in doing this assignment

##### Problems
The main problem that i faced in this project was actually the wriring, I had to do some research to re-acquaint myself with how to wire and LED correctly, but other than that there where very few problems that I face while doing this assignment. (I had one time when I got an error from the console, however, I just needed to restart the board. 
##### What I Learned!
For starters I learned how to properly wire and how to create a basi code on CircuitPython but I also re-discovered how to make an LED blink because I had forgotten how to do so.


## Servo

##### Objective

The next assignment I did was a servo assignment.
I basically just made a servo turn by touching 2
different wires which made it go in either
direction, I set it to 180 degrees which ment it
went from one end of the servo to the other.

##### Pictures

<img src="media/circuitpython_MetroM4ExpressServo_bb.jpg" width="300px" />

##### Problems
The main problem I faced in this assignment, was figruing out how to get the servo to turn. I already had a pretty good idea of how to wire a servo since that was my main project last year, however, it took me a few tries to get the servo to turn the ammount of degrees I wanted, which was very annoying. Another thing I had a problem with was figuring out how to make it turn by touching the wires. It took me about half a day and the help from other github pages to figure it out.
##### What I Learned!
I learned how to once again make a servo turn but this time using my fingers to touch a wire. 


## LCD Screen and botton
[[]]
##### Objective

The last assignment I did was I hooked up a button
and LCD screen to my metro board and then created a
code that allows it to count up by one on the LCD
if the button is pressed. The most difficult part was
trying to do it without an excessive use of time.sleep

##### Pictures

##### Problems
In this assignment I had 2 problems, getting the lcd screen to print what I wanted, to get the button to count up without using a time.sleep constantly. This assignment was one of the more difficult ones because I had to make a code which didnt use time.sleep as much, which, trust me, was very hard because up until now, time.sleep was the only delay type of tool I used (besides delay on Arduino). Getting what I wanted on the actual LCD screen was super hard for me. I didn't get it working until the very, infact I used the serial monitor to do all the numeric stuff involved. 
##### What I Learned!
This assignmetn taught me how to use the LCD to count up and how to wire a button to it to do so. I also taught me to desgin a code which counted up on click instead of on delay which was helpful and interesting. 


## Photo Interupter
[[]]
##### Objective

In this assignment I used a photo interupter to print the
number of interupts o nthe srial monitor. It was a bit
difficult to not get it to just print out random interupt
numbers.

##### Pictures

##### Problems
The only problem I had with this one was getting the serial montor to not just print random numbers when the photo interupter is interupted. It would print really odd numbers when I slid a piece of acrilyc through it and it took me a long time to figure out why it was doing that and how to fix it. 
##### What I Learned!
In the end I learned that I need to pay more attention to the corralation of my wiring to my coding to make sure everything is lined up correctly with each other, because in the assignments, one mistake can screw up the entire assignment. 


## Ultrasonic Sensor
[[]]
##### Objective

In this assignment we used an ultrasonic sensor in orde
to change the RGB led light on the metro bored from 
red to green while, displaying all the colors in between 
the too like, blu, teal, purple, etc. 

##### Pictures

##### Problems
This project was a difficult one. I had to get it to print differnt colors at differemt distances and it was tough. I say this because the ultrasonic sensor is somewhat glitchy sometimes, and it will print distances from all the way across the room. (so basically it would be transitioning accoringly and then random go to red because the distance was interupted) My wiring was right and coding was right, I just needed to do some fixing up to the delays and distances to make them run smoother. 
##### What I Learned!
In this assignment I learned that using a flat surface is the best way to minimize the ultrasonic sensor glitches, also I need to be smarter about the delays I use. 


## Fancy RGB LED
[[]]
##### Objective

The purpose of this assigment was to use 2 rgb leds and 
display all the colors of the rainbow in order, and then 
create a color shift rainbow sequence with the same led 
the previous colors are displayed. (Hardest part is 
getting the leds to work)

##### Pictures

##### Problems
The most significant problem I had with this assignment was getting the wiring and code synced up. It took me so long to get the LEDs to turn on and then after that to make the right colors. Other than that there few problems. (Occasional error in console) However, once I got to the rainbow light, it got super difficult. I had to keep switching the pins on the board to get the wires correct and I had to reverse a couple colors, which got super tedious and annoying. But I eventually figured it out. 
##### What I Learned!
I learned to use 3v instead of 5v to get better color definition. Also I learned how to wire and use an RGB LED and get the colors to work properly. 

