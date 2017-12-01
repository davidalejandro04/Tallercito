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

pwm.start(100)
pwm2.start(100)


class Signal(object):
    """docstring for Interrupt"""
    def __init__(self, pinA , pinB):
        self.pinA      = pinA
        self.pinB      = pinB
        self.gpio      = pigpio.pi()
        self.perimetro = 40*m.pi
        self.cuenta    = 0
        self.estado    = 0
        self.tiempo_actual = 0 
        self.tiempo_anterior = time.time()
        self.velocidad = 0

        self.interrupcionA  = self.gpio.callback(self.pinA, edge = pigpio.FALLING_EDGE ,func = self.guia)
        self.interrupcionB = self.gpio.callback(self.pinB, edge = pigpio.EITHER_EDGE , func = self.referencia)


    def guia(self,a,b,c):
        self.tiempo_actual = time.time()
        if self.estado:
            self.cuenta += 1

        if not self.estado:
            self.cuenta -= 1

        tiempo = self.tiempo_actual-self.tiempo_anterior
        self.tiempo_anterior  = self.tiempo_actual
        self.velocidad = (self.perimetro/1000)/tiempo
        print "cuenta en %s" % self.cuenta    

    def referencia(self,a,b,c):
        if int(self.gpio.read(self.pinB)):
            self.estado = 1

        if not int(self.gpio.read(self.pinB)):
            self.estado = 0              





class PID:
	"""
	Discrete PID control
	"""

	def __init__(self, P=2.0, I=0.0, D=1.0, Derivator=0, Integrator=0, Integrator_max=500, Integrator_min=-500):

		self.Kp=P
		self.Ki=I
		self.Kd=D
		self.Derivator=Derivator
		self.Integrator=Integrator
		self.Integrator_max=Integrator_max
		self.Integrator_min=Integrator_min

		self.set_point=0.0
		self.error=0.0

	def update(self,current_value):
		"""
		Calculate PID output value for given reference input and feedback
		"""

		self.error = self.set_point - current_value

		self.P_value = self.Kp * self.error
		self.D_value = self.Kd * ( self.error - self.Derivator)
		self.Derivator = self.error

		self.Integrator = self.Integrator + self.error

		if self.Integrator > self.Integrator_max:
			self.Integrator = self.Integrator_max
		elif self.Integrator < self.Integrator_min:
			self.Integrator = self.Integrator_min

		self.I_value = self.Integrator * self.Ki

		PID = self.P_value + self.I_value + self.D_value

		return PID

	def setPoint(self,set_point):
		"""
		Initilize the setpoint of PID
		"""
		self.set_point = set_point
		self.Integrator=0
		self.Derivator=0

	def setIntegrator(self, Integrator):
		self.Integrator = Integrator

	def setDerivator(self, Derivator):
		self.Derivator = Derivator

	def setKp(self,P):
		self.Kp=P

	def setKi(self,I):
		self.Ki=I

	def setKd(self,D):
		self.Kd=D

	def getPoint(self):
		return self.set_point

	def getError(self):
		return self.error

	def getIntegrator(self):
		return self.Integrator

	def getDerivator(self):
		return self.Derivator


def forward(v1,v2):
  
  pwm.ChangeDutyCycle(v1)
  pwm2.ChangeDutyCycle(v2)

  GPIO.output(Motor1A,GPIO.HIGH)
  GPIO.output(Motor1B,GPIO.LOW)

  GPIO.output(Motor2A,GPIO.HIGH)
  GPIO.output(Motor2B,GPIO.LOW)

  sleep(1)

 
  return 

forward(100,100)
forward(100,10)
forward(10,100)

pwm.stop()
pwm2.stop()

GPIO.cleanup()



