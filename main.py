from time import sleep
from socket import socket
try:
    s =socket()
    s.bind(('127.0.0.1', 1231))
    s.listen(1)
    d =a.accept()
except: ...

while True:
    sleep(10)
