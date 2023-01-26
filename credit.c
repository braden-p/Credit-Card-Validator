/* Credit Card Validator
Created by Braden Piper, bradenpiper.com
Created on Thu Jan 16, 2023
Version = 1.0
------------------------------------------
DESCRIPTION:
A program that checks the validity of a credit card number using Luhn's Algorithm.
The program accepts an input of a credit card number, and will calculate if the
number is syntactically valid using Luhn's Algorithm. In addition to checking the
validity of the card number, the program will also identify if the credit card number
is one issued by American Express, Visa, or Mastercard.
------------------------------------------
NOTES:
• This program was made for the class CS50x = Introduction to Computer Science
offered by Harvard University. It uses the cs50 header file which is not a
standard header. This header includes the function get_long(), which is used
to accept an integer input from the user.
• This program is meant for educational purposes only, and is not meant to be used
as an actual tool for validating credit card numbers.
• This program will only work for credit card numbers of American Express, Visa, and
Mastercard. Credit card numbers issued from other companies will be considered invalid.
• This program will only work with credit card numbers of length 13, 15, or 16 digits.
• This program will only work with Mastercard numbers starting in numbers 51, 52,
53, 54, or 55. */



#include <cs50.h>
#include <stdio.h>

int getlength(long num)
{
    int length = 0;
    while (num != 0)
    {
        num = num / 10;
        length++;
    }
    return length;
}

int getlastdigit(long ccnum)
{
    int lastdigit = ccnum % 10;
    return lastdigit;
}

long shorten(long ccnum)
{
    long shorter = ccnum / 10;
    return shorter;
}

long getfirstdigit(long ccnum)
{
    int numlength = getlength(ccnum);
    for (int i = 0; i < (numlength - 1); i++)
    {
        ccnum = shorten(ccnum);
    }
    return ccnum;
}

long getfirst2digits(long ccnum)
{
    int numlength = getlength(ccnum);
    for (int i = 0; i < (numlength - 2); i++)
    {
        ccnum = shorten(ccnum);
    }
    return ccnum;
}

int main(void)
{
    // get credit card number
    long ccnum;
    ccnum = get_long("Credit Card Number: ");

    // get length of the credit card number
    int cclength = getlength(ccnum);

    // check if a valid cc length, if not, print INVALID
    if (cclength == 13 || cclength == 15 || cclength == 16)
    {
        int sum = 0;
        long ccnumb = ccnum;
        for (int i = 0; i < cclength; i++)
        {
            // get last digit, add it to sum
            int lastdigit = getlastdigit(ccnumb);
            sum += lastdigit;

            // shorten ccnumb by 1
            ccnumb = shorten(ccnumb);

            // get last digit, multiply by 2
            lastdigit = getlastdigit(ccnumb);
            long nextnum = lastdigit * 2;
            // get length of nextnum
            int nextnumlength = getlength(nextnum);
            if (nextnumlength == 1)
            {
                sum += nextnum;
            }
            else
            {
                // get last digit, add it to sum
                int nextnumlastdigit = getlastdigit(nextnum);
                sum += nextnumlastdigit;
                // shorten by 1 digit
                long nextnumshorter = shorten(nextnum);
                // get last digit, add it to sum
                int finaldigit = getlastdigit(nextnumshorter);
                sum += finaldigit;
            }
            // shorten ccnumb by 1
            ccnumb = shorten(ccnumb);
        }
        // get last digit of sum
        int lastdigitsum = getlastdigit(sum);
        // if last digit of sum == 0
        if (lastdigitsum == 0)
        {
            // get first digit
            long firstdigit = getfirstdigit(ccnum);
            if (firstdigit == 4)
            {
                printf("VISA\n");
            }
            else
            {
                // get first two digits (prefix)
                long prefix = getfirst2digits(ccnum);
                if (prefix == 34 || prefix == 37)
                {
                    printf("AMEX\n");
                }
                else if (prefix > 50 && prefix < 56)
                {
                    printf("MASTERCARD\n");
                }
                else
                {
                    printf("INVALID\n");
                }
            }
        }
        else
        {
            printf("INVALID\n");
        }
    }
    else
    {
        printf("INVALID\n");
    }
}