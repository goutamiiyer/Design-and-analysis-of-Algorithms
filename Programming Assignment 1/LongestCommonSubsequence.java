import java.io.*;
import java.util.LinkedList;
import java.util.List;

public class LongestCommonSubsequence
{
    /* Main Method */
    public static void main(String[] args)
    {
        String inputFile = args[0];
        List<String> inputStringList = fileReader(inputFile);

        LongestCommonSubsequence lcs = new LongestCommonSubsequence();

        for (int stringIndex = 0; stringIndex < inputStringList.size(); stringIndex++) {
            String s1 = inputStringList.get(stringIndex);
            String s2 = inputStringList.get(++stringIndex);

            char[] X = s1.toCharArray();
            char[] Y = s2.toCharArray();

            char[][] B = lcs.longestCommonSubseq( X, Y );
            System.out.println("Longest Common Subsequence of " + s1 + " and " + s2 + " is ");
            printLcs(B,X,X.length,Y.length);
            System.out.println("");
            int length = lcs.lcsLength(s1, s2);
            System.out.println("Length of Longest Common Subsequence is " + length);
        }
    }

    /* Reads the contents of the file and stores it in the form of List */
    public static List<String> fileReader(String inputFile)
    {
        BufferedReader reader;
        List<String> inputStringList = new LinkedList<>();
        try {
            reader = new BufferedReader(new FileReader(inputFile));
            String line = reader.readLine();
            while (line != null) {
                inputStringList.add(line);
                line = reader.readLine();
            }
//            reader.close();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
        return inputStringList;
    }

    /* Returns the character array B which has the various symbols representing the array from which the Longest common Subsequence was derived.
    * The main logic of finding the LCS and building the array C lies here */
    char[][] longestCommonSubseq(char[] X, char[] Y )
    {
        int m = X.length;
        int n = Y.length;
        char B[][] = new char[m+1][n+1];
        int C[][] = new int[m+1][n+1];

        int i,j = 0;
        for (i=0; i<m+1;i++) {
            C[i][0] = 0;
        }
        for (j=0;j<n+1;j++) {
            C[0][j] = 0;
        }

    /* Following steps build C[m+1][n+1] in bottom up fashion */
        for (i=1; i<m+1; i++)
        {
            for (j=1; j<n+1; j++)
            {
                if (X[i-1] == Y[j-1]) {
                    C[i][j] = C[i-1][j-1] + 1;
                    B[i][j] = '\\';
                } else if (C[i-1][j] >= C[i][j-1]) {
                    C[i][j] = C[i-1][j];
                    B[i][j] = '|';
                } else {
                    C[i][j] = C[i][j-1];
                    B[i][j] = '-';
                }
            }
        }
        return B;
    }

    /* Prints or Displays the Longest Common Subsequence*/
    public static void printLcs(char[][] B, char[] X, int i, int j) {
        if (i == 0 || j == 0) {
            return;
        }
        if (B[i][j] == '\\') {
            printLcs(B,X,i-1,j-1);
            System.out.print(X[i-1]);
        } else if (B[i][j] == '|') {
            printLcs(B,X,i-1,j);
        } else {
            printLcs(B,X,i,j-1);
        }
    }

    /* Returns length of Longest Common Subsequence for s1[0..m-1], s2[0..n-1] */
    public static int lcsLength(String s1, String s2) {
        if (s1 == null || s2 == null || s1.length() == 0 || s2.length() == 0) {
            return 0;
        }
        int[][] arr = new int[s1.length()  + 1][s2.length() + 1];
        for (int i = 1; i <= s1.length(); i++) {
            for (int j = 1; j <= s2.length(); j++) {
                if (s1.charAt(i - 1) == s2.charAt(j - 1)) {
                    arr[i][j] = arr[i - 1][j - 1] + 1;
                } else {
                    arr[i][j] = Math.max(arr[i][j], arr[i - 1][j]);
                    arr[i][j] = Math.max(arr[i][j], arr[i][j - 1]);
                }
            }
        }
        return arr[s1.length()][s2.length()];
    }
}