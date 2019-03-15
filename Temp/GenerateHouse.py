import utilityFunctions as utilityFunctions

def perform(level, box, options):
	floorPlans = [
		[
			[0, 0, 0, 0, 0],
			[0, 1, 1, 1, 0],
			[0, 1, 1, 1, 0],
			[0, 1, 1, 1, 0],
			[0, 0, 0, 0, 0]
		]
	]
	house = House(box.minx, box.minz, box.miny, 4, floorPlans)
	house.build()

class House:
	beamBlock = (17,0)
	constructionPlans = []

	def __init__(self, xStart, zStart, baseHeight, floorHeight, floorPlans = []):
		self.xStart = xStart
		self.zStart = zStart
		self.baseHeight = baseHeight
		self.floorHeight = floorHeight
		self.floorPlans = floorPlans
	
	def createConstructionPlans(self):
		for floor in self.floorPlans:
			constructionFloor = []
			for line in floor:
				constructionFloorLine = []
				for block in line:
					if (block == 0):
						constructionFloorLine.append({"outside", ""})
					else:
						constructionFloorLine.append({"inside", ""})
				constructionFloor.append(constructionFloorLine)
			self.constructionPlans.append(constructionFloor)
	
	def build(self):
		print('yo')