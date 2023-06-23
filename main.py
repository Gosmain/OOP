from models.man import Man
from models.home import Home
from models.cat import Cat

if __name__ == "__main__":

  char = Man('Гусь', 33)
  char.home = Home(char)
  char.buy_cat()
  for i in range(1, 366):
    char.live_circle(i)
    if char.cat !='':
      char.cat.live_circle(i)
      print(f'День {i}\n{char}\n{char.cat}\n')
    else:
      print(f'День {i}\n{char}\n')
    if not char.is_alive():
      break
  print(f'Год закончен, котиков у человека: {len(char.l_of_cat)}')
  
