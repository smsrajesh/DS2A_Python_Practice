def rearrange_of_words(s,t):
    temp_str=s
    if len(s)!=len(t):
        return False
    elif s==t:
        return True
    for index in range(1,len(s)):
        result = temp_str[-1]+temp_str[0:-1]
        print(result)
        if result==t:
            return True
        temp_str=result
        print(temp_str)

    return False

print(rearrange_of_words(input("Enter first word :"),input("Enter second word :")))