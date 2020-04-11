import RPi.GPIO as GPIO
import time
import threading
import pygame
import sys

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)


LEFT_FWD = GPIO.PWM(17, 1000)
LEFT_REV = GPIO.PWM(22, 1000)
RIGHT_FWD = GPIO.PWM(23, 1000)
RIGHT_REV = GPIO.PWM(24, 1000)

class Sonar:
    
    def __init__(self, echo_pin = 25, trigger_pin = 8):
        self.echo_pin = echo_pin
        self.trigger_pin = trigger_pin
    
    def distance(self):
        #GPIO Mode (BOARD / BCM)         
        #set GPIO Pins
        GPIO_ECHO = self.echo_pin # Green
        GPIO_TRIGGER = self.trigger_pin # Yellow
        
         
        #set GPIO direction (IN / OUT)
        GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
        GPIO.setup(GPIO_ECHO, GPIO.IN)
        
        # set Trigger to HIGH
        GPIO.output(GPIO_TRIGGER, True)
     
        # set Trigger after 0.01ms to LOW
        time.sleep(0.00001)
        GPIO.output(GPIO_TRIGGER, False)
     
        StartTime = time.time()
        StopTime = time.time()
     
        # save StartTime
        while GPIO.input(GPIO_ECHO) == 0:
            StartTime = time.time()
     
        # save time of arrival
        while GPIO.input(GPIO_ECHO) == 1:
            StopTime = time.time()
     
        # time difference between start and arrival
        TimeElapsed = StopTime - StartTime
        # multiply with the sonic speed (34300 cm/s)
        # and divide by 2, because there and back
        distance = (TimeElapsed * 34300) / 2
     
        return distance
    def __del__(self):
        GPIO.cleanup()

class Tank:
        def __init__(self):                
                pass
        
        def move(self, fwd_val, rev_val, lt_val, rt_val):
                    if fwd_val:
                        LEFT_FWD.start(fwd_val*100)
                        LEFT_REV.start(0)
                        RIGHT_FWD.start(fwd_val*100)
                        RIGHT_REV.start(0)
                    elif rev_val:
                        LEFT_FWD.start(0)
                        LEFT_REV.start(rev_val*100)
                        RIGHT_FWD.start(0)
                        RIGHT_REV.start(rev_val*100)       
                    elif lt_val:
                        LEFT_FWD.start(lt_val*100)
                        LEFT_REV.start(0)
                        RIGHT_FWD.start(0)
                        RIGHT_REV.start(0)  
                    elif rt_val:
                        LEFT_FWD.start(0)
                        LEFT_REV.start(0)
                        RIGHT_FWD.start(rt_val*100)
                        RIGHT_REV.start(0)
                    else:
                        LEFT_FWD.start(0)
                        LEFT_REV.start(0)
                        RIGHT_FWD.start(0)
                        RIGHT_REV.start(0)
        def stop(self):                
                LEFT_FWD.start(0)
                LEFT_REV.start(0)
                RIGHT_FWD.start(0)
                RIGHT_REV.start(0)

        def init_test(self):
                LEFT_FWD.start(0)
                LEFT_REV.start(0)
                RIGHT_FWD.start(0)
                RIGHT_REV.start(0)
                print(f"Initialization Test Passed! {self.name} is ready to roll!")

