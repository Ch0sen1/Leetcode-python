class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
    return helper(matrix,target,matrix.length-1,0);
}

public boolean helper(int[][]matrix,int target,int i,int j)
{
    if(i<0 || j<0 || i>matrix.length-1 || j>matrix[0].length-1) return false;
    if(matrix[i][j]==target) return true;
    return (matrix[i][j]>target) ?helper(matrix,target,i-1,j):helper(matrix,target,i,j+1);
 }
}