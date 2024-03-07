#importing too much stuff
from hub import port
import time
import motor
from hub import light_matrix
import color_sensor
import color
#sets the position for arm
motor.run_to_absolute_position(port.E,40,200)
time.sleep(1)
motor.run_to_absolute_position(port.E,12,100)
time.sleep(1.8)
##insert movement towards energy here
while not color_sensor.color(port.A) is color.RED:
    if color_sensor.color(port.A) is color.BLACK:
        motor.run_for_degrees(port.F,1,200)
        time.sleep(0.001)
    else:
        motor.run_for_degrees(port.D,-1,200)
        time.sleep(0.001)
    if color_sensor.color(port.A) is color.RED:
        motor.run_for_degrees(port.D,-170,200)
        time.sleep(1)
while not color_sensor.color(port.A) is color.BLUE:
    if color_sensor.color(port.A) is color.BLACK:
        motor.run_for_degrees(port.D,-1,200)
        time.sleep(0.001)
    else:
        motor.run_for_degrees(port.F,1,200)
        time.sleep(0.001)
    if color_sensor.color(port.A) is color.BLUE:
        motor.run_for_degrees(port.D,400,200)
        motor.run_for_degrees(port.F,400,200)
#aproaches energy
motor.run_for_degrees(port.D,-400,200)
motor.run_for_degrees(port.F,400,200)
time.sleep(0.9)
#prepares for transport
motor.run_to_absolute_position(port.E,30,200)
time.sleep(0.6)
##insert movement to mission here

#move backwards/approach mission
motor.run_for_degrees(port.D,360,200)
motor.run_for_degrees(port.F,-360,200)
#turn (wait wat)
#DUNK
motor.run_to_absolute_position(port.E,180,100)
time.sleep(2)
motor.run_to_absolute_position(port.E,12,100)
light_matrix.write("WE COOL")
