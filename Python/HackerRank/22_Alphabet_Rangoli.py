def print_rangoli(size):
    import string
    letters = string.ascii_lowercase
    width = 4 * size - 3

    for i in range(size - 1, -size, -1):
        row = letters[size - 1:abs(i):-1] + letters[abs(i):size]
        print("-".join(row).center(width, "-"))

n = int(input())
print_rangoli(n)
