/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function(height) {
    
    let l = 0;
    let r = height.length - 1;
    let area = 0;
    let max_area = 0;
    
    while (l < r) {
        area = Math.min(height[l], height[r]) * (r - l);
        max_area = Math.max(area, max_area);
        
        if (height[l] > height[r]) {
            r --;
        } else {
            l ++;
        }
    }
    
    return max_area;
    
};