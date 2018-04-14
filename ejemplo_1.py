#encender Leds
import machine
pin = machine.Pin(2, machine.Pin.OUT)
pin2 = machine.Pin(14, machine.Pin.OUT)
#pin.on()
#pin.off()
def toggle(p):
    p.value(not p.value())


import time
while True:
    toggle(pin)
toggle(pin2)
time.sleep_ms(500)

import os
os.listdir()
os.mkdir('main.py')
os.remove('main.py')
with open("boot.py", "r") as f:
    print(f.read())
with open("main.py", "w") as f:
    f.write("""import network
               ap = network.WLAN(network.AP_IF)
               ap.config(essid="ESP-AP", password="12345678")
               ap.active(True)""")
#ingresar a la red
import network
sta_if = network.WLAN(network.STA_IF)
ap_if = network.WLAN(network.AP_IF)
sta_if.active()
ap_if.active()
ap_if.ifconfig()

#Wiffi
sta_if.active(True)
sta_if.connect('Wifi-zm', '00010701872Dz')
sta_if.isconnected()
sta_if.ifconfig()
ap_if.active(False)
#COnectadose al Wffi por medio de un solo metodo.
def do_connect():
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
    sta_if.active(True)
    sta_if.connect('Wifi-zm', '00010701872Dz')
    while not sta_if.isconnected():
        pass
print('network config:', sta_if.ifconfig())

#Sockets
import socket
addr_info = socket.getaddrinfo("towel.blinkenlights.nl", 23)
addr = addr_info[0][-1]
s = socket.socket()
s.connect(addr)
while True:
    data = s.recv(500)
    print(str(data, 'utf8'), end='')

#HTTP GET request
def http_get(url):
    import socket
    _, _, host, path = url.split('/', 3)
    addr = socket.getaddrinfo(host, 80)[0][-1]
    s = socket.socket()
    s.connect(addr)
    s.send(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (path, host), 'utf8'))
    while True:
        data = s.recv(100)
        if data:
            print(str(data, 'utf8'), end='')
        else:
            break
    s.close()

http_get('http://micropython.org/ks/test.html')