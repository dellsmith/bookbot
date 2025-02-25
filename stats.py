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

