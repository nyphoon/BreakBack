import math

# vector calculation
def reverse( vector ):
	return (-vector[0], -vector[1])

def vertical( vector ):
	return (-vector[1], vector[0])

def length( vector ):
	return math.sqrt( vector[0]**2 + vector[1]**2 )

def unit( vector ):
	l = length( vector )
	if (l == 0):
		return ( 0, 0 )
	return  ( vector[0]/l, vector[1]/l )

def dot( u, v ):
	return u[0]*v[1]+u[1]*v[0]

# point calculation
# a to b
def vector(a, b):
	return ( b[0]-a[0], b[1]-a[1] )

def distance(a, b):
	return math.sqrt( (a[0]-b[0])**2 + (a[1]-b[1])**2)
