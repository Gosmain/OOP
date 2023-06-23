from configs import fridge_config


class Fridge(object):

  def __init__(self,
               man_food=fridge_config.START_MAN_FOOD,
               cat_food=fridge_config.START_CAT_FOOD):
    self.man_food = man_food
    self.cat_food = cat_food
