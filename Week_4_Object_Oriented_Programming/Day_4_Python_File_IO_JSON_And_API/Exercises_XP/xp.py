# Exercise 1 – Random Sentence Generator
import json
import random


def get_words_from_file():
    with open(r"C:\Users\Leo\Course_in_Data_Analyse\Week_4_Object_Oriented_Programming\Day_4_Python_File_IO_JSON_And_API\Exercises_XP\sowpods.txt") as file:
        data = file.read()
        all_words = data.split("\n")
        return all_words


def get_random_sentence(all_words, length):
    random_words = random.sample(all_words, length)
    sentence = " ".join(random_words).lower()
    return sentence


def main():
    print("""Welcome to a Random Sentence Generator!
You should choose number in between 2 and 20, that will be length of your sentence.
          """)
    length = int(input("Plese select your number..."))
    if isinstance(length, int) and length in range(2, 21):
        output = ""
        all_words = get_words_from_file()
        output = get_random_sentence(all_words, length)
        print(f"Here your sentence: {output}")
    else:
        print("Wrong input value.")


main()

# Exercise 2: Working With JSON
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""
data = json.loads(sampleJson)
salary = data["company"]["employee"]["payable"]["salary"]
data["company"]["employee"]["birthdate"] = "29/02/1995"
with open(r'C:\Users\Leo\Course_in_Data_Analyse\Week_4_Object_Oriented_Programming\Day_4_Python_File_IO_JSON_And_API\Exercises_XP\sample_json.json', 'w') as outfile:
    json.dump(data, outfile, indent=4)
