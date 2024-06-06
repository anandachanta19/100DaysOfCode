import pandas

codes = None


def user_input():
    # Taking user Input
    global codes
    name = input("Enter your name: ").upper()
    try:
        codes = [nato[letter] for letter in name]
    except KeyError:
        print("Sorry only alphabets are allowed!")
        user_input()
    finally:
        return codes


# Converting CSV to DataFrame
data = pandas.read_csv("nato_phonetic_alphabet.csv")
# Creating nato alphabet dictionary
nato = {row.letter: row.code for (index, row) in data.iterrows()}
result = user_input()
print(result)
