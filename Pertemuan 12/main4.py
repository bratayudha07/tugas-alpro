x = "selamat pagi"


def scope():
    global x
    x += " dunia"
    return x


print(scope())
