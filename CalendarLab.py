from calendar import Calendar

class MyCalendar(Calendar):

  def count_weekday_in_year(self, yr,wkdays):
    num_of_weekdays = 0
    for mnths in range(1,13):
      mnthdys_wkdys = Calendar.monthdays2calendar(self, yr, mnths)
      #print(mnthdys_wkdys)
      for items in mnthdys_wkdys:
        #print(items)
        for item in items:
          #print(item)
          m, w = item
          if w == wkdays and m != 0:
            num_of_weekdays += 1
    return num_of_weekdays

cal = MyCalendar()
print(cal.count_weekday_in_year(2019,0))