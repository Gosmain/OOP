import random
from configs import cat_config


class Cat(object):

  def __init__(self,
               age,
               breed,
               owner='Unknown',
               name='Unknown',
               satieti=cat_config.START_SATIETI):
    self.name = name
    self.age = age
    self.breed = breed
    self.owner = owner
    self.satieti = satieti

  def is_alive(self):
    return self.satieti

  def eat(self):
    self.satieti = min(cat_config.MAX_SATIETI,
                       self.satieti + cat_config.EAT_SATIETI_STEP)

  def sleep(self):
    self.satieti = max(cat_config.MIN_SATIETI,
                       self.satieti - cat_config.SLEEP_SATIETI_STEP)

  def walk(self):
    self.satieti = max(cat_config.MIN_SATIETI,
                       self.satieti - cat_config.WALK_SATIETI_STEP)

  def look_out_the_window(self):
    self.satieti = max(
      cat_config.MIN_SATIETI,
      self.satieti - cat_config.LOOK_OUT_THE_WINDOW_SATIETI_STEP)

  def __str__(self):
    if self.is_alive():
      return f'{self.name} - {self.age}\nСытость - {self.satieti}'
    else:
      return f'{self.name} умер от голода'

  def action(self, selected_action):
    action_dict = {
      1: self.eat,
      2: self.sleep,
      3: self.walk,
      4: self.look_out_the_window
    }
    return action_dict[selected_action]()

  def live_circle(self):
    if self.satieti <= cat_config.LIVE_MIN_SATIETI:
      self.eat()
    else:
      self.action(random.randint(1, 4))
