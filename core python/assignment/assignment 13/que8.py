def count_word_frequency(text):
    cleaned_text = ""
    for char in text.lower():
        if char.isalnum() or char.isspace():
            cleaned_text += char
            

    words = cleaned_text.split()
    

    frequency_dict = {}
    for word in words:

        frequency_dict[word] = frequency_dict.get(word, 0) + 1
        
    return frequency_dict


sample_string = "Python is fun, and learning Python is rewarding."
result = count_word_frequency(sample_string)
print(result)