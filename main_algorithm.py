from turn import turn
from forward import forward_untill_edge_found,forward_upto_distance
from inclination import getXZangle,getYZangle,getTwoAngles,SLOPE
from detect_edge import close_edge

# code main algorithm
CUSTOM_DIST = 10

frwd = forward_untill_edge_found()
frwd2 = forward_upto_distance(dist=10)
right = turn(90)
left = turn(-90)


frwd()
right()
	
	
