/**
 * @param {string} s
 * @param {number} numRows
 * @return {string}
 */
var convert = function(s, numRows) {
    if (numRows == 1){
        return s
    }
    
    let start_idx = 1
    let going_up = true
    
    const rows = new Array(numRows).fill('')
    
    for (let i = 0; i < s.length; i++) {
        rows[start_idx-1] += s[i];
        going_up? start_idx++ : start_idx--;
        if (start_idx === numRows || start_idx === 1) {
            going_up = !going_up
        }
    }
    return rows.join('');
        
    
    
};