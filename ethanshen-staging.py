import motor
import distance_sensor
import time
import color_sensor
import color
#imports stuff
from hub import port
#imports the ports
motor.run_to_absolute_position(port.E, 15, 180)
while not color_sensor.color(port.A) is color.RED:
    if color_sensor.reflection(port.A) > 70:
        motor.run_for_degrees(port.D, -2, 100)
    else:
        motor.run_for_degrees(port.F, 2, 100)
motor.run_for_degrees(port.D, -280, 200)
time.sleep(1.5)
while not color_sensor.color(port.A) is color.BLUE:
    if color_sensor.reflection(port.A) > 70:
        motor.run_for_degrees(port.D, -1, 100)
    else:
        motor.run_for_degrees(port.F, 1, 100)
#line follower
motor.run_to_absolute_position(port.E, 10, 180)
#gets the thrower ready
time.sleep(0.05)
#waits for the amount of time it takes to load the thrower.
motor.run_for_degrees(port.D, -700, 500)
motor.run_for_degrees(port.F, 700, 500)
#move forward to grab the energy
time.sleep(2.3)
#waits the amount of time it takes to get to the energy
for i in range (0,10):
    motor.run_to_absolute_position(port.E, 40, 50)

#raises the thrower a little bit higher so that gravity will pull it down and then the energy won't fall down
time.sleep(1.5)
#waits the amount of time it takes to move the thrower a bit higher
motor.run_for_degrees(port.D, 150, 180)
time.sleep(1.3)
#turns
while not distance_sensor.distance(port.C) <=50:
    while distance_sensor.distance(port.C) >= 50:
        motor.run_for_degrees(port.D, 10, 200)
        motor.run_for_degrees(port.F, -10, 200)
#moves forward
#motor.run_for_degrees(port.D, 160, 200)
#motor.run_for_degrees(port.F, -160, 200)
time.sleep(1)
#waits the amount of time it takes to move backwards
motor.run_for_degrees(port.E, 250, 300)
#throws the energy
time.sleep(1.5)
#waits the amount of time it takes to throw the energy
motor.run_for_degrees(port.E, -180, 100)
#brings motor E back to the ground
time.sleep(1.50)
#waits the amount of time it takes to move backwards
motor.run_to_absolute_position(port.E, 10, 180)
#36 excluding comments
#19 comments
