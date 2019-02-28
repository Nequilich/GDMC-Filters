def getArea(surface, x, z):
	area = Area(x, z, x + 1, z + 1)
	canContinueUp = True
	canContinueRight = True
	canContinueDown = True
	canContinueLeft = True
	while(canContinueUp or canContinueRight or canContinueDown or canContinueLeft):
		if (canContinueUp):
			print("do stuff")
		if (canContinueRight):
			print("do stuff")
		if (canContinueDown):
			print("do stuff")
		if (canContinueLeft):
			print("do stuff")
	return area

class Area:

	def __init__(self, xStart, zStart, xEnd, zEnd):
		self.xStart = xStart
		self.zStart = zStart
		self.xEnd = xEnd
		self.zEnd = zEnd