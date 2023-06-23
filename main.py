from models.man import Man
from models.home import Home
from models.cat import Cat

if __name__ == "__main__":

  char = Man('Никитосов', 25)
  char.home = Home(char.name)
  print(char)
  char.go_to_work()
  print(char)
