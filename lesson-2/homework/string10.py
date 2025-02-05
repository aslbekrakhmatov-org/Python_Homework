sentence = input("Write a sentence:")
space=" "
num_words=1
for i in sentence:
    if i in space:
        num_words+=1
print("Number of words in your sentence:", num_words)