import re

natural_sorted_letters = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D',
        'L', 'W', 'U', 'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J',
        'X', 'Z']
with open("ciphertext.txt") as f:
    txt = f.read()
    letter_counts = {}
    total_letters = 0
    for char in txt:
        if re.match(r'[A-Z]', char):
            if char in letter_counts:
                letter_counts[char] += 1
            else:
                letter_counts[char] = 1
            total_letters += 1
    letter_frequencies = {char: count / total_letters
            for (char, count) in letter_counts.items()}
    sorted_pairs = sorted(letter_frequencies.items(), key=lambda x: x[1], reverse=True)
    sorted_letters = [letter for (letter, value) in sorted_pairs]

    cipher_mapping = dict(zip([ord(l) for l in sorted_letters], natural_sorted_letters))

    decrypted_text = txt.translate(cipher_mapping)
    #  print(cipher_mapping)
    print(decrypted_text)
