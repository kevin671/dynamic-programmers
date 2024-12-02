import argparse
import os
import random
import re
import string

import numpy as np


# def generate_regex_problem(length: int):
def generate_pattern_from_string(length: int):
    """
    Generates a regex matching problem starting from the input string s.

    Args:
        length (int): Length of the input string s.

    Returns:
        tuple: A tuple containing the input string s and the pattern p.
    """
    # Step 1: Generate the input string s with the specified length
    s = "".join(random.choices(string.ascii_lowercase, k=length))

    # Step 2: Replace 50% or more characters in s with '.' or 'character*'
    modified = list(s)
    for i in range(length):
        if random.random() < 0.5:
            if random.random() < 0.5:
                modified[i] = "."  # Replace with '.'
            else:
                modified[i] = s[i] + "*"  # Replace with 'character*'

    # Step 3: Add random alphabet characters at a random position in the pattern
    additional_chars = "".join(random.choices(string.ascii_lowercase, k=random.randint(0, 2)))
    insert_position = random.randint(0, len(modified))
    modified.insert(insert_position, additional_chars)

    # Create the final pattern
    p = "".join(modified)

    return s, p


def generate_string_from_pattern(length: int):
    """
    Generates an input string s and pattern p starting from p.

    Args:
        length (int): Length of the resulting string s.

    Returns:
        tuple: A tuple containing the input string s and the pattern p.
    """
    # Step 1: Generate the pattern p with random '.', '*', and alphabet characters
    pattern_length = length // 2
    pattern = []
    for _ in range(pattern_length):
        if random.random() < 0.3:
            pattern.append(".")  # Add '.'
        elif random.random() < 0.5:
            pattern.append(random.choice(string.ascii_lowercase) + "*")  # Add 'character*'
        else:
            pattern.append(random.choice(string.ascii_lowercase))  # Add alphabet character

    # Step 2: Generate the string s based on p
    s = []
    for char in pattern:
        if char == ".":
            s.append(random.choice(string.ascii_lowercase))  # Match any character
        elif "*" in char:
            s.extend(random.choices(char[0], k=random.randint(0, 5)))  # Match zero or more of preceding element
        else:
            s.append(char)  # Match the character directly

    # Adjust s to match the desired length
    if len(s) > length:
        s = s[:length]  # Trim the string to the desired length
    else:
        s.extend(random.choices(string.ascii_lowercase, k=length - len(s)))  # Add random characters to reach length

    # Step 3: Modify pattern to match the final string length
    additional_chars = "".join(random.choices(string.ascii_lowercase, k=random.randint(0, 2)))
    insert_position = random.randint(0, len(pattern))
    pattern.insert(insert_position, additional_chars)  # Insert additional characters at a random position

    final_pattern = "".join(pattern)

    return "".join(s), final_pattern


# Example usage
# length = 10
# s, p = generate_pattern_from_string(length)
# print("Input string (s):", s)
# print("Pattern (p):", p)

# print(re.match(p, s) is not None)

# pattern_length = 5
# s, p = generate_string_from_pattern(pattern_length)
##print("Generated string (s):", s)
# print("Generated pattern (p):", p)

# if s is regular expression of p
# print(re.match(p, s) is not None)


parser = argparse.ArgumentParser(description="data")

parser.add_argument("--file", type=str, default="Data")
parser.add_argument("--length", type=int, default=20)
parser.add_argument("--train_size", type=float, default=1e6)
parser.add_argument("--test_size", type=float, default=1e5)

args = parser.parse_args()
np.random.seed(2023)

output_dir = os.path.join(args.file, "decoder")
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

n = 0
with open(os.path.join(output_dir, "train_data.txt"), "w") as f:
    while n < args.train_size:
        s, p = generate_pattern_from_string(args.length)
        label = 1 if re.match(p, s) is not None else 0
        # final = f"{s} | {p} <sep> {label}"
        final = " ".join(s) + " | " + " ".join(p) + " <sep> " + str(label)

        f.write(final + "\n")

        s, p = generate_string_from_pattern(args.length)
        label = 1 if re.match(p, s) is not None else 0
        final = " ".join(s) + " | " + " ".join(p) + " <sep> " + str(label)
        f.write(final + "\n")

        n += 2

n = 0
with open(os.path.join(output_dir, "test_data.txt"), "w") as f:
    while n < args.test_size:
        s, p = generate_pattern_from_string(args.length)
        label = 1 if re.match(p, s) is not None else 0
        final = " ".join(s) + " | " + " ".join(p) + " <sep> " + str(label)
        f.write(final + "\n")

        s, p = generate_string_from_pattern(args.length)
        label = 1 if re.match(p, s) is not None else 0
        final = " ".join(s) + " | " + " ".join(p) + " <sep> " + str(label)
        f.write(final + "\n")

        n += 2
