import numpy as np
import qrcode 
import os
import time

#OS
base_dir = os.path.dirname(os.path.abspath(__file__))
path_qr = os.path.join(base_dir,'qrcode.png')

'''
name = input('what is your name ?')
password = input('what is your password ?')
'''

name = "bariscan"
password = "ceken"

list_name = list(name)
list_password = list(password)
list_ascii_name = []
list_ascii_password = []
ascii1 = ""
ascii2 = ""
ascii3 = ""

for i in list_name:
    list_ascii_name.append(ord(i))
    ascii1 = ascii1 + f"{ord(i)}"

for i in list_password:
    list_ascii_password.append(ord(i))
    ascii2 = ascii2 + f"{ord(i)}"

ascii3 = ascii1 + ascii2

np.random.seed(int(ascii3) % (2**32))

x = 100

random_array = np.random.rand(100)

for i in range(1,100):
    value = random_array[-i]
    data_str = str(value) + " bombardino crocodilo" + " lirili larila" + " tralalero tralala" + " nazlicano vicdansizo" 
    qr = qrcode.make(data_str)
    qr.save(path_qr)
    time.sleep(3)
