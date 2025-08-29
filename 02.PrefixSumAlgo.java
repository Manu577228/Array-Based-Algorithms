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

import java.util.*;

public class PrefixSumDemo {

    // function to build prefix array
    public static int[] buildPrefix(int[] arr) {
        int n = arr.length;
        int[] pref = new int[n];
        for (int i = 0; i < n; i++) {
            if (i == 0) {
                // first prefix is same as first element
                pref[i] = arr[i];
            } else {
                // cumulative sum
                pref[i] = pref[i - 1] + arr[i];
            }
        }
        return pref;
    }

    // function to get range sum using prefix
    public static int rangeSum(int[] pref, int l, int r) {
        if (l == 0) {
            return pref[r]; // sum from 0 to r
        }
        return pref[r] - pref[l - 1]; // subtract prefix up to l-1
    }

    public static void main(String[] args) {
        int[] arr = {3, 1, 4, 1, 5, 9}; 
        System.out.println("Original array: " + Arrays.toString(arr));

        int[] pref = buildPrefix(arr); 
        System.out.println("Prefix sums:   " + Arrays.toString(pref));

        // queries
        int[][] queries = {{0, 2}, {2, 4}, {1, 5}};
        for (int[] q : queries) {
            int l = q[0], r = q[1];
            int s = rangeSum(pref, l, r);
            System.out.println("Sum arr[" + l + ".." + r + "] = " + s);
        }
    }
}
