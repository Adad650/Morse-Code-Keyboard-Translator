import re

morse = {
    'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.',
    'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---',
    'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---',
    'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-',
    'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--',
    'z': '--..', ' ': '/'
}

text = input("Enter your text: ")

# Extract letters and spaces using regex and a for loop
filtered = []
for char in text:
    if re.match(r'[a-zA-Z ]', char):
        filtered.append(char)

# Convert each filtered character to Morse
for letter in filtered:
    code = morse.get(letter.lower(), '?')
    print(code,end=' ')
