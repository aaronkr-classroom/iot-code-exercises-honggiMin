# 3_set.py
# 두 집합 정의

set1 = {1, 2, 3, 'a', "Hello"}
set2 = {"Hello", 3, 4, 5, 'b'}

# 합집합
union_set = set1 | set2

# 교집합
intersection_set = set1 & set2

# 차집합
diff_set = set1 - set2

# 대칭 차집합
sym_diff_set = set1 ^ set2

print('union : ', union_set)
print(f"intersection : {intersection_set}")
print(f"dirrerence : {diff_set}")
print(f"Symmertic difference : {sym_diff_set}")
