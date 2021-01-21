a, cal, b = input().split()
a = int(a)
b = int(b)

if(cal == '+'):
    print(a + b)
elif(cal == '-'):
    print(abs(a - b))
elif(cal == '*'):
    print(a * b)
elif(cal == '/'):
    print(a / b)
else: print("입력 오류")