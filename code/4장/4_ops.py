# 4_operators.py

a = 132
b = 45

fmt0 = '{:<10}' #  변수 + 공백 10개까지
fmt1 = '0b{:08b} 0x{:02x} {:3}' # 0b________ 2진법 8개, 0x__ 16진법 2개, 10진법 3개

# bit &
print(fmt0.format('a'), fmt1.format(a, a, a))
print(fmt0.format('b'), fmt1.format(b, b, b))

n = 30
print('-'*n)

print(fmt0.format('a & b'), fmt1.format(a&b, a&b, a&b))

#bit |
print("\nbit OR")
print(fmt0.format('a'), fmt1.format(a, a, a))
print(fmt0.format('b'), fmt1.format(b, b, b))
print('-'*n)
print(fmt0.format('a | b'), fmt1.format(a|b, a|b, a|b))

#bit ^
print("\nbit XOR")
print(fmt0.format('a'), fmt1.format(a, a, a))
print(fmt0.format('b'), fmt1.format(b, b, b))
print('-'*n)
print(fmt0.format('a ^ b'), fmt1.format(a^b, a^b, a^b))

#bit ~
print("\nbit NOT")
print(fmt0.format('a'), fmt1.format(a, a, a))
print('-'*n)
print(fmt0.format('~ a'), fmt1.format(~a&0xFF, ~a&0xFF, ~a&0xFF))

#bit <<
print("\nbit left shift")
print(fmt0.format('a'), fmt1.format(a, a, a))
print('-'*n)
print(fmt0.format('a << 2'), fmt1.format(a<<2&0xFF, a<<2&0xFF, a<<2&0xFF))

#bit >>
print("\nbit rigth shift")
print(fmt0.format('a'), fmt1.format(a, a, a))
print('-'*n)
print(fmt0.format('a >> 2'), fmt1.format(a>>2&0xFF, a>>2&0xFF, a>>2&0xFF))