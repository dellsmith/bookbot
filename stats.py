FRANKENSTEIN_FILE = "books/frankenstein.txt"
def main():
    with open("~/workspace/bookbot/books/frankenstein.txt") as f:
        file_contents = f.read()

def count_words():
    word_count = 0
    with open(FRANKENSTEIN_FILE) as f:
        frankenstein_text = f.read()
        words = frankenstein_text.split()
        word_count = len(words)
    return word_count         

def character_count():
    char_dict = {}
    with open(FRANKENSTEIN_FILE) as f:
        frankenstein_text = f.read()
    lowered_text = frankenstein_text.lower()
    for character in lowered_text:
        if character not in char_dict:
            char_dict[character] = 1
        else:
            char_dict[character] += 1 
    return char_dict

def report():
    print(f"--- Begin report of {FRANKENSTEIN_FILE} ---")
    number_words = f"{count_words()} words found in the document"
    print(number_words)
    char_dict = character_count()
    char_list = []
    for char, count in char_dict.items():
        if char.isalpha():
            char_list.append({"char":char,"num": count})
    def sort_on(char_list):
        return char_list["num"]
    char_list.sort(reverse=True, key=sort_on)
    for character in char_list:
        print(f"{character["char"]}: {character["num"]}")    


report()