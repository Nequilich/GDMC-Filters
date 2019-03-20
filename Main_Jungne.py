from Common import setBlock
from Classes import Surface
from SurfaceManager import calculateHeightMapAdv
from BridgeBuilder import buildBridge
from BiomeFinder import findBiomes

inputs = (
    ("Width", 4),
    ("Material", ("Oak","Cobblestone", "Birch")),
    ("Creator: Jungne Losang", "label")
)

oakMaterial = {
    "normal": (17, 0),
    "upper slab": (126, 8),
    "lower slab": (126, 0),
    "fence": 85.0,
    "torch": 50
}

cobblestoneMaterial = {
    "normal": (4, 0),
    "upper slab": (44, 11),
    "lower slab": (44, 3),
    "fence": 139,
    "torch": 50
}

birchMaterial = {
    "normal": (17, 2),
    "upper slab": (126, 10),
    "lower slab": (126, 2),
    "fence": 189,
    "torch": 50
}

def perform(level, box, options):
    # BridgeBuilder
    bridgeWidth = options["Width"]

    surface = Surface(box.minx, box.minz, box.maxx, box.maxz)
    calculateHeightMapAdv(level, surface)
    startPoint = (box.minx, box.minz)
    endPoint = (box.maxx-1, box.maxz-1)
    bridgeY = surface.surfaceMap[0][0].height + 1  #+1 to raise above the surface

    chosenMaterial = options["Material"]
    if (chosenMaterial == "Oak"):
      materials = oakMaterial
    elif (chosenMaterial == "Cobblestone"):
      materials = cobblestoneMaterial
    elif (chosenMaterial == "Birch"):
      materials = birchMaterial
    else:
      materials = oakMaterial

    buildBridge(level, startPoint, endPoint, bridgeY, bridgeWidth, materials)

    # BiomeFinder
    # biomes = findBiomes(level, box)

    

