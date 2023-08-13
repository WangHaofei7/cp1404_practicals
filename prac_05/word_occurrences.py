text = input("Text: ")
words_list = text.split('')

statistic = {}
max_length = 0

for word in words_list:
    if len(word)>max_length:
        max_length = len(word)

        frequency = statistic.get(word, 0)
        statistic[word] = frequency + 1

words = list(statistic.keys())
words.sort()

for word in words:
    print(f"{word:{max_length}} : {statistic[word]}")