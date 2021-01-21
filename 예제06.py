n = list(map(int, input()))

for i in range(len(n)):
    print("*" * n[i], end="")
    print("")


for i in range(len(n)):
    for k in range(int(n[i])):
        print("*", end="")
    print("")
