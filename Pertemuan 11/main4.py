def cek_prima(bilangan):
    if bilangan <= 1:
        return False
    return all(bilangan % i != 0 for i in range(2, int(bilangan**0.5) + 1))


for i in range(1, 20):
    if cek_prima(i + 1):
        print(i + 1, end=" ")
print()
