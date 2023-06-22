from models.man import Man
from models.home import Home

if __name__ == "__main__":
  
  char = Man('Никитосов', 25)
  char.home = Home(char.name)
  for i in range(365, 370):
    print(f'День {i}\n{char}')
    if not char.is_alive():
      break
    char.live_circle(i)


      
  


  
  
