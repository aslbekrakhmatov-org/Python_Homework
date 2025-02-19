import string
from collections import Counter

def word_count(text):
    try:
        with open(text) as file:
            content = file.read()
    except FileNotFoundError:
        print("The file is not found. Please enter a text:")
        user_text = input()
        with open(text, 'w') as file:
            file.write(user_text)
        content = user_text  

    puncs = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    content = content.lower().translate(str.maketrans("", "", puncs)).split()


    words_dict = dict(Counter(content))
    sorted_dict = dict(sorted(words_dict.items(), key=lambda x: x[1], reverse=True))

    total_words = sum(words_dict.values())
    print(f"Total words: {total_words}")

    try:
        top_words = int(input("How many top common words do you want to see? "))
        if top_words > len(sorted_dict):
            top_words = len(sorted_dict)
    except ValueError:
        print("Invalid input. Showing top 5 words by default.")
        top_words = 5

    print(f"Top {top_words} words:")
    for n, (word, count) in enumerate(sorted_dict.items()):
        if n >= top_words:
            break
        print(f"{word} - {count} times")

    with open("word_count_report.txt", "a") as new_file:
        new_file.write(f"\nWord Count Report\n")
        new_file.write(f"Total words: {total_words}\n")
        new_file.write(f"Top {top_words} words:\n")
        for n, (word, count) in enumerate(sorted_dict.items()):
            if n >= top_words:
                break
            new_file.write(f"{word} - {count}\n")

word_count("sample.txt")