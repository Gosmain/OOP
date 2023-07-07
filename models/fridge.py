from models.food import ManFood, CatFood
from configs import fridge_config

class Fridge(object):

  def __init__(self):
    self.man_food = ManFood()
    self.cat_food = CatFood()

  def __str__(self):
    return f'Еда - {self.man_food.value}\nКошачья еда - {self.cat_food.value}'

  def free_place(self):
    return fridge_config.FRIDGE_CAPACITY - self.man_food.value

