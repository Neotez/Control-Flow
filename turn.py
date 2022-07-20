#make imports
from inclination import getYZangle
from gpiozero import Robot
from time import sleep
from detect_edge import close_edge
import RPi.GPIO as GPIO

ENPINL = 18
ENPINR = 12
Kp = 0.8
Kd = 0.8
Ki = 0.8
MAX = 180

robot = Robot(right = (27,17), left = (22,23))

class turn:
	def __init__(self,deg=90):
		self.deg = deg
		self.pwml = None
		self.pwmr = None
		#GPIO.setmode(GPIO.BOARD)
		GPIO.setup(ENPINL, GPIO.OUT)
		GPIO.output(ENPINL, GPIO.LOW)
		GPIO.setup(ENPINR, GPIO.OUT)
		GPIO.output(ENPINR, GPIO.LOW)
		self.pwml = GPIO.PWM(ENPINL, 1000)
		self.pwml.start(0)
		self.pwmr = GPIO.PWM(ENPINR, 1000)
		self.pwmr.start(0)


	'''def setuppwm(self):
		self.pwm = None
		#GPIO.setmode(GPIO.BOARD)
		GPIO.setup(ENPIN, GPIO.OUT)
		GPIO.output(ENPIN, GPIO.LOW)
		self.pwm = GPIO.PWM(ENPIN, 1000)
		self.pwm.start(0)'''
		
	def pulsePWM(self,p):
		if((p/MAX)<1):
			self.pwml.ChangeDutyCycle((p/MAX)*100)
			self.pwmr.ChangeDutyCycle((p/MAX)*100)
		else:
			self.pwml.ChangeDutyCycle(100)
			self.pwmr.ChangeDutyCycle(100)
		
	def __call__(self):
		ang = getYZangle()
		exp_ang = ang + self.deg
		error = (exp_ang - ang)
		i = 0
		d = 0
		print(error)
		while(1):
			delta = abs(error)
			p = delta
			i += delta 
			d = delta-d
			logic = Kp*p+Ki*i+Kd*d
			tme = 0.5
			#if(delta < 30):
			#	tme = (0.5 * (delta/30))
			if(delta<0.01):
				#sleep(2)
				robot.stop()
				#print("\n Yeah baby, error is low\n") 
			elif(error > 0):
				self.pulsePWM(logic)
				print(f"RIGHT TURN -> {logic}") 
				robot.right()
			else:
				print(f"LEFT TURN -> {logic}")
				self.pulsePWM(logic)
				robot.left()
			ang = getYZangle()
			error = (exp_ang - ang)
			print(f"Angle: {ang} -- EXP: {exp_ang} -- Error: {error}")
			#sleep(3)
		'''while(1):
			for i in range(0,50,10):
				self.pwml.ChangeDutyCycle(i)
				self.pwmr.ChangeDutyCycle(i)
				robot.forward()
				sleep(1)
			print("PWM Working!")
			for i in range(50,-1,-10):
				self.pwml.ChangeDutyCycle(i)
				self.pwmr.ChangeDutyCycle(i)
				robot.forward()
				sleep(1)
			print("PWM Working!")'''

if __name__ == '__main__':
	#check if working
	inp = int(input())
	while inp != 0:
		#break
		command = turn(inp)
		command()
		inp = 0
	print("WORKING")
