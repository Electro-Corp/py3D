import pygame
import wireframe
import numpy as np

class ProView:
  """Display 3d obj's in pygame!"""
  def __init__(self,width,height,title):
    self.width = width
    self.height = height
    self.screen = pygame.display.set_mode((width,height))
    pygame.display.set_caption(title)
    self.background = (10,10,50)
    self.title = title
    self.wireframes = {}
    self.displayNodes = True
    self.displayEdges = True
    self.nodeColor = (255,255,255)
    self.edgeColor = (200,200,200)
    self.nodeRadius = 4
  def run(self):
    key_to_function = {
      pygame.K_LEFT:   (lambda x: x.translateAll('x', -10)),
      pygame.K_RIGHT:  (lambda x: x.translateAll('x',  10)),
      pygame.K_DOWN:   (lambda x: x.translateAll('y',  10)),
      pygame.K_UP:     (lambda x: x.translateAll('y', -10)),
      pygame.K_SPACE:  (lambda x: x.translateAll('z', 10)),
      pygame.K_b: (lambda x: x.translateAll('z', -10)),
      pygame.K_EQUALS: (lambda x: x.scaleAll(1.25)),
      pygame.K_MINUS:  (lambda x: x.scaleAll( 0.8)),
      pygame.K_q: (lambda x: x.rotateAll('X',  0.1)),
      pygame.K_w: (lambda x: x.rotateAll('X', -0.1)),
      pygame.K_a: (lambda x: x.rotateAll('Y',  0.1)),
      pygame.K_s: (lambda x: x.rotateAll('Y', -0.1)),
      pygame.K_z: (lambda x: x.rotateAll('Z',  0.1)),
      pygame.K_x: (lambda x: x.rotateAll('Z', -0.1))
    }
    """Create window"""
    running = True
    automove = 0
    while running:
      if automove == 1:
        
        self.rotateAll('Z',-0.001)
        self.rotateAll('Y',-0.001)
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False
        elif event.type == pygame.KEYDOWN:
          if event.key in key_to_function:
            key_to_function[event.key](self)
            print(event.key)
        elif event.type == pygame.MOUSEBUTTONDOWN:
          
            
          (mouseX, mouseY) = pygame.mouse.get_pos()
          self.rotateAll('Z',mouseY-mouseX)
          self.rotateAll('Y',mouseY)
          self.rotateAll('X',mouseX)
      self.screen.fill(self.background)
      self.display()
      pygame.display.flip()
  def addWireFrame(self,name,wireframe):
    """Add wireframe."""
    self.wireframes[name] = wireframe
  
  def display(self):
    """Draw wireframe"""
    self.screen.fill(self.background)
    for wireframe in self.wireframes.values():
      if self.displayEdges:
        for edge in wireframe.edges:
          pygame.draw.aaline(self.screen, self.edgeColor, (edge.start.x,edge.start.y),(edge.stop.x, edge.stop.y), 1)
      if self.displayNodes:
        for node in wireframe.nodes:
          pygame.draw.circle(self.screen,self.nodeColor,(int(node.x),int(node.y)),self.nodeRadius,0)

  def translateAll(self,axis,d):
    """translate all wireframe along axis by d unit"""
    for wireframe in self.wireframes.itervalues():
      wireframe.translate(axis,d)

  def scaleAll(self,scale):
    """Same as last execpt scaling"""
    centerX = self.width/2
    centerY = self.height/2
    for wireframe in self.wireframes.itervalues():
      wireframe.scale((centerX,centerY),scale)
  def rotateAll(self,axis,theta):
    """same as last except rotation"""
    rotateFunction = 'rotate' + axis
    for wireframe in self.wireframes.itervalues():
      center = wireframe.findCenter()
      getattr(wireframe,rotateFunction)(center,theta)
      
      
if __name__ == '__main__':
  cube = wireframe.Wireframe()
  cube_nodes = []
  #file = "teapot.obj"
  #cube.read_obj()
  
  cube.addNodes(cube_nodes)
  cube.addNodes([(x ,y, z) for x in (50, 250) for y in (50, 250) for z in (50, 250)])

  cube.addEdges([(n,n+4) for n in range(0,4)]+[(n,n+1) for n in range(0,8,2)]+[(n,n+2) for n in (0,1,4,5)])

  
  pv = ProView(400,300,"wireframe test")
  pv.addWireFrame('cube',cube)
  pv.run()
  