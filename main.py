def main():
    book_path = "books/frankenstein.txt"
    print(f"--- Begin report of {book_path} ---")
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document\n")
    get_num_char(text)
    print("--- End report ---")
    
    
def get_book_text(path):
        with open(path) as f:
            file_contents = f.read()
        return file_contents

def get_num_words(text):
     words = text.split()
     return len(words)

def get_num_char(text):
     char = {}
     letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
     words = text.split()
     for word in words:
        for w in word:
            letter = w.lower()
            if letter in char and letter in letters:
                char[letter] += 1
            elif letter not in char and letter in letters:
                char[letter] = 1

     for c in char:
        print(f"The '{c}' character was found {char[c]} times")
     
     return char


main()
