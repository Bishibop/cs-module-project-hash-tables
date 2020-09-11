def word_count(s):
    words = s.translate({ord(i): None for i in '":;,.-+=/\\|[]{}()*^&'}).split()
    count_list = {}
    for word in words:
        if word.lower() in count_list:
            count_list[word.lower()] += 1
        else:
            count_list[word.lower()] = 1
    return count_list


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))
