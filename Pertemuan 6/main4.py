secret_number = 777

print("""
+=============================================+
| Selamat datang di game saya, muggle!        |
| masukkan suatu angka dan tebak              |
| angka berapa yang saya pilih                |
| untuk kamu.                                 |
| Jadi, berapa angka rahasianya?              |
+=============================================+
""")

tebakan = int(input("Masukkan tebakanmu: "))

while tebakan != secret_number:
    print("hahaha ! kamu nyangkut deh di Loop saya")
    tebakan = int(input("Coba lagi: "))

print("Selamat, Muggle! kamu bebas sekarang!")
