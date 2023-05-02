MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

user_choice = input("encode or decode ?")
if user_choice == "encode":
    sentence = input("What sentence u want to convert ?")
    letters = [letter.upper() for letter in sentence]
    def encode():
        encoded = []
        for letter in letters:
            encoded.append(MORSE_CODE_DICT[letter])

        return print(f"Your morse code is {encoded}")
    encode()
elif user_choice == "decode" :
    to_decode = input("What u want to translate ?")
    def decode():
        to_decode_fmt = [letter for letter in to_decode.split(" ")]
        decoded = []
        for code in to_decode_fmt :
            decoded.append(list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(code)])
        return print(f"your translation is {decoded}")
    decode()

