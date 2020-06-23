
def is_palindrome(word):
    if len(word) <= 1:
        return True
    else:
        if word[0] == word[-1]:
            return is_palindrome(word[1:-1])
        else:
            return False


words = ['tacocat', 'asa', 'carro', 'radar', 'animal']
for word in words:
    print(word, is_palindrome(word))
