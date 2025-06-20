import sys, tty, termios
import re

morse = {
    'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.',
    'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---',
    'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---',
    'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-',
    'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--',
    'z': '--..', ' ': '/'
}

def get_char():
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)  # Save terminal settings
    try:
        tty.setraw(fd)            # Set terminal to raw mode (no Enter needed)
        ch = sys.stdin.read(1)    # Read one character
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old)  # Restore settings
    return ch

print("Press keys to translate to Morse code (Ctrl+C to quit):")

while True:
    char = get_char()
    if re.match(r'[a-zA-Z ]', char):           # Only letters and space
        code = morse.get(char.lower(), '?')    # Lookup Morse or ? if unknown
        print(code, end=' ', flush=True)       # Print Morse immediately
