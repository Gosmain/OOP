import random

class Man(object):

  def __init__(self, name, age, satieti, money, happiness, food):
    self.name = name
    self.age = age
    self.satieti = satieti
    self.money = money
    self.happiness = happiness
    self.food = food     

  def eat(self):
    if self.food < 20:
      self.go_to_the_store()
    else:
      self.satieti = min(100, self.satieti+50)
      self.happiness = min(100, self.happiness+20)
      self.food -= 20
    

  def sleep(self):
    self.happiness = min(100, self.happiness+50)
    self.satieti -= 20

  def go_to_work(self):
    self.money += 100
    self.happiness -= 40

  def play_computer_games(self):
    self.happiness = min(100, self.happiness+60)
    self.satieti -= 20

  def go_to_the_store(self):
    if self.money < 50:
      self.go_to_work()
    else:
      self.food += 50
      self.satieti -= 20
      self.happiness -= 20
      self.money -= 50
    
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
    if self.satieti <= 0 and self.happiness <= 0:
      return 'от грусти и от голода'
    elif self.satieti <= 0:
      return 'от голода'
    else:
      return 'от грусти'
    
    

  
    
if __name__ == "__main__":
  character = Man('Никитосов', 26, 100, 100, 100, 100)
  day_count = 1
  
  while character.happiness>0 and character.satieti>0:
    print(f'''День {day_count}
{character.name} - {character.age+day_count//365}
Счастье - {character.happiness}
Сытость - {character.satieti}
Деньги - {character.money}
Еда - {character.food}
''')
    
    character.action(random.randint(1,5))
    print()
    day_count += 1
  else:
    print(f'''День {day_count}
{character.name} умер {character.couse_of_dead()}''')

    
    
    
  

  
  
  
  
  
  