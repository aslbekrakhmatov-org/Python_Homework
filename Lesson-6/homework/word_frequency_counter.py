def word_count(text):
    try:
        with open(text) as file:
            content = file.read()
    except FileNotFoundError:
        print("The file is not found.")
        txt = input("Please enter a text:")
        with open(text, 'w') as file:
            content = file.write(txt)
        content = txt
    puncs = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    content = content.lower().translate(str.maketrans("", "", puncs)).split()
    words = []
    frequency_list = []
    for i in content:
        if i not in words:
            words.append(i)
            frequency = content.count(i)
            frequency_list.append(frequency)
    
    words_dict = dict(zip(words, frequency_list))
    sorted_dict = dict(sorted(words_dict.items(), key= lambda x : x[1], reverse=True))
        
    total_words = sum(frequency_list)
    print(f"Total words: {total_words}")
    try:
        top_words = int(input("How many top common words do you want see?_ "))
        if top_words>len(sorted_dict):
            top_words=len(sorted_dict)
    except ValueError:
        print("Invalid input. Top 5 words as a default.")
        top_words=5


    print(f"Top {top_words} words")
    for n, (word, count) in enumerate(sorted_dict.items()):
        if n>=top_words:
            break
        print(f"{word} - {count} times")

    with open("word_count_report.txt", "a") as new_file:
        new_file.write(f"Word Count Report\n")
        new_file.write(f"Total words: {total_words}\n")
        new_file.write(f"Top {top_words} words:\n")
        for n, (word, count) in enumerate(sorted_dict.items()):
            if n>=top_words:
                break
            new_file.write(f"{word} - {count}\n")

dict_words = word_count("sample.txt")