import RPi.GPIO as GPIO
from time import sleep
import numpy as np
import math

GPIO.setmode(GPIO.BOARD)

Motor2A = 35
Motor2B = 37

Motor1A = 29
Motor1B = 31

v1=100
v2=40

GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor2A,GPIO.OUT)
GPIO.setup(Motor2B,GPIO.OUT)

pwm=GPIO.PWM(29,v1)
pwm2=GPIO.PWM(35,v2)



pwm.start(100)
pwm2.start(100)


def Forward(v1,v2):
  pwm.ChangeFrequency(v1*.5)
  pwm2.ChangeFrequency(v2*.5)

  GPIO.output(Motor1A,GPIO.HIGH)
  GPIO.output(Motor1B,GPIO.LOW)

  GPIO.output(Motor2A,GPIO.HIGH)
  GPIO.output(Motor2B,GPIO.LOW)

  sleep(2)

 
  return 


def Forward(v1,v2):

  pwm.ChangeDutyCycle(v1*.5)
  pwm2.ChangeDutyCycle(v2*.5)

  GPIO.output(Motor1A,GPIO.LOW)
  GPIO.output(Motor1B,GPIO.HIGH)

  GPIO.output(Motor2A,GPIO.LOW)
  GPIO.output(Motor2B,GPIO.HIGH)

  sleep(2)

  return 

pwm.stop()
pwm2.stop()

GPIO.cleanup()


