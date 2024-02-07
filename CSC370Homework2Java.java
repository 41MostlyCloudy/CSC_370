
/**
 *
 * @author johnp
 */

import java.util.Scanner;


public class CSC370Homework2Java {
  
    public static void main(String[] args)
    {
        Scanner keyboard = new Scanner(System.in);
        
        System.out.println("Enter the number of users you would like to add. \nHit enter when you are done:\n");
        
        int numberOfUsers = keyboard.nextInt();
        
        if (numberOfUsers > 50)
            numberOfUsers = 50;
        
        System.out.println("---------------------------------------------------------------------------------");
        
        int rights[] = new int[numberOfUsers];

        for (int i = 0; i < numberOfUsers; i++)
        {
            System.out.println("Enter the privilege level of user " + (i + 1) + ". \nHit enter when you are done:\n");
            rights[i] = keyboard.nextInt();
            
            if (rights[i] > 100)
                rights[i] = 100;
        }
        
        System.out.println("---------------------------------------------------------------------------------");

        System.out.println("\nplease enter the minimum permission the user must have to use this resource as a number:\nHit enter when you are done:\n");
        
        int permission = keyboard.nextInt();

        if (permission > 100)
            permission = 100;

        System.out.println("Access: " + AccessLevel(rights, permission));
    }
    
    
    static private String AccessLevel (int[] rights, int minPermission)
    {
        String returnString = "";
        
        for (int i = 0; i < rights.length; i++)
        {
            if (rights[i] >= minPermission)
                returnString += "A";
            else
                returnString += "D";
        }
        
        return returnString;
    }    
}