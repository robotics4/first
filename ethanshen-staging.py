import motor
import time
#imports stuff
from hub import port
#imports the ports
motor.run_to_absolute_position(port.E, 14, 360)
#gets the thrower ready
time.sleep(0.05)
#waits for the amount of time it takes to load the thrower.
motor.run_for_degrees(port.D, -450, 200)
motor.run_for_degrees(port.F, 450, 200)
#move forward to grab the energy
time.sleep(1)
#waits the amount of time it takes to get to the energy
motor.run_for_degrees(port.E, 40, 50)
#raises the thrower a little bit higher so that gravity will pull it down and then the energy won't fall down
time.sleep(0.9)
#waits the amount of time it takes to move the thrower a bit higher
motor.run_for_degrees(port.D, 180, 200)
motor.run_for_degrees(port.F, -180, 200)
#moves the motors backwards towards the toy factory
time.sleep(1.5)
#waits the amount of time it takes to move backwards
motor.run_for_degrees(port.E, 180, 300)
#throws the energy
time.sleep(0.7)
#waits the amount of time it takes to throw the energy
motor.run_for_degrees(port.E, -220, 360)
#brings motor E back to the ground
