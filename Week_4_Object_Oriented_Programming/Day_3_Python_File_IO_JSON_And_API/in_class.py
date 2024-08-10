with open(r"C:\Users\Leo\Course_in_Data_Analyse\Week_4_Object_Oriented_Programming\Day_3_Python_File_IO_JSON_And_API\nameslist.txt") as f:
    # all_lines = f.read()
    # print(all_lines)
    lines = f.readlines()
    fifth_line = lines[4]
    print(fifth_line)
    first_five = f.read(5)
    print(fifth_line)
    # list_of_names = [i for i in all_lines]
    # # splited_list_of_names = [i.split('') for i in all_lines]


def count(name):
    x = 0
    for n in all_lines:
        if name == n:
            x += 1
    return x


count("Darth")
count("Luke")
count("Lea")

# f.write('\nLeonid')

