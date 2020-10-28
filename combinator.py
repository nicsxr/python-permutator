from itertools import combinations

s = input("Enter a word: ")
c = int(input("How many letters? "))

if(c>len(s)):
     c = len(s)
        
t = list(combinations(s, c))
text_file = open("output.txt", "w")

for i in range(0, len(t)):
    text_file.write(''.join(t[i]) + "\n")

print(i+1)

