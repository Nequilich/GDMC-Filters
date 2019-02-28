def getRectangle(surface, xFirst, zFirst):
	rec = Rectangle(xFirst, zFirst, xFirst + 1, zFirst + 1)
	height = surface.surface[xFirst][zFirst].height
	continueUp = True
	continueRight = True
	continueDown = True
	continueLeft = True
	while(continueUp or continueRight or continueDown or continueLeft):
		if (continueUp):
			for x in range(rec.xStart, rec.xEnd):
				if (surface.surface[x][rec.zEnd].height != height):
					continueUp = False
			if (continueUp):
				rec.zEnd += 1
		if (continueRight):
			print("do stuff")
			continueRight = False
		if (continueDown):
			print("do stuff")
			continueDown = False
		if (continueLeft):
			print("do stuff")
			continueLeft = False
	return rec

class Rectangle:

	def __init__(self, xStart, zStart, xEnd, zEnd):
		self.xStart = xStart
		self.zStart = zStart
		self.xEnd = xEnd
		self.zEnd = zEnd