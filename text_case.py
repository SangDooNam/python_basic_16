"""Task

Write a Python program to convert all the characters in a string to uppercase.
Write a Python program to convert all the characters in a string to lowercase."""


# text = input('Enter any text: ')

# print(f'Original String: {text}')
# print(f'String in uppercase: {text.upper()}')

# text_low1 = text[:18].strip('')
# text_low2 = text[42:].strip('')
# result = text_low1.lower() + text_low2.lower()

# print('String in lowercase:', result.replace('nf', 'n f'))

#-----------------------------------------------------------------

# text = input('Enter any text: ')

# print(f'Original String: {text}')
# print(f'String in uppercase: {text.upper()}')

# index = text.index('X')
# index2 = text.index('n')
# index3 = text.index('!')

# new_text = text[:index2 + 1] +  ' ' + text[15:index + 1] + text[index3:]

# print(f'String in lowercase: {new_text.lower()}')

#-----------------------------------------------------------------

text = input('Enter any text: ')

print(f'Original String: {text}')
print(f'String in uppercase: {text.upper()}')

low_text1 = text[:14 + 1]
low_text2 = text[15:17 + 1]
low_text3 = text[42:]

new_text = low_text1 + ' ' + low_text2 + low_text3

print(f'String in lowercase: {new_text.lower()}')

#-----------------------------------------------------------------

# print(list(enumerate(text)))

"""
[(0, 'T'), (1, 'h'), (2, 'e'), (3, ' '), (4, 'Q'), (5, 'u'), (6, 'i'), (7, 'c'), (8, 'k'), (9, ' '), 
(10, 'B'), (11, 'r'), (12, 'o'), (13, 'W'), (14, 'n'), (15, 'F'), (16, 'o'), (17, 'X'), (18, ' '), (19, 'j'), 
(20, 'u'), (21, 'm'), (22, 'p'), (23, 's'), (24, ' '), (25, 'o'), (26, 'v'), (27, 'e'), (28, 'r'), (29, ' '), 
(30, 't'), (31, 'h'), (32, 'e'), (33, ' '), (34, 'l'), (35, 'a'), (36, 'Z'), (37, 'y'), (38, ' '), (39, 'D'), 
(40, 'o'), (41, 'g'), (42, '!')]
"""

# new_text = ''

# for i in text:
#     if i == i.lower():
#         new_text += i

# print(f'String in lowercase: {new_text}')

