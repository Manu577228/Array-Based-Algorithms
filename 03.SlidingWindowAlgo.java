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
import java.util.*;

public class SlidingWindowDemo {
    
    // -------- Fixed-size Sliding Window: Maximum sum of subarray of size k --------
    static int[] maxSumK(int[] arr, int k) {
        int n = arr.length;
        if (k <= 0 || k > n) return new int[]{0, -1, -1};
        
        int sum = 0;
        for (int i = 0; i < k; i++) sum += arr[i]; // first window sum
        int best = sum, bestStart = 0;
        
        for (int i = k; i < n; i++) {
            sum += arr[i];         // add new element
            sum -= arr[i - k];     // remove old element
            if (sum > best) {
                best = sum;
                bestStart = i - k + 1;
            }
        }
        return new int[]{best, bestStart, bestStart + k - 1};
    }
    
    // -------- Variable-size Sliding Window: Longest substring without repeats --------
    static Object[] longestUniqueSubstr(String s) {
        Map<Character, Integer> lastPos = new HashMap<>();
        int left = 0, bestLen = 0, bestStart = 0;
        
        for (int right = 0; right < s.length(); right++) {
            char c = s.charAt(right);
            if (lastPos.containsKey(c) && lastPos.get(c) >= left) {
                left = lastPos.get(c) + 1; // shrink window
            }
            lastPos.put(c, right); // update last seen index
            
            int curLen = right - left + 1;
            if (curLen > bestLen) {
                bestLen = curLen;
                bestStart = left;
            }
        }
        return new Object[]{s.substring(bestStart, bestStart + bestLen), bestStart, bestLen};
    }
    
    public static void main(String[] args) {
        int[] arr = {2, 1, 5, 1, 3, 2};
        int k = 3;
        int[] result1 = maxSumK(arr, k);
        
        String text = "abccabb";
        Object[] result2 = longestUniqueSubstr(text);
        
        // ---------- Outputs ----------
        System.out.println("Example 1 (Fixed-size):");
        System.out.println("Array: " + Arrays.toString(arr) + " k: " + k);
        System.out.println("MaxSum: " + result1[0] + " Window: " + 
            Arrays.toString(Arrays.copyOfRange(arr, result1[1], result1[2] + 1)) + 
            " StartIndex: " + result1[1] + " EndIndex: " + result1[2]);
        
        System.out.println("\nExample 2 (Variable-size):");
        System.out.println("String: " + text);
        System.out.println("LongestUniqueLen: " + result2[2] + " Substring: '" + result2[0] +
            "' StartIndex: " + result2[1]);
    }
}
