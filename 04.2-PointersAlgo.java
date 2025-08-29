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
/*    Portfolio : https://manu-bharadwaj-portfolio.vercel.app/portfolio      */
/* -----------------------------------------------------------------------  */

import java.io.*;

public class TwoPointersExample {
    
    // Function to find two numbers that sum to target
    static int[] twoSumSorted(int[] arr, int target) {
        int l = 0;                     // left pointer
        int r = arr.length - 1;        // right pointer
        
        while (l < r) {                // loop until pointers cross
            int sum = arr[l] + arr[r]; // sum of values at pointers
            
            if (sum == target) {       // case 1: sum matches target
                return new int[]{l, r};
            }
            if (sum < target) {        // case 2: sum too small
                l++;                   // move left pointer right to increase sum
            } else {                   // case 3: sum too large
                r--;                   // move right pointer left to decrease sum
            }
        }
        return new int[]{-1, -1};      // no pair found
    }

    public static void main(String[] args) throws Exception {
        int[] arr = {-2, 1, 2, 4, 7, 11};  // input sorted array
        int target = 9;                     // target sum to find

        int[] ans = twoSumSorted(arr, target); // run algorithm
        
        System.out.println("Array: " + java.util.Arrays.toString(arr));
        System.out.println("Target: " + target);
        System.out.println("Pair indices: " + java.util.Arrays.toString(ans));
        
        if (ans[0] != -1) {
            System.out.println("Pair values: (" + arr[ans[0]] + ", " + arr[ans[1]] + ")");
        }
    }
}
