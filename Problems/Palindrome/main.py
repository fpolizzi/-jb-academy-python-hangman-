word = input()


def is_palindrome(_word):
    if word[::-1] == word:
        print("Palindrome")
    else:
        print("Not palindrome")


is_palindrome(word)
