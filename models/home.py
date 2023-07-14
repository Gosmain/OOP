from models.fridge import Fridge
from configs import home_config
from models.man import Man


class Home:

  def __init__(self, owner=None):
    self.owner = None
    self.fridge = Fridge()
    self.cat_food = home_config.START_CAT_FOOD
    self.tenants = {
      'люди': [],
      'коты': []
    }

  def add_tenant(self, who):
    if isinstance(who, Man):
      self.tenants['люди'].append(who)
      who.home = self
    else:
      self.tenants['коты'].append(who)
      who.home = self

  def remove_tenant(self, who):
    if isinstance(who, Man):
      self.tenants['люди'].remove(who)
      who.home = None
    else:
      self.tenants['коты'].remove(who)
      who.home = None

  def change_owner(self, new_owner):
    self.owner = new_owner
