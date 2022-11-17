#make imports
from inclination import getXZangle,getYZangle,getTwoAngles,SLOPE
from gpiozero import Robot
from time import sleep
import RPi.GPIO as GPIO

ENPIN = 23

robot = Robot(left = (17,27), right = (23,22))

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
def turn_left(ang):
	exp_ang = ang - 90
	error = abs(exp_ang - ang)
	while(error>1):
		robot.left(0.5)
		ang = getYZangle()
		error = abs(exp_ang - ang)
		print("Turning left, Angle: ", ang)

def turn_right(ang):
	exp_ang = ang + 90
	error = abs(exp_ang - ang)
	print(error)
	while(error>1):
		robot.right(0.5)
		ang = getYZangle()
		error = abs(exp_ang - ang)
		print("Turning right, Angle: ", ang)
	
	
def rotate():
	# code here
	#self.setuppwm()
	
	while(1):# comes here only when edge detected,also to be done before going forward
		slope = getYZangle()
		print("Slope: ", slope)		
		if(slope>=85 and slope<=95):
			turn_right(slope)
			sleep(1)
			robot.forward(1)
			print("Robot is moving forward")
			slope = getYZangle()
			sleep(1)
			turn_right(slope)
			break
			
		elif(slope>=265 and slope<=275):
			turn_left(slope)
			sleep(1)
			robot.forward(1)
			print("Robot is moving forward")
			slope = getYZangle()
			sleep(1)
			turn_left(slope)
			break
			
		sleep(1)
		
	# counter clockwise -> +ve
	#print(f"turn {self.deg} -> {getXZangle()},{getYZangle()} -> slope = {SLOPE}")

if __name__ == '__main__':
	#check if working
	rotate()


