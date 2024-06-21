#1 Sorting

# Instructions
# Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
# Use List Comprehension

def sorting():
    user_input=input("Enter your words using `,`...")
    output=sorted([word for word in user_input.split(",")])
    return output
print(sorting())

#2 Longest Word

# Write a function that finds the longest word in a sentence. If two or more words are found, return the first longest word.
# Characters such as apostrophe, comma, period count as part of the word (e.g. O’Connor is 8 characters long).

def longest_word(sentence):
    longest_word=""
    for word in sentence.split(" "):
        if len(word)>len(longest_word):
            longest_word=word
    return (f"The longest word in `{sentence}` is {longest_word}")
print(longest_word("Margaret's toy is a pretty doll."))
print(longest_word("A thing of beauty is a joy forever."))
print(longest_word("Forgetfulness is by all means powerless!"))