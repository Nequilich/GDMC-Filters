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

	def __init__(self, x1, z1, x2, z2):
		self.x1 = x1
		self.z1 = z1
		self.x2 = x2
		self.z2 = z2