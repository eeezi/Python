# 예제 10
n = input()
print(n[2:])

# 예제 11
print(reversed(n))  # 문자열 거꾸로 출력
print(''.join(reversed(n)))

rvs = list(n)      # 리스트 이용
rvs.reverse()
print(''.join(rvs))

print(n[::-1])     # [::-1] 사용