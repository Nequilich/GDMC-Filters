from Classes import Surface
from Common import setBlock
from SurfaceManager import calculateHeightMapAdv
from SurfaceManager import calculateSectionMid
from SurfaceManager import calculateSections
from SurfaceManager import calculateSteepnessMap
from SurfaceManager import calculateWaterPlacement

def perform(level, box, options):
	surface = Surface(box.minx, box.minz, box.maxx, box.maxz)
	calculateHeightMapAdv(level, surface)
	calculateSteepnessMap(surface)
	calculateWaterPlacement(level, surface)

	sections = calculateSections(surface, 1, 15)
	calculateSectionMids(surface, sections)
	
	smallLandSections = []
	mediumLandSections = []
	bigLandSections = []
	waterSections = []

	arrangeSections(sections, waterSections, bigLandSections, mediumLandSections, smallLandSections)

	paintSections(level, surface, smallLandSections, mediumLandSections, bigLandSections, waterSections)

def calculateSectionMids(surface, sections):
	for section in sections:
		calculateSectionMid(surface, section)

def arrangeSections(sections, waterSections, bigLandSections, mediumLandSections, smallLandSections):
	for section in sections:
		if section.layerDepth < 2:
			continue
		if section.isWater:
			waterSections.append(section)
			continue
		if len(section.points) < 250:
			smallLandSections.append(section)
			continue
		if len(section.points) < 1000:
			mediumLandSections.append(section)
			continue
		bigLandSections.append(section)

def paintSections(level, surface, smallLandSections, mediumLandSections, bigLandSections, waterSections):
	for x in range(surface.xLength):
		for z in range(surface.zLength):
			setBlock(level, surface, x, 250, z, 35, 15)

	for s in smallLandSections:
		for p in s.points:
			setBlock(level, surface, p.x, 250, p.z, 35, 5)

	for s in mediumLandSections:
		for p in s.points:
			setBlock(level, surface, p.x, 250, p.z, 2)

	for s in bigLandSections:
		for p in s.points:
			setBlock(level, surface, p.x, 250, p.z, 35, 13)

	for s in waterSections:
		for p in s.points:
			setBlock(level, surface, p.x, 250, p.z, 35, 11)