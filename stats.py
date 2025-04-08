def get_num_words(str):
    new_list = []
    new_list = str.split()
    return len(new_list)

def get_total_character(str):
    char_dictionary = {}

    for char in str:
        char = char.lower()
        if char == ' ':
            char = 'Space'
        if char in char_dictionary:
            char_dictionary[char] += 1
        else:
            char_dictionary[char] = 1

    return char_dictionary

def sort_dict_by_value(dictionary):
    return dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True))
