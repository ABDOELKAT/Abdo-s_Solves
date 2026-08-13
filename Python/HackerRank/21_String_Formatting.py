n = int(input())

for i in range(1, n + 1):
    print(str(i).rjust(len(str(n))), oct(i)[2:].rjust(len(oct(n)) - 2),
          hex(i)[2:].upper().rjust(len(hex(n)) - 2),
          bin(i)[2:].rjust(len(bin(n)) - 2))
