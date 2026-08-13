import textwrap

text = input()
width = int(input())

print(textwrap.fill(text, width))
