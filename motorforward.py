#!/usr/bin/env python3


from smbus import SMBus
from time import sleep


motorT=SMBus(6) #sensor 1 is port3, then sensor3 is port5 (5)  [servo=sensor 3,motor=sensor4]
motorT.write_i2c_block_data(0x01, 0x48, [0xaa])
motorT.write_i2c_block_data(0x01, 0x45, [-18])   #left,positive forward
motorT.write_i2c_block_data(0x01, 0x46, [20])    #right
sleep(0.4)
motorT.write_i2c_block_data(0x01, 0x45, [0])   
motorT.write_i2c_block_data(0x01, 0x46, [0])
