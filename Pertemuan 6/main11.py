user_word = input("Masukkan suatu kata: ").upper()

for kata in user_word:
    if kata in "AIUEO":
        continue
    print(kata)
