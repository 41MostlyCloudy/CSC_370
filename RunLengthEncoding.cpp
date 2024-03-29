#include <iostream>
#include <string>


using namespace std;


string RunLengthEncode(string inputString)
{
    string result; // This will contain the returned string.
    string includedCharacters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 {}[]():;'+=.,"; // A list of characters that will be included.
    
    char lastChar = '\0'; // The previously encountered char.
    int repeats = 0; // The number of times the last character has repeated.

    for (int i = 0; i < inputString.length() + 1; i++)
    {
        char currentChar = '\0';
        if (i < inputString.length())
            currentChar = inputString.at(i);

        if (includedCharacters.find(currentChar, 0) <= includedCharacters.length() || currentChar == '\0') // Include only specified characters.
        {
            if (currentChar == lastChar && repeats < 98) // Add to repeated character number. This cannot be done with the last char or one that would overflow the repeats.
                repeats++;
            else
            {
                repeats++;

                if (repeats > 4) // Endode repeated numbers.
                {
                    result += '/';
                    char buffer[3]; // After testing, a buffer of 3 covered any length of repeat, from 0-99.
                    sprintf_s(buffer, "%02d", repeats); // sprintf_s allows for formatting return.
                    result += buffer;
                    result += lastChar;
                }
                else // Add non-repeating numbers
                {
                    for (int j = 0; j < repeats; j++)
                        result += lastChar;
                }
                repeats = 0;
                lastChar = currentChar;
            }
        }
    }

    return result;
}


int main(void)
{
    cout << RunLengthEncode("bbbbbabwwwwdtryrddddddddd%%%%%%%%%%%%%%%%ddddqqqqaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaetggggggg");

    return 0;
}