import sys
from stats import report

def arg_check(input):# checks if arguments are passed in
    if len(input) > 1:
        return input



def get_book_text(path2file):
    
    try:
        with open(path2file) as f:
            content = f.read()
            return content
    except: FileNotFoundError("File not found..."), IOError("Error reading file...")


def main():

    try:
        input = arg_check(sys.argv[1])
        content = get_book_text(input)
        report(content , input)
    except IndexError:
        print("No file path provided. Please provide a path to the book file. Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    except Exception as e:
        print(e)
    

main()
