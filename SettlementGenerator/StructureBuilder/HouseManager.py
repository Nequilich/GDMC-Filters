from Classes import Base
from Classes import Blueprint

def getHouseBlueprint(point, prop):
	blockRegister = []
	base = Base(point.x, point.z, prop.xLength, prop.zLength)
	blueprint = Blueprint(point, blockRegister, prop.height + 5, base, True)
	addFloor(point, prop, blueprint)
	addWall(point, prop, blueprint)
	return blueprint

def addFloor(point, prop, blueprint):
	for x in range(1, prop.xLength - 1):
		for z in range(1, prop.zLength - 1):
			blueprint.blockRegister.append({'type': 'oak_wood_planks', 'direction': None, 'verticalAllignment': None, 'id': 5, 'data': 0, 'x': x, 'y': 1, 'z': z})

def addWall(point, prop, blueprint):
	# North and south walls
	for x in range(2, prop.xLength - 2, 2):
		blueprint.blockRegister.append({'type': 'stone_brick', 'direction': None, 'verticalAllignment': None, 'id': 5, 'data': 0, 'x': x, 'y': 2, 'z': 1})
		blueprint.blockRegister.append({'type': 'stone_brick', 'direction': None, 'verticalAllignment': None, 'id': 5, 'data': 0, 'x': prop.xLength - 1 - x, 'y': 2, 'z': prop.zLength - 2})
		if x == prop.xLength - 4:
			blueprint.blockRegister.append({'type': 'stone_brick', 'direction': None, 'verticalAllignment': None, 'id': 5, 'data': 0, 'x': x + 1, 'y': 2, 'z': 1})
			blueprint.blockRegister.append({'type': 'stone_brick', 'direction': None, 'verticalAllignment': None, 'id': 5, 'data': 0, 'x': prop.xLength - 2 - x, 'y': 2, 'z': prop.zLength - 2})
	# North and south windows
	for x in range(3, prop.xLength - 3, 2):
		blueprint.blockRegister.append({'type': 'brick', 'direction': None, 'verticalAllignment': None, 'id': 5, 'data': 0, 'x': x, 'y': 2, 'z': 1})
		blueprint.blockRegister.append({'type': 'brick', 'direction': None, 'verticalAllignment': None, 'id': 5, 'data': 0, 'x': prop.xLength - 1 - x, 'y': 2, 'z': prop.zLength - 2})
	# East and west walls
	for z in range(2, prop.zLength - 2, 2):
		blueprint.blockRegister.append({'type': 'stone_brick', 'direction': None, 'verticalAllignment': None, 'id': 5, 'data': 0, 'x': 1, 'y': 2, 'z': z})
		blueprint.blockRegister.append({'type': 'stone_brick', 'direction': None, 'verticalAllignment': None, 'id': 5, 'data': 0, 'x': prop.xLength - 2, 'y': 2, 'z': prop.zLength - 1 - z})
		if z == prop.zLength - 4:
			blueprint.blockRegister.append({'type': 'stone_brick', 'direction': None, 'verticalAllignment': None, 'id': 5, 'data': 0, 'x': 1, 'y': 2, 'z': z + 1})
			blueprint.blockRegister.append({'type': 'stone_brick', 'direction': None, 'verticalAllignment': None, 'id': 5, 'data': 0, 'x': prop.xLength - 2, 'y': 2, 'z': prop.zLength - 2 - z})
	# East and west windows
	for z in range(3, prop.zLength - 3, 2):
		blueprint.blockRegister.append({'type': 'brick', 'direction': None, 'verticalAllignment': None, 'id': 5, 'data': 0, 'x': 1, 'y': 2, 'z': z})
		blueprint.blockRegister.append({'type': 'brick', 'direction': None, 'verticalAllignment': None, 'id': 5, 'data': 0, 'x': prop.xLength - 2, 'y': 2, 'z': prop.zLength - 1 - z})
	# Corners
	blueprint.blockRegister.append({'type': 'oak_wood', 'direction': None, 'verticalAllignment': None, 'id': 5, 'data': 0, 'x': 1, 'y': 2, 'z': 1})
	blueprint.blockRegister.append({'type': 'oak_wood', 'direction': None, 'verticalAllignment': None, 'id': 5, 'data': 0, 'x': prop.xLength - 2, 'y': 2, 'z': 1})
	blueprint.blockRegister.append({'type': 'oak_wood', 'direction': None, 'verticalAllignment': None, 'id': 5, 'data': 0, 'x': 1, 'y': 2, 'z': prop.zLength - 2})
	blueprint.blockRegister.append({'type': 'oak_wood', 'direction': None, 'verticalAllignment': None, 'id': 5, 'data': 0, 'x': prop.xLength - 2, 'y': 2, 'z': prop.zLength - 2})