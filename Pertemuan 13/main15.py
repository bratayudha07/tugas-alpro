data = {"nama": "Brata", "umur": "20"}

try:
    pilihan = int(input("Pilih (1=nama, 2=umur, 3=nilai): "))
    kunci = ["nama", "umur", "nilai"][pilihan - 1]
    hasil = int(data[kunci]) + 5
    print(f"Hasil: {hasil}")

except ValueError:
    print("Input bukan angka!")
except KeyError:
    print("Data tidak ditemukan!")
except IndexError:
    print("Pilihan di luar menu!")
