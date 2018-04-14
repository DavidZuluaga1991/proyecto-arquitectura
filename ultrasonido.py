# HC-SR04 Ultrasound Sensor
import time
from machine import Pin

# WeMos D4 maps GPIO2 machine.Pin(4) = TRIGGER
# WeMos D2 maps GPIO4 machine.Pin(3) = ECHO
triggerPort = 4
echoPort = 3

def loop():
    trigger = Pin(triggerPort, Pin.OUT)
    echo = Pin(echoPort, Pin.IN)
    print("Ultrasonic Sensor. Trigger Pin=%d and Echo Pin=%d" % (triggerPort, echoPort))
    trigger.value(not trigger.value())
    while True:
      # short impulse 10 microsec to trigger
      trigger.value(not trigger.value())
      time.sleep_us(10)
      trigger.value(not trigger.value())
      count = 0
      start = time.ticks_us() # get time in usec
      # Now loop until echo goes high
      while not echo.value():
          time.sleep_us(10)
          count += 1
          if count > 100:
              print("Counter exceeded")
              break
      duration = time.ticks_diff(start, time.ticks_us()) # compute time difference
      print("Duration: %f" % duration)

      # After 38ms is out of range of the sensor
      if duration > 38000 :
          print("Out of range")
          continue

      # distance is speed of sound [340.29 m/s = 0.034029 cm/us] per half duration
      distance = 0.017015 * duration
      print("Distance: %f cm" % distance)
      time.sleep(2)