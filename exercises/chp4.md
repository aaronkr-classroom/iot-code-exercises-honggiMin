# 4장 연습문제

6. 다음 정보를 참조해 dictionary 자료형의 변수를 표현하세요.
- 2개의 센서가 있습니다.
- 첫 번째 센서의 이름은 'dht11'이고 'temperature'와 'humidity' 값으로 23과 47을 나타냅니다.
- 첫 번째 센서의 온도 표현 방식('unit')은 섭씨('celsius')입니다.
- 두 번째 센서의 이름은 'bh1750'인데 조도 값으로 450을 나타냅니다.
- 두 번째 센서의 측정 단위는 룩스('lux')입니다.
- 다음과 같은 형식으로 표현합니다. sensors = {'dht11': { 중략 } , 중략 }
  - 소스코드<br>
  sensors = {'dht11' : {'temperature':23, 'humidity':47, 'unit':'celsious'},  
           'bh1750' : {'lux':450}  
           }  
print('dht11 :', sensors['dht11'])  
print('bh1750 :', sensors['bh1750'])  
2. 다음 내용을 하나의 조건식으로 만드세요.
- 홀수 달의 15일 또는 짝수 달의 16일이면 "그날"을 출력함.
- 8월 15일이면 "광복절"을 출력함.
- 그 외는 "평일"을 출력함.
- 변수는 month와 day를 사용함.
  - 소스코드<br>
month = int(input())  
day = int(input())  
print(f"{month}월 {day}일")  
if (((month == 8) & (day == 15))) :  
    print("광복절")  
elif (((month % 2 == 1) & (day == 15)) | ((month % 2 == 0) & (day == 16))) :  
    print("그날")  
else :  
    print("평일")  
3. for 문을 이용해 1~50의 짝수 합을 구하되, 3의 배수는 제외하세요.
  - 소스코드<br>
sum = 0  
for i in range(1, 51) :  
    if i % 3 == 0 :  
        continue  
    sum += i  
print(sum)  
5. 연습문제 4.3을 while 문으로 해결하세요. 
- while문을 사용하여 1~50까지의 짝수 합을 구하되, 3의 배수는 제외하여 출력
  - 소스코드<br>
sum = 0  
num = 1  
while num <= 50:  
    if num % 3 != 0 :  
        sum += num  
    num += 1  
print(sum)  
