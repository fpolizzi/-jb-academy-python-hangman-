dictionary = ['all', 'an', 'and', 'as', 'closely', 'correct', 'equivocal',
              'examine', 'indication', 'is', 'means', 'minutely', 'or', 'scrutinize',
              'sign', 'the', 'to', 'uncertain']

str_input = input()
list_input = str_input.split()
list_wrong = []

for word in list_input:
    if word not in dictionary:
        list_wrong.append(word)

if len(list_wrong) > 0:
    for word in list_wrong:
        print(word)
else:
    print("OK")
