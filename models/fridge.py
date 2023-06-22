from configs import fridge_config

class Fridge(object):

  def __init__(self, food=fridge_config.START_FOOD):
    self.food = food

  
  