import socket
import os

def print_values(s1,s2):
	os.system("clear")
	print(s1)
	print(s2)

def update (s, s1,s2):
	#print(s)
	if "ESP8266_1" in s:
		s1 = s
	else:
		s2 = s
	return s1,s2

s1=""
s2=""

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("0.0.0.0", 6660))

while True:
	data, addr = s.recvfrom(1024) # buffer size is 1024 bytes
	s1,s2 = update(data.decode("utf-8").strip().rstrip() , s1, s2)
	print_values(s1,s2)