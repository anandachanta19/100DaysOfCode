import pandas

# Converting CSV to DataFrame
data = pandas.read_csv("nato_phonetic_alphabet.csv")
# Creating nato alphabet dictionary
nato = {row.letter: row.code for (index, row) in data.iterrows()}
# Taking user Input
user_input = input("Enter your name: ").upper()
result = [nato[letter] for letter in user_input]
print(result)
