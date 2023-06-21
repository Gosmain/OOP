import random
from constant import man_constant
from models.home import Home
from models.fridge import Fridge

class Man(object):

  def __init__(self, name, age, satieti=man_constant.START_SATIETI, 
               money=man_constant.START_MONEY, happines=man_constant.START_HAPPINES):
    self.name = name
    self.age = age
    self.home = Home(name)
    self.satieti = satieti
    self.money = money
    self.happiness = happines
    
  def is_alive(self):
    if self.happiness > man_constant.MIN_HAPPINES and self.satieti >   man_constant.MIN_SATIETI:
      return True
    else:
      return False

  
  def eat(self):
    self.satieti = min(man_constant.MAX_SATIETI, self.satieti + man_constant.SATIETI_STEP_EAT)
    self.happiness = min(man_constant.MAX_HAPPINES, self.happiness + man_constant.HAPPINES_STEP_EAT)
    self.home.fridge.food -= man_constant.FOOD_STEP_EAT

  
  def sleep(self):
    self.happiness = min(man_constant.MAX_HAPPINES, self.happiness + man_constant.HAPPINES_STEP_SLEEP)
    self.satieti -= man_constant.SATIETI_STEP_SLEEP

  
  def go_to_work(self):
    self.money += man_constant.MONEY_STEP_WORK
    self.happiness -= man_constant.HAPPINES_STEP_WORK

  
  def play_computer_games(self):
    self.happiness = min(man_constant.MAX_HAPPINES, self.happiness + man_constant.HAPPINES_STEP_PLAY)
    self.satieti -= man_constant.SATIETI_STEP_PLAY

  
  def go_to_the_store(self):
    self.home.fridge.food += man_constant.FOOD_STEP_STORE
    self.satieti -= man_constant.SATIETI_STEP_STORE
    self.happiness -= man_constant.HAPPINES_STEP_STORE
    self.money -= man_constant.MONEY_STEP_STORE

  
  def action(self, selected_action):
    action_dict = {
      1: self.eat,
      2: self.sleep,
      3: self.go_to_work,
      4: self.play_computer_games,
      5: self.go_to_the_store
    }
    return action_dict[selected_action]()

  
  def couse_of_dead(self):
    if self.is_alive():
      return 'от грусти и от голода. R.I.P.'
    elif self.satieti <= man_constant.MIN_SATIETI:
      return 'от голода. R.I.P.'
    else:
      return 'от грусти. R.I.P.'

  
  def live(self):
    if self.happiness <= man_constant.LIVE_MIN_HAPPINES:
      self.play_computer_games()
    elif self.satieti <= man_constant.LIVE_MIN_SATIETI:
      if self.home.fridge.food >= man_constant.LIVE_EAT_FOOD:
        self.eat()
      else:
        if self.money >= man_constant.LIVE_EAT_MONEY:
          self.go_to_the_store()
        else:
          self.go_to_work()
    elif self.money <= man_constant.LIVE_MIN_MONEY:
      self.go_to_work()
    elif self.home.fridge.food <= man_constant.LIVE_MIN_FOOD:
      self.go_to_the_store()
    else:
      self.action(random.randint(1, 5))


  def grow_up(self, day):
    if day%365 == 0:
      self.age += 1
      self.happiness = min(man_constant.MAX_HAPPINES, self.happiness + man_constant.HAPPINES_STEP_GROW_UP)
      print('C днем рождения!!!', end='\n')
 
  
  def live_circle(self, day):
    if self.is_alive():
      self.grow_up(day)
      self.live()

  def __str__(self):
    if self.is_alive():
      return f'{self.name} - {self.age}\nСчастье - {self.happiness}\nСытость - {self.satieti}\nДеньги - {self.money}\n'
    else:
      return f'{self.name} умер {self.couse_of_dead()}'


  
  
          





