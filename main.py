import sys
from stats import get_word_count
from stats import count_characters
from stats import report

def arg_check(input):
    if len(input) > 1:
        return input
    else:
        raise ValueError("No Argument given. Please pass in a path to book file. USAGE: python3 main.py <bookname>")


def get_book_text(path2file):
    
    try:
        with open(path2file) as f:
            content = f.read()
            return content
    except: FileNotFoundError("File not found...")



def main2():
    try:
        input = "books/frankenstein.txt"

        content = get_book_text(input)
        report(content)

    except Exception as e:
        print(e)




main2()


















def main():

    try:
        input = arg_check(sys.argv)
        content = get_book_text(input)
        return content
    except Exception as e:
        print(e)

# main()