import sys
import time
import Drone

drone1 = Drone.Drone("128.1.1.1", 8889)

drone1.connect()

drone1.printinfo()

drone1.takeOff()
#time.sleep(2)

while (drone1.battery() > 10):
    drone1.up(20)
    drone1.forward(20)

drone1.land()
drone1.end()