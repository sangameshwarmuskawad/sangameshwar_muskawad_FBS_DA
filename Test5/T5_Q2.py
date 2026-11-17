n = int(input("enter original number of coins: "))

li = list(map(int, input("enter coin numbers: ").split()))

for i in li:
    if li.count(i) % 2 != 0:
        print("missing coin number:", i)
        break
