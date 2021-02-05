in_str = input()
in_list = in_str.split(" ")
out_list = []

for temp in in_list:
    if temp.endswith("s"):
        out_list.append(temp)

print("_".join(out_list))
