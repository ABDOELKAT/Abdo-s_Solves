from collections import Counter

n = int(input())
sizes = list(map(int, input().split()))
counter = Counter(sizes)

customers = int(input())
money = 0

for _ in range(customers):
    size, price = map(int, input().split())

    if counter[size] > 0:
        money += price
        counter[size] -= 1

print(money)
