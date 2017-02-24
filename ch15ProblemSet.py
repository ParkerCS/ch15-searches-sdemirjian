'''
Complete the following 3 searching problems using techniques
from class and from Ch15 of the textbook website
'''

#1.  (7pts) Write code which finds and prints the longest
# word in the provided dictionary.  If there are more
# than one longest word, print them all.
import re
def split_line(line):
    #this function takes in a line of text and returns
    #a list of words in the line
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)

file = open("dictionary.txt")

longest = [" "]

for line in file:
    words = split_line(line)
    for word in words:
        if len(word.upper()) > len(longest[0]):
            longest = [word]
        elif len(word) == len(longest[0]):
            longest.append(word)
print(longest)

file.close()
#2.  (10pts)  Write code which finds
# The total word count AND average word length
# in "AliceInWonderLand.txt"
file = open("AliceInWonderLand.txt")

word_count = 0
average = 0

for line in file:
    words = split_line(line)
    for word in words:
        word_count += 1
        average += len(word)
average //= word_count

print("There are", word_count, "words in Alice in Wonderland")
print("The average word length is:", average)

file.close()
# CHOOSE ONE OF THE FOLLOWING TWO PROBLEMS

#3 (13pts)  How many times does "Cheshire" occur in "AliceInWonderLand.txt"?
# How many times does "Cat" occur?
cheshire = 0
cat = 0

file = open("AliceInWonderLand.txt")

for line in file:
    words = split_line(line)
    for word in words:
        if word.upper() == "CHESHIRE":
            cheshire += 1
        elif word.upper() == "CAT":
            cat += 1

print("Cheshire is said", cheshire, "times.")
print("Cat is said", cat, "times.")

file.close()
# How many times does "Cheshire" immediately followed by "Cat" occur?
combo = 0
previous = ""
current = ""

file = open("AliceInWonderLand.txt")

for line in file:
    words = split_line(line)
    for word in words:
        current = word
        if previous.upper() == "CHESHIRE" and current.upper() == "CAT":
            combo += 1
        previous = current

print("Cheshire cat is said", combo, "Times")
file.close()

#### OR #####

#3  (13pts)Find the most frequently occurring
# seven letter word in "AliceInWonderLand.txt"

# Challenge problem (for fun).  What words appear in the text of "Alice in Wonderland" that DO NOT occur in "Alice Through the Looking Glass".  Make a list.  You can substitute this for any of the above problems.



