import motor
import time
import distance_sensor
from hub import port
motor.run_to_absolute_position(port.E, 8, 120)
time.sleep(5)
motor.run_for_degrees(port.D, -200, 200)
motor.run_for_degrees(port.F, 200, 200)
time.sleep(1)
motor.run_for_degrees(port.D, 200, 200)
motor.run_for_degrees(port.F, -200, 200)
time.sleep(1)
motor.run_for_degrees(port.E, 400, 180)
motor.run_to_absolute_position(port.E, 8, 120)
