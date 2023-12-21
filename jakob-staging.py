#importing too much stuff
from hub import port
import time
import motor
#sets the position for arm
motor.run_to_absolute_position(port.E,10,200)
motor.run_for_degrees(port.D,-350,200)
motor.run_for_degrees(port.F,350,200)
