#Takes user phrase and returns number of times each word was used

user_input = input("Type a phrase here, making sure to use some words at least twice. ").lower()

input_list = user_input.split(" ")
word_count = {}

for words in input_list:
   word_count.update({words: user_input.count(words)})

print(word_count)