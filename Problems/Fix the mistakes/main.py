text = input()
words = text.split()

for i, _ in enumerate(words):
    if 'www.' in words[i].casefold():
        print(words[i])
    elif 'https://' in words[i].casefold():
        print(words[i])
    elif 'http://' in words[i].casefold():
        print(words[i])
