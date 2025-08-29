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
/*    Portfolio : https://manu-bharadwaj-portfolio.vercel.app/portfolio       */
/* -----------------------------------------------------------------------  */

import java.util.*;

public class DutchNationalFlag {
    public static void dutchNationalFlag(int[] arr) {
        int low = 0, mid = 0, high = arr.length - 1; // Step 1: Initialize pointers

        while (mid <= high) { // Step 2: Traverse until mid crosses high
            if (arr[mid] == 0) {
                // Case 1: Current element is 0 → swap with low
                int temp = arr[low];
                arr[low] = arr[mid];
                arr[mid] = temp;
                low++;
                mid++;
            } else if (arr[mid] == 1) {
                // Case 2: Current element is 1 → just move mid
                mid++;
            } else {
                // Case 3: Current element is 2 → swap with high
                int temp = arr[mid];
                arr[mid] = arr[high];
                arr[high] = temp;
                high--;
            }
        }
    }

    public static void main(String[] args) {
        int[] arr = {2, 0, 2, 1, 1, 0};
        dutchNationalFlag(arr);
        System.out.println("Sorted array: " + Arrays.toString(arr));
    }
}
