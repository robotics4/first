import motor
import time
from hub import port

motor.run_to_absolute_position(port.E, 14, 150)
# makes the motor hand go to perfect position
motor.run_for_degrees(port.D, -400, 100)
motor.run_for_degrees(port.F, 400, 100)
# makes robot move foward
time.sleep(1.5)
motor.run_for_degrees(port.E, 40, 50)
time.sleep(1.5)
motor.run_for_degrees(port.D, 400, 100)
motor.run_for_degrees(port.F, -400, 100)
time.sleep(1.5)
motor.run_for_degrees(port.E, -220, 200)







import motor
import time
#imports stuff
from hub import port
#imports the ports
motor.run_to_absolute_position(port.E, 10, 360)
#gets the thrower ready
time.sleep(0.05)
#waits for the amount of time it takes to load the thrower.
motor.run_for_degrees(port.D, -250, 200)
motor.run_for_degrees(port.F, 250, 200)
#move forward to grab the energy
time.sleep(1)
#waits the amount of time it takes to get to the energy
motor.run_for_degrees(port.E, 30, 50)
#raises the thrower a little bit higher so that gravity will pull it down and then the energy won't fall down
time.sleep(0.9)
#waits the amount of time it takes to move the thrower a bit higher
motor.run_for_degrees(port.D, 220, 200)
motor.run_for_degrees(port.F, -220, 200)
#moves the motors backwards towards the toy factory
time.sleep(1.5)
#waits the amount of time it takes to move backwards
motor.run_for_degrees(port.E, 220, 250)
#throws the energy
time.sleep(0.7)
#waits the amount of time it takes to throw the energy
motor.run_for_degrees(port.E, -220, 300)
#brings motor E back to the ground
