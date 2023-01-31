import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")  # Imports the CSV data as a Pandas DataFrame
data_dict = {row.letter: row.code for (index, row) in data.iterrows()}  # Converts it into the following dictionary:
# {"A": "Alfa", "B": "Bravo"...}


def generate_phonetic():
    name = input("What is your name?: ").upper()
    try:
        nato_name = [data_dict[char] for char in name]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(nato_name)


generate_phonetic()
