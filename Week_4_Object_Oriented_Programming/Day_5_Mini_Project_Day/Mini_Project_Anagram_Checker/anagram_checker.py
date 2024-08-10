class AnagramChecker:
    def __init__(self, adress):
        with open(adress) as file:
            self.file = file.read().split("\n")
            self.anagram_groups = {}
            for word in self.file:
                sorted_word = ''.join(sorted(word))
                self.anagram_groups.setdefault(sorted_word, []).append(word)

    @classmethod
    def is_valid_word(cls, word):
        if word.isalpha():
            return word
        else:
            raise ValueError("Your input contain not only letters..")

    def get_anagrams(self, word):
        if self.is_anagram(word):
            k = self.is_anagram(word)
            return self.anagram_groups[k]

    def is_anagram(self, word):
        for k in self.anagram_groups.keys():
            if k.lower() == ''.join(sorted(word.lower())):
                return k


if __name__ == "__main__":
    anagram1 = AnagramChecker(
        "Week_4_Object_Oriented_Programming\Day_5_Mini_Project_Day\Mini_Project_Anagram_Checker\sowpods.txt")
    print(anagram1.get_anagrams("Meat"))
