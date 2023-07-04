from models.food import ManFood, CatFood


class Fridge(object):

  def __init__(self):
    self.man_food = ManFood()
    self.cat_food = CatFood()

  def __str__(self):
    return f'Еда - {self.man_food.value}\nКошачья еда - {self.cat_food.value}'
