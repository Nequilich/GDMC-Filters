

def spawnVillager(level, box):
    x = box.minx
    z = box.minz


    chunk = level.getChunk(x / 16, z / 16)
    chunk.Entities.append(villager)
    chunk.TileEntities.remove(chest)
    chunk.dirty = True