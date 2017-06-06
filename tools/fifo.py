import socket,serial

ser=serial.Serial("/dev/tnt0",115200)

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect(("10.208.20.42",9090))


print "Connect /dev/tnt1 and hit RETURN..."
raw_input()

while 1:
  rx=s.recv(200)
  print rx,
  ser.write(rx)

