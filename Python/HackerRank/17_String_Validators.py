text = input()

print(any(c.isalnum() for c in text))
print(any(c.isalpha() for c in text))
print(any(c.isdigit() for c in text))
print(any(c.islower() for c in text))
print(any(c.isupper() for c in text))
