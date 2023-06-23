from models.fridge import Fridge
from configs import home_config


class Home(object):

  def __init__(self, owner):
    self.owner = owner
    self.fridge = Fridge()
    self.cat_food = home_config.START_CAT_FOOD

  def __str__(self):
    return self.owner.name
