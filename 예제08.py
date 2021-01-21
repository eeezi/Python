a = list(map(int, input()))

a.append(5)    # 맨 마지막에 추가
print(a)

a.insert(0, 6) # 원하는 위치에 삽입
print(a)

a.remove(3)    # 첫 번째로 나오는 수 제거
print(a)