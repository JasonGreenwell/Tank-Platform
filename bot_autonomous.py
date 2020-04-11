import time
import sys
import pygame
from covid_bot import Mode
from autobot import Sonar, Tank

class Autonomous:
    
    def __init__(self):
        self.mode = Mode()
        self.tank = Tank()
        pygame.init()
        self.joystick = pygame.joystick.Joystick(0)
        self.joystick.init()
        

    def start(self):       
        fwd_sonar = Sonar()
        fwd_distance = 100
        left_sonar = Sonar(7,1)
        right_sonar = Sonar(16,20)


        try:
            while True:
                pygame.event.pump()
                fwd_measurement = fwd_sonar.distance()
                auto_speed = abs(self.joystick.get_axis(3))
                if fwd_measurement > 10:
                    #tank.forward()
                    #print ("Forward measured distance = %.1f cm" % fwd_measurement)
                    print("Going Forward")
                    self.tank.move(auto_speed,0,auto_speed,0)
                    time.sleep(.1)
                   
                elif fwd_measurement < 10:
                    #print(f"Forward distance is {fwd_measurement}: CHECKING LEFT QUADTRANT")
                    left_measurement = left_sonar.distance()
                    right_measurement = right_sonar.distance()
                    time.sleep(.1)
                    if left_measurement > 10:
                        print(f"Turning Left")
                        self.tank.move(0,0,auto_speed,0)
                        time.sleep(1)
                        self.tank.move(0,0,0,0)
                    elif left_measurement < 10:
                        print(f"Turning Right")
                        self.tank.move(0,0,0,auto_speed)
                        time.sleep(1)
                        self.tank.move(0,0,0,0)
                        
                if self.joystick.get_button(0):
                    self.mode.tele()
                    
                if self.joystick.get_button(10):
                    self.tank.stop()
                    sys.exit()
                     
        except KeyboardInterrupt:
            self.tank.stop()
            print("Measurement stopped by User")
            sys.exit()
