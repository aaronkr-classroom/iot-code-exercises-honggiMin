# 3_str.py
# 문자열 묶는 방법

f = "hong" # 큰 따음표
n = '길동' # 작은 따음표

# 문자열 연결하기
fn = f + n

# 글자 수 확인
ln = len(fn) # 4 + 2 = 6

# '와 " 출력하기
qt1 = "It's a beatiful day"
qt2 = 'He said, "Hello World!"'
qt3 = "She said, \"No, it's now!\""
qt4 = 'I\'m hungry.'
qt5 = 'C:\\Windows\\users\\Desktop\\'

print(1, fn)
print(f"2 {ln}")
print(3, qt1)
print(f"4 : {qt2}")
print(f"5 : {qt3}\n\t6 : {qt4}\t7 : {qt5}")
