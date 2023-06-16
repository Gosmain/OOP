class Man(object):

  def __init__(self, name, age, satieti, money, happiness, food):
    self.name = name
    self.age = age
    self.satieti = satieti
    self.money = money
    self.happiness = happiness
    self.food = food

    action_dict = {
    1: self.eat(),
    2: self.sleep(),
    3: self.go_to_work(),
    4: self.play_computer_games(),
    5: self.go_to_the_store()
    }
  

  def eat(self):
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
    self.food += 50
    self.satieti -= 20
    self.happiness -= 20
    self.money -= 50
    
  def action(self, selected_action):
    action_dict = {
    1: self.eat(),
    2: self.sleep(),
    3: self.go_to_work(),
    4: self.play_computer_games(),
    5: self.go_to_the_store()
    }
    return action_dict[selected_action]

  def dead(self, cause_of_dead):
    cause_of_dead_dict = {
      self.satieti: 'от голода',
      self.happiness: 'от грусти'
    }
    return cause_of_dead_dict[min(self.satieti, self.happiness)]
    
    

  
    
if __name__ == "__main__":
  
  print('Введите имя персонажа')
  name = input()
  print('Укажите возвраст персонажа')
  age = int(input())
  character = Man(name, age, 50, 0, 50, 0)
  print()  
  day_count = 1
  
  while character.happiness>0 and character.satieti>0:
    print(f'''День {day_count}
{character.name} - {character.age+day_count//365}
Счастье - {character.happiness}
Сытость - {character.satieti}
Деньги - {character.money}
Еда - {character.food}
''')
    print(f'''Выберите действие:
1. Есть
2. Cпать
3. Сходить на работу
4. Играть на компьютере
5. Сходить в магазин
''')
    character.action(int(input()))
    print()
    day_count += 1
  else:
    print(f'''День {day_count}
{character.name} умер от {character.dead}''')

    
    
    
  

  
  
  
  
  
  