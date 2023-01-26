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