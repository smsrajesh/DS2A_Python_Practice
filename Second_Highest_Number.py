l=list(map(int, input("Enter the elements of a list with space : ").split()))
# l=[1, 5, 6, 7, 9, 3, 4, 15]

def secondond_highest_number(l):
    maximum=0
    second_maximum=0
    for num in l:
        if num >maximum:
            second_maximum=maximum
            maximum=num
        elif maximum>num and num>second_maximum:
            second_maximum=num

    return second_maximum

print(secondond_highest_number(l))