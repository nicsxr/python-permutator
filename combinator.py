from itertools import combinations

s = input("Enter a word: ")

t = list(combinations(s, 2))
text_file = open("output.txt", "w")

for i in range(0, len(t)):
    text_file.write(''.join(t[i]) + "\n")

print(i)

