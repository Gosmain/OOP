import random

class Man(object):
  
  def __init__(self, name, age, satieti, money, happiness):
    self.name = name
    self.age = age
    self.satieti = satieti
    self.money = money
    self.happiness = happiness
    

  def eat(self):
    global food
    if food <= 20:
      self.go_to_the_store()
    else:
      self.satieti = min(100, self.satieti+50)
      self.happiness = min(100, self.happiness+20)
      food -= 20
    

  def sleep(self):
    if self.satieti <= 20:
      self.eat()
    else:
      self.happiness = min(100, self.happiness+50)
      self.satieti -= 20

  def go_to_work(self):
    if self.happiness <= 40:
      self.play_computer_games()
    else:
      self.money += 100
      self.happiness -= 40

  def play_computer_games(self):
    if self.satieti <= 20:
      self.eat()
    else:
      self.happiness = min(100, self.happiness+60)
      self.satieti -= 20

  def go_to_the_store(self):
    global food
    if self.money < 50:
      self.go_to_work()    
    elif self.happiness <= 20:
      self.play_computer_games()
    else:
      food += 50
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
      return 'от грусти и от голода. R.I.P.'
    elif self.satieti <= 0:
      return 'от голода. R.I.P.'
    else:
      return 'от грусти. R.I.P.'  
    
    

  
    
if __name__ == "__main__":
  character = Man('Товарищ', 25, 100, 100, 100)
  food = 0
  for i in range(1,367):
      if character.happiness > 0 and character.satieti > 0:
        print(f'''День {i}
{character.name} - {character.age+i//365}
Счастье - {character.happiness}
Сытость - {character.satieti}
Деньги - {character.money}
''')    
        character.action(random.randint(1,5))
        print()
      else:
        print(f'''День {i}
{character.name} умер {character.couse_of_dead()}''')
        break
    
    
    
  

  
  
  
  
  
  