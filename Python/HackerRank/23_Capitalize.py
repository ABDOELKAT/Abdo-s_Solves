text = input()
words = text.split(" ")

result = []

for word in words:
    if word:
        result.append(word[0].upper() + word[1:])
    else:
        result.append("")

print(" ".join(result))
