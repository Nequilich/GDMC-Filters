def findBiomes(level, surface):
	for x in range(surface.xStart, surface.xEnd):
		for z in range(surface.zStart, surface.zEnd):
			chunk = level.getChunk(x / 16, z / 16)
			chunkBiomeData = chunk.root_tag["Level"]["Biomes"].value
			surface.surfaceMap[x - surface.xStart][z - surface.zStart].biomeId = chunkBiomeData[(x % 16) * 16 + z % 16]