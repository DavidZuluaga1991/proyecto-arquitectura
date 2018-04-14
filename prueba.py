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

def toggle(p):
    p.value(not p.value())


import network

ap = network.WLAN(network.AP_IF)
ap.config(essid="ESP-AP", password="12345678")
wlan.connect('ESP-AP', '12345678')
ap.active(True)