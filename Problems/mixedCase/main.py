string_input = input()

word_list = string_input.split()
result_list = []

if len(word_list) == 1:
    print(word_list[0].lower())

elif len(word_list) > 1:
    result_list.append(word_list[0].lower())
    for word in word_list:
        if word == word_list[0]:
            continue
        result_list.append(word.capitalize())

    print("".join(result_list))
