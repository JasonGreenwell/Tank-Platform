import RPi.GPIO as GPIO
import time
import pygame
import sys

#Pygame Stuff for the joystick
pygame.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()
print(f"Initialized Joystick {joystick.get_name()}")


#GPIO stuff for the tank
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)  # 
GPIO.setup(22,GPIO.OUT)  # 
GPIO.setup(23,GPIO.OUT)  # 
GPIO.setup(24,GPIO.OUT)  #
#GPIO.setup(29,GPIO.OUT)  #

def init_test():
    self.forward(.05)
    time.sleep(.1)
    self.reverse(.05)
    time.sleep(.1)
    self.left(.05)
    time.sleep(.1)
    self.right(.05)
    print(f"Initialization Test Passed! {self.name} is ready to roll!")

print("Tank Initialized")

jmap = {
    "left_right":joystick.get_axis(0),
    "up_down":joystick.get_axis(1),
    'twist':joystick.get_axis(2),
    "trigger":joystick.get_button(0),
    "thumb":joystick.get_button(1),
    "button_3":joystick.get_button(2),
    "button_4":joystick.get_button(3),
    "button_5":joystick.get_button(4),
    "button_6":joystick.get_button(5),
    "button_7":joystick.get_button(6),
    "button_8":joystick.get_button(7),
    "button_9":joystick.get_button(8),
    "button_10":joystick.get_button(9),
    "button_11":joystick.get_button(10),
    "button_12":joystick.get_button(11),
    "hat":joystick.get_hat(0),
    "throttle":joystick.get_axis(3)
    }

def read():
    joystick = pygame.joystick.Joystick(0)
    axes = joystick.get_numaxes()
    while True:
        try:            
            pygame.event.pump()
            #print(joystick.get_axis(1))
            if joystick.get_axis(1) > .5:
                reverse()
            elif joystick.get_axis(1) < -.5:
                forward()
            elif joystick.get_axis(0) > .5:
                right()
            elif joystick.get_axis(0) < -.5:
                left()
            else:
                stop()
        except KeyboardInterrupt as e:
            GPIO.cleanup()
            sys.exit


def forward():
    print("Going Forward")
    GPIO.output(17,False)
    GPIO.output(22,True) 
    GPIO.output(23,False)
    GPIO.output(24,True)
    
def reverse():
    print("Going in reverse")
    GPIO.output(17,True)
    GPIO.output(22,False)
    GPIO.output(23,True)
    GPIO.output(24,False)

def right():
    print("Going Right")
    GPIO.output(17,False)
    GPIO.output(22,True)
    GPIO.output(23,True)
    GPIO.output(24,False)

def left():
    print("Going Left")
    GPIO.output(17,True)
    GPIO.output(22,False)
    GPIO.output(23,False)
    GPIO.output(24,True)
    

def stop():
    print("Stopping")
    GPIO.output(17,False)
    GPIO.output(22,False)
    GPIO.output(23,False)
    GPIO.output(24,False)
    
read()