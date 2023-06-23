import random

from configs import man_config
from models.home import Home
from models.fridge import Fridge
from models.cat import Cat


class Man(object):

  def __init__(self,
               name,
               age,
               satieti=man_config.START_SATIETI,
               money=man_config.START_MONEY,
               happines=man_config.START_HAPPINES):
    self.name = name
    self.age = age
    self.satieti = satieti
    self.money = money
    self.happiness = happines
    self.cat = ''
    self.l_of_cat = []

  def __str__(self):
    if self.is_alive():
      return f'{self.name} - {self.age}\nСчастье - {self.happiness}\nСытость - {self.satieti}\nДеньги - {self.money}\n'
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

  def sleep(self):
    self.happiness = min(man_config.MAX_HAPPINES,
                         self.happiness + man_config.HAPPINES_STEP_SLEEP)
    self.satieti = max(man_config.MIN_SATIETI,
                       self.satieti - man_config.SATIETI_STEP_SLEEP)

  def go_to_work(self):
    self.money += man_config.MONEY_STEP_WORK
    self.happiness = max(man_config.MIN_HAPPINES,
                         self.happiness - man_config.HAPPINES_STEP_WORK)

  def play_computer_games(self):
    self.happiness = min(man_config.MAX_HAPPINES,
                         self.happiness + man_config.HAPPINES_STEP_PLAY)
    self.satieti = max(man_config.MIN_SATIETI,
                       self.satieti - man_config.SATIETI_STEP_PLAY)

  def go_to_the_store(self):
    self.home.fridge.cat_food += man_config.CAT_FOOD_STEP_STORE
    self.home.fridge.man_food += man_config.MAN_FOOD_STEP_STORE
    self.satieti = max(man_config.MIN_SATIETI,
                       self.satieti - man_config.SATIETI_STEP_STORE)
    self.happiness = max(man_config.MIN_HAPPINES,
                         self.happiness - man_config.HAPPINES_STEP_STORE)
    self.money -= man_config.MONEY_STEP_STORE

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
    self.cat = Cat(random.randint(1, 3), self,
                   random.choice(man_config.CAT_NAMES))
    self.home.fridge.cat_food += man_config.CAT_FOOD_STEP_STORE
    self.l_of_cat.append(self.cat)

  def feed_cat(self):
    self.home.cat_food += 20
    self.home.fridge.cat_food -= 20

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
    elif min(self.home.fridge.man_food, self.home.fridge.cat_food) <= min(
        man_config.LIVE_MIN_MAN_FOOD, man_config.LIVE_MIN_CAT_FOOD):
      self.go_to_the_store()
    elif self.home.cat_food < 20:
      if self.home.fridge.cat_food < 20:
        self.go_to_work
      else:
        self.go_to_the_store
    elif len(self.l_of_cat) < 1:
      self.buy_cat
    else:
      self.action(random.randint(1, 6))

  def live_circle(self, day):
    if self.is_alive():
      self.lived_day(day)
      self.live()