"""Count words in file."""


# put your code here.
#count how many times each space separated word appears in file
#commas etc included

def count_words_in_file(file_name):
    file_to_open = open(file_name)
    word_counts= {}

    
    for line in file_to_open:
        line = line.rstrip()
        word_list = line.split(" ")   #this creates a list, not a string
        for word in word_list:
            word_counts[word] = word_counts.get(word, 0) +1 

    print(word_counts)
    



    

    

count_words_in_file("test.txt")



