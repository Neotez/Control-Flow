from turn import turn
from forward import forward_untill_edge_found,forward_upto_distance


# code main algorithm
CUSTOM_DIST = 10
commands = [forward_untill_edge_found(),turn(90),forward_upto_distance(dist=CUSTOM_DIST),turn(90),forward_untill_edge_found(),turn(-90),forward_upto_distance(dist=CUSTOM_DIST),turn(-90)]

for i in range(2):
	for command in commands:
		command()

