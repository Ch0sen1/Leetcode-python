class Solution {
    public int longestConsecutive(int[] nums) {
        int maxLong = 0;
        
        Set<Integer> set = new HashSet<Integer>();
        for (int i = 0; i < nums.length; i++){
            set.add(nums[i]);
        }
        
        for (int i = 0; i < nums.length; i++){
            int curLong = 1;
            
            int num = nums[i];
            int j = 1;
                
            while (set.contains(num - j)){
                curLong ++;
                set.remove(num-j);
                j++;
            }
            
            j = 1;
            
            while (set.contains(num + j)){
                curLong ++;
                set.remove(num + j);
                j++;
            }
            
            
            maxLong = Math.max(maxLong, curLong);
        }
        
        return maxLong;
        
    }
}