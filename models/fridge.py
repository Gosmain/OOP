from configs import fridge_config


class Fridge(object):

  def __init__(self):
    self.man_food = fridge_config.START_MAN_FOOD
    self.cat_food = fridge_config.START_CAT_FOOD

  def __str__(self):
    return f'Еда - {self.man_food}\nКошачья еда - {self.cat_food}'
