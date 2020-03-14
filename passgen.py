"""
Generator for simple or complex passwords.
"""
import argparse
import random
import string
import sys


parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--length", type=int, default=12,
                    help="number of characters in password")
parser.add_argument("--no-lower", action="store_true",
                    help="don't use lowercase letters")
parser.add_argument("--no-upper", action="store_true",
                    help="don't use uppercase letters")
parser.add_argument("--no-number", action="store_true",
                    help="don't use numeric characters")
parser.add_argument("--no-special", action="store_true",
                    help="don't use special characters")

def main(arguments):
    args = parser.parse_args(arguments)
    password = ""

    allowed_chars = []
    if not args.no_lower:
        allowed_chars.extend(string.ascii_lowercase)
    if not args.no_upper:
        allowed_chars.extend(string.ascii_uppercase)
    if not args.no_number:
        allowed_chars.extend(string.digits)
    if not args.no_special:
        allowed_chars.extend(string.punctuation)

    if not allowed_chars:
        raise ValueError("Cannot generate password with 0 allowed characters.")

    print("".join(random.choices(allowed_chars, k=args.length)))


if __name__ == "__main__":
    main(sys.argv[1:])
