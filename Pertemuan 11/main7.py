def cek_segitiga(a, b, c):
    if a + b <= c or b + c <= a or c + a <= b:
        return False
    return True


print(cek_segitiga(3, 4, 10))
print(cek_segitiga(4, 7, 9))
