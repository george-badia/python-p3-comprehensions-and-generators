#!/usr/bin/env python3

def return_evens(num_list):
    #Returns a list of even numbers from the input list.
    return [num for num in num_list if num % 2 == 0]

def make_exclamation(sentence_list):
    #Adds an exclamation mark at the end of each sentence in the input list.~
    return [sentence + '!' for sentence in sentence_list]