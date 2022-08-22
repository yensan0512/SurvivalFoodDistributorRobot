#!/usr/bin/env python3

from ev3dev.ev3 import LargeMotor
from ev3dev.ev3 import MediumMotor
from ev3dev.ev3 import *
import time
from smbus import SMBus

motor = MediumMotor('outD')
m=LargeMotor('outC')
servoT=SMBus(5) #sensor 1 is port3, then sensor3 is port5 (5)  [servo=sensor 3,motor=sensor4]
servoT.write_i2c_block_data(0x01, 0x48, [0xaa])
motorT=SMBus(6) #sensor 1 is port3, then sensor3 is port5 (5)  [servo=sensor 3,motor=sensor4]
motorT.write_i2c_block_data(0x01, 0x48, [0xaa])


servoT.write_i2c_block_data(0x01, 0x42, [255])
time.sleep(1)
#m.run_to_rel_pos(position_sp=-180, speed_sp=150, stop_action="hold")  #arm up
#time.sleep(6)


#m.run_to_rel_pos(position_sp=50, speed_sp=100, stop_action="hold")  #arm down
#time.sleep(3)
motor.run_timed(time_sp=2000, speed_sp=400) #arm for pick item package
time.sleep(3)
m.run_to_rel_pos(position_sp=60, speed_sp=100, stop_action="hold")  #arm down
time.sleep(4)

motor.run_timed(time_sp=3000, speed_sp=-250)  #close gripper
time.sleep(2)
#motor.run_timed(time_sp=1000, speed_sp=-250)  #close gripper
#time.sleep(3)

m.run_to_rel_pos(position_sp=-150, speed_sp=90, stop_action="hold")  #arm turn up
time.sleep(8)

for i in range(255,130,-5):                                            #arm turn to back
  servoT.write_i2c_block_data(0x01, 0x42, [i])
  time.sleep(0.1)
time.sleep(1)

  
motor.run_timed(time_sp=3000, speed_sp=250)                          #gripper open
time.sleep(3)
motor.run_timed(time_sp=3000, speed_sp=-300)
time.sleep(3)

for i in range(130,255,5):                                        #arm turn to front
  servoT.write_i2c_block_data(0x01, 0x42, [i])
  time.sleep(0.1)
time.sleep(1)

m.run_to_rel_pos(position_sp=90, speed_sp=100, stop_action="hold")  #arm down
time.sleep(3)
