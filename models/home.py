from models.fridge import Fridge

class Home(object):

  def __init__(self, owner, fridge='Холодильник'):
    self.owner = owner
    self.fridge = Fridge()
    

  
    