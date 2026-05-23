# Langkah 1
exo = []

# Langkah 2
exo.append("Suho")
exo.append("Kai")
exo.append("Chanyeol")
exo.append("Sehun")

# Langkah 3
for member in ["DO", "Baekhyun", "Kris", "Lay", "Luhan", "Tao", "Chen"]:
    exo.append(member)

# Langkah 4
for member in ["Kris", "Luhan", "Tao"]:
    exo.remove(member)

# Langkah 5
exo.insert(-2, "Xiumin")

print(exo)
