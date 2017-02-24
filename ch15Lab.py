'''
Complete the chapter lab at http://programarcadegames.com/index.php?chapter=lab_spell_check
'''
import re
 
def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)

file = open("dictionary.txt")

word_list = []

for line in file:
    words = split_line(line)
    for word in words:
        word_list.append(word)

file.close()

print(" === Linear Search === ")
file = open("AliceInWonderLand200.txt")
line_number = 0
for line in file:
    line_number += 1
    words = split_line(line)
    for word in words:
        key = word
        for i in range(len(word_list)):
            if key.upper() == word_list[i]:
                break
        else:
            print("Possible misspelling at line", line_number,":", key)

file.close()

print(" === Binary Search === ")
file = open("AliceInWonderLand200.txt")
line_number = 0
upper_bound = len(word_list) - 1
lower_bound = 0
found = False
for line in file:
    line_number += 1
    words = split_line(line)
    for word in words:
        key = word
        while lower_bound <= upper_bound and not found:
            middle_position = (lower_bound + upper_bound) // 2

            if word_list[middle_position] < key.upper():
                lower_bound = middle_position + 1
            elif word_list[middle_position] > key.upper():
                upper_bound = middle_position - 1
            else:
                found = True

        if not found:
            print("Possible misspelling at line", line_number, ":", key)
        found = False
        upper_bound = len(word_list) - 1
        lower_bound = 0
file.close()