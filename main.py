from models.man import Man
from models.home import Home
from models.cat import Cat

if __name__ == "__main__":

  char = Man('Никитосов', 25)
  char.home = Home(char.name)
  for i in range(1, 370):
    char.live_circle(i)
    print(f'День {i}\n{char}')
    if not char.is_alive():
      break
    
