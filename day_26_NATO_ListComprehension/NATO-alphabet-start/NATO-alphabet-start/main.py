student_dict = {
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
nato_frame = pandas.read_csv('nato_phonetic_alphabet.csv')
#for (index, row) in nato_frame.iterrows():
    #print(row.letter)
nato_comparing = {row.letter:row.code for (index, row) in nato_frame.iterrows()}
print(nato_comparing)
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
name = str(input('digite seu nome: ')).upper()
letter_list = [letter for letter in name]
nato_names = [nato_comparing[row] for row in letter_list]

print(nato_names)
#for index, row in nato_comparing.items():
#    print(row)

emoji_map = {
    "A": "🍎",
    "B": "🐝",
    "C": "🌊",
    "D": "🐬",
    "E": "🐘",
    "F": "🔥",
    "G": "🎸",
    "H": "🏠",
    "I": "🍦",
    "J": "🕹️",
    "K": "🎋",
    "L": "🦁",
    "M": "🌝",
    "N": "🌃",
    "O": "🐙",
    "P": "🥞",
    "Q": "❓",
    "R": "🌈",
    "S": "🐍",
    "T": "🌴",
    "U": "☂️",
    "V": "🎻",
    "W": "🌊",
    "X": "❌",
    "Y": "🪀",
    "Z": "⚡"
}
frase = str(input('digite a frase: ')).upper().strip(" ")
list_frase = [letter for letter in frase]
print(list_frase)
emogi_frase = [emoji_map[emogi] for emogi in list_frase if emogi in emoji_map]
print(emogi_frase)