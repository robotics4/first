from hub import light_matrix
import motor
from hub import port
import runloop
import time
import hub
import distance_sensor

if distance_sensor.distance(9):
    ##insert movement to mission here
    #move backwards/approach mission
    motor.run_for_degrees(port.D,360,200)
    motor.run_for_degrees(port.F,-360,200)
    #turn (wait wat)
    #DUNK
    motor.run_to_absolute_position(port.E,180,100)
    time.sleep(2)
    motor.run_to_absolute_position(port.E,10,100)
    light_matrix.write("WE COOL")




