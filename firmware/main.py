import time
import machine
import network
import socket
import neopixel

port_dest = 6660
addr_dest = '192.168.1.14'
dest = (addr_dest, port_dest)
np = neopixel.NeoPixel(machine.Pin(0, machine.Pin.OUT), 1) 
f=open("ID","r")
id = f.read(32)
f.close()
s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
led = machine.Pin(2, machine.Pin.OUT)
i=0

while 1:
    #print(f"i: {i}")
    if led.value():
        led.off()
    else:
        led.on()

    if i%7 == 0:
        np[0] = (255, 0, 0) #Rosso
    elif i%7 == 1:
        np[0] = (0, 255, 0) #Verde
    elif i%7 == 2:
        np[0] = (0, 0, 255) #Blue
    elif i%7 == 3:
        np[0] = (0, 255, 255) #Ciano
    elif i%7 == 4:
        np[0] = (255, 255, 255) #Bianco
    elif i%7 == 5:
        np[0] = (255, 255,0) #Giallo
    elif i%7 == 6:
        np[0] = (255, 0,255) #Magenta

    np.write()
    s.sendto(str(i)+" "+id+"\n",dest)
    i+=1
    time.sleep(1)

