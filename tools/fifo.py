import socket,serial
import sys

if len(sys.argv)>1:
  ttyport=sys.argv[1]
else:
  ttyport="/dev/ttyUSB1"

ser=serial.Serial(ttyport,115200)

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect(("10.208.20.42",9090))


print "Connect /dev/ttyUSB0/x and hit RETURN..."
raw_input()

while 1:
  rx=s.recv(200)
  print rx,
  ser.write(rx)

