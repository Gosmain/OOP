import random

from configs import man_config
from models.cat import RussianBlueCat, ScotishCat, SphinxCat


class Man(object):

  def __init__(self,
               name,
               age,
               home=None,
               satieti=man_config.START_SATIETI,
               money=man_config.START_MONEY,
               happines=man_config.START_HAPPINES):
    self.home = home
    self.name = name
    self.age = age
    self.satieti = satieti
    self.home = 'Бездомный'
    self.money = money
    self.happiness = happines
    self.cat = ''

  def __str__(self):
    if self.is_alive():
      return f'{self.name} - {self.age}\nСчастье - {self.happiness}\nСытость - {self.satieti}\nДеньги - {self.money}\nЕда - {self.home.fridge.man_food}\nКошачья еда - {self.home.fridge.cat_food}\nЕда в кормушке - {self.home.cat_food}\n'
    else:
      return f'{self.name} умер {self.couse_of_dead()}'

  def is_alive(self):
    return self.satieti and self.happiness

  def eat(self):
    self.satieti = min(man_config.MAX_SATIETI,
                       self.satieti + man_config.SATIETI_STEP_EAT)
    self.happiness = min(man_config.MAX_HAPPINES,
                         self.happiness + man_config.HAPPINES_STEP_EAT)
    self.home.fridge.man_food -= man_config.FOOD_STEP_EAT
    print(f'{self.name} поел.')

  def sleep(self):
    self.happiness = min(man_config.MAX_HAPPINES,
                         self.happiness + man_config.HAPPINES_STEP_SLEEP)
    self.satieti = max(man_config.MIN_SATIETI,
                       self.satieti - man_config.SATIETI_STEP_SLEEP)
    print(f'{self.name} поспал.')

  def go_to_work(self):
    self.money += man_config.MONEY_STEP_WORK
    self.happiness = max(man_config.MIN_HAPPINES,
                         self.happiness - man_config.HAPPINES_STEP_WORK)
    print(f'{self.name} сходил на работу.')

  def play_computer_games(self):
    self.happiness = min(man_config.MAX_HAPPINES,
                         self.happiness + man_config.HAPPINES_STEP_PLAY)
    self.satieti = max(man_config.MIN_SATIETI,
                       self.satieti - man_config.SATIETI_STEP_PLAY)
    print(f'{self.name} поиграл в компьютерные игры.')

  def go_to_the_store(self):
    self.home.fridge.cat_food += man_config.CAT_FOOD_STEP_STORE * len(
      self.list_of_alive_cats())
    self.home.fridge.man_food += man_config.MAN_FOOD_STEP_STORE
    self.satieti = max(man_config.MIN_SATIETI,
                       self.satieti - man_config.SATIETI_STEP_STORE)
    self.happiness = max(man_config.MIN_HAPPINES,
                         self.happiness - man_config.HAPPINES_STEP_STORE)
    self.money -= man_config.MONEY_STEP_STORE
    print(f'{self.name} сходил в магазин.')

  def action(self, selected_action):
    action_dict = {
      1: self.eat,
      2: self.sleep,
      3: self.go_to_work,
      4: self.play_computer_games,
      5: self.go_to_the_store,
      6: self.buy_cat
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
    name = random.choice(man_config.CAT_NAMES)
    self.cat = random.choice([
      ScotishCat(self, name),
      RussianBlueCat(self, name),
      SphinxCat(self, name)
    ])
    self.cat.home = self.home
    self.home.tenants['коты'].append(self.cat)
    self.home.fridge.cat_food += man_config.CAT_FOOD_STEP_STORE
    self.list_of_alive_cats().append(self.cat)
    print(f'{self.name} купил кота.')

  def list_of_alive_cats(self, cat_list=[]):
    return cat_list

  def list_of_dead_cats(self, cat_list=[]):
    return cat_list

  def bury_the_cat(self):
    for el in self.list_of_alive_cats():
      if el.satieti <= 0:
        item = self.list_of_alive_cats().pop(
          self.list_of_alive_cats().index(el))
        self.list_of_dead_cats().append(item)
        self.happiness -= man_config.HAPPINES_STEP_BURY_CAT
        self.home.tenants['коты'].remove(el)

  def feed_cat(self):
    self.happiness = min(man_config.MAX_HAPPINES,
                         self.happiness + man_config.HAPPINES_STEP_FEED_CAT)
    self.satieti = max(man_config.MIN_SATIETI,
                       self.satieti - man_config.SATIETI_STEP_FEED_CAT)
    self.home.cat_food += man_config.FOOD_STEP_FEED_CAT * len(
      self.list_of_alive_cats())
    self.home.fridge.cat_food -= man_config.FOOD_STEP_FEED_CAT * len(
      self.list_of_alive_cats())
    print(f'{self.name} наполнил кошачью миску.')

  def move_to_a_new_house(self, house):
    self.home = house
    self.home.tenants['люди'].append(self)
    for el in self.list_of_alive_cats():
      el.home = self.home
      self.home.tenants['коты'].append(el)

  def remove_home(self):
    self.home = None
    self.home.tenants['люди'].remove(self)
    for el in self.list_of_alive_cats():
      el.home = self.home
      self.home.tenants['коты'].remove(el)

  def live(self):
    if self.happiness <= man_config.LIVE_MIN_HAPPINES:
      self.play_computer_games()
    elif self.satieti <= man_config.LIVE_MIN_SATIETI:
      if self.home.fridge.man_food >= man_config.LIVE_EAT_FOOD:
        self.eat()
      else:
        if self.money >= man_config.LIVE_EAT_MONEY:
          self.go_to_the_store()
        else:
          self.go_to_work()
    elif self.money <= man_config.LIVE_MIN_MONEY:
      self.go_to_work()
    elif self.home.fridge.man_food + self.home.fridge.cat_food <= man_config.FRIDGE_CAPACITY:
      self.go_to_the_store()
    elif self.home.cat_food <= man_config.LIVE_MIN_HOME_CAT_FOOD * len(
        self.list_of_alive_cats()) and len(
          self.list_of_alive_cats()) > 0 and self.home.fridge.cat_food > len(
            self.list_of_alive_cats()) * 20:
      if self.home.fridge.cat_food < 20:
        self.go_to_the_store()
      else:
        self.feed_cat()
    elif self.money >= man_config.MONEY_FOR_BUY_CAT:
      self.buy_cat()
      self.money -= man_config.CAT_COST
    else:
      self.action(random.randint(1, 4))
    self.bury_the_cat()

  def live_circle(self, day):
    if self.is_alive():
      self.lived_day(day)
      self.live()
