def is_palindrome(inp):

    return inp == inp[::-1]



inp = str(input("Enter a stroing : "))

print(is_palindrome(inp))

