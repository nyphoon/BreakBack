import math

def reverse( vector ):
	return (-vector[0], -vector[1])

def vertical( vector ):
	return (-vector[1], vector[0])

def distance(a, b):
	return math.sqrt( (a[0]-b[0])**2 + (a[1]-b[1])**2)