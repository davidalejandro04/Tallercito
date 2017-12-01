import RPi.GPIO as GPIO
from time import sleep
import numpy as np
import math

GPIO.setmode(GPIO.BOARD)

Motor2A = 35
Motor2B = 37

Motor1A = 29
Motor1B = 31

GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor2A,GPIO.OUT)
GPIO.setup(Motor2B,GPIO.OUT)

pwm=GPIO.PWM(29,40)
pwm2=GPIO.PWM(35,100)

pwm3=GPIO.PWM(35,40)
pwm4=GPIO.PWM(37,100)

pwm.start(100)
pwm2.start(100)

pwm3.start(100)
pwm4.start(100)

def Forward(v1,v2):
  
  pwm.ChangeFrequency(v1*.5)
  pwm2.ChangeFrequency(v2*.5)

  GPIO.output(Motor1A,GPIO.HIGH)
  GPIO.output(Motor1B,GPIO.LOW)

  GPIO.output(Motor2A,GPIO.HIGH)
  GPIO.output(Motor2B,GPIO.LOW)

  sleep(2)

 
  return 


def Backward(v1,v2):

  pwm3.ChangeFrequency(v1*.5)
  pwm4.ChangeFrequency(v2*.5)

  GPIO.output(Motor1A,GPIO.LOW)
  GPIO.output(Motor1B,GPIO.HIGH)

  GPIO.output(Motor2A,GPIO.LOW)
  GPIO.output(Motor2B,GPIO.HIGH)

  sleep(2)

  return 

pwm.stop()
pwm2.stop()
pwm3.stop()
pwm4.stop()

Forward(100,100)
Backward(100,100)

GPIO.cleanup()


