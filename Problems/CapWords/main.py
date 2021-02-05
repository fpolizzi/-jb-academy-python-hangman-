str_input = input()

str_output = ""
str_result = ""
str_output = str_input.split("_")
for temp in str_output:
    str_result = str_result + temp.capitalize()

print(str_result)
