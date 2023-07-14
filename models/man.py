import random

from configs import man_config
from models.pet_shop import PetShop


class Man:

  def __init__(self, name, age):
    self.name = name
    self.age = age
    self.satieti = man_config.START_SATIETI
    self.money = man_config.START_MONEY
    self.happiness = man_config.START_HAPPINES
    self.cats = {
      'живые': [],
      'мертвые': []
    }
    self.home = None
    self.spouse = None

  def __str__(self):
    if self.is_alive():
      return (
        f'{self.name} - {self.age}\nСчастье - {self.happiness}\n'
        f'Сытость - {self.satieti}\nДеньги - {self.money}\n'
        f'{self.home.fridge}\nЕда в кормушке - {self.home.cat_food}\n'
      )
    else:
      return f'{self.name} умер {self.couse_of_dead()}'

  def __add__(self, other):
    self.home.add_tenant(other)
    self.spouse = other
    other.spouse = self
    self.up_top_overall(other.money)

  def is_alive(self):
    return self.satieti > 0 and self.happiness > 0

  def get_married(self, who):
    self + who

    print(f'{self.name} и {who.name} теперь муж и жена.')

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
    
    products_in_the_cart = min(self.money, self.home.fridge.get_free_place_man_food())
    self.home.fridge.man_food.value += products_in_the_cart
    self.money -= products_in_the_cart

    if len(self.cats['живые'])>0:
      cat_products_in_the_cart = min(self.money, self.home.fridge.get_free_place_cat_food())
      self.home.fridge.cat_food.value += cat_products_in_the_cart
      self.money -= cat_products_in_the_cart
    
    self.satieti = max(man_config.MIN_SATIETI,
                       self.satieti - man_config.SATIETI_STEP_STORE)
    self.happiness = max(man_config.MIN_HAPPINES,
                         self.happiness - man_config.HAPPINES_STEP_STORE)
    
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

  def lived_day(self, day):
    if day % 365 == 0:
      self.age += man_config.GROW_STEP
      self.happiness = min(man_config.MAX_HAPPINES,
                           self.happiness + man_config.HAPPINES_STEP_GROW_UP)

  def buy_cat(self):
    self.cats['живые'].append(PetShop.sell())
    self.cats['живые'][-1].owner = self
    self.home.add_tenant(self.cats['живые'][-1])
    self.home.fridge.cat_food.value += man_config.CAT_FOOD_STEP
    self.happiness = min(man_config.MAX_HAPPINES,
                         self.happiness + man_config.HAPPINES_STEP_BUY_CAT)
    self.money -= man_config.CAT_COST
    if self.is_married():
      self.spouse.money = self.money

    print(f'{self.name} купил кота.')

  def take_cat(self, cat):
    self.cats['живые'].append(cat)
    self.home.add_tenant(cat)
    if self.is_married():
      self.spouse.cats['живые'].append(cat)
    
  def bury_cat(self):
    for cat in self.cats['живые']:
      if not cat.is_alive():
        item = self.cats['живые'].pop(
          self.cats['живые'].index(cat))
        self.cats['мертвые'].append(item)
        self.happiness = max(
          man_config.MIN_HAPPINES,
          self.happiness - man_config.HAPPINES_STEP_BURY_CAT)
        self.home.tenants['коты'].remove(cat)

  def fill_cat_bowl(self):
    self.happiness = min(man_config.MAX_HAPPINES,
                         self.happiness + man_config.HAPPINES_STEP_FEED_CAT)
    self.satieti = max(man_config.MIN_SATIETI,
                       self.satieti - man_config.SATIETI_STEP_FEED_CAT)
    self.home.cat_food += min(self.home.fridge.cat_food.value, man_config.FOOD_STEP_FEED_CAT*len(
      self.cats['живые']))
    self.home.fridge.cat_food.value -= min(self.home.fridge.cat_food.value, man_config.FOOD_STEP_FEED_CAT * len(
      self.cats['живые']))

    print(f'{self.name} наполнил кошачью миску.\n')

  def move_to_new_house(self, house):
    self.home = house
    self.home.tenants['люди'].append(self)
    for cat in self.cats['живые']:
      cat.home = self.home
      self.home.tenants['коты'].append(cat)
    self.home.change_owner(self)

  def remove_home(self):
    self.home = None
    self.home.tenants['люди'].remove(self)
    for cat in self.cats['живые']:
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
        self.cats['живые']):
      self.go_to_work()

    elif self.money >= man_config.LIVE_MIN_MONEY and self.home.fridge.get_free_place_man_food(
    ) >= 200:
      self.go_to_store()

    elif self.home.cat_food <= man_config.LIVE_MIN_HOME_CAT_FOOD * len(
        self.cats['живые']) and len(self.cats['живые']) > 0 and self.home.fridge.cat_food.value > len(
          self.cats['живые']) * 20:
      if self.home.fridge.cat_food.value < 20 * len(
          self.cats['живые']):
        self.go_to_store()
      else:
        self.fill_cat_bowl()

    elif self.money >= man_config.MONEY_FOR_BUY_CAT and len(
        self.cats['живые']) < 1:
      self.buy_cat()

    else:
      self.action(random.randint(2, 5))

    self.bury_cat()

  def up_top_overall(self, how_many):
    self.money += how_many
    self.spouse.money += how_many

  def down_top_overall(self, how_many):
    self.money -= how_many
    self.spouse.money -= how_many

  def live_circle(self, day):
    if self.is_alive():
      self.lived_day(day)
      self.live()


class Husband(Man):

  def __init__(self, name, age):
    super().__init__(name, age)

  def action(self, selected_action):
    action_dict = {
      1: self.eat,
      2: self.sleep,
      3: self.go_to_work,
      4: self.pick_wildflowers,
      5: self.play_computer_games,
      6: self.go_to_store
    }
    return action_dict[selected_action]()

  def pick_wildflowers(self):
    if self.is_married():
      self.happiness = min(man_config.MAX_HAPPINES,
                           man_config.BUY_FLOWERS_HAPPINESS_STEP)
      self.spouse.hapiness = min(man_config.MAX_HAPPINES,
                                 man_config.BUY_FLOWERS_HAPPINESS_STEP)
      self.money -= man_config.BUY_FLOWERS_MONEY_STEP
      self.spouse.money = self.money


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

    elif min(self.home.fridge.get_free_place_man_food(), self.home.fridge.get_free_place_man_food()) >= 300:
      self.go_to_store()

    elif len(self.cats['живые']) > 0 and self.home.fridge.cat_food.value >= 20 * len(
        self.cats['живые']) and self.home.cat_food < man_config.LIVE_MIN_HOME_CAT_FOOD * len(
          self.cats['живые']):
      self.fill_cat_bowl()

    elif self.money >= man_config.MONEY_FOR_BUY_CAT and len(
        self.cats['живые']) < 1:
      self.buy_cat()

    else:
      self.action(random.randint(2, 3))

    self.bury_cat()