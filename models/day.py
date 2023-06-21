from constant import day_constant

class Day(object):

  def __init__(self, today=START_TODAY):
    self.today = today

  def next_day(self):
    self.today += 1
    