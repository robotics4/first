import motor
import time
import distance_sensor
from hub import port

while not color_sensor.color(port.A) is color.RED:
    if color_sensor.reflection(port.A) > 70:
        motor.run_for_degrees(port.D, -3, 100)
    else:
        motor.run_for_degrees(port.F, 3, 100)
time.sleep(3.4)
motor.run_for_degrees(port.D, -380, 200)
time.sleep(2.2)
while not color_sensor.color(port.A) is color.BLUE:
    if color_sensor.reflection(port.A) > 70:
        motor.run_for_degrees(port.D, -3, 100)
    else:
        motor.run_for_degrees(port.F, 3, 100)
time.sleep(2.5)
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
time.sleep(1.5)
