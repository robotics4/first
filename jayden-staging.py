import motor
import time
import distance_sensor
from hub import port
import motor
import time
import color_sensor
import color
#imports stuff
from hub import port
#imports the ports
while not color_sensor.color(port.A) is color.RED:
    if color_sensor.reflection(port.A) > 70:
        motor.run_for_degrees(port.D, -3, 100)
    else:
        motor.run_for_degrees(port.F, 3, 100)
time.sleep(4)
motor.run_for_degrees(port.D, -300, 200)
time.sleep(2.2)
while not color_sensor.color(port.A) is color.BLUE:
    if color_sensor.reflection(port.A) > 70:
        motor.run_for_degrees(port.D, -3, 200)
    else:
        motor.run_for_degrees(port.F, 3, 200)
while not color_sensor.color(port.A) is color.BLACK:
    if color_sensor.reflection(port.A) > 70:
        motor.run_for_degrees(port.D, -3, 200)
    else:
        motor.run_for_degrees(port.F, 3, 200)
time.sleep(4)
while distance_sensor.distance(port. C)>50:
    motor.run_for_degrees(port.D, 1, 200)
motor.run_for_degrees(port.D, -600, 200)
motor.run_to_absolute_position(port.E, 8, 120)
time.sleep(5)
motor.run_for_degrees(port.D, -200, 200)
motor.run_for_degrees(port.F, 200, 200)
time.sleep(1)
motor.run_for_degrees(port.E, 30, 180)
time.sleep(1)
time.sleep(1)
motor.run_for_degrees(port.E, 400, 180)
