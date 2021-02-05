in_string = input()

result_string = ""

for char in in_string:
    if char.isupper():
        result_string = result_string + "_" + char.lower()
    elif char.islower():
        result_string = result_string + char

if result_string.startswith("_"):
    print(result_string[1:])
else:
    print(result_string.lower())
