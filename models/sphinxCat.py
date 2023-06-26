from models.cat import Cat
from configs import cat_config


class SphinxCat(Cat):

  def __init__(self,
               owner,
               name,
               breed='сфинкс',
               satieti=cat_config.START_SATIETI):
    Cat.__init__(self,
                 owner,
                 name,
                 breed='Unknown',
                 satieti=cat_config.START_SATIETI)
    self.breed = breed
