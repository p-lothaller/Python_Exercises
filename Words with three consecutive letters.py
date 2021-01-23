# Returns a list of all words that contain three consecutive letters of the alphabet,
# as found in the file with the given name.
def words_consecutive_letters(filename):
    f = open(filename,'r')
    consec_letter_lst = []
    for words in f:
        lst = []
        word = words.rstrip()
        for letter in word:
            lst.append(ord(letter)-2)
        for i in range(len(lst)-2):
            print(len(lst))
            if lst[i] == (lst[i+1]-1) == (lst[i+2]-2):  
                consec_letter_lst.append(word)
                break
            else:
                i+=1
    return print(consec_letter_lst)
            
            



words_consecutive_letters("one_word.txt")
    
