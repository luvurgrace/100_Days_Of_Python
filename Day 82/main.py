"""
Morse Code Translator
=====================
A simple program to encode and decode Morse code.

Author: Lutik Nikita
GitHub: https://github.com/luvurgrace
"""

MORSE_CODE_DICT = {
    # Letters
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
    'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    # Numbers
    '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.',
    # Punctuation
    '.': '.-.-.-', ',': '--..--', '?': '..--..', '!': '-.-.--',
    '-': '-....-', '/': '-..-.', '(': '-.--.', ')': '-.--.-',
    "'": '.----.', '"': '.-..-.', ':': '---...', ';': '-.-.-.',
    # Space
    ' ': '/'
}

REVERSE_DICT = {value: key for key, value in MORSE_CODE_DICT.items()}


def encode_to_morse(text: str) -> str:
    """Convert plain text to Morse code."""
    result = []
    for char in text.upper():
        if char in MORSE_CODE_DICT:
            result.append(MORSE_CODE_DICT[char])
        else:
            result.append(char)  # Keep unknown characters
    return ' '.join(result)


def decode_from_morse(morse_code: str) -> str:
    """Convert Morse code to plain text."""
    result = []
    for code in morse_code.split(' '):
        if code in REVERSE_DICT:
            result.append(REVERSE_DICT[code])
        elif code == '':
            continue  # Skip empty strings
        else:
            result.append(code)  # Keep unknown codes
    return ''.join(result)


def morse_translator(text: str, mode: str) -> str:
    """
    Translate text to/from Morse code.

    Args:
        text: The input text to translate
        mode: 'encode' or 'decode'

    Returns:
        Translated string
    """
    if mode == 'encode':
        return encode_to_morse(text)
    elif mode == 'decode':
        return decode_from_morse(text)
    else:
        raise ValueError("Mode must be 'encode' or 'decode'")


def main():
    """Main program loop."""
    print("=" * 40)
    print("   MORSE CODE TRANSLATOR")
    print("=" * 40)

    while True:
        # Get user input
        print("\nOptions: 'encode' | 'decode' | 'quit'")
        mode = input("Choose mode: ").lower().strip()

        if mode == 'quit':
            print("\nGoodbye! 👋")
            break

        if mode not in ('encode', 'decode'):
            print("❌ Invalid option. Try again.")
            continue

        text = input("Enter your message: ")

        if not text:
            print("❌ Empty message. Try again.")
            continue

        # Translate and display result
        try:
            result = morse_translator(text, mode)
            print(f"\n✅ Result: {result}")
        except Exception as e:
            print(f"❌ Error: {e}")


if __name__ == "__main__":
    main()
