#make imports
from inclination import getYZangle
from gpiozero import Robot
from time import sleep
from detect_edge import close_edge
import RPi.GPIO as GPIO

ENPIN = 23
Kp = 0.1
MAX = 180

robot = Robot(left = (17,27), right = (23,22))

class turn:
	def __init__(self,deg=90):
		self.deg = deg
		

	def setuppwm(self):
		global pwm
		#GPIO.setmode(GPIO.BOARD)
		GPIO.setup(ENPIN, GPIO.OUT)
		GPIO.output(ENPIN, GPIO.LOW)
		pwm = GPIO.PWM(ENPIN, 1000)
		pwm.start(0)
        
	def pulseWM(self,p):
		if(p>MAX):
			pwm.ChangeDutyCycle(100)
		else:
			pwm.ChangeDutyCycle(p/MAX*100)
        
	def __call__(self):
		ang = getYZangle()
		exp_ang = ang + self.deg
		error = (exp_ang - ang)
		print(error)
		while(abs(error)>1):
			if(error > 0):
				print("RIGHT TURN")
				#robot.right(0.5)
			else:
				print("LEFT TURN")
				#robot.left(0.5)
			ang = getYZangle()
			error = (exp_ang - ang)
			print(f"Angle: {ang} -- EXP: {exp_ang}")

if __name__ == '__main__':
	#check if working
	command = turn(-90)
	command()
