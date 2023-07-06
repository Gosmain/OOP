import random
from faker import Faker
from models.cat import RussianBlueCat, ScotishCat, SphinxCat


class PetShop:

  animals_dict = {1: RussianBlueCat, 2: ScotishCat, 3: SphinxCat}

  @classmethod
  def sell(cls):
    return cls.animals_dict[random.randint(1, 3)]
