import re


with open('text.txt') as file:
    lines = file.readlines()

for count,line in enumerate(lines):
    sum_of_chars = sum([1 for word in line.split() for letter in word if letter in r'-,\.!?\''])
    sum_of_letters = sum([len(word) for word in line.split()]) - sum_of_chars

    print(f'Line {count + 1}: {line} ({sum_of_letters})({sum_of_chars})')