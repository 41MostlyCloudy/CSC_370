/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package csc370homework1.java;

/**
 *
 * @author johnp
 */
public class CSC370Homework1Java {

    public static void main(String[] args)
    {
        System.out.println(RunLengthEncode("bbbbbabwwwwdtryrddddddddd%%%%%%%%%%%%%%%%ddddqqqqaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaetggggggg"));
    }
    
    static private String RunLengthEncode (String inputString)
    {
        String result = "";
        String includedCharacters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 {}[]():;'+=.,"; // A list of characters that will be included.
        
        char lastChar = '\0'; // The previously encountered char.
        int repeats = 0; // The number of times the last character has repeated.
        
        for (int i = 0; i < inputString.length() + 1; i++)
        {
            char currentChar = '\0';
            if (i < inputString.length())
                currentChar = inputString.charAt(i);

            if (includedCharacters.lastIndexOf(currentChar) != -1 || currentChar == '\0') // Include only specified characters.
            {
                if (currentChar == lastChar && repeats < 98) // Add to repeated character number. This cannot be done with the last char or one that would overflow the repeats.
                    repeats++;
                else
                {
                    repeats++;
                    if (repeats > 4) // Encode repeated numbers.
                    {
                        result += '/';
                        result += String.format("%02d", repeats);
                        result += lastChar;
                    }
                    else
                    {
                        for (int j = 0; j < repeats; j++)
                        {
                            result += lastChar;
                        }
                    }
                    repeats = 0;
                    lastChar = currentChar;
                }
            }
        }
        
        return result;
    }
}
