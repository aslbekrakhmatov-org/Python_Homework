sentence = input("Write a sentence: ").split()
acr = "".join(word[0].upper() for word in sentence)
print(acr)