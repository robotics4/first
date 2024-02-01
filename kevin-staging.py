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
time.sleep(1.5)
