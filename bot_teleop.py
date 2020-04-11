import pygame
import sys
from bot_autonomous import Autonomous
from autobot import Tank

class Teleop:
    
    #Pygame Stuff for the joystick
    pygame.init()
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    print(f"Initialized Joystick {joystick.get_name()}")
    
    def __init__(self):
        self.autonomous = Autonomous()
        self.tank = Tank()  

    def start(self):
        joystick = pygame.joystick.Joystick(0)
        axes = joystick.get_numaxes()
        while True:
            try:            
                pygame.event.pump()
                if joystick.get_axis(2) < 0.09:
                    print (f"Going Left: {abs(joystick.get_axis(2))}")
                    self.tank.move(0,0,abs(joystick.get_axis(2)),0)
                elif joystick.get_axis(2) > 0.09:
                    print (f"Going Right: {joystick.get_axis(2)}")
                    self.tank.move(0,0,0,joystick.get_axis(2))
                                
                if joystick.get_axis(1) < 0.09:
                    print (f"Going Forward: {abs(joystick.get_axis(1))}")
                    self.tank.move(abs(joystick.get_axis(1)),0,0,0)            
                elif joystick.get_axis(1) > 0.09:
                    print (f"Going Reverse: {joystick.get_axis(1)}")
                    self.tank.move(0,joystick.get_axis(1),0,0)
                            
                if joystick.get_button(1):
                    print("Thumb Button Pressed...Going Autonomous")
                    self.autonomous.start()        
                if joystick.get_button(0):
                    print("Trigger Pressed")
                                        
                if self.joystick.get_button(10):
                    self.tank.stop()
                    sys.exit()
                
            except KeyboardInterrupt as e:
                sys.exit
