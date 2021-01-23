
# Returns a list of all words that contain all vowels, as found in the file with the given name.
def words_all_vowels(filename):
    #print(filename)
    f = open(filename, "r")
    lst = []
    vowels = ['a', 'e', 'i', 'o', 'u']
    lines = f.readlines()
    #print(lines)
    for x in lines:
        words = x.split(" ")
        for word in words:
            word = word.rstrip()
            word = word.lower()
            for vowel in vowels:
                if word.find(vowel) == -1:
                    break
            else:
                lst.append(word)

    return print(lst)             
            
                


        
    
  

words_all_vowels('one_word.txt')
