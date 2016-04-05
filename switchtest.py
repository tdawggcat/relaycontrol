#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

Sensor1SwitchPin = 5
Sensor2SwitchPin = 6

GPIO.setup(Sensor1SwitchPin, GPIO.OUT)
GPIO.output(Sensor1SwitchPin, GPIO.LOW)
time.sleep(5)
GPIO.output(Sensor1SwitchPin, GPIO.HIGH)
time.sleep(1)

GPIO.setup(Sensor2SwitchPin, GPIO.OUT)
GPIO.output(Sensor2SwitchPin, GPIO.LOW)
time.sleep(5)
GPIO.output(Sensor2SwitchPin, GPIO.HIGH)
time.sleep(1)


GPIO.cleanup()
