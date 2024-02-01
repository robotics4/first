from hub import light_matrix
import motor
from hub import port
import runloop
import time
import hub
import distance_sensor

if distance_sensor.distance(20):
    ##insert movement to mission here
    #turn (wait wat)
    #DUNK
    motor.run_to_absolute_position(port.E,180,100)
    time.sleep(2)
    motor.run_to_absolute_position(port.E,10,100)
    light_matrix.write("WE COOL")




