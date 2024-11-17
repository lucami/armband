import time
import machine
import network
import socket

port_dest = 6660
addr_dest = '192.168.1.3'
dest = (addr_dest, port_dest)

f=open("ID","r")
id = f.read(32)
f.close()

s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

led = machine.Pin(2, machine.Pin.OUT)

i=0

while 1:
    if led.value():
        led.off()
    else:
        led.on()
    
    
    s.sendto(str(i)+" "+id+"\n",dest)
    i+=1
    time.sleep(1)

