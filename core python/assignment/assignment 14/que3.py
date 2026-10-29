def count_unique_word_frequencies(strings_list):
    all_words = []
    for string in strings_list:
        all_words.extend(string.split())
    unique_words = set(all_words)
    return {word: all_words.count(word) for word in unique_words}

strings = ["apple banana apple", "banana orange apple", "grape apple"]
print(count_unique_word_frequencies(strings))