def no_dups(s):
    words = s.split()
    memo = {}
    unique_words = []
    for word in words:
        if word in memo:
            pass
        else:
            unique_words.append(word)
            memo[word] = 1
    return ' '.join(unique_words)


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
