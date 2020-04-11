import bot_teleop
import bot_autonomous

# Thumb is auto, Trigger is tele

class Mode:
	
	def __init__(self):
		pass
	
	def tele(self):
		t = bot_teleop.Teleop()
		t.start()
	
	def auto(self):
		a = bot_autonomous.Autonomous()
		a.start()
		
	
def main():
	mode = Mode()
	mode.tele()

if __name__ == '__main__': main()
