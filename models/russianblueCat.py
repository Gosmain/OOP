from models.cat import Cat
from configs import cat_config


class RussianBlueCat(Cat):

  def __init__(self,
               owner,
               name,
               breed='русская голубая',
               satieti=cat_config.START_SATIETI):
    Cat.__init__(self,
                 owner,
                 name,
                 breed='Unknown',
                 satieti=cat_config.START_SATIETI)
    self.breed = breed
