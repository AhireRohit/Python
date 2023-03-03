# Below program is used to find double spaces

b = "Hello  my    name is"
print(b.find("  "))                 # Find double spaces
print(b.replace("  ", "    "))      # Find double spaces and replace with triple space

# replace(oldword, newword) : This function replaces the old word with the new word in the entire string.

letter = '''Dear <|NAME|>,
            Greetings from Python coders,
            You are selected!
            <|DATE|>'''

name = input("Enter name: ")
date = input("Enter date: ")
# print(letter)
letter = letter.replace("<|NAME|>", name)
letter = letter.replace("<|DATE|>", date)
print(letter)

# Use of escape Sequence

l = "Dear Harry,\n \t This Python course in nice.\n Thanks!!"
print(l)