#Takes user input and returns number of times each letter was used.

user_input = input("Type a word. ").lower()

alpha_dict = {}

for letters in user_input:
        alpha_dict.update({letters : user_input.count(letters)})

print(alpha_dict)