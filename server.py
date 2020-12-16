#!/usr/bin/env python
#print("test")
#exit()

import socket
import time
sock=socket.socket()
sock.bind(('192.168.137.39',8080))
sock.listen(5)
while True:
	conn,addr=sock.accept()
	data=conn.recv(8096)
	t=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
	str_t=str(t)
	print(str_t)
	a=bytes(str_t,'utf-8')
	conn.send(a)
	conn.close()

