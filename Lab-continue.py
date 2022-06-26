final_word = ""
user_word = input("Enter word ")# Prompt the user to enter a word
user_word = user_word.upper()# and assign it to the user_word variable.

for letter in user_word:
    if letter in "AEIOU":
        continue
    else:
        final_word +=letter# Complete the body of the for loop.
print(final_word)
    
