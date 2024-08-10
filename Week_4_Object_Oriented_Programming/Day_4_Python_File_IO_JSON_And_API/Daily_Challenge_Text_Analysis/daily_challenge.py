class Text:
    def __init__(self, user_text):
        self.user_text = user_text

    def word_frequency(self):
        str_to_words = self.user_text.split(" ")
        unique_words = set(str_to_words)
        for i in unique_words:
            print(f"Frequency of {i} is : {str_to_words.count(i)}")

    def most_common_word(self):
        str_to_words = self.user_text.split(" ")
        unique_words = set(str_to_words)
        word_frequency = {}
        for i in unique_words:
            word_frequency[i] = str_to_words.count(i)
        max_val = max(word_frequency.values())
        most_common = []
        for k, v in word_frequency.items():
            if v == max_val:
                most_common.append(k)
        print(f"Most common word(s) is: {", ".join(
            most_common)} it`s mentioned {max_val} times")

    def unique_words(self):
        str_to_words = self.user_text.split(" ")
        unique_words = set(str_to_words)
        return list(unique_words)

    @classmethod
    def from_file(cls, filename):
        with open(filename) as file:
            data = file.read()
            return cls(data)

# Part 1


text1 = Text("A good book would sometimes cost as much as a good house.")
text1.word_frequency()
text1.most_common_word()
print(text1.unique_words())

# Part 2

new_text = Text.from_file(
    r"C:\Users\Leo\Course_in_Data_Analyse\Week_4_Object_Oriented_Programming\Day_4_Python_File_IO_JSON_And_API\Daily_Challenge_Text_Analysis\the_stranger.txt")
new_text.most_common_word()
print(f"List of unique words from text: {text1.unique_words()}")
