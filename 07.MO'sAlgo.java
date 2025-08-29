/* ----------------------------------------------------------------------------  */
/*   ( The Authentic JS/JAVA CodeBuff )                                          */
/*  ___ _                      _              _                                  */
/*  | _ ) |_  __ _ _ _ __ _ __| |_ __ ____ _ (_)                                 */
/*  | _ \ ' \/ _` | '_/ _` / _` \ V  V / _` || |                                 */
/*  |___/_||_\__,_|_| \__,_\__,_|\_/\_/\__,_|/ |                                 */
/*                                     |__/                                      */
/* ----------------------------------------------------------------------------  */
/*    Youtube: https://youtube.com/@code-with-Bharadwaj                          */
/*    Github : https://github.com/Manu577228                                     */
/*    Portfolio : https://manu-bharadwaj-portfolio.vercel.app/portfolio          */
/* ---------------------------------------------------------------------------  */

import java.io.*;
import java.util.*;

public class MosAlgorithm {
    
    // Query structure
    static class Query {
        int l, r, idx;
        Query(int l, int r, int idx) {
            this.l = l;
            this.r = r;
            this.idx = idx;
        }
    }
    
    public static void main(String[] args) throws IOException {
        // Step 1: Input array
        int[] arr = {1,2,3,4,5,6,7,8,9};
        
        // Step 2: Queries (L, R)
        int[][] queries = {
            {0,4},
            {1,3},
            {2,8},
            {0,8}
        };
        
        int n = arr.length;
        int q = queries.length;
        
        // Step 3: Block size = √N
        int blockSize = (int)Math.sqrt(n);
        
        // Step 4: Store queries with indices
        Query[] qList = new Query[q];
        for(int i=0; i<q; i++) {
            qList[i] = new Query(queries[i][0], queries[i][1], i);
        }
        
        // Step 5: Sort queries by block, then by R
        Arrays.sort(qList, (a,b) -> {
            int blockA = a.l / blockSize;
            int blockB = b.l / blockSize;
            if(blockA != blockB) return blockA - blockB;
            return a.r - b.r;
        });
        
        // Step 6: Process queries
        int currL = 0, currR = -1, currSum = 0;
        int[] ans = new int[q];
        
        for(Query query : qList) {
            int L = query.l;
            int R = query.r;
            
            // Expand left
            while(currL > L) {
                currL--;
                currSum += arr[currL];
            }
            // Expand right
            while(currR < R) {
                currR++;
                currSum += arr[currR];
            }
            // Shrink left
            while(currL < L) {
                currSum -= arr[currL];
                currL++;
            }
            // Shrink right
            while(currR > R) {
                currSum -= arr[currR];
                currR--;
            }
            
            ans[query.idx] = currSum;
        }
        
        // Step 7: Print results
        for(int i=0; i<q; i++) {
            System.out.println("Query " + i + ": Sum = " + ans[i]);
        }
    }
}
