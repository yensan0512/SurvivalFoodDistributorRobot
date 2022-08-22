#!/usr/bin/env python3
import rpyc
import time
from subprocess import call

conn = rpyc.classic.connect('ev3dev')  # host name or IP address of the EV3
subprocess = conn.modules['subprocess']
ev3 = conn.modules['ev3dev.ev3']
motor = ev3.MediumMotor('outD')
m = ev3.LargeMotor('outC')
cl = ev3.ColorSensor()
#us = ev3.UltrasonicSensor('in2')
cl.mode='COL-COLOR'
DISTANCE_DETECT = True
COLOR_DETECT = True
btn = ev3.Button()
colors=('unknown','black','blue','green','yellow','red','white','brown')
#initial = us.value()

if __name__ == '__main__':

  print(colors[cl.value()])
  print(cl.value())
  subprocess.call("python3 robot/servofront.py", shell=True)
  time.sleep(1)
  m.run_to_rel_pos(position_sp=-60, speed_sp=150, stop_action="hold")  #arm up
  time.sleep(6)
  while not btn.any():
    if (colors[cl.value()] == "red" ):
      subprocess.call("python3 robot/motorstop.py", shell=True)
      print("---> It is red color...")
      ev3.Sound.speak('Red').wait()
      #m.run_to_rel_pos(position_sp=-180, speed_sp=150, stop_action="hold")
      #subprocess.call("python3 vscode-hello-python-master/red.py", shell=True)
      #if(initial-us.value > 1):
      subprocess.call("python3 robot/red.py", shell=True)
      subprocess.call("python3 robot/motorforward.py", shell=True)
      

    elif (colors[cl.value()] == "blue" ):
      print("---> It is blue color...")
      subprocess.call("python3 robot/motorstop.py", shell=True)
      ev3.Sound.speak('Blue').wait()
      #m.run_to_rel_pos(position_sp=-50, speed_sp=150, stop_action="hold")
      #if(initial-us.value > 1):S
      subprocess.call("python3 robot/blue.py", shell=True)
      subprocess.call("python3 robot/motorforward.py", shell=True)
      # motorT.write_i2c_block_data(0x01, 0x45, [-14])  
      # motorT.write_i2c_block_data(0x01, 0x46, [16])      #right,positive forward
      #left,positive forward

    else:
      print("---> Error input...")
      ev3.Sound.speak('Error').wait()
      subprocess.call("python3 robot/servofront.py", shell=True)
      time.sleep(1)
      #m.run_to_rel_pos(position_sp=-180, speed_sp=150, stop_action="hold")  #arm up
      #time.sleep(6)
      subprocess.call("python3 robot/motorforward.py", shell=True)
      #m.run_to_rel_pos(position_sp=120, speed_sp=100, stop_action="hold")
      pass
      #subprocess.call("python3 robot/motorforward.py", shell=True)
      #time.sleep(1)
        
    #if btn.any():
  print("Button is pressed,change task !")
  call("python C:/Users/ASUS/Downloads/robot/combine.py", shell=True)
    #else:
    #  time.sleep(0.5)


    
    

