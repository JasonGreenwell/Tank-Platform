import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)


LEFT_FWD = GPIO.PWM(17, 1000)
LEFT_REV = GPIO.PWM(22, 1000)
RIGHT_FWD = GPIO.PWM(23, 1000)
RIGHT_REV = GPIO.PWM(24, 1000)


def move(fwd_val, rev_val, lt_val, rt_val):
    
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
        
try:
    while True:
        move(0,0,0,1)
except KeyboardInterrupt:
    GPIO.cleanup()
