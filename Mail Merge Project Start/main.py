# Getting Letter from the file
with open("Input/Letters/starting_letter.txt", 'r') as sample:
    data = sample.read()

# Getting names from the names file
with open('Input/Names/invited_names.txt', 'r') as name_file:
    names = []
    for line in name_file:
        names.append(line)

# Deleting the new line from the retrieved names
for i in range(len(names)):
    if i != len(names) - 1:
        names[i] = names[i][0:len(names[i]) - 1]

# Creating the modified letters
for name in names:
    with open(f'Output/ReadyToSend/letter_for_{name}.txt', 'w') as letter:
        modified_letter = data.replace("[name]", name)
        letter.write(modified_letter)
