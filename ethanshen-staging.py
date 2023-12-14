import motor
import time

from hub import port
motor.run_to_absolute_position(port.E, 17, 360)
time.sleep(0.1)
motor.run_for_degrees(port.D, 200, 200)
motor.run_for_degrees(port.F, -200, 200)
time.sleep(1)
motor.run_for_degrees(port.D, 200, 200)
motor.run_for_degrees(port.F, -200, 200)
time.sleep(1)
motor.run_for_degrees(port.E, 40, 200)
time.sleep(0.2)
motor.run_for_degrees(port.D, -400, 200)
motor.run_for_degrees(port.F, 400, 200)
time.sleep(1)
motor.run_for_degrees(port.E, 140, 200)
time.sleep(1)
motor.run_for_degrees(port.E, -180, 360)

