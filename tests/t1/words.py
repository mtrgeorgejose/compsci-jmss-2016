# Write a program to read in words from the keyboard one at a time until the word "quit" is typed.
# Store them in a list then print them alphabetically
list_words =[]
word = (input(">>>"))
while word != "quit":
    if word == "quit":
        pass
    else:
        list_words.append(word)
        word = (input(">>>"))

list_words.sort()
print(list_words)