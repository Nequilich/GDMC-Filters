import math

from Classes import Surface
from Common import setBlock
from SurfaceManager import calculateHeightMapAdv

def perform(level, box, options):
	surface = Surface(box.minx, box.minz, box.maxx, box.maxz)
	calculateHeightMapAdv(level, surface)

	xStart = 2
	zStart = 2
	xEnd = surface.xLength - 3
	zEnd = surface.zLength - 3
	x = xStart
	z = zStart
	y = 90
	
	xChange = 1
	if xStart > xEnd:
		xChange = -1
	zChange = 1
	if zStart > zEnd:
		zChange = -1

	angle1 = math.atan2(zEnd - z, xEnd - x)
	angle2 = math.pi
	angleDif = math.pi - abs(abs(angle1 - angle2) - math.pi)
	print("a1: " + str(angle1) + ", a2: " + str(angle2) + ", dif: " + str(angleDif))

	#while x != xEnd and z != zEnd:
	#	angle = math.atan2(zEnd - z, xEnd - x)
	#setBlock(level, surface, xEnd, y, zEnd, 57)