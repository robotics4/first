import motor
import time
import color
import color_sensor
from hub import port

# imports all the things we need
motor.run_to_absolute_position(port.E, 10, 60)
while not color_sensor.color(port.A) is color.RED:
    if color_sensor.reflection(port.A) > 70:
        motor.run_for_degrees(port.D, -1, 100)
    else:
        motor.run_for_degrees(port.F, 1, 100)
motor.run_for_degrees(port.D, -300, 200)
# makes hub turn on red and follow the road
time.sleep(2.2)
while not color_sensor.color(port.A) is color.BLUE:
    if color_sensor.reflection(port.A) > 70:
        motor.run_for_degrees(port.D, -1, 100)
    else:
        motor.run_for_degrees(port.F, 1, 100)
        motor.run_to_absolute_position(port.E,10,60)
        # makes the hub turn on blue and follow the road
time.sleep(0.9)
# moves foward to get energy
motor.run_to_absolute_position(port.E,20,60)
# makes the hand use gravity to hold energy
time.sleep(0.9)
motor.run_for_degrees(port.D,-50,200)
time.sleep(0.5)
#turns
motor.run_to_absolute_position(port.F,30,200)
time.sleep(0.6)
motor.run_for_degrees(port.D,-400,200)
motor.run_for_degrees(port.F,400,200)
# move foward
time.sleep(0.9)
# sets hub motor E (arm) go to the level of the energy
time.sleep(0.9)
motor.run_for_degrees(port.D,-400,200)
motor.run_for_degrees(port.F,400,200)
motor.run_to_absolute_position(port.E,80,80)
time.sleep(1.5)
motor.run_for_degrees(port.D,150,200)
time.sleep(1.5)
motor.run_for_degrees(port.D,150,200)
motor.run_for_degrees(port.F,-150,200)
