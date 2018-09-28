#!/usr/bin/python
def encodedJS(decimal_string):
    decimal_string = raw_input(">>> ") 
    for char in decimal_string:
        decimal_string += str(ord(char)) + ","
    return decimal_string[:-1]

print encodedJS("")
