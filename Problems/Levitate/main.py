spell = "Wingardium Leviosa"
search = input()

try:
    print(spell.index(search))
except ValueError:
    print(-1)
