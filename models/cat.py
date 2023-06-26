import random
from configs import cat_config


class Cat(object):

  def __init__(self,
               owner,
               name,
               breed='Unknown',
               satieti=cat_config.START_SATIETI):
    self.name = name
    self.owner = owner
    self.satieti = satieti
    self.breed = breed

  def __str__(self):
    if self.is_alive():
      return f'{self.name}. Сытость - {self.satieti}. Порода - {self.breed}.'
    else:
      self.owner.cat = ''
      return f'{self.name} умер от голода'

  def is_alive(self):
    return self.satieti

  def eat(self):
    if self.owner.home.cat_food >= 20:
      self.owner.home.cat_food -= 20
      self.satieti = min(cat_config.MAX_SATIETI,
                       self.satieti + cat_config.EAT_SATIETI_STEP)
    else:
      self.satieti = max(cat_config.MIN_SATIETI,
                       self.satieti - cat_config.STEP_HUNGER)

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

  def action(self, selected_action):
    action_dict = {
      1: self.eat,
      2: self.sleep,
      3: self.walk,
      4: self.look_out_the_window
    }
    return action_dict[selected_action]()

  def live(self):
    if self.satieti <= cat_config.LIVE_MIN_SATIETI:
      self.eat()
    else:
      self.action(random.randint(1, 4))

  # def lived_day(self, day):
  #   if day % 365 == 0:
  #     self.age += cat_config.GROW_STEP

  def live_circle(self):
    if self.is_alive():
      self.live()
      