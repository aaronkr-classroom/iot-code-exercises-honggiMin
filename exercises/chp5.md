다음 조건으로 클래스와 그 클래스를 사용하는 프로그램을 만드세요.

[조건 1] 클래스 만들기

- 클래스 이름 : SayDays
- 오브젝트 만들 때 전달할 매개변수 : year, month, day
- 입력된 year를 기준으로 윤년(2월이 29일까지 있는 해)을 찾아야 함
- 메소드 days( ) : 당해년도 1월 1일 기준으로 몇째 날인지 알려줌
- 메소드 days_left( ) : 당해년도 12월 31일 기준으로 남은 일수를 알려줌
- 메소드 weekday( ) : 숫자로 요일을 알려줌( 0 : 토요일)
- 메소드 weekday_name( ) : 요일을 한글로 알려줌( 0 : 토요일)
- 요일 계산은 Zeller 계산법에 따름
- import 문은 사용하지 말 것

[조건 2] 앞에서 만든 클래스를 사용해 다음과 같이 프로그램 만들기

- SayDays 오브젝트 생성
- while True :
- input 문으로 임의의 날짜 입력받음
- days( ), days_left( ), week( ), week_name( )을 출력

    - 소스코드

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
        inp = input("날짜 입력(종료 : q) : ")
    
        if inp[0] == 'q' :
            break
    
        y, m, d = map(int, inp.split())
        sayDays = SayDays(y, m, d)
    
        print(f"1월 1일로부터 {sayDays.days()}일")
        print(f"12월 31일까지 {sayDays.days_left()}일")
        print(f"숫자 : 요일 : {sayDays.weekday()}")
        print(f"요일 계산   : {sayDays.weekday_name()}요일")
