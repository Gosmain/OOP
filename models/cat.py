import random
from configs import cat_config


class Cat(object):

  def __init__(self,
               owner,
               name,
               home=None,
               breed='Unknown',
               satieti=cat_config.START_SATIETI):
    self.name = name
    self.owner = owner
    self.satieti = satieti
    self.breed = breed
    self.home = home

  def __str__(self):
    if self.is_alive():
      return f'{self.name}. Сытость - {self.satieti}. Порода - {self.breed}.'
    else:
      self.owner.cat = ''
      return f'{self.name} умер от голода'

  def is_alive(self):
    return self.satieti

  def eat(self):
    if self.owner.home.cat_food >= cat_config.MIN_EAT_HOME_CAT_FOOD:
      self.owner.home.cat_food -= cat_config.STEP_EAT_FOOD
      self.satieti = min(cat_config.MAX_SATIETI,
                         self.satieti + cat_config.EAT_SATIETI_STEP)
      print(f'{self.name} поел.')
    else:
      self.satieti = max(cat_config.MIN_SATIETI,
                         self.satieti - cat_config.STEP_HUNGER)
      print(f'{self.name} голодает.')

  def steal_food(self):
    if random.randint(1, 10) <= cat_config.STEAL_CHANCE:
      self.owner.home.fridge.man_food -= cat_config.STEAL_FOOD_STEP_FOOD
      self.satieti += min(cat_config.MAX_SATIETI,
                          self.satieti + cat_config.STEAL_FOOD_STEP_SATIETI)
      print(f'{self.name} стащил еду.')
    else:
      print(f'{self.name} попытался стащить еду, но потелпел неудачу.')
      self.satieti = max(
        cat_config.MIN_SATIETI,
        self.satieti - cat_config.STEAL_FOOD_STEP_SATIETI_UNLUCK)

  def sleep(self):
    self.satieti = max(cat_config.MIN_SATIETI,
                       self.satieti - cat_config.SLEEP_SATIETI_STEP)
    print(f'{self.name} поспал.')

  def walk(self):
    self.satieti = max(cat_config.MIN_SATIETI,
                       self.satieti - cat_config.WALK_SATIETI_STEP)
    print(f'{self.name} погулял.')

  def look_out_the_window(self):
    self.satieti = max(
      cat_config.MIN_SATIETI,
      self.satieti - cat_config.LOOK_OUT_THE_WINDOW_SATIETI_STEP)
    print(f'{self.name} смотрел в окно.')

  def action(self, selected_action):
    action_dict = {
      1: self.eat,
      2: self.sleep,
      3: self.walk,
      4: self.look_out_the_window,
      5: self.steal_food
    }
    return action_dict[selected_action]()

  def live(self):
    if self.satieti <= cat_config.LIVE_MIN_SATIETI:
      if self.owner.home.cat_food >= 20:
        self.eat()
      else:
        self.steal_food()
    else:
      self.action(random.randint(2, 4))

  # def lived_day(self, day):
  #   if day % 365 == 0:
  #     self.age += cat_config.GROW_STEP

  def live_circle(self):
    if self.is_alive():
      self.live()


class RussianBlueCat(Cat):

  def __init__(self,
               owner,
               name,
               breed='русская голубая',
               satieti=cat_config.START_SATIETI):
    Cat.__init__(self,
                 owner,
                 name,
                 breed='Unknown',
                 satieti=cat_config.START_SATIETI)
    self.breed = breed


class ScotishCat(Cat):

  def __init__(self,
               owner,
               name,
               breed='шотландская',
               satieti=cat_config.START_SATIETI):
    Cat.__init__(self,
                 owner,
                 name,
                 breed='Unknown',
                 satieti=cat_config.START_SATIETI)
    self.breed = breed


class SphinxCat(Cat):

  def __init__(self,
               owner,
               name,
               breed='сфинкс',
               satieti=cat_config.START_SATIETI):
    Cat.__init__(self,
                 owner,
                 name,
                 breed='Unknown',
                 satieti=cat_config.START_SATIETI)
    self.breed = breed
