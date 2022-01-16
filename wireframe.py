import math
import os as o


import numpy

import matplotlib
class Node:
  def __init__(self,coordinates):
    self.x = coordinates[0]
    self.y = coordinates[1]
    self.z = coordinates[2]

class Edge:
  def __init__(self,start,stop):
    self.start = start
    self.stop = stop

class Wireframe:
  def __init__(self):
    self.nodes = []
    self.edges = []

  def addNodes(self,nodeList):
    for nodes in nodeList:
      self.nodes.append(Node(nodes))

  def addEdges(self, edgelist):
    for (start,stop) in edgelist:
      self.edges.append(Edge(self.nodes[start],self.nodes[stop]))

  def translate(self,axis, d):
    """translation"""
    if axis in ['x','y','z']:
      for node in self.nodes:
        setattr(node,axis,getattr(node,axis)+d)
  def scale(self,(centerX,centerY),scale):
    """Scaling"""
    for node in self.nodes:
      node.x = centerX+scale*(node.x-centerX)
      node.y = centerY+scale*(node.y-centerY)
      node.z *=scale
  def findCenter(self):
    """find center"""
    num_nodes = len(self.nodes)
    meanX = sum([node.x for node in self.nodes])/num_nodes
    meanY = sum([node.y for node in self.nodes])/num_nodes
    meanZ = sum([node.z for node in self.nodes])/num_nodes
    return (meanX,meanY,meanZ)
  def rotateX(self, (cx,cy,cz), radians):
    for node in self.nodes:
        y      = node.y - cy
        z      = node.z - cz
        d      = math.hypot(y, z)
        theta  = math.atan2(y, z) + radians
        node.z = cz + d * math.cos(theta)
        node.y = cy + d * math.sin(theta)
  def rotateY(self, (cx,cy,cz), radians):
    for node in self.nodes:
        x      = node.x - cx
        z      = node.z - cz
        d      = math.hypot(x, z)
        theta  = math.atan2(x, z) + radians
        node.z = cz + d * math.cos(theta)
        node.x = cx + d * math.sin(theta)
  def rotateZ(self,(cx,cy,cz),radians):
    for node in self.nodes:
      x = node.x-cx
      y = node.y-cy
      z = node.z-cz
      d = math.hypot(y,x)
      theta = math.atan2(y,x) + radians
      node.x = cx+d*math.cos(theta)
      node.y = cy+d*math.sin(theta)
  # def readObj(self, file):
  #   try:
      
  #     File_object = open(r"teapot.obj", "r")
  #     for line in File_object:
  #       File_object.readline()
        
  #     cube_nodes = [x,y,z]
  #   except OSError:
  #     print("File not found.")
  #   finally:
  #     print("Read finished with or without errors.")
  # def read_obj(in_file):
  #   vertices = []
  #   faces = []
  #   in_file = open("teapot.obj")
  #   try:
  #     line = 0
  #     for k, v in in_file.readline(line+1):
  #         if k == 'v':
  #             cube_nodes.append(v)
  #         elif k == 'f':
  #             for i in v:
                
  #               cube.addEdges(i)
  #         else:
            
  #           print("epic loser fail.")
  #         line += 1
        
  #   except:
  #     print("fail.")
    # if not len(faces) or not len(vertices):
    #     return None

    # pos = torch.tensor(vertices, dtype=torch.float)
    # face = torch.tensor(faces, dtype=torch.long).t().contiguous()

    # data = Data(pos=pos, face=face)

    
  #debug func
  def outputnode(self):
    print"\n ----Nodes-----"
    for i,node in enumerate(self.nodes):
      print " %d: (%.2f, %.2f, %.2f)" % (i, node.x, node.y, node.z)
  def outputEdges(self):
    print "\n --- Edges --- "
    for i, edge in enumerate(self.edges):
        print " %d: (%.2f, %.2f, %.2f)" % (i, edge.start.x, edge.start.y, edge.start.z),
        print "to (%.2f, %.2f, %.2f)" % (edge.stop.x,  edge.stop.y,  edge.stop.z)





#cube
if __name__ == "__main__":
  cube_nodes = []
  Wireframe.read_Obj("teapot.obj")
  cube = Wireframe()
  cube.addNodes(cube_nodes)
  # cube.addEdges([(n,n+4) for n in range(0,4)])
  # cube.addEdges([(n,n+1) for n in range(0,8,2)])
  # cube.addEdges([(n,n+2) for n in (0,1,4,5)])
    
  # cube.outputNodes()
  # cube.outputEdges()

