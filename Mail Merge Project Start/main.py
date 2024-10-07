# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".
    
# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)

# my code
# initialize list
# names = []

# open txt and put names in list and strip \n from text
# with open(".\\Input\\Names\\invited_names.txt", 'rt') as names_files:
#     for name in names_files:
#         names.append(name.strip("\n"))
# loop through and create files




# for people in names:
#     with open(".\\Input\\Letters\\starting_letter.txt", "r") as file1:
#         with open(f".\\Output\\ReadyToSend\\letter_for_{people}.txt", "w") as file2:
#             for line in file1:
#                 file2.write(line)
#             file2.close()
#             file1.close()
#
#
# # loop through names list and replace string in test files created previously with [Name] with names for m list
# for name in names:
#     with open(f".\\Output\\ReadyToSend\\letter_for_{name}.txt", "r") as file3:
#         data = file3.read()
#         data = data.replace('[name]', name)
#         with open(f".\\Output\\ReadyToSend\\letter_for_{name}.txt", "w") as file4:
#             file4.write(data)
#         file3.close()
#         file4.close()

# for name in names:
#     with open(".\\Input\\Letters\\starting_letter.txt", "r") as file1, open("")
# names = open(".\\Input\\Names\\invited_names.txt", 'r')
# print(names.readlines())
# with open(".\\Input\\Names\\invited_names.txt", 'rt') as file:
#     with open(".\\Input\\Letters\\starting_letter.txt", "rt") as file2:
#         for name in file:
#             x = open(f".\\input\\output\\ReadyToSend\\{name}.txt") as file3:
#                 name.replace("[Name]", name)
#                 print(file)
