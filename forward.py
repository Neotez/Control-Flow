#make import
from detect_edge import close_edge

class forward_untill_edge_found:
	def __init__(self,speed=255):
		self.speed = speed
		
		
	def __call__(self):
		#code here
		print(f"FORWARD UNTILL EDGE speed = {self.speed}")
		


class forward_upto_distance:
	def __init__(self,speed=255,dist=10):
		self.speed = speed
		self.dist = dist
		
		
	def __call__(self):
		#code here
		print(f"FORWARD UPTO dist {self.dist} speed = {self.speed}")
		



if __name__ == '__main__':
	#check if working
	command1 = forward_untill_edge_found(speed=100)
	command1()
	
	command2 = forward_upto_distance(speed=100,dist=10)
	command2()
