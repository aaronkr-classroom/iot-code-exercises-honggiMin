# 5_hw_SayDay_class
class SayDays :
  def __init__(self, year, month, day):
      self.year = year
      self.month = month
      self.day = day
      self.leap = (year % 4 == 0 & year % 100 != 0) | year % 400 == 0
      
      self.lastdays = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
      if self.leap :
          self.lastdays[2] = 29

  def days(self) :
      return sum(self.lastdays[:self.month]) + self.day

  def days_left(self) :
      num = 0
      if self.leap :
          num = 366
      else :
          num = 365

      return num - self.days()
  
  def weekday(self) :
      y, m, d = self.year, self.month, self.day
      if m < 3 :
          m += 12
          y -= 1

      k = y % 100
      j = y // 100
      h = (d + ((13 * (m +1)) //5) + k + (k // 4) + (j //4) - (2 * j)) % 7

      return h
  
  def weekday_name(self) :
      wNames = ["토", "일", "월", "화", "수", "목", "금"]
      return wNames[self.weekday()]
        
while True :
    inp = input("날짜 띄어서 입력(종료 : q) : ")
    if inp[0] == 'q' :
      break

    y, m, d = map(int, inp.split())
    sayDays = SayDays(y, m, d)

    print(f"1월 1일로부터 {sayDays.days()}일")
    print(f"12월 31일까지 {sayDays.days_left()}일")
    print(f"숫자 : 요일 : {sayDays.weekday()}")
    print(f"요일 계산   : {sayDays.weekday_name()}요일")

