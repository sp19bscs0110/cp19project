# -*- coding: utf-8 -*-
"""project.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VPcovdmmpBwoMw5PfwCioZQjEuCKSshZ
"""

print("Name:Shahmeer ")
print("Section:BM")
print("ID:sp19-bsse-0007")
#codeimagetransfer


#!/usr/bin/env python
# coding: utf-8

# In[ ]:

#Shahmeer
#Sp19bsse0007

import socket
s= socket.socket()
host=input(str("Please ener the host address of the sender :"))
port = 8080
s.connect((host,port))
print("connected...")
filename = input(str("Please enter a filename for the incoming file: "))
file = open(filename,'wb')
file_data = s.recv(1024)
file.write(file_data)
file.close()
print("Fle has been recieve succesfully.")
