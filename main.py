# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

from itertools import count


def read_file_content(filename):
    #[assignment] Add your code here 
        with open("story.txt",'r') as file:
          data = file.read()
          print(data)
          return (data)

read_file_content(filename="story.txt")


def count_words():
    text = read_file_content("story.txt")
    # [assignment] Add your code here
    words_of_text = text.split()
    count = dict()

    for word in words_of_text:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1

    return count
a = count_words()
print(a)





    

          
         
    

