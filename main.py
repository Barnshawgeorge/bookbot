def read_words():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        return file_contents

def count_words():
    count = 0
    x = read_words()
    x = x.split()
    for i in x:
        count += 1
    return count
    

def count_chars():
    char_list = []
    char_dic = {}
    all_chars = read_words().lower()

    for i in all_chars:
        char_list.append(i)
           
    for i in char_list:
           if(i in char_dic):
               char_dic[i] += 1
           if(i not in char_dic):
               char_dic[i] = 1
    return char_dic

def report():
    char_dic = count_chars()
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count_words()} words found in the document")
    for i in char_dic.items():
        if(i[0].isalpha()):
            print(f"The '{i[0]}' character was found {i[1]} times")

        


        
    



read_words()
count_words()
count_chars()
report()