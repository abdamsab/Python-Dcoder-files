
class WeekDayError(Exception):
    pass
  

class Weeker:
  
  def __init__(self, day):
    self.__day = day
    if self.__day.lower() not in ['mon','tue','wed','thur','fri','sat','sun']:
      raise WeekDayError
        

  def __str__(self):
    return self.__day

  
  def add_days(self, n):
    days = ['','Mon','Tue','Wed','Thur','Fri','Sat','Sun']
    indx = days.index(self.__day)
    wk = n//7
    rmd = n%7
    self.__day = days[indx+wk+rmd]
       
  def subtract_days(self, n):
    days = ['','Mon','Tue','Wed','Thur','Fri','Sat','Sun']
    indx = days.index(self.__day)
    wk = n//7
    rmd = n%7
    self.__day = days[indx-wk-rmd]
     


try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")
