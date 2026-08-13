string = input()
k = int(input())

for i in range(0, len(string), k):
    part = string[i:i + k]
    result = ""

    for char in part:
        if char not in result:
            result += char

    print(result)
