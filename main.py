from stats import get_num_words 
from stats import get_total_character 
from stats import sort_dict_by_value
import sys

def get_book_text(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    text = get_book_text(book_path)
    word_count = get_num_words(text)
    char_count = get_total_character(text)
    char_count = sort_dict_by_value(char_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")  
    print("--------- Character Count -------")
    for key, value in char_count.items():
        print(f"{key}: {value}")
    print("============= END ===============")



main()

