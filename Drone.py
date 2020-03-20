import socket
import sys
import time


class Drone(object):
    """description of class"""

    def __init__(self, ip, port):
        self.TelloIp = ip
        print("ip: " + ip)
        self.TelloPort = port
        # UDP Socket
        self.Host = ''
        self.HostPort = 9000
        self.locaddr = (self.Host, self.HostPort)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.tello_address = ('192.168.10.1', 8889)
        self.sock.bind(self.locaddr)

    def sendMessage(self,TelloMessage):
       print("send message " + TelloMessage + " end ")
       msg = TelloMessage.encode(encoding="utf-8")
       sent = self.sock.sendto(msg,self.tello_address)
       data, server = self.sock.recvfrom(1518)
       print(data.decode(encoding="utf-8")) 
       return "from sendmessage " + TelloMessage + " end "

    def printinfo(self):
        print("Hallo Drone at : " + self.TelloIp)

    def connect(self):
        print ("Connect")
        result = self.sendMessage("command")
        print(result)

    def takeOff(self):
        print("takeoff")
        result = self.sendMessage(" takeoff")

    def land(self):
        print("land")
        result = self.sendMessage(" land")

    def end(self):
        print("end")
        self.sock.close()

    def cw(self,x):
        print("cw")
        result = self.sendMessage(" cw "+x)

    def ccw(self,X):
        print("ccw")
        result = self.sendMessage(" ccw "+ X)

    def battery(self):
        result = self.sendMessage(" battery?")
        return result

    def up(self, x):
        print("up")
        result = self.sendMessage("up " + x)

    def forward(self, x):
        print("forward")
        if (x > 20 and x < 500):
            result = self.sendMessage("forward " + x)
        else:
            print("cm has to be between 20-500")