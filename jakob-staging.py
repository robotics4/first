#importing too much stuff
from hub import port
import time
import motor
#sets the position for arm
motor.run_to_absolute_position(port.E,40,200)
time.sleep(0.3)
motor.run_to_absolute_position(port.E,13,60)
time.sleep(0.9)
##insert movement towards energy here
#aproaches energy
motor.run_for_degrees(port.D,-400,200)
motor.run_for_degrees(port.F,400,200)
time.sleep(0.9)
#prepares for transport
motor.run_to_absolute_position(port.E,30,200)
time.sleep(0.6)
##insert movement to mission here
#turn (wait wat)
#DUNK
motor.run_to_absolute_position(port.E,180,80)
