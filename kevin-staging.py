import motor
import time
import color
import color_sensor
from hub import port
# imports all the things we need

while not color_sensor.color(port.A) is color.RED:
    if color_sensor.reflection(port.A) > 70:
        motor.run_for_degrees(port.D, -3, 100)
    else:
        motor.run_for_degrees(port.F, 3, 100)
motor.run_for_degrees(port.D, -300, 200)
# makes hub turn on red and follow the road
time.sleep(2.2)
while not color_sensor.color(port.A) is color.BLUE:
    if color_sensor.reflection(port.A) > 70:
        motor.run_for_degrees(port.D, -3, 100)
    else:
        motor.run_for_degrees(port.F, 3, 100)
        motor.run_to_absolute_position(port.E,40,200)
        # makes the hub turn on blue and follow the road
time.sleep(0.3)
motor.run_to_absolute_position(port.E,10,60)
# sets hub motor E (arm) go to the level of the energy
time.sleep(0.9)
motor.run_for_degrees(port.D,-400,200)
motor.run_for_degrees(port.F,400,200)
# moves foward
time.sleep(0.9)
motor.run_for_degrees(port.D,-150,200)
time.sleep(0.5)
motor.run_to_absolute_position(port.E,30,200)
time.sleep(0.6)
motor.run_for_degrees(port.D,-200,200)
motor.run_for_degrees(port.F,200,200)
time.sleep(0.9)
motor.run_to_absolute_position(port.E,180,80)
