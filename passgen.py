"""
Generator for simple or complex passwords.
"""

import sys
import argparse
import random

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--length", type=int, default=12,
                    help="number of characters in password")
parser.add_argument("--no-lower", action="store_true",
                    help="don't use lowercase letters")
parser.add_argument("--no-upper", action="store_true",
                    help="don't use uppercase letters")
parser.add_argument("--no-numer", action="store_true",
                    help="don't use numeric characters")
parser.add_argument("--no-special", action="store_true",
                    help="don't use special characters")

lower = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
         "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
upper = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N",
         "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
numer = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
special = ["?", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "+"]


def main(arguments):
    args = parser.parse_args(arguments)
    password = ""

    allowed_chars = list()
    if args.no_lower is False:
        for char in lower:
            allowed_chars.append(char)
    if args.no_upper is False:
        for char in upper:
            allowed_chars.append(char)
    if args.no_numer is False:
        for char in numer:
            allowed_chars.append(char)
    if args.no_special is False:
        for char in special:
            allowed_chars.append(char)

    if len(allowed_chars) == 0:
        raise ValueError("Cannot generate password with 0 allowed characters.")

    while len(password) < args.length:
        password += random.choice(allowed_chars)

    print(password)


if __name__ == "__main__":
    main(sys.argv[1:])
