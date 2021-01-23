
# Reads the contents of the specified file and creates a dictionary with the number of occurrences for each word.
def word_frequencies(filename):
    f = open(filename,'r')
    dictionary = {}
    lst = []
    for line in f:
            line = line.rsplit()
            for word in line:
                word = word.lower()
                if word in dictionary:
                    dictionary[word] +=1
                else:
                    dictionary[word] = 1
           
    return dictionary





#            for words in line:
#                lst.append(words.rstrip().lower())
#        else:
#            lst.append(line.rstrip().lower())
#    for word in lst:
#        dictionary[word] = lst.count(word)
#    if lst == []:
#        dictionary = dict()
#        return dictionary
#    else:
#       return dictionary
        

word_frequencies("emptyline.txt")
word_frequencies("multiline.txt")


