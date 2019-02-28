def getRectangle(surface, xFirst, zFirst, heightRange):
	rec = Rectangle(xFirst, zFirst, xFirst + 1, zFirst + 1)
	height = surface.surface[xFirst][zFirst].height
	continueUp = True
	continueRight = True
	continueDown = True
	continueLeft = True
	while(continueUp or continueRight or continueDown or continueLeft):
		if (continueUp):
			for x in range(rec.xStart, rec.xEnd):
				if (surface.surface[x][rec.zEnd].height < height or surface.surface[x][rec.zEnd].height > height - 1 + heightRange):
					continueUp = False
			if (continueUp):
				rec.zEnd += 1
				if (rec.zEnd == surface.zLength):
					continueUp = False
		if (continueRight):
			for z in range(rec.zStart, rec.zEnd):
				if (surface.surface[rec.xEnd][z].height < height or surface.surface[rec.xEnd][z].height > height - 1 + heightRange):
					continueRight = False
			if (continueRight):
				rec.xEnd += 1
				if (rec.xEnd == surface.xLength):
					continueRight = False
		if (continueDown):
			for x in range(rec.xStart, rec.xEnd):
				if (surface.surface[x][rec.zStart - 1].height < height or surface.surface[x][rec.zStart - 1].height > height - 1 + heightRange):
					continueDown = False
			if (continueDown):
				rec.zStart -= 1
				if (rec.zStart == 0):
					continueDown = False
		if (continueLeft):
			for z in range(rec.zStart, rec.zEnd):
				if (surface.surface[rec.xStart - 1][z].height < height or surface.surface[rec.xStart - 1][z].height > height - 1 + heightRange):
					continueLeft = False
			if (continueLeft):
				rec.xStart -= 1
				if (rec.xStart == 0):
					continueLeft = False
	return rec

class Rectangle:

	def __init__(self, xStart, zStart, xEnd, zEnd):
		self.xStart = xStart
		self.zStart = zStart
		self.xEnd = xEnd
		self.zEnd = zEnd