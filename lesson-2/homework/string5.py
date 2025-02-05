word = input()
vowels="aeuioAEUIO"
vowels_in_word=0
consonants_in_word=0
for i in word:
    if i in vowels:
        vowels_in_word+=1
    else:
        consonants_in_word+=1
print("Number of vowels:" ,vowels_in_word, "\nNumber of consonants:" ,consonants_in_word)