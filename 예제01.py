money = int(input())

fiveH = int(money / 500)
oneH = int(money % 500 / 100)
fifty = int(money % 100 / 50)
ten = int(money % 50 / 10)

print("오백원: ", fiveH,"개\n백원: ", oneH, "개\n오십원: ", fifty, "개\n십원: ",ten, "개")