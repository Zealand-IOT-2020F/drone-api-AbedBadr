import sys
import time
import Drone

#drone1 = Drone.Drone("128.1.1.1", 8889)
drone1 = Drone.Drone("192.168.10.1", 8889)

drone1.connect()

drone1.printinfo()

drone1.takeOff()
#time.sleep(2)

drone1.up(50)

# while (drone1.battery() > 10):
#     drone1.forward(50)
#     drone1.cw(90)
drone1.forward(50)
drone1.cw(90)

drone1.land()
drone1.end()