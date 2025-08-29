/* ----------------------------------------------------------------------------  */
/*   ( The Authentic JS/JAVA CodeBuff )
 ___ _                      _              _ 
 | _ ) |_  __ _ _ _ __ _ __| |_ __ ____ _ (_)
 | _ \ ' \/ _` | '_/ _` / _` \ V  V / _` || |
 |___/_||_\__,_|_| \__,_\__,_|\_/\_/\__,_|/ |
                                        |__/ 
 */
/* --------------------------------------------------------------------------   */
/*    Youtube: https://youtube.com/@code-with-Bharadwaj                        */
/*    Github : https://github.com/Manu577228                                  */
/*    Portfolio : https://manu-bharadwaj-portfolio.vercel.app/portfolio        */
/* -----------------------------------------------------------------------  */

import java.io.*;

public class BoyerMoore {
    
    // Function to find the majority element
    public static int majorityElement(int[] nums) {
        // Step 1: Initialize candidate and count
        int candidate = -1; 
        int count = 0;

        // Step 2: Traverse through the array
        for (int num : nums) {
            if (count == 0) {
                // If count is 0, choose current element as candidate
                candidate = num;
            }
            if (num == candidate) {
                // If element matches candidate, increase count
                count++;
            } else {
                // Otherwise, decrease count
                count--;
            }
        }

        // Step 3: Return candidate (majority element)
        return candidate;
    }

    // Main function to test the algorithm
    public static void main(String[] args) throws IOException {
        // Example input array
        int[] arr = {2, 2, 1, 1, 1, 2, 2};

        // Call the function and store result
        int result = majorityElement(arr);

        // Print the majority element
        System.out.println("Majority Element: " + result);
    }
}
