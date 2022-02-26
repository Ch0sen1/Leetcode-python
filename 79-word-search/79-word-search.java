class Solution {
    public boolean exist(char[][] board, String word) {
        char[] w = word.toCharArray();
        for (int x = 0; x < board.length; x++){
            for (int y = 0; y < board[0].length; y++){
                if (dfs(x, y, w, board, 0)) {
                    return true;
                }   
            }   
        }
        return false;
    }
    
    private boolean dfs(int x, int y, char[] w, char[][] board, int i){
        if (i == w.length) {
            return true;
        }
        
        if ( x < 0 || y < 0 || x == board.length || y == board[0].length || board[x][y] != w[i]){
            return false;
        } 
        
        char tmp = board[x][y];
        board[x][y] = '!';
        boolean trueExist = 
            dfs(x+1, y, w, board, i+1) ||
            dfs(x-1, y, w, board, i+1) ||
            dfs(x, y+1, w, board, i+1) ||
            dfs(x, y-1, w, board, i+1);
        board[x][y] = tmp;
        return trueExist;
    }
}