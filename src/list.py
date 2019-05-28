# list comprehensions

names = ["Antonio", "Novina", "connor", "bob", "Samar", "lukasz"]

# l = []

# l = [1 + 1]

# l = [i for i in range(0, 6)]

# l = [i * 2 for i in range(0, 6)]

# l = [i ** 2 for i in range(0, 6)]

# l = [name.capitalize() for name in names]

# l = [name.upper() for name in names]

l = []
for name in names:
    l.append(name.upper())

print(l)
