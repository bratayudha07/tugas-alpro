print("Instruksi break:")
for i in range(1, 6):
    if i == 3:
        break
    print("Bagian ini ada di dalam loop.", i)
print("Bagian ini ada di luar loop.")

print("\nInstruksi continue:")
for i in range(1, 6):
    if i == 3:
        continue
    print("Bagian ini ada di dalam loop.", i)
print("Bagian ini ada di luar loop.")
