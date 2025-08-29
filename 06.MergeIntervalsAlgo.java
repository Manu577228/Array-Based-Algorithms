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

public class MergeIntervals {
    
    // Step 1: Function to merge intervals
    public static int[][] mergeIntervals(int[][] intervals) {
        // Sort intervals by start time
        Arrays.sort(intervals, (a, b) -> Integer.compare(a[0], b[0]));
        
        // Use a list to store merged intervals
        List<int[]> merged = new ArrayList<>();
        merged.add(intervals[0]);
        
        // Step 2: Iterate through remaining intervals
        for (int i = 1; i < intervals.length; i++) {
            int[] current = intervals[i];
            int[] last = merged.get(merged.size() - 1);
            
            // If overlap → merge them
            if (current[0] <= last[1]) {
                last[1] = Math.max(last[1], current[1]);
            } else {
                // No overlap → add directly
                merged.add(current);
            }
        }
        
        // Convert list back to 2D array
        return merged.toArray(new int[merged.size()][]);
    }
    
    public static void main(String[] args) throws IOException {
        int[][] intervals = {{1,3},{2,6},{8,10},{15,18}};
        System.out.println("Input: " + Arrays.deepToString(intervals));
        
        int[][] result = mergeIntervals(intervals);
        System.out.println("Merged Intervals: " + Arrays.deepToString(result));
    }
}
