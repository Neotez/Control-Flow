#make imports
from inclination import getXZangle,getYZangle,getBothAngles,SLOPE

class turn:
	def __init__(self,deg=90):
		self.deg = deg
	
	def __call__(self):
		# code here
		# counter clockwise -> +ve
		print(f"turn {self.deg} -> {getXZangle()},{getYZangle()} -> slope = {SLOPE}")




if __name__ == '__main__':
	#check if working
	command = turn(90)
	command()
