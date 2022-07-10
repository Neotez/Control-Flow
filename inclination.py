#make imports
import time
from math import atan2, degrees
import board
import adafruit_mpu6050

i2c = board.I2C()  # uses board.SCL and board.SDA
sensor = adafruit_mpu6050.MPU6050(i2c)


def vector_2_degrees(x, y):
    angle = degrees(atan2(y, x))
    if angle < 0:
        angle += 360
    return angle



def get_inclination(_sensor):
    x, y, z = _sensor.acceleration
    return vector_2_degrees(x, z), vector_2_degrees(y, z)



SLOPE = 30

#return X-Z angle
def getXZangle():
	return get_inclination(sensor)[0]

#return Y-Z angle	
def getYZangle():
	return get_inclination(sensor)[1]

#return (X-Y,Y-Z)
def getBothAngles():
	return get_inclination(sensor)
	
if __name__ == '__main__':
	#check if working
	while True:
		angle_xz, angle_yz = get_inclination(sensor)
		print("XZ angle = {:6.2f}deg   YZ angle = {:6.2f}deg".format(angle_xz, angle_yz))
		time.sleep(0.2)
