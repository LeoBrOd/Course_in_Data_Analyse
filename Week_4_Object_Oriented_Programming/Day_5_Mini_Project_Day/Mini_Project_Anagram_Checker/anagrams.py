from anagram_checker import AnagramChecker
text = AnagramChecker(
    "Week_4_Object_Oriented_Programming\Day_5_Mini_Project_Day\Mini_Project_Anagram_Checker\sowpods.txt")


def main():
    while True:
        print("Menu:")
        print("E - Enter a word")
        print("X - Exit")
        choice = input("Enter your choice (`E` or `X`): ")
        if choice.lower() == 'e':
            word = input("Enter a word: ")
            output = f"Anagrams for your word:{
                ', '.join(text.get_anagrams(word))}"
            if AnagramChecker.is_valid_word(word):
                print(f"{"-"*len(output)}\nYour word: {
                      word}\nThis is a valid English word.\n{output}\n{"-"*len(output)}")

        elif choice.lower() == 'x':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter `E` or `X`.")


main()
