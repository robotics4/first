import motor
import time

from hub import port
motor.run_to_absolute_position(port.E, 14, 360)
time.sleep(0.05)
motor.run_for_degrees(port.D, -400, 200)
motor.run_for_degrees(port.F, 400, 200)
time.sleep(1)
motor.run_for_degrees(port.E, 40, 200)
time.sleep(0.2)
motor.run_for_degrees(port.D, 300, 200)
motor.run_for_degrees(port.F, -300, 200)
time.sleep(2.5)
motor.run_for_degrees(port.E, 180, 300)
time.sleep(1)
motor.run_for_degrees(port.E, -220, 360)
