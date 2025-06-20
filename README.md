# Morse Code Translator
This script translates a line of English text into Morse code. It filters out invalid characters and outputs the corresponding Morse code for each valid character. The script begins by prompting the user to enter a line of text. It then filters the input to include only valid characters (letters and spaces) using a regular expression. Each valid character is converted to Morse code using a predefined dictionary. The Morse code for each character is printed, separated by spaces.
## Example Usage
Run the script using Python:
python standardInputs.py
Sample Input:
Enter your text: Hello World
Sample Output:
.... . .-.. .-.. --- / .-- --- .-. .-.. -..
## Code Explanation
The script uses the following dictionary to map each letter and space to its corresponding Morse code:
morse = {
    'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.',
    'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---',
    'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---',
    'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-',
    'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--',
    'z': '--..', ' ': '/'
}
The user input is processed character by character. A regular expression is used to filter out invalid characters, allowing only letters (a-z, A-Z) and spaces. Each valid character is converted to Morse code using the dictionary. If a character is not found in the dictionary, it is replaced with ?. The Morse code for each character is printed immediately, separated by spaces.
## Requirements
Python 3.x
## License
No license specified. Use for educational purposes.
