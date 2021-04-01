# Sum Mixed Array: easiest
# Given an array of integers as strings and numbers, return the sum of the array values as if all were numbers.
# Return your answer as a number.

def sum_mix(arr):
  # # keep a running total
  total = 0

  # iterate over every item in the list
  for element in arr:
    # check the type if it is a string
    if type(element) == str:
      total += int(element)
    # add the item to our total
    else:
      total += element

  return total 
  # solution using list comprehension
  # https://www.w3schools.com/python/python_lists_comprehension.asp
  # return sum(int(element) for element in arr)

# Vowel Count: mediumest
# Return the number (count) of vowels in the given string.
# We will consider a, e, i, o, u as vowels for this Kata (but not y).
# The input string will only consist of lower case letters and/or spaces.

def get_count(input_str):
    num_vowels = 0
    # loop over input_str
    vowels = 'aeiou'
    for letter in input_str:
      # check if the letter is in vowels
      if letter in vowels: num_vowels += 1

    return num_vowels

# Convert string to camel case: hardest
# Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case).
# Examples
# "the-stealth-warrior" gets converted to "theStealthWarrior"
# "The_Stealth_Warrior" gets converted to "TheStealthWarrior"

def to_camel_case(text):
    # replace underscores with dashes so the strings can be split
    words = text.replace('_', '-')
    # split the string at dashes and make into a list 
    words = words.split('-')
    # this will be the return string -- start it off with the first word so it doesn't get capitalized
    string = words[0] 
    # loop over the rest of the words and and capitalize them (range 1 - list length)
    for i in range(1, len(words)):
        # add the capitalized words to the string 
        string += words[i].capitalize()
    
    # return the string
    return string

