import random

from configs import food_config


class Food(object):

  def __init__(self):
    self.value = food_config.START_FOOD

  def __str__(self):
    return f'Количество еды {self.value}.'

  def get_chance_spoil(self):
    return random.randint(1, 10) <= food_config.SPOIL_FOOD_CHANCE

  def spoil(self):
    if self.get_chance_spoil():
      self.value = max(food_config.MIN_FOOD_VALUE,
                       self.value - food_config.SPOIL_FOOD_STEP)

      print('Еда испортилась')


class ManFood(Food):

  def __init__(self):
    super().__init__()


class CatFood(Food):

  def __init__(self):
    super().__init__()
