def minion_game(string):
    stuart = 0
    kevin = 0
    n = len(string)

    for i in range(n):
        score = n - i

        if string[i] in "AEIOU":
            kevin += score
        else:
            stuart += score

    if stuart > kevin:
        print("Stuart", stuart)
    elif kevin > stuart:
        print("Kevin", kevin)
    else:
        print("Draw")

s = input()
minion_game(s)
