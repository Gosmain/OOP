from models.man import Man
from models.home import Home
from models.cat import Cat

if __name__ == "__main__":

  cat = Cat('Кот', 3, 'Котовский', 'Илай')
  for i in range(1, 370):
    print(f'День {i}\n{cat}')
    if not cat.is_alive():
      break
    cat.live_circle()
  
  
  #char = Man('Никитосов', 25)
  #char.home = Home(char.name)
  #for i in range(1, 370):
  #  print(f'День {i}\n{char}')
  #  if not char.is_alive():
  #    break
  #  char.live_circle(i)



  
  
