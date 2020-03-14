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
parser.add_argument("--min-lower", type=int, default=1,
                    help="minimum number of lowercase letters")
parser.add_argument("--min-upper", type=int, default=1,
                    help="minimum number of uppercase letters")
parser.add_argument("--min-number", type=int, default=1,
                    help="minimum number of numeric characters")
parser.add_argument("--min-special", type=int, default=1,
                    help="minimum number of special characters")
parser.add_argument("--special", type=str,
                    help="\"\"-enclosed chars to use instead of punctuation")


def main(arguments):
    args = parser.parse_args(arguments)

    # Sanity check that sum of minimum char counts is not larger than
    # specified password length.
    if sum([args.min_lower, args.min_upper,
            args.min_number, args.min_special]) > args.length:
        raise ValueError(f"Cannot create password of length {args.length} "
                         f"and satisfy other given criteria.")

    # Store the allowed alphabets in a dictionary with integer keys
    allowed_chars = dict()
    pw = ""

    if args.min_lower > 0:
        allowed_chars[len(allowed_chars)] = string.ascii_lowercase
        pw += "".join(random.choices(string.ascii_lowercase, k=args.min_lower))
    if args.min_upper > 0:
        allowed_chars[len(allowed_chars)] = string.ascii_uppercase
        pw += "".join(random.choices(string.ascii_uppercase, k=args.min_upper))
    if args.min_number > 0:
        allowed_chars[len(allowed_chars)] = string.digits
        pw += "".join(random.choices(string.digits, k=args.min_number))
    if args.min_special > 0:
        if not args.special:
            allowed_chars[len(allowed_chars)] = string.punctuation
            pw += "".join(random.choices(string.punctuation, k=args.min_special))
        else:
            allowed_chars[len(allowed_chars)] = args.special
            pw += "".join(random.choices(args.special, k=args.min_special))

    if not allowed_chars:
        raise ValueError(f"Cannot create password of length {args.length} "
                         f"with no allowed characters.")

    # Get the password up to the final length with randomly chosen chars
    # from randomly chosen allowed alphabets
    while len(pw) < args.length:
        key = random.randrange(0, len(allowed_chars))
        pw += random.choice(allowed_chars[key])

    # Shuffle the password a few (0-10) times by using random sampling on
    # the password without replacement
    times = random.randint(0, 10)
    while times > 0:
        pw = "".join(random.sample(pw, len(pw)))
        times -= 1

    print(pw)


if __name__ == "__main__":
    main(sys.argv[1:])
