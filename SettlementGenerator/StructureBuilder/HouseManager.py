from Classes import Base
from Classes import Blueprint

def getHouseBlueprint(point, prop):
	blockRegister = []
	base = Base(point.x, point.z, prop.xLength, prop.zLength)
	blueprint = Blueprint(point, blockRegister, prop.height + 5, base, True)
	addFloor(point, prop, blueprint)
	return blueprint

def addFloor(point, prop, blueprint):
	for x in range(1, prop.xLength - 1):
		for z in range(1, prop.zLength - 1):
			blueprint.blockRegister.append({'type': 'oak_wood_planks', 'direction': None, 'verticalAllignment': None, 'id': 5, 'data': 0, 'x': x, 'y': 1, 'z': z})
