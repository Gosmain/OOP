import random
from faker import Faker

from configs import man_config
from models.pet_shop import PetShop


class Man:

  def __init__(self, name, age):
    self.name = name
    self.age = age
    self.satieti = man_config.START_SATIETI
    self.home = None
    self.money = man_config.START_MONEY
    self.happiness = man_config.START_HAPPINES
    self.cat = None
    self.spouse = None

  def __str__(self):
    if self.is_alive():
      return f'{self.name} - {self.age}\nСчастье - {self.happiness}\nСытость - {self.satieti}\nДеньги - {self.money}\n{self.home.fridge}\nЕда в кормушке - {self.home.cat_food}\n'
    else:
      return f'{self.name} умер {self.couse_of_dead()}'

  def __add__(self, other):
    self.home.add_tenant(other)
    self.spouse = other
    other.spouse = self
    self.up_top_overall(other.money)
    

  def is_alive(self):
    return self.satieti > 0 and self.happiness > 0

  def is_married(self):
    return self.spouse != None

  def eat(self):
    self.satieti = min(man_config.MAX_SATIETI,
                       self.satieti + man_config.SATIETI_STEP_EAT)
    self.happiness = min(man_config.MAX_HAPPINES,
                         self.happiness + man_config.HAPPINES_STEP_EAT)
    self.home.fridge.man_food.value -= man_config.FOOD_STEP_EAT
    print(f'{self.name} поел.\n')

  def sleep(self):
    self.happiness = min(man_config.MAX_HAPPINES,
                         self.happiness + man_config.HAPPINES_STEP_SLEEP)
    self.satieti = max(man_config.MIN_SATIETI,
                       self.satieti - man_config.SATIETI_STEP_SLEEP)
    print(f'{self.name} поспал.\n')

  def go_to_work(self):
    self.money += man_config.MONEY_STEP_WORK
    if self.is_married():
      self.spouse.money = self.money
    self.happiness = max(man_config.MIN_HAPPINES,
                         self.happiness - man_config.HAPPINES_STEP_WORK)
    print(f'{self.name} сходил на работу.\n')

  def play_computer_games(self):
    self.happiness = min(man_config.MAX_HAPPINES,
                         self.happiness + man_config.HAPPINES_STEP_PLAY)
    self.satieti = max(man_config.MIN_SATIETI,
                       self.satieti - man_config.SATIETI_STEP_PLAY)
    print(f'{self.name} поиграл в компьютерные игры.\n')

  def go_to_store(self):
    self.home.fridge.cat_food.value += man_config.CAT_FOOD_STEP_STORE * len(
      self.remember_living_cats())
    self.home.fridge.man_food.value += man_config.MAN_FOOD_STEP_STORE
    self.satieti = max(man_config.MIN_SATIETI,
                       self.satieti - man_config.SATIETI_STEP_STORE)
    self.happiness = max(man_config.MIN_HAPPINES,
                         self.happiness - man_config.HAPPINES_STEP_STORE)
    self.money -= man_config.MAN_FOOD_COST + man_config.CAT_FOOD_COST * len(
      self.remember_living_cats())
    if self.is_married():
      self.spouse.money = self.money
    print(f'{self.name} сходил в магазин.\n')

  def action(self, selected_action):
    action_dict = {
      1: self.eat,
      2: self.sleep,
      3: self.go_to_work,
      4: self.play_computer_games,
      5: self.go_to_store
    }
    return action_dict[selected_action]()

  def couse_of_dead(self):
    if self.satieti == self.happiness:
      return 'от грусти и от голода. R.I.P.'
    elif self.happiness:
      return 'от голода. R.I.P.'
    else:
      return 'от грусти. R.I.P.'

  # def lived_day(self, day):
  #   if day % 365 == 0:
  #     self.age += man_config.GROW_STEP
  #     self.happiness = min(man_config.MAX_HAPPINES,
  #                          self.happiness + man_config.HAPPINES_STEP_GROW_UP)

  def choose_cat_name(self):
    return Faker('ru_RU').first_name()

  def buy_cat(self, name):
    self.cat = PetShop.sell()(name)
    self.cat.owner = self
    self.home.add_tenant(self.cat)
    self.home.fridge.cat_food.value += man_config.CAT_FOOD_STEP_STORE
    self.remember_living_cats().append(self.cat)
    self.happiness = min(man_config.MAX_HAPPINES,
                         self.happiness + man_config.HAPPINES_STEP_BUY_CAT)
    self.money -= man_config.CAT_COST
    if self.is_married():
      self.spouse.money = self.money
    print(f'{self.name} купил кота.')

  def take_cat(self, cat):
    self.cat = cat
    self.home = cat.home
    self.remember_living_cats().append(cat)

  def remember_living_cats(self, cat_list=[]):
    return cat_list

  def remember_dead_cats(self, cat_list=[]):
    return cat_list

  def bury_cat(self):
    for cat in self.remember_living_cats():
      if not cat.is_alive():
        item = self.remember_living_cats().pop(
          self.remember_living_cats().index(cat))
        self.remember_dead_cats().append(item)
        self.happiness = max(
          man_config.MIN_HAPPINES,
          self.happiness - man_config.HAPPINES_STEP_BURY_CAT)
        self.home.tenants['коты'].remove(cat)

  def fill_cat_bowl(self):
    self.happiness = min(man_config.MAX_HAPPINES,
                         self.happiness + man_config.HAPPINES_STEP_FEED_CAT)
    self.satieti = max(man_config.MIN_SATIETI,
                       self.satieti - man_config.SATIETI_STEP_FEED_CAT)
    self.home.cat_food += man_config.FOOD_STEP_FEED_CAT * len(
      self.remember_living_cats())
    self.home.fridge.cat_food.value -= man_config.FOOD_STEP_FEED_CAT * len(
      self.remember_living_cats())
    print(f'{self.name} наполнил кошачью миску.\n')

  def move_to_new_house(self, house):
    self.home = house
    self.home.tenants['люди'].append(self)
    for cat in self.remember_living_cats():
      cat.home = self.home
      self.home.tenants['коты'].append(cat)
    self.home.change_owner(self)

  def remove_home(self):
    self.home = None
    self.home.tenants['люди'].remove(self)
    for cat in self.remember_living_cats():
      cat.home = self.home
      self.home.tenants['коты'].remove(cat)

  def live(self):
    if self.happiness <= man_config.LIVE_MIN_HAPPINES:
      self.play_computer_games()

    elif self.satieti <= man_config.LIVE_MIN_SATIETI:
      if self.home.fridge.man_food.value >= man_config.LIVE_EAT_FOOD:
        self.eat()
      else:
        if self.money >= man_config.LIVE_EAT_MONEY:
          self.go_to_store()
        else:
          self.go_to_work()

    elif self.money <= man_config.LIVE_MIN_MONEY + man_config.LIVE_MIN_MONEY_CAT * len(
        self.remember_living_cats()):
      self.go_to_work()

    elif self.home.fridge.man_food.value + self.home.fridge.cat_food.value <= man_config.FRIDGE_CAPACITY:
      self.go_to_store()

    elif self.home.cat_food <= man_config.LIVE_MIN_HOME_CAT_FOOD * len(
        self.remember_living_cats()) and len(self.remember_living_cats(
        )) > 0 and self.home.fridge.cat_food.value > len(
          self.remember_living_cats()) * 20:
      if self.home.fridge.cat_food.value < 20 * len(
          self.remember_living_cats()):
        self.go_to_store()
      else:
        self.fill_cat_bowl()

    elif self.money >= man_config.MONEY_FOR_BUY_CAT:
      self.buy_cat(self.choose_cat_name())

    else:
      self.action(random.randint(1, 4))

    self.bury_cat()

  def up_top_overall(self, how_many):
    self.money += how_many
    self.spouse.money += how_many

  def down_top_overall(self, how_many):
    self.money -= how_many
    self.spouse.money -= how_many

  def live_circle(self):
    if self.is_alive():
      # self.lived_day(day)
      self.live()


class Wife(Man):

  def __init__(self, name, age):
    super().__init__(name, age)

  def action(self, selected_action):
    action_dict = {
      1: self.eat,
      2: self.sleep,
      3: self.play_computer_games,
      4: self.go_to_store
    }
    return action_dict[selected_action]()
    

  def live(self):
    
    if self.happiness <= man_config.LIVE_MIN_HAPPINES:
      self.play_computer_games()

    elif self.satieti <= man_config.LIVE_MIN_SATIETI and self.home.fridge.man_food.value >= 20:
      self.eat()

    elif self.money >= man_config.LIVE_MIN_MONEY and self.home.fridge.man_food.value + self.home.fridge.cat_food.value <= man_config.FRIDGE_CAPACITY:
          self.go_to_store()

    elif len(self.remember_living_cats()) > 0 and self.home.fridge.cat_food.value >= 20 * len(self.remember_living_cats()) and self.home.cat_food < man_config.LIVE_MIN_HOME_CAT_FOOD*len(self.remember_living_cats()):
      self.fill_cat_bowl()      

    elif self.money >= man_config.MONEY_FOR_BUY_CAT:
      self.buy_cat(self.choose_cat_name())

    else:
      self.action(random.randint(1, 3))

    self.bury_cat()

    
    
