def get_word_count(book_string):
    book_as_list = book_string.split()
    return len(book_as_list)

def char_count(book_string):
    char_dict = {}
    lower_string = book_string.lower()
    for char in lower_string:
        is_char_present = char in char_dict
        if is_char_present:
            char_dict[char] += 1 
        elif char != " ":
            char_dict[char] = 1
    del char_dict["\n"]
    return char_dict

def sort_on(dict):
    for char in dict:
        return dict[char]
    
def report(word_count, char_dict, path):
    sorted_dict = sorted(char_dict.items(), key=lambda x: x[1], reverse=True) 
    print(f"============ BOOKBOT ============\nAnalyzing book found at {path}")
    print(f"----------- Word Count ----------\nFound {word_count} total words\n--------- Character Count -------")
    for char in sorted_dict:
            print(char[0] + f": {char[1]}")
    print("============= END ===============")

