# Your code here

with open("robin.txt") as f:
    txt = f.read()
    clean_txt = txt.translate({ord(i): None for i in '":;,.-+=/\\|[]{}()*^&'})
    words = clean_txt.split()
    word_count = {}
    for word in words:
        if word.lower() in word_count:
            word_count[word.lower()] += 1
        else:
            word_count[word.lower()] = 1
    pairs = sorted(list(word_count.items()), key=lambda x: x[1], reverse=True)
    for pair in pairs:
        print(f'{pair[0]:18}' + (pair[1] * '#'))
