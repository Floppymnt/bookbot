def get_word_count(content):
    words = content.split()
    return len(words)

def sort_on(items):
    return items["count"]

def count_characters(content):
    # This function counts the number of characters in the content
    # for each letter in content add 1 to the count for that letter in a dictionary
    char_count = {}
    for char in content:
        
        char = char.lower()
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    dictionary_list = []
    for char, count in char_count.items():
        dictionary_list.append({"char": char, "count": count})

    # sort the list by count in descending order
    dictionary_list.sort(reverse=True, key=sort_on)
    return char_count, dictionary_list




def report(content):
    char_count, dictionary_list = count_characters(content)
    print(f"============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...\n----------- Word Count ----------\nFound {get_word_count(content)} total words\n--------- Character Count -------")
    
    #for each dictionary in the list print the char and count but only if isaphabetical
    for item in dictionary_list:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['count']}")
    print("============= END ===============")
    return 