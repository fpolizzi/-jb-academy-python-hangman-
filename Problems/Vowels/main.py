vowels = 'aeiou'

in_str = str(input())
# create your list here
new_list = [x for x in in_str if x in vowels]
print(new_list)
