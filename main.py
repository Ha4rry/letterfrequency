import matplotlib.pyplot as plt

letters="abcdefghijklmnopqrstuvwxyz"
input_file_name=input("Location of input file?: ")
with open(input_file_name, 'r') as input_file:
    string = input_file.read().lower()
char_amounts={}
for char in string:
    if char in letters:
           
        if char not in char_amounts:
            char_amounts[char] = 1
        else:
            char_amounts[char] += 1

print(char_amounts)


xpoints = sorted(list(char_amounts.keys()), key=lambda x: char_amounts[x], reverse=True)
ypoints = list(map(lambda x: char_amounts[x], xpoints))

plt.figure(figsize=(12,6), dpi=300)
plt.bar(xpoints, ypoints)

plt.xlabel("Letter")
plt.ylabel("Amount of times it appeared")
plt.title(str("Letter frequency in a given text\n(Input File: "+input_file_name+")"))

plt.savefig(str("graph_"+input_file_name+"_letters.png"))

plt.show()
