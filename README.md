# Credit Card Validator
#### Created by Braden Piper, bradenpiper.com
#### Created on Thu Jan 23, 2023
#### Version = 1.0
---
## DESCRIPTION
A program that checks the validity of a credit card number using Luhn's Algorithm.
The program accepts an input of a credit card number, and will calculate if the
number is syntactically valid using Luhn's Algorithm. In addition to checking the
validity of the card number, the program will also identify if the credit card number
is one issued by American Express, Visa, or Mastercard.
---
## INSTRUCTIONS
* There are two versions of this program available to run:
    - credit.c (written in C)
    - credit.py (written in Python)
* Open whichever version you prefer to use, and run it!
---
##### NOTES:
* This program is meant for educational purposes only, and is not meant to be used
as an actual tool for validating credit card numbers.
* This program will only work for credit card numbers of American Express, Visa, and
Mastercard. Credit card numbers issued from other companies will be considered invalid.
* This program will only work with credit card numbers of length 13, 15, or 16 digits.
* This program will only work with Mastercard numbers starting in numbers 51, 52,
53, 54, or 55.
* The C version of this programwas made for the class CS50x = Introduction to Computer Science offered by Harvard University. It uses the cs50 header file which is not a standard header. This header includes the function get_long(), which is used
to accept an integer input from the user.