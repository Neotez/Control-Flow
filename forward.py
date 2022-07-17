#make import
from detect_edge import close_edge
from gpiozero import Robot
from time import sleep
import RPi.GPIO as GPIO

robot = Robot(left = (17,27), right = (23,22))

class forward_untill_edge_found:
	def __init__(self,speed=255):
		self.speed = speed
		
		
	def __call__(self):
		#code here
		while !close_edge():
			robot.forward(1)
		
		
		


class forward_upto_distance:
	def __init__(self,speed=255,dist=10):
		self.speed = speed
		self.dist = dist
		
		
	def __call__(self):
		#code here
		robot.forward(0.5)
		if(!close_edge):
			robot.forward(0.5)
		



if __name__ == '__main__':
	#check if working
	command1 = forward_untill_edge_found(speed=100)
	command1()
	
	command2 = forward_upto_distance(speed=100,dist=10)
	command2()
