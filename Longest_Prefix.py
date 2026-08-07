words=list(map(str, input("Enter the words of a list with space : ").split()))

def longest_prefix(words):
    min_word=min(words, key=len)
    l_p=0
    for index in range(len(min_word)):
        count=0
        while count<len(words)-1 and words[count][index]==words[count+1][index]:
            count+=1
        if count==len(words)-1:
            l_p+=1
    return l_p

print(longest_prefix(words))
