#
# Test to mask a text
# Written by Zoltan Dul, DMD, Phd
# 2021
#

import string
import random

list_of_sources = [
					string.ascii_letters,
					string.ascii_lowercase,
					string.ascii_uppercase,
					string.digits,
					string.hexdigits,
					string.octdigits,
					string.punctuation,
					string.printable]

#
# CREATING RANDOM MASK FOR A STRING USING RANDOM
#

ascii_change = ""

while len(ascii_change) < len(string.printable):
	random_ascii_character = random.choice(string.printable)
	if (ascii_change.find(random_ascii_character) != -1):
		continue
	else:
		ascii_change = ascii_change + random_ascii_character

print(ascii_change)

#
# Text to test cipher
#

# Test Text
text = "I wanna say that I'm not good at anything. I like to play football and I like to play tennis, however I used to get injured most of the time."

# ENCODE

# String in
s_in = string.printable
# String mask
s_out = ascii_change
# Creating cipher
cipher = str.maketrans(s_in, s_out)
# Encoding text
coded = text.translate(cipher)
# Print to console
print(coded)

# DECODE

# String in
s_in = ascii_change
# String mask
s_out = string.printable
# Creating cipher
cipher = str.maketrans(s_in, s_out)
# Encoding text
decoded = coded.translate(cipher)
# Print to console
print(decoded)

