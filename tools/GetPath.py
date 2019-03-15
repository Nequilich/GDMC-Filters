import heapq
import math
import sys

def getPath(surface, xStart, zStart, xEnd, zEnd):
  return getAStarPath(surface, xStart, zStart, xEnd, zEnd)

def getAStarPath(surface, xSource, zSource, xTarget, zTarget):
  openSet = []
  nodes = []
  for _ in range(surface.xLength):
    row = []
    for _ in range(surface.zLength):
      row.append(None)
    nodes.append(row)

  targetNode = Node(surface, xTarget, zTarget, None)

  sourceNode = Node(surface, xSource, zSource, targetNode)
  sourceNode.gScore = 0
  sourceNode.fScore = sourceNode.hScore

  nodes[sourceNode.x][sourceNode.z] = sourceNode
  nodes[targetNode.x][targetNode.z] = targetNode

  heapq.heappush(openSet, (sourceNode.fScore, sourceNode))

  while openSet:
    #currentNode = extractMin(openSet)
    currentNode = heapq.heappop(openSet)[1]
    currentNode.isOpen = False
    currentNode.isClosed = True
    
    if currentNode == targetNode:
      return reconstructPath(currentNode)

    for neighbourNode in getNeighbourNodes(surface, currentNode, nodes, targetNode):
      if neighbourNode.isClosed:
        continue
      tentativeGSCore = currentNode.gScore + getStepCost(surface, currentNode, neighbourNode)
      if (tentativeGSCore >= neighbourNode.gScore):
        continue
      neighbourNode.gScore = tentativeGSCore
      neighbourNode.fScore = tentativeGSCore + neighbourNode.hScore
      neighbourNode.cameFrom = currentNode
      if not neighbourNode.isOpen:
        neighbourNode.isOpen = True
        heapq.heappush(openSet, (neighbourNode.fScore, neighbourNode))
      else:
        neighbourNodeIndex = getIndex(openSet, neighbourNode)
        openSet[neighbourNodeIndex] = (neighbourNode.fScore, neighbourNode)
        heapq.heapify(openSet)
  return []

def extractMin(openSet):
  minElements = [heapq.heappop(openSet)]
  fScore = minElements[0][1].fScore
  while openSet and openSet[0][0] == fScore:
    minElements.append(heapq.heappop(openSet))
  minElement = minElements[0]
  minElementIndex = 0
  for i, e in enumerate(minElements):
    if e[1].hScore < minElement[1].hScore:
      minElementIndex = i
  minElements.pop(minElementIndex)
  for e in minElements:
    heapq.heappush(openSet, e)
  return minElement[1]

def getIndex(openSet, neighbourNode):
  for i, element in enumerate(openSet):
    if element[1] == neighbourNode:
      return i

def getNeighbourNodes(surface, node, nodes, targetNode):
  neighbourNodes = []
  for x in range(node.x - 1, node.x + 2):
    if x < 0 or x >= surface.xLength:
      continue
    for z in range(node.z - 1, node.z + 2):
      if z < 0 or z >= surface.zLength:
        continue
      if x == node.x and z == node.z:
        continue
      if nodes[x][z] == None:
        nodes[x][z] = Node(surface, x, z, targetNode)
      neighbourNodes.append(nodes[x][z])
  return neighbourNodes

def reconstructPath(node):
  path = [] # TODO: use Point class
  currentNode = node
  path.insert(0, currentNode)
  while currentNode.cameFrom != None:
    currentNode = currentNode.cameFrom
    path.insert(0, currentNode)
  return path

def getSimpleHeuristicCostEstimate(surface, node, targetNode):
  heightCost = 40
  xLength = abs(targetNode.x - node.x)
  zLength = abs(targetNode.z - node.z)
  yLength = abs(targetNode.y - node.y)
  longHorizontalLength = max(xLength, zLength)
  shortHorizontalLength = min(xLength, zLength)
  minimumDistance = shortHorizontalLength * 14 + (longHorizontalLength - shortHorizontalLength) * 10
  cost = minimumDistance + yLength * heightCost
  return cost

def getStepCost(surface, node, neighbourNode):
  heightCost = 40
  waterCost = 40
  isWater = 0
  if surface.surfaceMap[neighbourNode.x][neighbourNode.z].isWater:
    isWater = 1
  xLength = abs(neighbourNode.x - node.x)
  zLength = abs(neighbourNode.z - node.z)
  yLength = abs(neighbourNode.y - node.y)
  if xLength + zLength == 2:
    return 14 + yLength * heightCost + isWater * waterCost # Diagonal step
  return 10 + yLength * heightCost + isWater * waterCost # Normal step

class Node:

  def __init__(self, surface, x, z, targetNode):
    self.x = x
    self.y = surface.surfaceMap[x][z].height
    self.z = z
    self.gScore = sys.maxint
    self.fScore = sys.maxint
    self.cameFrom = None
    self.isOpen = False
    self.isClosed = False
    if targetNode == None:
      self.hScore = 0
    else:
      self.hScore = getSimpleHeuristicCostEstimate(surface, self, targetNode)
  
  def __eq__(self, node):
    if not node:
      return False
    return self.x == node.x and self.z == node.z