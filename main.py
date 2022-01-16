import pygame
import wireframe

class ProView:
  """Display 3d obj's in pygame!"""
  def __init__(self,width,height):
    self.width = width
    self.height = height
    self.screen = pygame.display.set_mode((width,height))
    pygame.display.set_caption("Wireframe")
    self.background = (10,10,50)

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
      pygame.K_EQUALS: (lambda x: x.scaleAll(1.25)),
      pygame.K_MINUS:  (lambda x: x.scaleAll( 0.8))
    }
    """Create window"""
    running = True
    while running:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False
        elif event.type == pygame.KEYDOWN:
          if event.key in key_to_function:
            key_to_function[event.key](self)
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
      
      
      
if __name__ == '__main__':
  cube = wireframe.Wireframe()
  cube.addNodes([(x ,y, z) for x in (50, 250) for y in (50, 250) for z in (50, 250)])

  cube.addEdges([(n,n+4) for n in range(0,4)]+[(n,n+1) for n in range(0,8,2)]+[(n,n+2) for n in (0,1,4,5)])
  
  pv = ProView(400,300)
  pv.addWireFrame('cube',cube)
  pv.run()
  