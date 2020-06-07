def word_count_dict(filename):
   
    word_count = {}  
    file = open('c:/Users/AUSU/Downloads/google-python-exercises/google-python-exercises/basic/alice.txt', 'r')
    
    for line in input_file:
        words = line.split()
   
    for word in words:
        word = word.lower()
        
        if not word in word_count:
            word_count[word] = 1
        else:
            word_count[word] = word_count[word] + 1
   
    file.close()
    print (word, word_count[word])
    return word_count
    
    
def print_words(filename):
    word_count = word_count_dict(filename)
    words = sorted(word_count.keys())
    for word in words:
        print (word, word_count[word])
        
        
        
def get_count(word_count_tuple):
return word_count_tuple[1]



def print_top(filename):
    word_count = word_count_dict(filename)

    items = sorted(word_count.items(), key=get_count, reverse=True)
    for item in items[:20]:
        print (item[0], item[1])
