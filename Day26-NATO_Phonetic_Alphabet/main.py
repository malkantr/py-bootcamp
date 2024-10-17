# Keyword Methods()
# new_dict = {new_key:new_value for (index, row) in df.iterrows()}

# for (key, value) in df.items():
# for (index, row) in df.iterrows():

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

print("\nto_dict() method")
test_dict = data.to_dict()
print(test_dict)

print("\niterrows() method")
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

word = input("\nEnter a word: ").upper()
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)
