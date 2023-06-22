from models.fridge import Fridge

class Home(object):

  def __init__(self, owner):
    self.owner = owner
    self.fridge = Fridge()
    

  
    