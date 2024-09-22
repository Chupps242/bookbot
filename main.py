def main():
    book_path = "books/frankenstein.txt"
    with open(book_path) as f:
        file_contents = f.read()
    num_words = get_num_words(file_contents)
    print(f"--- Begin report of {book_path} ---")
    print("  ")
    print(f"{num_words} words found in the document")
    num_chars = get_num_chars(file_contents)
    for i in num_chars:
        print(f"The {i} character was found {num_chars[i]} times")
    print("--- End report ---")

def get_num_words(file_contents):
    words = file_contents.split()
    return len(words)

def get_num_chars(file_contents):
    import string
    alphabet = list(string.ascii_lowercase)
    words = file_contents.lower()
    letters_list = []
    letters_dict = {}
    for words in words:
        if words in alphabet:
            letters_list.append(words)
    for i in alphabet:
        letters_dict[i] = letters_list.count(i)  
    return letters_dict
       
main()
