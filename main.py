class Man(object):
  name = 'Alex'
  age = 0
  money = 0
  satiety = 0
  happiness = 0
  food = 0
  

  def eat(self):
    if food >= 20:
      satieti += 50
      happiness += 20
      food -= 20
    else:
      print('Недостаточно еды! Сходите в магазин!')

  def work(self):
    money += 100
    happines -= 40