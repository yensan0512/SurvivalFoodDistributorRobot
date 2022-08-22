#!/usr/bin/env python3
from ev3dev.ev3 import LargeMotor
from ev3dev.ev3 import MediumMotor
from ev3dev.ev3 import *
import time
from smbus import SMBus

motor = MediumMotor('outD')
m= LargeMotor('outC')
servoT=SMBus(5) #sensor 1 is port3, then sensor3 is port5 (5)  [servo=sensor 3,motor=sensor4]
servoT.write_i2c_block_data(0x01, 0x48, [0xaa]) # this is register, it do nothing
#motorT=SMBus(6)
#motorT.write_i2c_block_data(0x01, 0x48, [0xaa])
#motor.run_timed(time_sp=2000, speed_sp=-1000)
# #remember to change device mode to i2c on ev3, on ev3 go to device broswer->port->in3->mode->other_i2c

 #more value then curve little
# 0x01 i also dont know
# 0x42 is channel 1, then 0x43 is channel 2
# [70] this is start to move, with power of 70, the range is 0 to 254, 0 is 0 degree, 254 is 180 degree, 127 then is 90 degree
servoT.write_i2c_block_data(0x01, 0x42, [255])                        #turn front
time.sleep(3)
m.run_to_rel_pos(position_sp=-180, speed_sp=70, stop_action="hold")  #arm turn up
time.sleep(6)

for i in range(254,110,-2):                              #arm turn to back
    servoT.write_i2c_block_data(0x01, 0x42, [i])
    time.sleep(0.1)
time.sleep(1)

motor.run_timed(time_sp=1500, speed_sp=600)                            #open gripper
time.sleep(5)
motor.run_timed(time_sp=1000, speed_sp=100)                            #open gripper
time.sleep(3)

m.run_to_rel_pos(position_sp=100, speed_sp=60, stop_action="hold")  #arm turn down
time.sleep(3)

motor.run_timed(time_sp=750, speed_sp=-600)   #close gripper
time.sleep(3)
motor.run_timed(time_sp=650, speed_sp=-200)
time.sleep(3)
m.run_to_rel_pos(position_sp=-90, speed_sp=80, stop_action="hold")  #arm turn up
time.sleep(6)


for i in range(110,254,2):                                        #arm turn to front
    servoT.write_i2c_block_data(0x01, 0x42, [i])
    time.sleep(0.1)
time.sleep(1)


m.run_to_rel_pos(position_sp=160, speed_sp=50, stop_action="hold")  #arm down
time.sleep(6)


motor.run_timed(time_sp=1250, speed_sp=600) #arm open
time.sleep(3)

m.run_to_rel_pos(position_sp=-180, speed_sp=60, stop_action="hold")  #arm turn up
time.sleep(6)

motor.run_timed(time_sp=1250, speed_sp=-550) #close gripper
time.sleep(3)
motor.run_timed(time_sp=1250, speed_sp=-500)
time.sleep(3)

m.run_to_rel_pos(position_sp=100, speed_sp=100, stop_action="hold")  #arm turn down
time.sleep(1)


#motorT.write_i2c_block_data(0x01, 0x46, [20])#right, positive forward
#motorT.write_i2c_block_data(0x01, 0x45, [-20])#left, negavite forward



#motorT.write_i2c_block_data(0x01, 0x46, [20])#right, positive forward
#motorT.write_i2c_block_data(0x01, 0x45, [-20])#left, negavite forward




#motorT.write_i2c_block_data(0x01, 0x46, [20])#right, positive forward
#motorT.write_i2c_block_data(0x01, 0x45, [-20])#left, negavite forward

