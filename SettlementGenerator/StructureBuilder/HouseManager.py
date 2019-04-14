from Classes import Base
from Classes import Blueprint

def getHouseBlueprint(point, prop):
	blockRegister = []
	base = Base(prop.xStart, prop.zStart, prop.xLength, prop.zLength)
	return Blueprint(point, blockRegister, prop.height, base, True)