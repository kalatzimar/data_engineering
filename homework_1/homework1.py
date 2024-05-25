# -*- coding: utf-8 -*-
"""
Purpose: Data Engineering Class: Homework 1

Author: Marilena Kalatzi

Date: 22/05/24
"""

# Exercise 1: Create a list of 12 numbers ranging from 1 to 50 
# choosing each unique number no more than twice

numbers = [12,29,50,1,3,22,34,8,42,49,7,25]

# program that prints out all the elements of list: numbers that are less
# than the median of the numbers

# calculate the median of numbers
import statistics

median = statistics.median(numbers)

for num in numbers:
    if num < median:
        print(num)
        
# create array to index

import numpy as np

numbers_array = np.array(numbers)

# create new list with the elements smaller than the median

small_numbers = numbers_array[numbers_array<median]

# print those numbers

print(small_numbers)

# ask user to provide number between 1 and 50 and print elements smaller than this numbers

user_num = input("Provide a number between 1 and 50 please: ")
user_num = int(user_num)

print(f"The elements of the list numbers that are smaller than {user_num} are: {numbers_array[numbers_array<user_num]}")

# Exercise 2: Ask the user  for a one-word string and print out whether the string can also be read backwards, ignoring capitalization

user_word = input("Provide a one word string please: ")

if user_word[::-1] == user_word:
    print("The word you provided can be read backwards")
else:
    print("The word you provided cannot be read backwards")
    
    
    
    